from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from crud import get_customers, create_customer, get_customer, update_customer, delete_customer
from schemas import CustomerCreate, CustomerUpdate, CustomerResponse
from models.customer import Customer
from database import get_db

router = APIRouter(prefix="/customers", tags=["Клиенты"])

@router.post("/", response_model=CustomerResponse)
def create_customer_endpoint(customer: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = get_customer_by_email(db, email=customer.email)
    if db_customer:
        raise HTTPException(status_code=400, detail="Такой email уже существует")
    return create_customer(db=db, customer=customer)

def get_customer_by_email(db: Session, email: str):
    return db.query(Customer).filter(Customer.email == email).first()

@router.get("/", response_model=List[CustomerResponse])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = get_customers(db, skip=skip, limit=limit)
    return customers

@router.get("/{customer_id}", response_model=CustomerResponse)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = get_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Клиент не найден")
    return db_customer

@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer_endpoint(customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    db_customer = update_customer(db, customer_id=customer_id, customer_update=customer)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Клиент не найден")
    return db_customer

@router.delete("/{customer_id}")
def delete_customer_endpoint(customer_id: int, db: Session = Depends(get_db)):
    db_customer = delete_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Клиент не найден")
    return {"message": "Клиент удален"}