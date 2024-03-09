using Web.Models;

namespace Web.ViewModels;

public class PredictionViewModel
{
    public int ProductAmount { get; set; } = 5;
    public double RetourRatio { get; set; } = 3;
    public double Price { get; set; } = 59.99;
}
