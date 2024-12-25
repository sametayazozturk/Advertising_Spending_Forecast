using Advertising_Forecast.Models;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using System.Diagnostics;

namespace Advertising_Forecast.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public async Task<ActionResult> Index(PredictionModel model)
        {


            if (ModelState.IsValid)
            {

                string apiUrl = "http://127.0.0.1:5000/predict";

                using (var client = new HttpClient())
                {
                    try
                    {
                        // API anahtarýný headers'a ekleyelim
                        client.DefaultRequestHeaders.Add("API-Key", "asdjaslkjdlkasjdlkas");

                        var inputData = new { TV = model.TV, Radio = model.Radio, Newspaper = model.Newspaper };
                        var jsonData = JsonConvert.SerializeObject(inputData);
                        var content = new StringContent(jsonData, System.Text.Encoding.UTF8, "application/json");

                        HttpResponseMessage response = await client.PostAsync(apiUrl, content);

                        if (response.IsSuccessStatusCode)
                        {
                            var result = await response.Content.ReadAsStringAsync();
                            ViewBag.Prediction = result;
                        }
                        else
                        {
                            ViewBag.Prediction = $"API ile iletiþimde bir hata oluþtu. {response.StatusCode}";
                        }
                    }
                    catch (Exception ex)
                    {
                        ViewBag.Prediction = $"Hata: {ex.Message}";
                    }
                }
            }
         

            return View(model);


        }




        public IActionResult Privacy()
        {
            return View();
        }

       
       
    }
}
