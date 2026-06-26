from pydantic import BaseModel, Field
from typing import Optional, Annotated
from fastapi import Form


class ProductCreate(BaseModel):
    name: Annotated[str,Field(..., max_length=120)]
    description: Annotated[Optional[str], Field(max_length=1000) ]=None
    price: Annotated[float ,  Field(..., gt=0)]          
    sale_price:Annotated[ Optional[float],Field(gt=0)] = None
    weight: Annotated[Optional[float],Field(gt=0)] = None
    dimensions: Optional[str] = None
    stock:Annotated[ int , Field(..., ge=0) ]           # negative nahi ho sakta
    category: Annotated[str,Field(...,max_length=120)]

    @classmethod
    def as_form(
        cls,
        name: str = Form(...),
        description: Optional[str] = Form(None),
        price: float = Form(...),
        sale_price: Optional[float] = Form(None),
        weight: Optional[float] = Form(None),
        dimensions: Optional[str] = Form(None),
        stock: int = Form(...),
        category: str = Form(...),
    ):
        return cls(
            name=name,
            description=description,
            price=price,
            sale_price=sale_price,
            weight=weight,
            dimensions=dimensions,
            stock=stock,
            category=category,
        )