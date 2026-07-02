from fastapi import UploadFile , HTTPException

# -----------import pydantic model-------------
from app.schema.job_application_schema import JobApplication

# =================================================
from app.services.job_portal_service import serv_save_applicant_with_resume


async def handle_create_applicant(application:JobApplication, resume:UploadFile)->dict:
  saved_applicant=await serv_save_applicant_with_resume(application,resume)
  if not saved_applicant :
    raise HTTPException(status_code=400 , detail="Bad request")
  raise HTTPException(status_code=201 , detail="application submited successfully")

async def handle_create_applicant(
    application: JobApplication,
    resume: UploadFile,
):
    
  return await serv_save_applicant_with_resume(application, resume)
