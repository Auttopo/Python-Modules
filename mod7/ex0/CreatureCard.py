
from ex0.Card import Card
from typing import Any
from ex2.Combatable import Combatable


class CreatureCard(Card):  # type: ignore

    def __init__(
            self, name: str, cost: int, rarity: str, attack: int, health: int):
        if attack < 1:
            raise Exception(
                name, "creation error, attack need to be positive or 0")
            return
        if health < 1:
            raise Exception(name, "creation error health need to be positive")
        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.health: int = health
        self.charge = 1
        self.allies = "allies"

    def play(self, game_state: dict[str, Any]) -> dict[str, bool]:
        print("trying play", self.name)
        mana: int | None = game_state.get("mana")
        if mana is None:
            mana = 0
        if self.is_playable(mana):
            print(self.name, "summoned successfully")
            game_state["mana"] -= self.cost
            self.state = True
            game_state[self.allies].append(self)
            return {"state": True}
        print(
            f"can't be play; need: {self.cost} \
mana, current: {game_state.get('mana')}")
        return {"state": False}

    def attack_target(self, target: "CreatureCard") -> dict[str, bool | None]:
        if not self.state:
            print("the card is not active")
            return {"return": None}
        print(f"{self.name} \
-attack- {target.name} ({self.attack} damage)")
        target.health -= self.attack
        self.charge = 0
        if target.health < 1 and not isinstance(target, Combatable):
            print(f"{target.name} died")
            target.state = False
            return {"return": True}
        if not isinstance(target, Combatable):
            print(f"{target.name} have now {target.health} pv")
        return {"return": False}

    def damage(self, damage: int) -> None:
        self.health -= damage
        if self.health < 1:
            print(self.name, "died")
            self.state = False
