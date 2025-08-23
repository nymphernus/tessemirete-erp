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

class OrderResponse(OrderBase):
    id: int
    total_amount: float
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True