from pydantic import BaseModel, StrictStr, StrictInt
from typing import List
from inventory.validators.inventory_validator import Product


class AddProduct(BaseModel):
    id: StrictInt = Product.entity_id
    name: StrictStr = Product.name
    count: StrictInt = Product.count
    category: StrictStr = Product.category
    price: StrictInt = Product.price
    status: StrictStr = Product.status

    class Config:
        orm_mode = True


class PatchProduct(BaseModel):
    count: StrictInt | None
    price: StrictInt | None
    status: StrictStr | None

    class Config:
        orm_mode = True


class ProductSchema(BaseModel):
    id: int | None
    name: str | None
    count: int | None
    category: str | None
    price: int | None
    status: str | None

    class Config:
        orm_mode = True
