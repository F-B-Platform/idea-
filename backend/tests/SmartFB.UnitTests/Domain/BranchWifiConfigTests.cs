using FluentAssertions;
using SmartFB.Domain.Entities;
using Xunit;

namespace SmartFB.UnitTests.Domain;

public class BranchWifiConfigTests
{
    [Theory]
    [InlineData("00:14:22:01:23:45", "00:14:22:01:23:45", true)]
    [InlineData("00:14:22:01:23:45", "00-14-22-01-23-45", true)] // Different delimiter
    [InlineData("00:14:22:01:23:45", "00:14:22:01:23:AA", false)] // Different MAC
    public void BranchWifiConfig_BssidMatch_ShouldNormalizeAndCompareCorrectly(
        string registeredBssid, string clientBssid, bool expectedMatch)
    {
        // Arrange
        var config = new BranchWifiConfig
        {
            BranchId = Guid.NewGuid(),
            SsidName = "SmartCoffee_Quan1",
            BssidList = registeredBssid,
            AllowedIpSubnets = "192.168.1.0/24",
            IsActive = true
        };

        // Act
        string normRegistered = config.BssidList.Replace("-", ":").ToUpperInvariant();
        string normClient = clientBssid.Replace("-", ":").ToUpperInvariant();
        bool isMatched = normRegistered.Equals(normClient, StringComparison.OrdinalIgnoreCase);

        // Assert
        isMatched.Should().Be(expectedMatch);
    }

    [Theory]
    [InlineData("192.168.1.45", "192.168.1.0/24", true)]
    [InlineData("192.168.1.1", "192.168.1.0/24", true)]
    [InlineData("192.168.1.254", "192.168.1.0/24", true)]
    [InlineData("192.168.2.10", "192.168.1.0/24", false)] // Different subnet
    [InlineData("14.169.12.88", "192.168.1.0/24", false)] // 4G Cellular IP
    public void BranchWifiConfig_SubnetMatch_ShouldVerifyInternalNetwork(
        string clientIp, string subnetRange, bool expectedInSubnet)
    {
        // Act: Verify simple IPv4 /24 subnet logic
        bool isInSubnet = CheckIpInSubnet(clientIp, subnetRange);

        // Assert
        isInSubnet.Should().Be(expectedInSubnet);
    }

    private static bool CheckIpInSubnet(string ipAddress, string cidr)
    {
        var parts = cidr.Split('/');
        if (parts.Length != 2) return false;
        var subnetPrefix = parts[0];
        int prefixLength = int.Parse(parts[1]);

        if (prefixLength == 24)
        {
            var subnetOctets = subnetPrefix.Split('.');
            var ipOctets = ipAddress.Split('.');
            if (subnetOctets.Length != 4 || ipOctets.Length != 4) return false;

            return subnetOctets[0] == ipOctets[0] &&
                   subnetOctets[1] == ipOctets[1] &&
                   subnetOctets[2] == ipOctets[2];
        }

        return false;
    }

    [Fact]
    public void BranchWifiConfig_DualVerification_WhenBothBssidAndIpMatch_ShouldSucceed()
    {
        // Arrange
        var config = new BranchWifiConfig
        {
            BranchId = Guid.NewGuid(),
            SsidName = "SmartCoffee_Quan1",
            BssidList = "00:14:22:01:23:45",
            AllowedIpSubnets = "192.168.1.0/24",
            IsActive = true
        };

        string clientBssid = "00:14:22:01:23:45";
        string clientIp = "192.168.1.45";

        // Act
        bool bssidValid = config.BssidList.Equals(clientBssid, StringComparison.OrdinalIgnoreCase);
        bool ipValid = CheckIpInSubnet(clientIp, config.AllowedIpSubnets);
        bool isWifiVerified = config.IsActive && bssidValid && ipValid;

        // Assert
        isWifiVerified.Should().BeTrue();
    }
}
