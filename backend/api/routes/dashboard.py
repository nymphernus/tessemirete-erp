from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import DashboardStats
from crud import get_customers, get_products, get_orders
from database import get_db

router = APIRouter(prefix="/dashboard", tags=["Статистика"])

@router.get("/stats", response_model=DashboardStats)
def get_dashboard_stats(db: Session = Depends(get_db)):

    customers_count = len(get_customers(db))
    products_count = len(get_products(db))
    
    orders_data = get_orders(db)
    orders_count = len(orders_data)
    
    total_revenue = sum(order.total_amount for order in orders_data)
    
    return DashboardStats(
        customers=customers_count,
        products=products_count,
        orders=orders_count,
        revenue=total_revenue
    )