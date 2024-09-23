from pydantic import BaseModel, EmailStr, field_validator
from enum import Enum
from typing import Optional
from datetime import date


class Partner(BaseModel):
    id: Optional[int]=None
    name: str
    acronym: str
    address: str
    email: Optional[str]=None #Optional[EmailStr] = None
    phone_1: str
    phone_2: Optional[str] = None
    created_in: int
    leader_name: str
    leader_age: int
    leader_sex: str
    nb_goat: Optional[int] = None
    nb_cattle: Optional[int] = None
    nb_sheep: Optional[int] = None
    nb_poultry: Optional[int] = None
    gps_lat:Optional[float] = None
    gps_lng:Optional[float] = None
    date_joined: Optional[date]=None
    community_id: Optional[int]


    @field_validator('phone_1')
    def validate_phone_1(cls, value):
        if value in [None, '']:
            return value
        if len(value) != 8 or not value.isdigit():
            raise ValueError('phone_1 must be an 8-digit number')
        return value

    @field_validator('phone_2')
    def validate_phone_2(cls, value):
        if value in [None, '']:
            return value
        if len(value) != 8 or not value.isdigit():
            raise ValueError('phone_2 must be an 8-digit number')
        return value

    class Config:
        """Pydantic config class"""
        frozen = True


if __name__ == '__main__':
    try:
        partner = Partner(
                        id=1,
                        name="Wisner", 
                        address="Tabarre", 
                        phone_1="33511641")
        
        print(partner)
    except Exception as e:
        print(e)
    
    