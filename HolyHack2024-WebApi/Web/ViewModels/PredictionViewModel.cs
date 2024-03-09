using Web.Models;

namespace Web.ViewModels;

public class PredictionViewModel
{
    public int ProductAmount { get; set; } = 5;
    public double RetourRatio { get; set; } = 3;
    public double Price { get; set; } = 59.99;

    public double RiskScore { get; set; } = 0;
    public double SuggestedFee => 0.01*RiskScore*Math.Pow(Price, 0.5);
    public double FeePercentage => SuggestedFee * 100 / Price;
}
