using IronPython.Hosting;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;
using Web.Models;
using Web.ViewModels;

namespace Web.Controllers
{
    public class HomeController(ILogger<HomeController> logger) : Controller
    {
        public ILogger<HomeController> Logger { get; } = logger;

        public IActionResult Index() => View(new ParameterViewModel());


        [HttpGet("/ExampleCase1")]
        public IActionResult ExampleCase1()
        {
            var engine = Python.CreateEngine();
            var scope = engine.CreateScope();
            engine.ExecuteFile("C:\\Users\\thiba\\Documents\\GithubRepos\\HolyHack2024\\HolyHack2024-WebApi\\Web\\Script\\model_class.py");

            var result = scope.GetVariable("result");

            return View(new ExampleCaseViewModel(1));
        }

        [HttpGet("/Prediction")]
        public IActionResult Prediction() => View(new PredictionViewModel());

        [HttpGet("/GetPredictionTable")]
        public IActionResult GetPredictionTable(int productAmount, double retourRatio, double price) => PartialView("~/Views/Shared/Tables/_PredictionTable.cshtml", new PredictionTableViewModel(productAmount, retourRatio, price));



        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error() => View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
