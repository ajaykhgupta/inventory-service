from fastapi import APIRouter, Request, Depends
from typing import List
from inventory.handler.inventory_handler import ProductHandler
from inventory.validators.common_validation import NotFoundException
from sqlalchemy.orm import Session
from inventory.product_schema import AddProduct, PatchProduct, ProductSchema
from inventory.connection_registry import get_db

router = APIRouter()


@router.get("/")
def root():
    return {"message": "hello world"}


@router.get("/product", response_model=List[AddProduct], status_code=200)
def get_products(db: Session = Depends(get_db), name: str = None, category: str = None):
    products = ProductHandler().get_products(db, name, category)
    if not products:
        raise NotFoundException
    return products


@router.get("/product/{product_id}", response_model=AddProduct, status_code=200)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = ProductHandler().get_product(db, product_id)
    if not product:
        raise NotFoundException
    return product


@router.post("/product", response_model=AddProduct, status_code=200)
def add_product(product_schema: AddProduct, db: Session = Depends(get_db)):
    product = ProductHandler().add_product(product_schema, db)
    return product


@router.post("/product/bulk-upload", status_code=200)
def bulk_upload_product(product_schema: List[ProductSchema], db: Session = Depends(get_db)):
    bulk_product = ProductHandler().bulk_upload_product(product_schema, db)
    if bulk_product:
        return {"response": "Bulk products uploaded successfully!!"}


@router.patch("/product/{product_id}", status_code=200)
def patch_product(product_id: int, product_schema: PatchProduct, db: Session = Depends(get_db)):
    product = ProductHandler().patch_product(product_id, product_schema, db)
    if product:
        return product
