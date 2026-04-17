from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class User(BaseModel):
    full_name: str = Field(min_length=5, max_length=30,
                           description="User full name")
    age: int = Field(ge=0, le=120)
    username: Optional[str] = None


class Event(BaseModel):
    date: datetime


try:
    u = User(full_name="Jhon Doe", age="23", username="Jhone_22")
    print(u.full_name)
    print(u.age)

    e = Event(date="2024-01-01T10:00:00")
    print(e.date)
except ValidationError as e:
    print(f"{e.errors()[0]['msg']}")


age: int = Field(ge=18, le=80)
x: int = Field(ge=18, le=80)
# print(age)
# print(x)


class Test(BaseModel):
    age: int = Field(default=220, ge=10, le=30)

    # pydantic doesn't validate the default values automaticly
    # force to validate the default value
    model_config = {
        "validate_default": True
    }


try:
    t = Test()
    print(t.age)
except ValidationError as e:
    print(f"{e.errors()[0]['msg']}")

age: int = Field(ge=10, le=44)
age = 99
print(age)

# Implicit
x = 5
print(type(x))

# Explicit
y: int = "x"
print(type(y))
y = "abc"
print(y)

class Testing(BaseModel):
    age: int

s = Testing(age="22")
print(s.age)

