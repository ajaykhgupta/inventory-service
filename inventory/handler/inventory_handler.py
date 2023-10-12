from inventory.models import Product
from inventory.validators.common_validation import BadRequestException


class ProductHandler:

    @staticmethod
    def get_products(db, name, category):
        if name and category:
            products = db.query(Product).filter(Product.name == name, Product.category == category).all()
        elif name:
            products = db.query(Product).filter(Product.name == name).all()
        elif category:
            products = db.query(Product).filter(Product.category == category).all()
        else:
            products = db.query(Product).all()
        return products

    @staticmethod
    def get_product(db, product_id):
        product = db.query(Product).filter(Product.id == product_id).first()
        return product

    @staticmethod
    def add_product(product_schema, db):
        product = Product(**product_schema.dict())
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def bulk_upload_product(product_schema, db):
        for each in product_schema:
            product = Product(**each.dict())
            db.add(product)
            db.commit()
            db.refresh(product)
        return True

    @staticmethod
    def patch_product(product_id, product_schema, db):
        item = db.query(Product).filter(Product.id == product_id)
        if not item:
            raise BadRequestException(status_code=400,
                                      detail="Product with the given id {} not found!".format(product_id))
        product_item = item.first()
        update_data = product_schema.dict(exclude_unset=True)
        item.filter(Product.id == product_id).update(update_data, synchronize_session=False)
        db.commit()
        db.refresh(product_item)
        return product_item
