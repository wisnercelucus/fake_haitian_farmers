from pydantic import BaseModel, EmailStr, field_validator, ValidationError
from enum import Enum
from typing import Optional
from datetime import date


class TypeOfProduct(str, Enum):
    male = "Male"
    female = "Female"
    other = "Other"


class Sale(BaseModel):
    id: Optional[int]=None
    partner_id: Optional[int]=None
    participant_id: Optional[int]=None
    type_of_product: str


    class Config:
        """Pydantic config class"""
        frozen = True


if __name__ == '__main__':
    pass
    
    