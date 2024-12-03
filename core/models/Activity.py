from pydantic import BaseModel
from datetime import date
from typing import Optional
from enum import Enum


class TypeOfActivity(str, Enum):
    capacity_building = "Formation/renforcement des capacités"
    distrib_intrant = "Distribution d'intrants"
    reunion_de_plaidoyer = "Réunion de plaidoyer"
    liaison_avec_le_marche = "Liaison avec le marché"
    autre="Autre"



class Activity(BaseModel):
    id: int
    name: str
    community_id: int
    partner_id: int
    activity_type: str
    total_participant: Optional[int]=None
    total_male_participant: Optional[int]=None
    total_female_participant: Optional[int]=None
    total_male_youth_participant: Optional[int]=None
    total_female_youth_participant: Optional[int]=None
    total_youth_participant: Optional[int]=None
    description: Optional[str]=None
    date: date

    #Formation/
    #


if __name__ == '__main__':
    print("A new class")