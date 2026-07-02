import os
import uuid
from fastapi import UploadFile, HTTPException

from app.repository.job_portal_repository import add_application

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

UPLOAD_DIR = os.path.join(BASE_DIR, "upload_resume")
os.makedirs(UPLOAD_DIR, exist_ok=True)


async def save_resume(resume: UploadFile | None) -> str | None:
    if resume is None:
        return None

    # Validate PDF
    if resume.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="File must be a PDF"
        )

    ext = os.path.splitext(resume.filename)[1]
    filename = f"{uuid.uuid4().hex}{ext}"

    file_path = os.path.join(UPLOAD_DIR, filename)

    content = await resume.read()

    with open(file_path, "wb") as f:
        f.write(content)

    return filename


async def serv_save_applicant_with_resume(application, resume: UploadFile | None) -> dict:
    filename = await save_resume(resume)

    application_dict = application.model_dump(mode="json")
    application_dict["id"] = str(uuid.uuid4())
    application_dict["resume"] = filename

    saved_applicant = add_application(application_dict)

    return saved_applicant