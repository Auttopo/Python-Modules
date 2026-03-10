
from ex3.FantasyCardFactory import FantasyCardFactory
import traceback
import random
from typing import Any
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


def random_list(data: list[Any]) -> list[Any]:
    new: list[Card] = []
    for i in range(len(data)):
        r = random.choice(data)
        new.append(r)
        data.remove(r)
    return new


class ClassicStrategy(GameStrate):  # type: ignore

    def __init__(self, game_state: GameDict) -> None:
        self.game_state: GameDict = game_state
        self.card_choice_pos: int | None = None
        self.mana_push: int = 0

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

        if self.game_state["player"].ability == "warlock" and \
                self.game_state["player"].health < 26:
            return ["no target"]
        if self.game_state["player"].charge == 1 and \
                self.game_state["player"].cost <= self.game_state["mana"]:
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
        lower_i: int = 1
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
        self.logs: list[str] = []

    def register_card(self, card: TournamentCard) -> str:
        self.tournament.append(card)
        return f"{card.name} added to the tournament"

    def create_match(
            self, card1_id: str, card2_id: str) -> dict[str, TournamentCard]:
        p1: None | TournamentCard = None
        p2: None | TournamentCard = None

        for elem in self.tournament:
            if elem.name == card1_id:
                p1 = elem
            elif elem.name == card2_id:
                p2 = elem
        if p2 is None and p1 is None:
            raise Exception("error : card not registered")
        if p1 is None:
            raise Exception(f"error : card {card1_id} not registered")
        if p2 is None:
            raise Exception(f"error : card {card2_id} not registered")

        print("MATCH BEGIN ----------------------------------------- !")
        print(p1.name, ":", p1.ability, "VS", p2.name, p2.ability)
#        time.sleep(2)
        winner: TournamentCard = TournamentPlatform.setup_and_exec_match(
            p1, p2)
        if p1 == winner:
            loser = p2
        elif p2 == winner:
            loser = p1
        winner.update_wins(1)
        loser.update_losses(1)

        log = f"{winner.name} winner |VS| {loser.name} loser |  \
{card1_id} (ClassicStrategy) : {card2_id} (AgressiveStrategy) "
        print("\n\n", log)
        self.logs.append(log)
        return {"winner": winner}

    def get_leaderboard(self) -> list[str]:
        out: list[TournamentCard] = TournamentCard.get_classement()
        return out

    def generate_tournament_report(self) -> dict[str, Any]:
        print("REPORT ----------------------------------------------")
        board = self.get_leaderboard()
        print("\nLEADERBOARD:")
        for elem in board:
            print(elem)
        print("\nMATCHS LOG")
        i: int = 0
        print("number of matchs :", len(self.logs))
        for elem in self.logs:
            print(elem)
            i += 1
        return {
            "matchs done": i,
            "match logs": self.logs
        }

    def exec_real_tournament(self) -> None:
        winners: TournamentCard

        if len(self.tournament) < 2:
            print("not enough people for the tournament")
            return
        wtf = 0
        while len(self.tournament) > 1:
            winners = []
            while len(self.tournament) > 1:
                self.tournament = random_list(self.tournament)
                result = self.create_match(
                    self.tournament[0].name, self.tournament[1].name)
                try:
                    winners.append(result["winner"])
                except Exception as e:
                    print("error occured:", e)
                    return
                self.tournament.pop(1)
                self.tournament.pop(0)
                if len(self.tournament) == 1:
                    winners.append(self.tournament[0])
            self.tournament = winners
            wtf += 1

    @staticmethod
    def setup_and_exec_match(
            player: TournamentCard, enemy: TournamentCard) -> Any:

        try:
            factory = FantasyCardFactory(
                "basic theme",
                [
                    (FantasyCardFactory.create_creature,
                     20, CreatureCard, len(creature_set())),
                    (FantasyCardFactory.create_spell, 5,
                     SpellCard, len(spell_set())),
                    (FantasyCardFactory.create_artifact,
                     5, ArtifactCard, len(artifact_set()))
                ])

#            player = TournamentCard("bob", 2, "commun", "warrior")
#            enemie = TournamentCard("doofenshmirtz", 2, "rare", "warlock")

            player._ia = 1
            enemy._ia = 1

            game = GameEngine(player, enemy)
            game.configure_engine(factory, AggressiveStrategy)
            game.set_second_strategy(ClassicStrategy, 1)

            result = game.exec()
            return result
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
