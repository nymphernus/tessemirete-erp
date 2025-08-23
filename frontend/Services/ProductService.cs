using System.Net.Http.Json;
using frontend.Models;

namespace frontend.Services;

public interface IProductService
{
    Task<IEnumerable<Product>?> GetProductsAsync();
    Task<Product?> GetProductByIdAsync(int id);
    Task<Product?> CreateProductAsync(Product product);
    Task<Product?> UpdateProductAsync(int id, Product product);
    Task<bool> DeleteProductAsync(int id);
}

public class ProductService : IProductService
{
    private readonly IHttpClientFactory _httpClientFactory;

    public ProductService(IHttpClientFactory httpClientFactory)
    {
        _httpClientFactory = httpClientFactory;
    }

    public async Task<IEnumerable<Product>?> GetProductsAsync()
    {
        var _httpClient = _httpClientFactory.CreateClient("API");
        try
        {
            var products = await _httpClient.GetFromJsonAsync<IEnumerable<Product>>("products/");
            return products;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка при получении товаров: {ex.Message}");
            return null;
        }
    }

    public async Task<Product?> GetProductByIdAsync(int id)
    {
        var _httpClient = _httpClientFactory.CreateClient("API");
        try
        {
            var product = await _httpClient.GetFromJsonAsync<Product>($"products/{id}");
            return product;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка при получении товара: {ex.Message}");
            return null;
        }
    }

    public async Task<Product?> CreateProductAsync(Product product)
    {
        var _httpClient = _httpClientFactory.CreateClient("API");
        try
        {
            var response = await _httpClient.PostAsJsonAsync("products/", product);
            if (response.IsSuccessStatusCode)
            {
                return await response.Content.ReadFromJsonAsync<Product>();
            }
            return null;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка при создании товара: {ex.Message}");
            return null;
        }
    }

    public async Task<Product?> UpdateProductAsync(int id, Product product)
    {
        var _httpClient = _httpClientFactory.CreateClient("API");
        try
        {
            var response = await _httpClient.PutAsJsonAsync($"products/{id}", product);
            if (response.IsSuccessStatusCode)
            {
                return await response.Content.ReadFromJsonAsync<Product>();
            }
            return null;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка при обновлении товара: {ex.Message}");
            return null;
        }
    }

    public async Task<bool> DeleteProductAsync(int id)
    {
        var _httpClient = _httpClientFactory.CreateClient("API");
        try
        {
            var response = await _httpClient.DeleteAsync($"products/{id}");
            return response.IsSuccessStatusCode;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка при удалении товара: {ex.Message}");
            return false;
        }
    }
}