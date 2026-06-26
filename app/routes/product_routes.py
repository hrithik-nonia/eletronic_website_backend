from fastapi import APIRouter, Depends, UploadFile, File

from app.schema.product_schema import ProductCreate
from app.controllers.product_controller import handle_create_product

router = APIRouter(prefix="/api/products", tags=["Products"])


@router.post("/create")
async def create_product(
    product: ProductCreate = Depends(ProductCreate.as_form),
    image: UploadFile = File(...),
):
    return await handle_create_product(product, image)