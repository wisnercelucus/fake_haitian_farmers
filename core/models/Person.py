from pydantic import BaseModel, EmailStr, field_validator, ValidationError
from enum import Enum
from typing import Optional
from datetime import date


class Sex(str, Enum):
    male = "Male"
    female = "Female"
    other = "Other"


class TypeID(str, Enum):
    nif = "NIF"
    cin = "CIN"
    passport = "Passport"

class TypePerson(str, Enum):
    type_1: "Les gens au gouvernement"
    type_2: "Personnes travaillant dans des entreprises du secteur privé soutenues par le gouvernement américain"
    type_3: "Les gens de la société civile"
    type_4: "Petit producteur"
    type_5: "Producteur non-petit exploitant"
    type_6: "Other"


class Person(BaseModel):
    first_name: str
    last_name: str
    address: str
    sex: Sex
    birth_date: Optional[date]=None
    birth_year: Optional[int] = None
    age: Optional[int] = None
    type_person: Optional[TypePerson] = None
    type_id: Optional[TypeID]=None
    cin: Optional[str] = None
    nif: Optional[str] = None
    passport: Optional[str] = None
    photo: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_1: str
    phone_2: Optional[str] = None
    nb_goat: Optional[int] = None
    nb_cattle: Optional[int] = None
    nb_sheep: Optional[int] = None
    nb_poultry: Optional[int] = None
    gps_lat:Optional[float] = None
    gps_lng:Optional[float] = None
    date_joined: Optional[date]=None


    @field_validator('phone_1')
    def validate_phone_1(cls, value):
        if len(value) != 8 or not value.isdigit():
            raise ValueError('phone_1 must be an 8-digit number')
        return value

    @field_validator('phone_2')
    def validate_phone_2(cls, value):
        if len(value) != 8 or not value.isdigit():
            raise ValueError('phone_2 must be an 8-digit number')
        return value

if __name__ == '__main__':
    try:
        person = Person(first_name="Wisner", 
                        last_name="Celucus", 
                        sex=Sex.male, 
                        address="Tabarre", 
                        phone_1="33511641")
        
        print(person)
    except Exception as e:
        print(e)
    
    