
from abc import ABC, abstractmethod
from typing import Any


class Magical (ABC):

    @abstractmethod
    def cast_spell(
            self, spell_name: str, targets: list[Any]) -> dict[Any, Any]:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict[Any, Any]:
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict[Any, Any]:
        pass
