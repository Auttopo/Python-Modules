
from ex0.Card import Card
from typing import Any, cast
import random


class ArtifactCard(Card):  # type: ignore

    def __init__(
            self, name: str, cost: int, rarity: str,
            durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.allies = "effects"

    @classmethod
    def active_game(cls) -> None:
        cls.game = 1

    def play(self, game_state: dict[str, Any]) -> dict[str, bool]:
        print("try to use:", self.name)

        mana = game_state.get("mana")
        if self.cost > mana:
            print("not enough mana")
            return {"state": False}
        effects = game_state.get(self.allies)
        if effects is None:
            effects = []
        effects.append(self)
        game_state.update({self.allies: effects})
        return {"state": True}

    @classmethod
    def effects_update(cls, game_state: dict[str, Any]) -> None:
        artifacts = game_state.get("effects")
        if not artifacts:
            return
        for elem in artifacts:
            print(elem.name, end="affect the game ! ")
            match elem.effect:
                case "aoe":
                    print("gravels falls into the battle cry")

                case "single_random":
                    rnd: int = random.randint(1, 3)
                    if rnd == 1:
                        if not len(game_state["allies"]):
                            print("no active allied to attack")
                        else:
                            print(end="allied ")
                            rnd = random.randint(
                                0, len(game_state["allies"]) - 1)
                            print(game_state["allies"][rnd].name,
                                  "designed, lose 15 pv")
                            game_state["allies"][rnd].damage(15)
                    else:
                        pass
                case "direct":
                    print("the enemy take 5 damage")
                    pv: int = cast(int, game_state.get("enemy_pv")) - 5
                    game_state.update({"enemy_pv": pv})
            elem.durability -= 1
            if elem.durability == 0:
                artifacts.remove(elem)
                game_state.update({"effects": artifacts})
