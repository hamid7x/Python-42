from pydantic import BaseModel  # type: ignore
from typing import Union, Optional


class MyFirstModel(BaseModel):
    first_name: str
    last_name: str


class MySecondModel(BaseModel):
    first_name: str
    middle_name: Union[str, None]
    title: Optional[str]
    last_name: str


validating = MyFirstModel(first_name="marc", last_name="nealer")
print(validating.first_name)
print(validating.last_name)


val = MySecondModel(
    first_name="marc",
    middle_name=None,
    title="",
    last_name="wilson"
    )

print(val)