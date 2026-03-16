
from pydantic import BaseModel, Field
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)

    def show(self) -> None:
        print("OBJECT INFORMATIONS:")
        print(
            "station_id:",
            self.station_id,
        )
        print(
            "name:",
            self.name,
        )
        print(
            "crew_size:",
            self.crew_size,
        )
        print(
            "power_level:",
            self.power_level,
        )
        print(
            "oxygen_level:",
            self.oxygen_level,
        )
        print(
            "last_maintenance:",
            self.last_maintenance,
        )
        print(
            "is_operational:",
            self.is_operational,
            "\n"
        )


def main() -> None:
    user = SpaceStation(station_id="he33", name="coucou",
                        crew_size=15, power_level=99.1, oxygen_level=99.1,
                        last_maintenance=datetime.now())
    user.show()

    try:
        user = SpaceStation(station_id="he33", name="coucou",
                            crew_size=82, power_level=99.1, oxygen_level=99.1,
                            last_maintenance=datetime.now())
    except Exception as e:
        print(" ------------------------ CREW_SIZE ERROR :", e)
    try:
        user = SpaceStation(station_id="he33", name="coucou",
                            crew_size=15, power_level=100.000001,
                            oxygen_level=99.1,
                            last_maintenance=datetime.now())
    except Exception as e:
        print(" ------------------------ POER_LEVEL ERROR :", e)
    try:
        user = SpaceStation(station_id="he33", name="coucou",
                            crew_size=15, power_level=99.1, oxygen_level=101.1,
                            last_maintenance=datetime.now())
    except Exception as e:
        print(" ------------------------ OXYGEN_LEVEL ERROR :", e)
    try:
        user = SpaceStation(station_id="he33", name="coucou",
                            crew_size=15, power_level=99.1, oxygen_level=99.1,
                            last_maintenance=64668955127217516)  # type: ignore
    except Exception as e:
        print(" ------------------------ LAST_MAINTENANCE ERROR :", e)
    try:
        user = SpaceStation(station_id="he33", name="coucou",
                            crew_size=15, power_level=99.1, oxygen_level=99.1,
                            last_maintenance=datetime.now(),
                            is_operational=2)  # type: ignore
    except Exception as e:
        print(" ------------------------ IS_OPERATIONAL ERROR :", e)


if __name__ == "__main__":
    main()
