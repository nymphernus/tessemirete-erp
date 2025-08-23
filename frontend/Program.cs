using Microsoft.AspNetCore.Components.Web;
using Microsoft.AspNetCore.Components.WebAssembly.Hosting;
using frontend;
using MudBlazor.Services;
using frontend.Services;

var builder = WebAssemblyHostBuilder.CreateDefault(args);
builder.RootComponents.Add<App>("#app");
builder.RootComponents.Add<HeadOutlet>("head::after");

var baseUrl = builder.Configuration["ApiSettings:BaseUrl"] ?? "http://localhost:8000";

builder.Services.AddHttpClient("API", client =>
{
    client.BaseAddress = new Uri(baseUrl);
});


builder.Services.AddMudServices();

builder.Services.AddHttpClient();
builder.Services.AddScoped<IDashboardService, DashboardService>();
builder.Services.AddScoped<ICustomerService, CustomerService>();

await builder.Build().RunAsync();