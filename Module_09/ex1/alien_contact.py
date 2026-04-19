from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_rules(self) -> 'AlienContact':

        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.telepathic
           and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (>7.0) must include a message")
        return self


def display_alien(alien: AlienContact) -> None:
    print(f"ID: {alien.contact_id}")
    print(f"Type: {alien.contact_type.value}")
    print(f"location: {alien.location}")
    print(f"Signal: {alien.signal_strength}/10")
    print(f"Duration: {alien.duration_minutes} minutes")
    print(f"Witness: {alien.witness_count}")
    print(f"Message: '{alien.message_received}'")
    print()


def main() -> None:
    alien_data: list[dict[str, Any]] = [
        {
            "contact_id": "AC_2024_001",
            "timestamp": "2026-04-15T16:30:00",
            "location": " Area 51, Nevada",
            "contact_type": ContactType.radio,
            "signal_strength": 8.9,
            "duration_minutes": 45,
            "witness_count": 5,
            "message_received": "Greetings from Zeta Reticuli",
            "is_verified": True
        },
        {
            "contact_id": "AC_2024_001",
            "timestamp": "2026-04-15T16:30:00",
            "location": " Area 51, Nevada",
            "contact_type": ContactType.telepathic,
            "signal_strength": 8.45,
            "duration_minutes": 45,
            "witness_count": 1,
            "message_received": "Greetings from Zeta Reticuli",
            "is_verified": True
        },
    ]

    print("Alien Contact Log Validation")
    for d in alien_data:
        print("=" * 40)
        try:
            alien = AlienContact(**d)
            print("Valid contact report")
            display_alien(alien)
        except ValidationError as e:
            print("Expected validation error:")
            print(e.errors()[0]['msg'].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
