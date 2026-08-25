using FluentAssertions;
using Xunit;

namespace SmartFB.UnitTests.Domain;

public record IngredientRecipeItem(string IngredientName, decimal QuantityPerUnit, string Unit);
public record ProductBomRecipe(string ProductName, string Size, List<IngredientRecipeItem> Ingredients);

public class ProductBomTests
{
    [Fact]
    public void ProductBom_MatchaLatteSizeL_ShouldCalculateCorrectIngredientsForTwoCups()
    {
        // Arrange: Recipe for 1 cup of Matcha Latte Size L: 15g Matcha powder, 180ml Fresh milk, 20ml Sugar syrup
        var recipe = new ProductBomRecipe(
            ProductName: "Matcha Latte",
            Size: "L",
            Ingredients: new List<IngredientRecipeItem>
            {
                new("Matcha Powder", 15m, "g"),
                new("Fresh Milk", 180m, "ml"),
                new("Sugar Syrup", 20m, "ml")
            }
        );

        const int orderQuantity = 2;

        // Act: Multiply each ingredient requirement by quantity
        var calculatedIngredients = recipe.Ingredients.Select(i => new
        {
            i.IngredientName,
            TotalRequired = i.QuantityPerUnit * orderQuantity,
            i.Unit
        }).ToList();

        // Assert
        var matcha = calculatedIngredients.First(i => i.IngredientName == "Matcha Powder");
        matcha.TotalRequired.Should().Be(30m);
        matcha.Unit.Should().Be("g");

        var milk = calculatedIngredients.First(i => i.IngredientName == "Fresh Milk");
        milk.TotalRequired.Should().Be(360m);
        milk.Unit.Should().Be("ml");

        var syrup = calculatedIngredients.First(i => i.IngredientName == "Sugar Syrup");
        syrup.TotalRequired.Should().Be(40m);
        syrup.Unit.Should().Be("ml");
    }

    [Fact]
    public void ProductBom_InventoryDeduction_NormalStock_ShouldDeductAccurately()
    {
        // Arrange
        decimal currentMilkStock = 500m; // 500ml in stock
        decimal requiredMilk = 360m; // Required for 2 cups

        // Act
        decimal remainingStock = currentMilkStock - requiredMilk;
        bool isNegative = remainingStock < 0;

        // Assert
        remainingStock.Should().Be(140m);
        isNegative.Should().BeFalse();
    }

    [Fact]
    public void ProductBom_InventoryDeduction_InsufficientStock_ShouldAllowNegativeAndFlagAlert()
    {
        // Arrange: Current stock in bar counter is 50ml, required is 180ml
        decimal currentStock = 50m;
        decimal required = 180m;

        // Act: Negative inventory is allowed on KDS to not block customer order, but raises alert
        decimal remainingStock = currentStock - required;
        bool isShortageAlertTriggered = remainingStock < 0;

        // Assert: 50 - 180 = -130ml
        remainingStock.Should().Be(-130m);
        isShortageAlertTriggered.Should().BeTrue("Shortage alert must be triggered when inventory drops below zero");
    }

    [Fact]
    public void ProductBom_MultiProductAggregation_ShouldCombineCommonIngredients()
    {
        // Arrange: 2 Matcha Latte L (180ml milk each = 360ml) + 1 Bac Xiu M (120ml milk)
        var orderItems = new List<(string Product, int Quantity, decimal MilkPerUnit)>
        {
            ("Matcha Latte L", 2, 180m),
            ("Bac Xiu M", 1, 120m)
        };

        // Act
        decimal totalMilkRequired = orderItems.Sum(item => item.Quantity * item.MilkPerUnit);

        // Assert: (2 * 180) + (1 * 120) = 360 + 120 = 480ml
        totalMilkRequired.Should().Be(480m);
    }
}
