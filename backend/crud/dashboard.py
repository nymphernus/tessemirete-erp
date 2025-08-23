from sqlalchemy.orm import Session
from sqlalchemy import func
from models import Customer, Product, Order

def get_dashboard_stats(db: Session):
    customers_count = db.query(func.count(Customer.id)).scalar()
    products_count = db.query(func.count(Product.id)).scalar()
    orders_count = db.query(func.count(Order.id)).scalar()
    total_revenue = db.query(func.sum(Order.total_amount)).scalar() or 0.0
    
    return {
        "customers": customers_count,
        "products": products_count,
        "orders": orders_count,
        "revenue": float(total_revenue)
    }