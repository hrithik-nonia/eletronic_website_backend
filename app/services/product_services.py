import os
import uuid

from fastapi import UploadFile, HTTPException
from app.repository.product_repository import get_all_products
from app.repository.product_repository import add_product


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)


async def save_product_image(image: UploadFile|None) -> str:
    if image is None:
        return None
    """Validates and saves the uploaded image, returns the generated filename."""
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    ext = os.path.splitext(image.filename)[1]
    filename = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    content = await image.read()
    with open(file_path, "wb") as f:
        f.write(content)

    return filename


async def create_product_with_image(product, image: UploadFile) -> dict:
    """Orchestrates image save + product persistence."""
    filename = await save_product_image(image)

    product_dict = product.model_dump()
    product_dict["id"] = str(uuid.uuid4())
    product_dict["image"] = filename

    saved_product = add_product(product_dict)
    return saved_product


# fliter product by sale price
def get_products_on_sale(skip: int = 0, limit: int = 10) -> list:
    """Returns only products that have a valid sale_price set."""
    products = get_all_products()
    sale_products = [
        p for p in products
        if p.get("sale_price") not in (None, "", 0)
    ]
    return sale_products[skip : skip + limit]