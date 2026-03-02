
from ex0.Card import Card
from typing import Any


class CreatureCard(Card):  # type: ignore

    def __init__(
            self, name: str, cost: int, rarity: str, attack: int, health: int):
        if attack < 1:
            print(name, "creation error, attack need to be positive or 0")
            return
        if health < 1:
            print(name, "creation error health need to be positive")
            return
        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: dict[str, Any]) -> None:
        print("trying play", self.name)
        mana: int | None = game_state.get("mana")
        if mana is None:
            mana = 0
        if self.is_playable(mana):
            print(self.name, "summoned successfully")
            game_state.update({"mana": mana - 10})
            self.state = True
            allies = game_state["allies"]
            allies.append(self)
            game_state.update({"allies": allies})
            return
        print(
            f"can't be play; need: {self.cost} \
mana, current: {game_state.get('mana')}")

    def attack_target(self, target: "CreatureCard") -> bool | None:
        if not self.state:
            print("the card is not active")
            return None
        print(f"{self.name} pv:{self.health} \
-attack- {target.name} pv:{target.health} ({self.attack} damage)")
        target.health -= self.attack
        if target.health < 1:
            print(f"{target.name} died")
            target.state = False
            return True
        print(f"{target.name} have now {target.health} pv")
        return False

    def damage(self, damage: int) -> None:
        self.health -= damage
        if self.health < 1:
            print(self.name, "died")
            self.state = False
