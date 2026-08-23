import os
import re
import sys
import subprocess
import shutil

sys.stdout.reconfigure(encoding='utf-8')

FILE_PATH = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md"

def extract_csharp_files():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    code_blocks = re.findall(r'```([a-zA-Z0-9_-]*)\r?\n(.*?)```', content, re.DOTALL)
    csharp_blocks = [code for lang, code in code_blocks if lang.lower() == 'csharp']
    
    files = {}
    for code in csharp_blocks:
        m = re.search(r'//\s*File:\s*(.*?)\r?\n', code)
        if m:
            file_rel_path = m.group(1).strip()
            files[file_rel_path] = code
        else:
            print("Warning: no // File: header found in C# block!")
            
    return files

def setup_and_build_csharp():
    test_dir = r"d:\Idea_DoAn\tests\dotnet_verification"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir, ignore_errors=True)
    os.makedirs(test_dir, exist_ok=True)
    
    # Create csproj
    csproj_content = """<Project Sdk="Microsoft.NET.Sdk.Web">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="MediatR" Version="12.4.1" />
    <PackageReference Include="FluentValidation" Version="11.9.2" />
    <PackageReference Include="FluentValidation.DependencyInjectionExtensions" Version="11.9.2" />
    <PackageReference Include="Microsoft.EntityFrameworkCore" Version="8.0.8" />
  </ItemGroup>
</Project>
"""
    with open(os.path.join(test_dir, "SmartFB.TestHarness.csproj"), "w", encoding="utf-8") as f:
        f.write(csproj_content)
        
    # Write extracted C# files
    extracted_files = extract_csharp_files()
    for rel_path, code in extracted_files.items():
        dest_path = os.path.join(test_dir, rel_path.replace("/", os.sep))
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Wrote extracted file: {rel_path}")

    # Write domain common & contracts needed to compile aggregate root & handlers
    common_stubs = """
using System;
using System.Collections.Generic;

namespace SmartFB.Domain.Common
{
    public interface IDomainEvent { }

    public abstract class BaseEntity<TId>
    {
        public TId Id { get; protected set; } = default!;
        private readonly List<IDomainEvent> _domainEvents = new();
        public IReadOnlyCollection<IDomainEvent> DomainEvents => _domainEvents.AsReadOnly();
        public void AddDomainEvent(IDomainEvent domainEvent) => _domainEvents.Add(domainEvent);
        public void ClearDomainEvents() => _domainEvents.Clear();
    }

    public abstract class AggregateRoot<TId> : BaseEntity<TId> { }
}

namespace SmartFB.Domain.Enums
{
    public enum OrderChannel { DineIn, TakeAway, Delivery }
    public enum OrderStatus { PendingPayment, Confirmed, Preparing, Ready, Served, Completed, Cancelled }
    public enum PaymentMethod { Cash, VietQR, CreditCard, InternalWallet }
    public enum PaymentStatus { Pending, Paid, Failed, Refunded }
    public enum PaymentBranchType { PrePaidVietQR, PostPaidCash }
}

namespace SmartFB.Domain.Events
{
    using SmartFB.Domain.Common;
    using SmartFB.Domain.Entities;
    public sealed record OrderCreatedEvent(Order Order) : IDomainEvent;
    public sealed record OrderPaidEvent(Guid OrderId, decimal Amount, string TransactionCode) : IDomainEvent;
    public sealed record OrderStatusChangedEvent(Guid OrderId, Enums.OrderStatus OldStatus, Enums.OrderStatus NewStatus) : IDomainEvent;
}

namespace SmartFB.Domain.Exceptions
{
    public class DomainException : Exception
    {
        public DomainException(string message) : base(message) { }
    }
    public class NotFoundException : Exception
    {
        public NotFoundException(string message) : base(message) { }
    }
    public class UnauthorizedException : Exception
    {
        public UnauthorizedException(string message) : base(message) { }
    }
}

namespace SmartFB.Application.Common.Models
{
    public class Result<T>
    {
        public bool IsSuccess { get; }
        public T? Value { get; }
        public string? Error { get; }
        protected Result(bool isSuccess, T? value, string? error)
        {
            IsSuccess = isSuccess;
            Value = value;
            Error = error;
        }
        public static Result<T> Success(T value) => new(true, value, null);
        public static Result<T> Failure(string error) => new(false, default, error);
    }
}

namespace SmartFB.Application.Common.Interfaces
{
    using Microsoft.EntityFrameworkCore;
    using SmartFB.Domain.Entities;
    using System.Threading;
    using System.Threading.Tasks;

    public interface IApplicationDbContext
    {
        DbSet<Order> Orders { get; }
        Task<int> SaveChangesAsync(CancellationToken cancellationToken = default);
    }

    public interface IPayOsPaymentService
    {
        Task<string> CreatePaymentLinkAsync(Guid orderId, string orderCode, decimal amount, string description, CancellationToken cancellationToken = default);
    }

    public interface IKitchenNotificationService
    {
        Task NotifyNewOrderTicketAsync(Order order, CancellationToken cancellationToken = default);
    }
}
"""
    with open(os.path.join(test_dir, "SupportingContracts.cs"), "w", encoding="utf-8") as f:
        f.write(common_stubs)
        
    print("\nRunning 'dotnet build'...")
    res = subprocess.run(["dotnet", "build", os.path.join(test_dir, "SmartFB.TestHarness.csproj"), "-c", "Release"], capture_output=True, text=True)
    print("STDOUT:\n", res.stdout)
    if res.stderr:
        print("STDERR:\n", res.stderr)
    print(f"Exit code: {res.returncode}")
    return res.returncode == 0

if __name__ == "__main__":
    success = setup_and_build_csharp()
    print("DOTNET BUILD TEST:", "PASS" if success else "FAIL")
