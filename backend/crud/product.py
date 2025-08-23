from sqlalchemy.orm import Session
from models.product import Product
from schemas.product import ProductCreate, ProductUpdate

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product_update: ProductUpdate):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        return None
    
    update_data = product_update.dict(exclude_unset=True)
    
    if 'sku' in update_data and update_data['sku'] != db_product.sku:
        existing = db.query(Product).filter(
            Product.sku == update_data['sku'],
            Product.id != product_id
        ).first()
        if existing:
            raise ValueError("Артикул уже существует")
    
    for key, value in update_data.items():
        setattr(db_product, key, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product