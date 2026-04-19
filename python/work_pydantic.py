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
y = "33"
print(y)

class Testing(BaseModel):
    age: float
try:
    s = Testing(age="33")
    print(s.age)
except ValidationError as e:
    print(f"{e.errors()[0]['msg']}")

print(int(44.3))
# print(int("343.3")) # this is error


class myClass(BaseModel):
    # def __init__(self, **kwargs):
    #     annotations = self.__annotations__
    #     for field_name, field_type in annotations.items():
    #         value = kwargs.get(field_name)
    #         try:
    #             value = field_type(value)
    #         except:
    #             raise ValidationError("...")
            
    #         setattr(self, field_name, value)
    #     self.__pydantic_fields_set__ = set(kwargs.keys())

    name: str = Field(min_length=3, max_length=30)
    age: int
    city: str = "Paris"


print(myClass.__annotations__)
try:
    c1 = myClass(name='jhon', age=200)
    c2 = myClass(name='jhon', age=200, city="London")

    print(c1 == c2)
    print(c1 is c2)
    print(c1.__pydantic_fields_set__)
    print(c2.__pydantic_fields_set__)
except Exception as e:
    print(e)

print('hi', myClass.model_fields)
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)
print(a is b)
print(a == c)
print(a is c)

x = 10
y = 10
print(x == y)
print(x is y)

x = 1000
y = 1000
print('hi', x is y)

name1 = 'jhon'
name2 = 'jhon'
print(name1 == name2)
print(name1 is name2)


def get_number():
    return 1000

x = 1000
y = get_number()
print(x is y)

x = 1000
y = int("1000")
print(x is y)

a = [1, 2, 3]
b = a  # b points to SAME object as a

b.append(4)
print(a)  # [1, 2, 3, 4] ← a is affected too!


class MyClass:
    name: str
    age: int


class my_class:
    pass


Dog = type('Dog', (), {})
d = Dog()
d.name = 'bob'
print(d.name)
print(type(Dog))
print(type(my_class))
print(type(myClass))
print(MyClass.__name__)
print(MyClass.__bases__)
print(MyClass.__dict__)
print()
print(type(object))   # who created object itself?
print(type(type))     # who created type itself?
print()
print(isinstance(type, object))   # is type an instance of object?
print(isinstance(object, type))   # is object an instance of type?