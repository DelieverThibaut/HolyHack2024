namespace Web.Models;

public class Order
{
    public int ProductAmount { get; set; } = 0;
    public List<int> ProductPrices { get; set; } = [];
    public int RetourAmount { get; set; } = 0;
    public List<int> RetourPrices { get; set; } = [];


    public double RiskScore { get; set; } = 0;
    public double Price { get; set; } = 0;
    public double SuggestedPrice { get; set; } = 0;

    public double ExtraFeeDiscount => Price - SuggestedPrice;
}
