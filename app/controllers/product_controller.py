from fastapi import UploadFile

from app.schema.product_schema import ProductCreate
from app.services.product_services import create_product_with_image
from app.services.product_services import get_products_on_sale


async def handle_create_product(product: ProductCreate, image: UploadFile) -> dict:
    saved_product = await create_product_with_image(product, image)
    return {"msg": "Product added successfully", "product": saved_product}

def handle_get_sale_products(skip: int = 0, limit: int = 10) -> list:
    return get_products_on_sale(skip, limit)