
from pydantic import BaseModel, Field, model_validator
from enum import Enum
from typing_extensions import Self
from typing import Optional
from datetime import datetime


class ContactType(Enum):
    radio = 1
    visual = 2
    physical = 3
    telepathic = 4


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500, default=None)
    is_verified: bool = Field(default=False)

    def show(self) -> None:
        print("OBJECT INFORMATIONS:")
        print(
            "contact_id:",
            self.contact_id,
            "\ntimestamp:",
            self.timestamp,
            "\nlocation:",
            self.location,
            "\ncontact_type:",
            self.contact_type,
            "\nsignal_strength:",
            self.signal_strength,
            "\nduration_minutes:",
            self.duration_minutes,
            "\nwitness_count:",
            self.witness_count,
            "\nmessage_received:",
            self.message_received,
            "\nis_verified:",
            self.is_verified,
            "\n"
        )

    @model_validator(mode="after")
    def check_contact_id(self) -> Self:
        if self.contact_id[:2] != "AC":
            raise ValueError("contact_id must start with AC")
        return self

    @model_validator(mode="after")
    def check_contact_type(self) -> Self:
        if self.contact_type == ContactType.physical:
            if self.is_verified is False:
                raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.telepathic:
            if self.witness_count < 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses")
        return self

    @model_validator(mode="after")
    def check_signal_strength(self) -> Self:
        if self.signal_strength >= 7.0:
            try:
                if not self.message_received:
                    raise
            except Exception:
                raise ValueError(
                    "Strong signals (> 7.0) should include received messages")
        return self


def is_created(obj: AlienContact | None) -> bool:
    if obj:
        return True
    return False


def main() -> None:
    obj1 = AlienContact(
        contact_id="AC 001",
        timestamp=datetime.now(),
        location="Lyon west-side",
        contact_type=ContactType.radio,
        signal_strength=4.31,
        duration_minutes=163,
        witness_count=2,
        message_received="coucoutwa",
        is_verified=True
    )
    obj1.show()
    try:
        obj2 = AlienContact(
            contact_id="Contact 001",
            timestamp=datetime.now(),
            location="Lyon west-side",
            contact_type=ContactType.radio,
            signal_strength=4.31,
            duration_minutes=163,
            witness_count=2,
            message_received="coucoutwa",
            is_verified=True
        )
        is_created(obj2)
    except Exception as e:
        print("------------------------- ERROR OCCURED:", e)
    try:
        obj3 = AlienContact(
            contact_id="AC 001",
            timestamp=datetime.now(),
            location="Lyon west-side",
            contact_type=ContactType.physical,
            signal_strength=4.31,
            duration_minutes=163,
            witness_count=2,
            message_received="coucoutwa",
        )
        is_created(obj3)
    except Exception as e:
        print("------------------------- ERROR OCCURED:", e)
    try:
        obj4 = AlienContact(
            contact_id="AC 001",
            timestamp=datetime.now(),
            location="Lyon west-side",
            contact_type=ContactType.telepathic,
            signal_strength=4.31,
            duration_minutes=163,
            witness_count=2,
            message_received="coucoutwa",
            is_verified=True
        )
        is_created(obj4)
    except Exception as e:
        print("------------------------- ERROR OCCURED:", e)
    try:
        obj5 = AlienContact(
            contact_id="AC 001",
            timestamp=datetime.now(),
            location="Lyon west-side",
            contact_type=ContactType.radio,
            signal_strength=9.2,
            duration_minutes=163,
            witness_count=2,
            is_verified=True
        )
        is_created(obj5)
    except Exception as e:
        print("------------------------- ERROR OCCURED:", e)


if __name__ == "__main__":
    main()
