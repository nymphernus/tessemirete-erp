namespace frontend.Models;
using System.Text.Json.Serialization;

public class Order
{
    public int Id { get; set; }
    
    [JsonPropertyName("customer_id")]
    public int CustomerId { get; set; }
    
    [JsonPropertyName("total_amount")]
    public decimal TotalAmount { get; set; }
    public string Status { get; set; } = string.Empty;
    
    [JsonPropertyName("created_at")]
    public DateTime CreatedAt { get; set; }
    
    [JsonPropertyName("updated_at")]
    public DateTime UpdatedAt { get; set; }
    [JsonPropertyName("customer_name")]
    public string CustomerName { get; set; } = string.Empty;

    [JsonPropertyName("items")]
    public List<OrderItem> Items { get; set; } = new();
}

public class OrderItem
{
    public int Id { get; set; }
    [JsonPropertyName("order_id")]
    public int OrderId { get; set; }
    [JsonPropertyName("product_id")]
    public int ProductId { get; set; }
    [JsonPropertyName("product_name")]
    public string ProductName { get; set; } = string.Empty;
    public int Quantity { get; set; }
    [JsonPropertyName("price_per_unit")]
    public decimal PricePerUnit { get; set; }
    [JsonPropertyName("total_price")]
    public decimal TotalPrice { get; set; }
}

public class OrderCreate
{
    [JsonPropertyName("customer_id")]
    public int CustomerId { get; set; }
    public List<OrderItemCreate> Items { get; set; } = new();
}

public class OrderItemCreate
{
    [JsonPropertyName("product_id")]
    public int ProductId { get; set; }
    public int Quantity { get; set; }
}

public class OrderUpdate
{
    public string? Status { get; set; }
}