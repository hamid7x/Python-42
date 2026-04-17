"""
Manual validation (WITHOUT Pydantic)
"""


data = {
    "name": "john",
    "age": "20",
    "signal": "8.5",
    "contact_type": "telepathic",
    "witness_count": 1
}

try:
    # --- parsing step (manual) ---
    name = str(data["name"])
    age = int(data["age"])
    signal = float(data["signal"])
    contact_type = str(data["contact_type"])
    witness_count = int(data["witness_count"])

    # --- validation rules (manual) ---
    if len(name) < 3:
        raise ValueError("name too short")

    if age < 18 or age > 70:
        raise ValueError("age out of range")

    if signal < 0 or signal > 10:
        raise ValueError("signal out of range")

    if contact_type not in ["radio", "visual", "physical", "telepathic"]:
        raise ValueError("invalid contact type")

    # --- cross-field rule (EX1 logic) ---
    if contact_type == "telepathic" and witness_count < 3:
        raise ValueError("telepathic contact requires at least 3 witnesses")

    print("VALID DATA:", name, age, signal, contact_type, witness_count)

except Exception as e:
    print("ERROR:", str(e))


"""
Pydantic version (WITH Pydantic)
"""

from pydantic import BaseModel, Field, ValidationError
from enum import Enum


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(ge=18, le=70)
    signal: float = Field(ge=0, le=10)
    contact_type: ContactType
    witness_count: int = Field(ge=1, le=100)


    def model_post_init(self, __context):
        if self.contact_type == "telepathic" and self.witness_count < 3:
            raise ValueError("telepathic contact requires at least 3 witnesses")




data = {
    "name": "john",
    "age": "20",
    "signal": "8.5",
    "contact_type": "telepathic",
    "witness_count": 1
}

try:
    contact = AlienContact(**data)
    print("VALID DATA:", contact)

except ValidationError as e:
    print(e.errors()[0]["msg"])
