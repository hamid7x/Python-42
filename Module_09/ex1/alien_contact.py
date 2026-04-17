from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum


class ContactType(str, Enum):
    radio = "radio",
    visual = "visual",
    physical = "telepathic",
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    def validate_rules() -> None:
        if not self.contact_id.start



def display_alien(alien: AlienContact) -> None:
    print(f"ID: {alien.contact_id}")
    print(f"Type: {alien.contact_type}")
    print(f"location: {alien.location}")
    print(f"Signal: {alien.signal_strength}%")
    print(f"Duration: {alien.duration_minutes}%")
    print(f"Witness: {alien.witness_count}")
    print(f"Message: {alien.message_received}")


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("=" * 40)
    print("Valid contact report")
    try:
        alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2026-04-15 16:30:00",
            location=" Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength="8.5",
            duration_minutes="45",
            witness_count="5",
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
        display_alien(alien)
    except ValidationError as e:
        print(f"{e.errors()[0]['msg']}")

    
