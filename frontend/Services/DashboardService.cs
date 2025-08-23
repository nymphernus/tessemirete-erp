using System.Net.Http.Json;
using frontend.Models;

namespace frontend.Services;

public interface IDashboardService
{
    Task<DashboardStats?> GetDashboardStatsAsync();
}

public class DashboardService : IDashboardService
{
    private readonly IHttpClientFactory _httpClientFactory;
    public DashboardService(IHttpClientFactory httpClientFactory)
    {
        _httpClientFactory = httpClientFactory;
    }

    public async Task<DashboardStats?> GetDashboardStatsAsync()
    {
        var _httpClient = _httpClientFactory.CreateClient("API");
        try
        {
            var stats = await _httpClient.GetFromJsonAsync<DashboardStats>("dashboard/stats");
            return stats;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка при получении статистики: {ex.Message}");
            return null;
        }
    }
}