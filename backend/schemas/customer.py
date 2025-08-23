from pydantic import BaseModel
from typing import Optional

class CustomerBase(BaseModel):
    name: str
    org_name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    org_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class CustomerResponse(CustomerBase):
    id: int
    
    class Config:
        from_attributes = True