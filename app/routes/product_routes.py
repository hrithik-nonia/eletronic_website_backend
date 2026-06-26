import os
import uuid
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException

from app.schema.product_schema import ProductCreate
from app.utils.json_handler import add_product

router = APIRouter(prefix="/api/products", tags=["Products"])

UPLOAD_DIR = "app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/create")
async def create_product(
    product: ProductCreate = Depends(ProductCreate.as_form),
    image: UploadFile = File(...),
):
    # Image type validate karo
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    # Unique filename banao taaki overwrite na ho
    ext = os.path.splitext(image.filename)[1]
    filename = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    # Image disk pe save karo
    with open(file_path, "wb") as f:
        content = await image.read()
        f.write(content)

    # Product dict banao JSON mein save karne ke liye
    product_dict = product.model_dump()
    product_dict["id"] = str(uuid.uuid4())
    product_dict["image"] = filename

    saved_product = add_product(product_dict)

    return {"msg": "Product added successfully", "product": saved_product}