
from abc import ABC, abstractmethod
from typing import Any


class Combatable (ABC):

    @abstractmethod
    def attack(self, target: Any) -> dict[Any, Any]:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict[Any, Any]:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict[Any, Any]:
        pass
