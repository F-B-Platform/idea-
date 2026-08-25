namespace SmartFB.Application.Common.Exceptions;

public class NotFoundException : SmartFB.Domain.Exceptions.NotFoundException
{
    public NotFoundException(string name, object key) : base(name, key)
    {
    }

    public NotFoundException(string message) : base(message)
    {
    }
}
