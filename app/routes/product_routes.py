from fastapi import APIRouter, Depends, UploadFile, File

# ----------pydantic model----------
from app.schema.product_schema import ProductCreate

# ---------------imports for admin------------
from app.controllers.product_controller import handle_create_product
from app.controllers.product_controller import handle_get_all_products_count
from app.controllers.product_controller import handle_get_active_products_count
from app.controllers.product_controller import handle_get_low_stock_products

# ---------------imports for user------------
from app.controllers.product_controller import handle_get_sale_products

router = APIRouter(prefix="/api/products", tags=["Products"])

# ---------------admin panel routes---------------
# create product
@router.post("/create" , tags=["admin routes"])
async def create_product(
    product: ProductCreate = Depends(ProductCreate.as_form),
    image: UploadFile = File(None),
):
    return await handle_create_product(product, image)

# get all products count for admin panel
@router.get("/count",tags=["admin routes"])
def get_all_products_count():
    return handle_get_all_products_count()

# get active product count
@router.get("/active_count",tags=["admin routes"])
def get_active_products_count():
    return handle_get_active_products_count()

# get low stock products count
@router.get("/low_stock_count",tags=["admin routes"])
def get_low_stock_products():
    return handle_get_low_stock_products()

# ---------------user routes---------------
# get which product in sale
@router.get("/sale",tags=["user routes"])
def get_sale_products(skip: int = 0, limit: int = 10):
    return handle_get_sale_products(skip, limit)



