
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from typing import Any, cast


class SpellCard(Card):  # type: ignore

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict[str, Any]) -> dict[str, bool]:
        print("try to use:", self.name)

        mana = game_state.get("mana")
        if self.cost > mana:
            print("not enough mana")
            return {"state": False}
        game_state.update({"mana": mana - self.cost})
        self.resolve_effect([game_state, game_state.get(
            "enemies"), game_state.get("allies")])
        return {"state": True}

    def resolve_effect(
        self, targets: list[dict[str, Any] | list[CreatureCard] | None]
    ) -> dict[str, Any]:
        game_state: dict[str, Any] | Any = targets[0]
        enemies: Any = targets[1]
        allies: Any = targets[2]

        print(end="success. ")
        match self.effect_type:
            case "heal":
                print("you recover 10 pv")
                game_state.update({"pv": cast(int, game_state.get("pv")) + 10})
            case "get mana":
                print("you get 10 mana")
                game_state.update(
                    {"mana": cast(int, game_state.get("mana")) + 10})
            case "fire wave":
                damage: int = 10
                for elem in enemies:
                    elem.health -= damage
                    print(elem.name, "take", damage, "damage")
                    if elem.health < 1:
                        elem.state = False
                        print(elem.name, "died")
            case "magic rain":
                for elem in allies:
                    elem.health += 10
                    print(elem.name, "get 10 pv, now have:", elem.health)
        game_state.update({"enemies": enemies})
        game_state.update({"allies": allies})
        return game_state
