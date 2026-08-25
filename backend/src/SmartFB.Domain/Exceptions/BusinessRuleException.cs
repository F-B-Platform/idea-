namespace SmartFB.Domain.Exceptions;

public class BusinessRuleException : DomainException
{
    public string RuleCode { get; }

    public BusinessRuleException(string message, string ruleCode = "BUSINESS_RULE_VIOLATION") : base(message)
    {
        RuleCode = ruleCode;
    }
}
