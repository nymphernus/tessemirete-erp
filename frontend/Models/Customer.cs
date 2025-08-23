namespace frontend.Models;
using System.Text.Json.Serialization;

public class Customer
{
    public int Id { get; set; }
    public string Name { get; set; }
    [JsonPropertyName("org_name")]
    public string Organization { get; set; }
    public string Email { get; set; }
    public string Phone { get; set; }
    public string Address { get; set; }
}