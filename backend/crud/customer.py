from sqlalchemy.orm import Session
from models.customer import Customer
from schemas.customer  import CustomerCreate, CustomerUpdate

def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Customer).offset(skip).limit(limit).all()

def get_customer(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()

def create_customer(db: Session, customer: CustomerCreate):
    existing = db.query(Customer).filter(Customer.email == customer.email).first()
    if existing:
        raise ValueError("Email уже зарегистрирован")
        
    db_customer = Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def update_customer(db: Session, customer_id: int, customer_update: CustomerUpdate):
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not db_customer:
        return None
        
    update_data = customer_update.dict(exclude_unset=True)
    
    if 'email' in update_data and update_data['email']:
        existing = db.query(Customer).filter(
            Customer.email == update_data['email'],
            Customer.id != customer_id
        ).first()
        if existing:
            raise ValueError("Email уже существует")
    
    for key, value in update_data.items():
        setattr(db_customer, key, value)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def delete_customer(db: Session, customer_id: int):
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if db_customer:
        db.delete(db_customer)
        db.commit()
    return db_customer