import os
import uuid

from fastapi import UploadFile, HTTPException

from app.repository.product_repository import add_product

UPLOAD_DIR = "app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


async def save_product_image(image: UploadFile) -> str:
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