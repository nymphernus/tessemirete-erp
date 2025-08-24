using System.Net.Http.Json;
using frontend.Models;

namespace frontend.Services;

public interface IOrderService
{
    Task<IEnumerable<Order>?> GetOrdersAsync();
    Task<Order?> GetOrderByIdAsync(int id);
    Task<Order?> CreateOrderAsync(OrderCreate order);
    Task<Order?> UpdateOrderAsync(int id, OrderUpdate order);
    Task<bool> DeleteOrderAsync(int id);
}

public class OrderService : IOrderService
{
    private readonly IHttpClientFactory _httpClientFactory;

    public OrderService(IHttpClientFactory httpClientFactory)
    {
        _httpClientFactory = httpClientFactory;
    }

    public async Task<IEnumerable<Order>?> GetOrdersAsync()
    {
        var _httpClient = _httpClientFactory.CreateClient("API");
        try
        {
            var orders = await _httpClient.GetFromJsonAsync<IEnumerable<Order>>("orders/");
            return orders;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка при получении заказов: {ex.Message}");
            return null;
        }
    }

    public async Task<Order?> GetOrderByIdAsync(int id)
    {
        var _httpClient = _httpClientFactory.CreateClient("API");
        try
        {
            var order = await _httpClient.GetFromJsonAsync<Order>($"orders/{id}");
            return order;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка при получении заказа: {ex.Message}");
            return null;
        }
    }

    public async Task<Order?> CreateOrderAsync(OrderCreate order)
    {
        var _httpClient = _httpClientFactory.CreateClient("API");
        try
        {
            var response = await _httpClient.PostAsJsonAsync("orders/", order);
            if (response.IsSuccessStatusCode)
            {
                return await response.Content.ReadFromJsonAsync<Order>();
            }
            return null;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка при создании заказа: {ex.Message}");
            return null;
        }
    }

    public async Task<Order?> UpdateOrderAsync(int id, OrderUpdate order)
    {
        var _httpClient = _httpClientFactory.CreateClient("API");
        try
        {
            var response = await _httpClient.PutAsJsonAsync($"orders/{id}", order);
            if (response.IsSuccessStatusCode)
            {
                return await response.Content.ReadFromJsonAsync<Order>();
            }
            return null;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка при обновлении заказа: {ex.Message}");
            return null;
        }
    }

    public async Task<bool> DeleteOrderAsync(int id)
    {
        var _httpClient = _httpClientFactory.CreateClient("API");
        try
        {
            var response = await _httpClient.DeleteAsync($"orders/{id}");
            return response.IsSuccessStatusCode;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка при удалении заказа: {ex.Message}");
            return false;
        }
    }
}