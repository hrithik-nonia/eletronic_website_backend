from fastapi import APIRouter, Depends, UploadFile, File

# --------------pydantic model---------------
from app.schema.job_application_schema import JobApplication

# =================================================
from app.controllers.job_portal_controller import handle_create_applicant


router = APIRouter(prefix="/api/job", tags=["job portal"])



@router.post("/application",tags=["job application"])
async def job_application(
    application: JobApplication = Depends(JobApplication.applicant),
    resume: UploadFile = File(...)
):
    return await handle_create_applicant(application, resume)