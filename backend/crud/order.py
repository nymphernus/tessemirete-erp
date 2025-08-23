from sqlalchemy.orm import Session
from models.order import Order, OrderItem
from models.product import Product
from schemas.order import OrderCreate, OrderUpdate
from fastapi import HTTPException

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Order).offset(skip).limit(limit).all()

def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()

def create_order(db: Session, order: OrderCreate):
    from crud.customer import get_customer
    customer = get_customer(db, order.customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Клиент не найден")
    
    total = 0
    order_items = []
    
    for item in order.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product or product.stock < item.quantity:
            raise HTTPException(status_code=400, detail=f"Недостаточный запас продукта - {item.product_id}")
        
        item_total = item.quantity * product.price
        total += item_total
        
        product.stock -= item.quantity
        db.add(product)
        
        order_items.append(OrderItem(
            product_id=item.product_id,
            quantity=item.quantity,
            price_per_unit=product.price,
            total_price=item_total
        ))
    
    db_order = Order(
        customer_id=order.customer_id,
        total_amount=total,
        status=order.status.value if order.status else "ожидание"
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    
    for item in order_items:
        item.order_id = db_order.id
        db.add(item)
    
    db.commit()
    db.refresh(db_order)
    
    return db_order

def update_order(db: Session, order_id: int, order_update: OrderUpdate):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order:
        update_data = order_update.dict(exclude_unset=True)
        if 'status' in update_data and update_data['status'] is not None:
            update_data['status'] = update_data['status'].value
        for key, value in update_data.items():
            setattr(db_order, key, value)
        db.commit()
        db.refresh(db_order)
    return db_order

def delete_order(db: Session, order_id: int):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
    return db_order