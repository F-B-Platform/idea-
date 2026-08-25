namespace SmartFB.Application.Common.Exceptions;

public class UnauthorizedException : SmartFB.Domain.Exceptions.UnauthorizedException
{
    public UnauthorizedException(string message) : base(message)
    {
    }
}

public class BusinessRuleException : SmartFB.Domain.Exceptions.BusinessRuleException
{
    public BusinessRuleException(string message, string ruleCode = "BUSINESS_RULE_VIOLATION") : base(message, ruleCode)
    {
    }
}
