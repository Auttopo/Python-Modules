
from ex0.Card import Card
from typing import Any


class SpellCard(Card):

    @staticmethod
    def init_all(name: str, cost: int, rarity: str, effect_type: str, effect: Any) -> object:
        obj = SpellCard(name, cost, rarity, effect_type)

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        self.super(name, cost, rarity)
        self.effect_type = effect_type
        self.effect: Any = None

    def play(self, game_state: dict) -> dict:
        match self.effect_type:
            case "mana":
            case "heal":
            case "deck":

    def resolve_effect(self, targets: list) -> dict:
        pass
