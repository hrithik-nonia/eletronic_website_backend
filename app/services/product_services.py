import os
import uuid

from fastapi import UploadFile, HTTPException

# ----------imports for admin----------
from app.repository.product_repository import add_product


# ----------imports for user----------
from app.repository.product_repository import get_all_products




# ----------admin functions----------
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
    product_dict["sku"] = f"SKU-{uuid.uuid4().hex[:8].upper()}"
    product_dict["id"] = str(uuid.uuid4())
    product_dict["image"] = filename

    saved_product = add_product(product_dict)
    return saved_product

# get all products count
def get_products_count() -> int:
    """Returns the total number of products."""
    products = get_all_products()
    return len(products)


# get active products count
def get_active_products_count() -> int:
    """Returns the number of active products."""
    products = get_all_products()
    count =0
    for p in products:
        if p.get("stock") >0:
            count +=1
    return count

# get low stock products count
def get_low_stock_products_count() -> int:
    """Returns the number of products with stock less than 10."""
    products = get_all_products()
    count =0
    for p in products:
        if p.get("stock") < 10:
            count +=1
    return count


# get all products
def service_get_all_products() -> list :
    return get_all_products()
    

# ----------user functions----------
# fliter product by sale price
def get_products_on_sale(skip: int = 0, limit: int = 10) -> list:
    """Returns only products that have a valid sale_price set."""
    products = get_all_products()
    sale_products = [
        p for p in products
        if p.get("sale_price") not in (None, "", 0)
    ]
    return sale_products[skip : skip + limit]