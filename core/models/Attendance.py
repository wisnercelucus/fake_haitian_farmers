from pydantic import BaseModel

class Attendance(BaseModel):
    id: int
    pass


if __name__ == '__main__':
    print("A new class")