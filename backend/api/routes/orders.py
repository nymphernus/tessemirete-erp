from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List
from crud import get_orders, create_order, get_order, update_order, delete_order
from schemas import OrderCreate, OrderUpdate, OrderResponse
from database import get_db
from models.order import Order, OrderItem
from models.customer import Customer
from models.product import Product

router = APIRouter(prefix="/orders", tags=["Заказы"])

@router.post("/", response_model=OrderResponse)
def create_order_endpoint(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db=db, order=order)

@router.get("/", response_model=List[OrderResponse])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders_data = db.query(Order).options(
        joinedload(Order.customer),
        joinedload(Order.items).joinedload(OrderItem.product)
    ).offset(skip).limit(limit).all()
    
    result = []
    for order in orders_data:
        # Получаем имя клиента
        customer_name = order.customer.name if order.customer else ""
        org_name = order.customer.org_name if order.customer else ""
        
        # Формируем элементы заказа
        items = []
        for item in order.items:
            items.append({
                "id": item.id,
                "order_id": item.order_id,
                "product_id": item.product_id,
                "product_name": item.product.name if item.product else "",
                "quantity": item.quantity,
                "price_per_unit": float(item.price_per_unit),
                "total_price": float(item.total_price)
            })
        
        result.append({
            "id": order.id,
            "customer_id": order.customer_id,
            "total_amount": float(order.total_amount),
            "status": order.status,
            "created_at": order.created_at,
            "updated_at": order.updated_at,
            "customer_name": customer_name,
            "org_name": org_name,
            "items": items
        })
    
    return result

@router.get("/{order_id}", response_model=OrderResponse)
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).options(
        joinedload(Order.customer),
        joinedload(Order.items).joinedload(OrderItem.product)
    ).filter(Order.id == order_id).first()
    
    if order is None:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    
    # Получаем имя клиента
    customer_name = order.customer.name if order.customer else ""
    org_name = order.customer.org_name if order.customer else ""
    
    # Формируем элементы заказа
    items = []
    for item in order.items:
        items.append({
            "id": item.id,
            "order_id": item.order_id,
            "product_id": item.product_id,
            "product_name": item.product.name if item.product else "",
            "quantity": item.quantity,
            "price_per_unit": float(item.price_per_unit),
            "total_price": float(item.total_price)
        })
    
    return {
        "id": order.id,
        "customer_id": order.customer_id,
        "total_amount": float(order.total_amount),
        "status": order.status,
        "created_at": order.created_at,
        "updated_at": order.updated_at,
        "customer_name": customer_name,
        "org_name": org_name,
        "items": items
    }

@router.put("/{order_id}", response_model=OrderResponse)
def update_order_endpoint(order_id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    db_order = update_order(db, order_id=order_id, order_update=order)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    return db_order

@router.delete("/{order_id}")
def delete_order_endpoint(order_id: int, db: Session = Depends(get_db)):
    db_order = delete_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    return {"message": "Заказ удален"}