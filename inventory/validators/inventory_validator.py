from pydantic import Field


class Product:
    entity_id = Field(..., alias="id")
    name = Field(...)
    count = Field(...)
    category = Field(...)
    price = Field(...)
    status = Field(...)
