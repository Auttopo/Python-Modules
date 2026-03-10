
from abc import ABC, abstractmethod
from typing import Any


class Card(ABC):

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity
        self.state: bool = False
        self.description: str = ""
        self.allies: str

    @property
    def rarity(self) -> str:
        return self.__rarity

    @rarity.setter
    def rarity(self, value: str) -> None:
        if value != "common" and \
                value != "rare" and \
                value != "mythic" and \
                value != "legendary" and value != "epic":
            raise Exception(f"unknown rarity : {value}")
        self.__rarity = value

    def set_description(self, descrition: str) -> None:
        self.description = descrition

    @abstractmethod
    def play(self, game_state: dict[str, Any]) -> dict[str, bool]:
        pass

    def get_card_info(self) -> dict[Any, Any]:
        print(
            f"creature info; {self.name} : {self.rarity}, cost : {self.cost}")
        return {"self": self.name}

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= self.cost:
            return True
        return False

    def set_allies(self, allies: str) -> None:
        self.allies = allies
