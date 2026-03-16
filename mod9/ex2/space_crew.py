
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, model_validator
from typing_extensions import Self
from datetime import datetime


class RankEnum(Enum):
    cadet = 1
    officer = 2
    lieutenant = 3
    captain = 4
    commander = 5


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: RankEnum
    age: int = Field(ge=18, le=80)
    specialisation: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: Optional[bool] = Field(default=True)

    def show(self, tab: str = "\n    ") -> None:
        print(tab, end="---MEMBER-INFO---:")
        print(
            tab,
            "member_id:",
            self.member_id,
            tab,
            "name:",
            self.name,
            tab,
            "rank:",
            self.rank,
            tab,
            "age:",
            self.age,
            tab,
            "specialisation:",
            self.specialisation,
            tab,
            "years_experience:",
            self.years_experience,
            tab,
            "is_active:",
            self.is_active
        )


class SpaceMission(BaseModel):

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validation(self) -> Self:

        if self.mission_id[:1] != "M":
            raise ValueError("Mission ID must start with \"M\"")

        check = False
        valid = 0
        for elem in self.crew:
            if elem.rank.value > 3:
                check = True
            if elem.years_experience > 4:
                valid += 1
            if not elem.is_active:
                raise ValueError(
                    f"{elem.member_id} not active, \
All crew members must be active")

        if not check:
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            if valid < (len(self.crew) / 2):
                raise ValueError(
                    "Long missions (> 365 days) \
need 50% experienced crew (5+ years)")

        return self

    def add_member(self, obj: CrewMember) -> None:
        self.crew.append(obj)

    def show(self) -> None:
        print("MISSION INFORMATIONS")
        print(
            "mission_id:",
            self.mission_id,
            "\nmission_name:",
            self.mission_name,
            "\ndestination:",
            self.destination,
            "\nlaunch_date:",
            self.launch_date,
            "\nduration_days:",
            self.duration_days,
            "\nmission_status:",
            self.mission_status,
            "\nbudget_millions:",
            self.budget_millions
        )
        print("member(s):")
        for elem in self.crew:
            elem.show()
        print("")


def main() -> None:
    first_member = CrewMember(
        member_id="001",
        name="elwin",
        rank=RankEnum.cadet,
        age=21,
        specialisation="mecanic",
        years_experience=3
    )
    second_member = CrewMember(
        member_id="002",
        name="jessie",
        rank=RankEnum.commander,
        age=27,
        specialisation="pilot",
        years_experience=9
    )
    third_member = CrewMember(
        member_id="003",
        name="payton",
        rank=RankEnum.cadet,
        age=30,
        specialisation="cartographer",
        years_experience=2
    )
    mission1 = SpaceMission(
        mission_id="M001|001",
        mission_name="yolo",
        destination="andromed",
        launch_date=datetime.now(),
        duration_days=63,
        crew=[first_member, second_member],
        budget_millions=2.052
    )
    mission1.mission_status = "finished"
    mission1.show()
    try:
        mission1 = SpaceMission(
            mission_id="001|001",
            mission_name="yolo",
            destination="andromed",
            launch_date=datetime.now(),
            duration_days=63,
            crew=[first_member],
            budget_millions=2.052
        )
        mission1.mission_status = "finished"
    except Exception as e:
        print("------------------------------------- Error Occured:", e)
    try:
        mission1 = SpaceMission(
            mission_id="M001|001",
            mission_name="yolo",
            destination="andromed",
            launch_date=datetime.now(),
            duration_days=63,
            crew=[first_member],
            budget_millions=2.052
        )
        mission1.mission_status = "finished"
    except Exception as e:
        print("------------------------------------- Error Occured:", e)
    try:
        mission1 = SpaceMission(
            mission_id="M001|001",
            mission_name="yolo",
            destination="andromed",
            launch_date=datetime.now(),
            duration_days=401,
            crew=[first_member, second_member, third_member],
            budget_millions=2.052
        )
        mission1.mission_status = "finished"
    except Exception as e:
        print("------------------------------------- Error Occured:", e)
    try:
        second_member.is_active = False
        mission1 = SpaceMission(
            mission_id="M001|001",
            mission_name="yolo",
            destination="andromed",
            launch_date=datetime.now(),
            duration_days=401,
            crew=[first_member, second_member],
            budget_millions=2.052
        )
        mission1.mission_status = "finished"
    except Exception as e:
        print("------------------------------------- Error Occured:", e)


if __name__ == "__main__":
    main()
