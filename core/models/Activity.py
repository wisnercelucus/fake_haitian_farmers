from pydantic import BaseModel
from datetime import date
from typing import Optional

class Activity(BaseModel):
    id: int
    name: str
    community_id: int
    partner_id: int
    total_participant: Optional[int]=None
    total_male_participant: Optional[int]=None
    total_female_participant: Optional[int]=None
    total_youth_participant: Optional[int]=None
    date: date


if __name__ == '__main__':
    print("A new class")