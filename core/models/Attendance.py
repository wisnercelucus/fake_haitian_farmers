from pydantic import BaseModel

class Attendance(BaseModel):
    id: int
    participant_id: int
    activity_id: int


if __name__ == '__main__':
    print("A new class")