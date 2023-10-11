from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from inventory.connection_registry import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    count = Column(Integer)
    category = Column(String)
    price = Column(Integer)
    status = Column(String)
