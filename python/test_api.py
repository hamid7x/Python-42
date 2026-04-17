from user_data import data
from pydantic import BaseModel, Field, ValidationError


class User(BaseModel):
    name: str = Field(min_length=3, max_length=40)
    age: int = Field(ge=18, le=70)

class NormalUser:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"(name={self.name}, age={self.age})"
print("hi hello world")
try:
    nu = NormalUser(**data)
    print(nu)
    u = User(**data)
    print(u)
except ValidationError as e:
    print(f"{e.errors()[0]['msg']}")

