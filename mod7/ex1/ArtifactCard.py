
from ex0.Card import Card
from typing import Any
import random


class ArtifactCard(Card):  # type: ignore

    def __init__(
            self, name: str, cost: int, rarity: str,
            durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.allies = "effects"
        self.state = False

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
        self.activate_ability()
        return {"state": True}

    def activate_ability(self) -> dict[Any, Any]:
        self.state = True
        return {self.name: "activated"}

    def is_active(self) -> bool:
        if self.state is True:
            print(self.name, " is active")
            return True
        return False

    @classmethod
    def effects_update(cls, game_state: dict[Any, Any]) -> None:
        artifacts = game_state["effects"]
        if not artifacts:
            return
        for artifact in artifacts:
            if artifact.durability > 0:
                print(artifact.name, end="affect the game ! ")
                match artifact.effect:
                    case "aoe":
                        print("gravels falls into the battle cry")
                        for elem in game_state["enemies"]:
                            print(elem.name, "take 5 damage")
                            elem.damage(5)

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
                            if not len(game_state["enemies"]):
                                print("no active enemy to attack")
                            else:
                                print(end="enemy ")
                                rnd = random.randint(
                                    0, len(game_state["enemies"]) - 1)
                                print(game_state["enemies"][rnd].name,
                                      "designed, lose 15 pv")
                                game_state["enemies"][rnd].damage(15)
                    case "direct":
                        print("the enemy take 5 damage")
                        game_state["enemy_pv"] -= 5
                    case other:
                        raise Exception(
                            f"error occured. unknown value : {other}")
            artifact.durability -= 1
        artifacts = [a for a in artifacts if a.durability >= 1]
