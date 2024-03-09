using IronPython.Hosting;
using Web.Models;

namespace Web.ViewModels;

public class PredictionTableViewModel
{
    public int ProductAmount { get; set; } = 5;
    public double RetourRatio { get; set; } = 3;
    public double Price { get; set; } = 59.99;

    public double RiskScore { get; set; } = 0;
    public double SuggestedFee => 0.01 * RiskScore * Math.Pow(Price, 0.5);
    public double FeePercentage => 100 * SuggestedFee / Price;

    public PredictionTableViewModel()
    {}

    public PredictionTableViewModel(int productAmount, double retourRatio, double price)
    {
        ProductAmount = productAmount;
        RetourRatio = retourRatio;
        Price = price;
        RiskScore = RunPython(); //Tried to connect python script to generate the riskscore here...
    }

    private double RunPython()
    {
        var engine = Python.CreateEngine();
        var scope = engine.CreateScope();
        scope.SetVariable("x", ProductAmount);
        scope.SetVariable("y", RetourRatio);
        scope.SetVariable("z", Price);

        var source = engine.CreateScriptSourceFromFile("C:\\Users\\thiba\\Documents\\GithubRepos\\HolyHack2024\\HolyHack2024-WebApi\\Web\\Script\\model_fast.py");
        var compilation = source.Compile();
        var result = compilation.Execute(scope);




        var res = scope.GetVariable("predict")();
        _ = double.TryParse(res, out double resDouble);
        Console.WriteLine(res);
        Console.WriteLine(resDouble);
        return resDouble;
    }
}
