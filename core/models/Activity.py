from pydantic import BaseModel

class Activity(BaseModel):
    id: int

if __name__ == '__main__':
    print("A new class")