from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Any
from datetime import datetime
from enum import Enum


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def crew_rules(self) -> 'SpaceMission':
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")
        ranks = [c.rank for c in self.crew]
        if Rank.commander not in ranks and Rank.captain not in ranks:
            raise ValueError(
                "Mission must have at least one Commander or Captain")
        experienced = len([c for c in self.crew if c.years_experience >= 5])
        total_crew = len(self.crew)
        precnt_expre = experienced / total_crew * 100
        if self.duration_days > 365 and not precnt_expre >= 50:
            raise ValueError(
                "Long missions require at least 50% experienced crew")
        active_crew = [c.is_active for c in self.crew]
        if not all(active_crew):
            raise ValueError("All crew members must be active")
        return self


def display_mission(mission: SpaceMission) -> None:
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for c in mission.crew:
        print(f"- {c.name} ({c.rank.value}) - {c.specialization}")
    print()


def main() -> None:
    missions_data: list[dict[str, Any]] = [
        {
            "mission_id": "M2026_MARS",
            "mission_name": "Mars Colony Establishment",
            "destination": "Mars",
            "launch_date": "2026-05-01T10:00:00",
            "duration_days": 900,
            "budget_millions": 2500.0,
            "crew": [
                    {
                        "member_id": "C01",
                        "name": "Sarah Connor",
                        "rank": "commander",
                        "age": 45,
                        "specialization": "Mission Command",
                        "years_experience": 20
                    },
                    {
                        "member_id": "C02",
                        "name": "John Smith",
                        "rank": "lieutenant",
                        "age": 34,
                        "specialization": "Navigation",
                        "years_experience": 6
                    },
                    {
                        "member_id": "C03",
                        "name": "Alice Johnson",
                        "rank": "officer",
                        "age": 29,
                        "specialization": "Engineering",
                        "years_experience": 5
                    }
                ]

        },
        {
            "mission_id": "M2026_MARS",
            "mission_name": "Mars Colony Establishment",
            "destination": "Mars",
            "launch_date": "2026-05-01T10:00:00",
            "duration_days": 900,
            "budget_millions": 2500.0,
            "crew": [
                    {
                        "member_id": "C01",
                        "name": "Sarah Connor",
                        "rank": "cadet",
                        "age": 45,
                        "specialization": "Mission Command",
                        "years_experience": 20
                    },
                    {
                        "member_id": "C02",
                        "name": "John Smith",
                        "rank": "lieutenant",
                        "age": 34,
                        "specialization": "Navigation",
                        "years_experience": 6
                    },
                    {
                        "member_id": "C03",
                        "name": "Alice Johnson",
                        "rank": "officer",
                        "age": 29,
                        "specialization": "Engineering",
                        "years_experience": 5
                    }
                ]

        },

    ]
    print("Space Mission Crew Validation")
    for d in missions_data:
        try:
            mission = SpaceMission(**d)
            print("=" * 40)
            print("Valid mission created:")
            display_mission(mission)
        except ValidationError as e:
            print("=" * 40)
            print("Expected validation error:")
            print(e.errors()[0]['msg'].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
