from pydantic import BaseModel
from typing import Optional


class Department(BaseModel):
    id: int
    name: str
    population: Optional[float] = None
    gps_lat: Optional[float] = None
    gps_lng: Optional[float] = None


if __name__ == '__main__':
    print("A new class")