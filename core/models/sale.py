from pydantic import BaseModel, EmailStr, field_validator, ValidationError
from enum import Enum
from typing import Optional
from datetime import date


class TypeOfProduct(str, Enum):
    goat_meat     = "Viande de chèvre"
    full_cattle   = "Bovin entier"
    cow_milk      = "Lait de vache"
    full_sheep    = "Mouton entier"
    poultry       = "Volaille"
    full_goat     = "Chèvre entière"
    eggs          = "Oeufs"
    sheep_meat    = "Viande de mouton"
    cattle_meat   = "Viande de bovin"


class Sale(BaseModel):
    id: Optional[int]=None
    partner_id: Optional[int]=None
    participant_id: Optional[int]=None
    type_of_product: str
    date: date
    qty: float
    total: float


    class Config:
        """Pydantic config class"""
        frozen = True


if __name__ == '__main__':
    pass
    
    