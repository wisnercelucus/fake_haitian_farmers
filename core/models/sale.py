from pydantic import BaseModel, EmailStr, field_validator, ValidationError
from enum import Enum
from typing import Optional
from datetime import date
import random


def random_int(min_val, max_val) -> int:
    random_int = random.randint(min_val, max_val)
    return random_int

def random_float(min_val, max_val) -> float:
    return random.uniform(min_val, max_val)


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

TYPE_LIST = [
    {
        "name": "Viande de chèvre",
        "unit": "lb",
        'max_price_unit': 800,
        'min_price_unit': 650,
        "currency": "HTG",
        'min_qty': 10,
        'max_qty': 3500,
    },
    {
        "name": "Bovin entier",
        "unit": "animal",
        'max_price_unit': 75000,
        'min_price_unit': 350000,
        "currency": "HTG",
        'min_qty': 5,
        'max_qty': 15,
    },
    {
        "name": "Lait de vache",
        "unit": "gallon",
        'max_price_unit': 450,
        'min_price_unit': 550,
        "currency": "HTG",
        'min_qty': 5,
        'max_qty': 50,
    },
    {
        "name": "Mouton entier",
        "unit": "animal",
        'max_price_unit': 17500,
        'min_price_unit': 40000,
        "currency": "HTG",
        'min_qty': 5,
        'max_qty': 25,
    },
    {
        "name": "Volaille",
        "unit": "animal",
        'max_price_unit': 750,
        'min_price_unit': 2000,
        "currency": "HTG",
        'min_qty': 20,
        'max_qty': 5000,
    },
    {
        "name": "Oeufs",
        "unit": "douzaine",
        'max_price_unit': 150,
        'min_price_unit': 200,
        "currency": "HTG",
        'min_qty': 500,
        'max_qty': 10000,
    },
    {
        "name": "Viande de mouton",
        "unit": "lb",
        'max_price_unit': 570,
        'min_price_unit': 700,
        "currency": "HTG",
        'min_qty': 20,
        'max_qty': 2500,
    }, 
    {
        "name": "Viande de bovin",
        "unit": "lb",
        'max_price_unit': 550,
        'min_price_unit': 700,
        "currency": "HTG",
        'min_qty': 20,
        'max_qty': 7500,
    },
]

class Sale(BaseModel):
    id: int
    partner_id: Optional[int]=None
    participant_id: Optional[int]=None
    partner_name: str
    type_of_product: str
    date: date
    currency: str
    qty: int
    unit_price: float
    unit: str
    total: float
    total_usd: float


    class Config:
        """Pydantic config class"""
        frozen = True


if __name__ == '__main__':
    pass
    
    