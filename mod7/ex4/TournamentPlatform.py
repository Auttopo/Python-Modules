
from ex3.FantasyCardFactory import FantasyCardFactory
import traceback
import time
from ex3 import error_print
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine
from ex1.Deck import creature_set, spell_set, artifact_set
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from ex4.TournamentCard import TournamentCard
from ex3.GameStrategy import GameStrate
from ex3.GameEngine import GameDict
from ex0.Card import Card


class ClassicStrategy(GameStrate):  # type: ignore

    def __init__(self, game_state: GameDict) -> None:
        self.game_state: GameDict = game_state
        self.card_choice_pos: int | None = None
        self.mana_push: int = 0

    def execute_turn(
            self, hand: list[Card], battlefield: list[CreatureCard]
    ) -> dict[str, str]:

        i: int = 0
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

        i = 0
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
                    if len(self.game_state["allies"]) > 0:
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

        data = self.prioritize_targets(self.game_state["allies"])
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

        if self.game_state["player"].charge == 1:
            self.card_choice_pos = 0
            return ["2", self.game_state["player"]]
        return ["no target"]

    @classmethod
    def enter_choice(cls, game_state: GameDict) -> str:
        obj = ClassicStrategy(game_state)
        data = obj.execute_turn(game_state["hand"], game_state["enemies"])
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
        if len(game_state["enemies"]) == 0:
            return "0"

        lower = game_state["enemies"][0]
        i: int = 0
        lower_i: int = 0
        for elem in game_state["enemies"]:
            i += 1
            if elem.health < lower.health:
                lower_i = i
                lower = elem
        if lower.health >= game_state["enemy_pv"]:
            return "0"
        return str(lower_i)


class TournamentPlatform ():

    def __init__(self) -> None:
        self.tournament: list[TournamentCard] = []

    def register_card(self, card: TournamentCard) -> str:
        self.tournament.append(card)
        return f"{card.name} added to the tournament"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        pass

    def get_leaderboard(self) -> list[TournamentCard]:
        out: list[TournamentCard] = TournamentCard.get_classement()
        return out

    def generate_tournament_report(self) -> dict:
        return {
            "match done": ""
        }

    def programm_main(self) -> None:

        try:
            factory = FantasyCardFactory(
                "basic theme",
                [
                    (FantasyCardFactory.create_creature,
                     20, CreatureCard, len(creature_set())),
                    (FantasyCardFactory.create_spell, 10,
                     SpellCard, len(spell_set())),
                    (FantasyCardFactory.create_artifact,
                     10, ArtifactCard, len(artifact_set()))
                ])

            player = TournamentCard("bob", 2, "commun", "priest")
            enemie = TournamentCard("doofenshmirtz", 2, "rare", "warlock")

            player._ia = 1
            enemie._ia = 1

            game = GameEngine(player, enemie)
            game.configure_engine(factory, AggressiveStrategy)
            game.set_second_strategy(ClassicStrategy)

            game.exec()
        except Exception:
            print("\nbadly you fond a rare bug, \
    report what happened at abenabde@student.42lyon.fr")
            print("/-------------------------------\
    -------------------------------------\\")
            error_print()
            print("FULL TRACE BACK \\/")
            traceback.print_exc()
            print("\\-------------------------------\
    -------------------------------------/")
