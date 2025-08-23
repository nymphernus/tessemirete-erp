from pydantic import BaseModel

class DashboardStats(BaseModel):
    customers: int
    products: int
    orders: int
    revenue: float