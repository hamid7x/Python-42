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
