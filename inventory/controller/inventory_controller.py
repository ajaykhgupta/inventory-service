from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from inventory.models import Product
from inventory.connection_registry import Base, SessionLocal, engine
from inventory.product_schema import AddProduct

router = APIRouter()
Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def root():
    return {"message": "hello world"}


@router.get("/product", status_code=200)
def get_product(db: Session = Depends(get_db)):
    return db.query(Product).all()


@router.post("/product", status_code=200)
def add_product(product_schema: AddProduct, db: Session = Depends(get_db)):
    product = Product(**product_schema.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
