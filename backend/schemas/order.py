from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum

class OrderStatus(str, Enum):
    PENDING = "ожидание"
    CONFIRMED = "подтверждено"
    PROCESSING = "обработка"
    SHIPPED = "отправлено"
    DELIVERED = "доставлено"
    CANCELLED = "отменено"

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class OrderBase(BaseModel):
    customer_id: int
    status: Optional[OrderStatus] = OrderStatus.PENDING

class OrderCreate(OrderBase):
    items: List[OrderItemCreate]

class OrderUpdate(BaseModel):
    status: Optional[OrderStatus] = None

class OrderItemResponse(BaseModel):
    id: int
    order_id: int
    product_id: int
    product_name: str = ""
    quantity: int
    price_per_unit: float
    total_price: float

    class Config:
        from_attributes = True

class OrderResponse(OrderBase):
    id: int
    total_amount: float
    created_at: datetime
    updated_at: datetime
    customer_name: str = ""
    org_name: str = ""
    items: List[OrderItemResponse] = []
    
    class Config:
        from_attributes = True