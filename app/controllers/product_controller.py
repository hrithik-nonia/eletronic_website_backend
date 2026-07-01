from fastapi import UploadFile , HTTPException

# ----------imports for pydantic models----------
from app.schema.product_schema import ProductCreate

# ----------imports for admin----------
from app.services.product_services import create_product_with_image
from app.services.product_services import get_products_count
from app.services.product_services import get_active_products_count
from app.services.product_services import get_low_stock_products_count
from app.services.product_services import get_out_of_stock_products_count
from app.services.product_services import service_get_all_products

# ----------imports for user----------
from app.services.product_services import get_products_on_sale
from app.services.product_services import get_product_by_id
from app.services.product_services import get_product_by_category



# --------------admin functions----------------
async def handle_create_product(product: ProductCreate, image: UploadFile) -> dict:
    saved_product = await create_product_with_image(product, image)
    return {"msg": "Product added successfully", "product": saved_product}

# get all products count
def handle_get_all_products_count() -> int:
    count = get_products_count()
    if count == 0:
        raise HTTPException(status_code=404, detail="No products found")
    return count

# get active products count
def handle_get_active_products_count() -> int:
    active_count = get_active_products_count()

    if active_count == 0:
        raise HTTPException(status_code=404, detail="No active products found")

    return active_count

# get low stock products count
def handle_get_low_stock_products() -> int:
    low_stock_count = get_low_stock_products_count()

    if low_stock_count == 0:
        raise HTTPException(status_code=404, detail="No low stock products found")

    return low_stock_count

# get all products
def handle_get_all_products(skip: int = 0, limit: int = 10) -> list:
    products=service_get_all_products(skip, limit)
    if len(products) == 0:
        raise HTTPException(status_code=404, detail="No products found")

    return products

# get out of stock products count
def handle_get_out_of_stock_products() -> int:
    out_of_stock_count = get_out_of_stock_products_count()
    
    if out_of_stock_count == 0:
        raise HTTPException(status_code=404, detail="No out of stock products found")
    
    return out_of_stock_count

# --------------user functions------------------
def handle_get_sale_products(skip: int = 0, limit: int = 10) -> list:
    products=get_products_on_sale(skip, limit)
    if len(products) == 0:
        raise HTTPException(status_code=404, detail="No products found")
    return products

# get product by id
def handle_get_product_by_id(product_id: str) -> dict:
    product=get_product_by_id(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# get product by category
def handle_get_product_by_category(category: str) -> list:
    products=get_product_by_category(category)
    if len(products) == 0:
        raise HTTPException(status_code=404, detail="No products found")
    return products

