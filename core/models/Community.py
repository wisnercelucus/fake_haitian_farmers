from pydantic import BaseModel
from typing import Optional

class Community(BaseModel):
    id: int
    name: str
    population: Optional[float] = None
    gps_lat: Optional[float] = None
    gps_lng: Optional[float] = None
    section_id: Optional[int] = None
    
if __name__ == '__main__':
    print("A new class")