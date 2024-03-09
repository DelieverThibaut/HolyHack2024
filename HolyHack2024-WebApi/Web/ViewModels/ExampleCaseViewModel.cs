using IronXL;
using Web.Models;

namespace Web.ViewModels;

public class ExampleCaseViewModel
{
    public List<Order> Orders { get; set; } = [];
    public PredictionTableViewModel PredictionTableViewModel { get; set; } = new PredictionTableViewModel();

    public ExampleCaseViewModel(int id)
    {
        WorkBook workbook = WorkBook.Load($"~/Script/ExampleCase{id}.xlsx");
        WorkSheet sheet = workbook.WorkSheets.First();

        foreach (var cell in sheet["A2:A10"])
        {
            CreateOrder(cell.IntValue);
        }
    }

    private void CreateOrder(int id)
    {
        Orders.Add(new Order
        {
            ProductAmount = id,
        });
    }
}
