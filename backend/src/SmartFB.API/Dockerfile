FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app
EXPOSE 5000

FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY ["src/SmartFB.Domain/SmartFB.Domain.csproj", "src/SmartFB.Domain/"]
COPY ["src/SmartFB.Application/SmartFB.Application.csproj", "src/SmartFB.Application/"]
COPY ["src/SmartFB.Infrastructure/SmartFB.Infrastructure.csproj", "src/SmartFB.Infrastructure/"]
COPY ["src/SmartFB.API/SmartFB.API.csproj", "src/SmartFB.API/"]
RUN dotnet restore "src/SmartFB.API/SmartFB.API.csproj"
COPY . .
WORKDIR "/src/src/SmartFB.API"
RUN dotnet build "SmartFB.API.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "SmartFB.API.csproj" -c Release -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "SmartFB.API.dll"]
