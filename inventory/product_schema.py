from pydantic import BaseModel, StrictStr, StrictInt
from inventory.validators.inventory_validator import Product


class AddProduct(BaseModel):
    name: StrictStr = Product.name
    count: StrictInt = Product.count
    category: StrictStr = Product.category
    price: StrictInt = Product.price
    status: StrictStr = Product.status

    class Config:
        orm_mode = True
