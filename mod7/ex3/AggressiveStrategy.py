
from ex3.GameStrategy import GameStrate
from ex0.CreatureCard import CreatureCard
from ex3.GameEngine import GameDict
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.Card import Card


class AggressiveStrategy(GameStrate):  # type: ignore

    def __init__(self, game_state: GameDict) -> None:
        self.game_state: GameDict = game_state
        self.card_choice_pos: int | None = None
        self.mana_push: int = 0
    # Prioritizes attacking and dealing damage
    # Plays low-cost creatures first for board presence
    # Targets enemy creatures and player directly
    # Returns comprehensive turn execution results

    def execute_turn(
            self, hand: list[Card], battlefield: list[CreatureCard]
    ) -> dict[str, str]:

        i: int = 0
        for elem in hand:
            i += 1
            if isinstance(elem, CreatureCard) and \
                    elem.cost <= self.game_state["mana"]:
                self.card_choice_pos = i
                return {"return": "1"}

        i = 0
        for elem in hand:
            i += 1
            if isinstance(elem, SpellCard) and \
                    elem.cost <= self.game_state["mana"]:
                if elem.effect_type == "heal":
                    self.card_choice_pos = i
                    return {"return": "1"}
                elif elem.effect_type == "fire wave":
                    if len(battlefield) > 0:
                        self.card_choice_pos = i
                        return {"return": "1"}
                elif elem.effect_type == "magic rain":
                    if len(self.game_state["enemies"]) > 0:
                        self.card_choice_pos = i
                        return {"return": "1"}
        i = 0
        for elem in hand:
            i += 1
            if isinstance(elem, ArtifactCard) and \
                    elem.cost <= self.game_state["mana"]:
                if elem.effect == "aoe" and len(battlefield) > 1:
                    self.card_choice_pos = i
                    return {"return": "1"}
                elif elem.effect == "single_random" and len(battlefield) > 1:
                    self.card_choice_pos = i
                    return {"return": "1"}
                elif elem.effect == "direct":
                    self.card_choice_pos = i
                    return {"return": "1"}

        i = 0
        if self.mana_push == 0:
            for elem in hand:
                i += 1
                if isinstance(elem, SpellCard) and \
                        elem.cost <= self.game_state["mana"]:
                    if elem.effect_type == "get mana":
                        self.mana_push = 1
                        self.game_state["mana"] += 9
                        inchoice: dict[str, str] = self.execute_turn(
                            hand, battlefield)
                        self.game_state["mana"] -= 9
                        if inchoice["return"] == "1":
                            self.card_choice_pos = i
                            return {"return": "1"}

        data = self.prioritize_targets(self.game_state["enemies"])
        if data[0] and data[0] == "2":
            return {"return": "2"}

        return {"return": "3"}

    def get_strategy_name(self) -> str:
        return str(self.__class__.__name__)

    def prioritize_targets(
            self, available_targets: list[CreatureCard]
    ) -> list[str | CreatureCard]:
        i = 0

        for elem in available_targets:
            i += 1
            if elem.charge == 1:
                self.card_choice_pos = i
                return ["2", elem]

        if self.game_state["enemy"].ability == "warlock" and \
                self.game_state["enemy"].health < 26:
            return ["no target"]
        if self.game_state["enemy"].charge == 1 and \
                self.game_state["enemy"].cost <= self.game_state["mana"]:
            self.card_choice_pos = 0
            return ["2", self.game_state["enemy"]]
        return ["no target"]

    @classmethod
    def enter_choice(cls, game_state: GameDict) -> str:
        obj = AggressiveStrategy(game_state)
        data = obj.execute_turn(game_state["e_hand"], game_state["allies"])
        out = str(data["return"])
        cls.card_choice_pos = obj.card_choice_pos
        return out

    @classmethod
    def card_choice(cls, game_state: GameDict) -> str:
        return str(cls.card_choice_pos)

    @classmethod
    def ability_choice(cls, game_state: GameDict) -> str:
        return str(cls.card_choice_pos)

    @classmethod
    def target_choice(cls, game_state: GameDict) -> str:
        return "0"
