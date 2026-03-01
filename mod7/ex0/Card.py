
from abc import ABC, abstractmethod
from typing import Any


class Card(ABC):

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity
        self.state: bool = False
        self.description: str = ""

    def set_description(self, descrition: str) -> None:
        self.description = descrition

    @abstractmethod
    def play(self, game_state: dict[str, Any]) -> None:
        pass

    def get_card_info(self) -> None:
        print(
            f"creature info; {self.name} : {self.rarity}, cost : {self.cost}")

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= self.cost:
            return True
        return False
