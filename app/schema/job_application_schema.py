from pydantic import BaseModel, Field,EmailStr
from typing import Annotated
from fastapi import Form
from datetime import date


class JobApplication(BaseModel):
  first_name:Annotated[str,Field(...,max_length=120)]
  last_name:Annotated[str,Field(...,max_length=120)]
  email:Annotated[EmailStr,Field(...,max_length=120)]
  phone:Annotated[int,Field(...)]
  position:Annotated[str,Field(...,max_length=120)]
  start_date:Annotated[date,Field(...)]

  @classmethod
  def applicant(
    cls,
    first_name:str=Form(...),
    last_name:str=Form(...),
    email:EmailStr=Form(...),
    phone:int=Form(...),
    position:str=Form(...),
    start_date:date=Form(...),
  ):
    return cls(
      first_name=first_name,
      last_name=last_name,
      email=email,
      phone=phone,
      position=position,
      start_date=start_date
    )

  
