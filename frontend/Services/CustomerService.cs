using System.Net.Http.Json;
using frontend.Models;

namespace frontend.Services;

public interface ICustomerService
{
    Task<IEnumerable<Customer>?> GetCustomersAsync();
    Task<Customer?> GetCustomerByIdAsync(int id);
    Task<Customer?> CreateCustomerAsync(Customer customer);
    Task<Customer?> UpdateCustomerAsync(int id, Customer customer);
    Task<bool> DeleteCustomerAsync(int id);
}

public class CustomerService : ICustomerService
{
    private readonly IHttpClientFactory _httpClientFactory;

    public CustomerService(IHttpClientFactory httpClientFactory)
    {
        _httpClientFactory = httpClientFactory;
    }

    public async Task<IEnumerable<Customer>?> GetCustomersAsync()
    {
        var _httpClient = _httpClientFactory.CreateClient("API");
        try
        {
            var customers = await _httpClient.GetFromJsonAsync<IEnumerable<Customer>>("customers/");
            return customers;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка при получении клиентов: {ex.Message}");
            return null;
        }
    }

    public async Task<Customer?> GetCustomerByIdAsync(int id)
    {
        var _httpClient = _httpClientFactory.CreateClient("API");
        try
        {
            var customer = await _httpClient.GetFromJsonAsync<Customer>($"customers/{id}");
            return customer;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка при получении клиента: {ex.Message}");
            return null;
        }
    }

    public async Task<Customer?> CreateCustomerAsync(Customer customer)
    {
        var _httpClient = _httpClientFactory.CreateClient("API");
        try
        {
            var response = await _httpClient.PostAsJsonAsync("customers/", customer);
            if (response.IsSuccessStatusCode)
            {
                return await response.Content.ReadFromJsonAsync<Customer>();
            }
            return null;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка при создании клиента: {ex.Message}");
            return null;
        }
    }

    public async Task<Customer?> UpdateCustomerAsync(int id, Customer customer)
    {
        var _httpClient = _httpClientFactory.CreateClient("API");
        try
        {
            var response = await _httpClient.PutAsJsonAsync($"customers/{id}", customer);
            if (response.IsSuccessStatusCode)
            {
                return await response.Content.ReadFromJsonAsync<Customer>();
            }
            return null;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка при обновлении клиента: {ex.Message}");
            return null;
        }
    }

    public async Task<bool> DeleteCustomerAsync(int id)
    {
        var _httpClient = _httpClientFactory.CreateClient("API");
        try
        {
            var response = await _httpClient.DeleteAsync($"customers/{id}");
            return response.IsSuccessStatusCode;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка при удалении клиента: {ex.Message}");
            return false;
        }
    }
}