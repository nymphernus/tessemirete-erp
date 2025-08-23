from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    category: Optional[str] = None
    price: float
    stock: Optional[int] = 0
    sku: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    sku: Optional[str] = None

class ProductResponse(ProductBase):
    id: int
    
    class Config:
        from_attributes = True