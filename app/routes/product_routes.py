from fastapi import APIRouter, Depends, UploadFile, File

from app.schema.product_schema import ProductCreate
from app.controllers.product_controller import handle_create_product
from app.controllers.product_controller import handle_get_sale_products

router = APIRouter(prefix="/api/products", tags=["Products"])


# create product
@router.post("/create")
async def create_product(
    product: ProductCreate = Depends(ProductCreate.as_form),
    image: UploadFile = File(None),
):
    return await handle_create_product(product, image)


# get which product in sale
@router.get("/sale")
def get_sale_products(skip: int = 0, limit: int = 10):
    return handle_get_sale_products(skip, limit)