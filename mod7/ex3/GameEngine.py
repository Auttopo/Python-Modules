from __future__ import annotations

from ex0.Card import Card
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrate as GameStrategy
from ex3.FantasyCardFactory import FantasyCardFactory, GameDict
from ex3.AggressiveStrategy import AggressiveStrategy
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck, creature_set, spell_set, artifact_set
from typing import TypedDict, Any, cast
import subprocess
import time
import sys

# FROM THE FUTURE

# TournamentCard (Multiple Inheritance: Card + Combatable + Rankable)
# def calculate_rating(self) -> int:
# get_tournament_stats(self) -> dict:

# FROM STRATEGY

# def execute_turn(self, hand: list, battlefield: list) -> dict:
# def get_strategy_name(self) -> str:
# def prioritize_targets(self, available_targets: list) -> list:


class Player(Card):  # type: ignore

    ability_limit = 0
    attack_limit = 0

    @classmethod
    def uplm_ability(cls) -> None:
        cls.ability_limit += 1

    @classmethod
    def uplm_attack(cls) -> None:
        cls.attack_limit += 1

    @classmethod
    def res_limits(cls) -> None:
        cls.ability_limit = 0
        cls.attack_limit = 0

    def __init__(self, name: str, cost: int, rarity: str, ability: str) -> None:
        super().__init__(name, cost, rarity)
        self.ability = ability
        self.health = 0
        self._ia = 0

    def set_ia(self) -> None:
        self._ia = 1

    def play(self, game_state: dict[str, Any]) -> dict:
        game_state = cast(GameDict, game_state)

        game_state["mana"] = 500

        print(end="\nHAND: ")
        i: int = 0
        for elem in game_state["hand"]:
            i += 1
            print(end=f"[({i})")
            print(end=f"{elem.name}] ")
        print("")
        if self._ia == 0:
            choice: str = str(input(
                "For play, ENTER:-- 1: play a card | 2 play ability | 3 end turn --: "))
        else:
            choice = game_state["strategy"].enter_choice(game_state)

        if choice == "exit":
            sys.exit()

        try:
            ichoice: int = int(choice)
            if ichoice < 1 or ichoice > 3:
                raise
        except Exception:
            return {"return": "wrong"}
        if ichoice == 1:

            if self._ia == 0:
                play_card: str = str(input("Enter the hand card number: "))
            else:
                play_card: str = game_state["strategy"].card_choice(game_state)
            hand_len = len(game_state["hand"])
            try:
                result = int(play_card)
                if result < 1 or result > hand_len or hand_len == 0:
                    raise
            except Exception:
                return {"return": "wrong"}
            game_state["hand"][result - 1].play(game_state)
            game_state["hand"].pop(result - 1)

        if ichoice == 2:

            if self._ia == 0:
                play_card = str(
                    input(
                        "PLAY ABILITY : Enter allie minion number or 0 for chief: "
                    ))
            else:
                play_card = game_state["strategy"].ability_choice(
                    game_state)

            sum_len = len(game_state["allies"])
            try:
                result = int(play_card)
                if result < 0 or result > sum_len:
                    raise
            except Exception:
                return {"return": "wrong"}

            if result == 0:
                print(game_state["player"].name, "selected")
                attacker = game_state["player"]
                self.inject_attack(game_state, game_state["enemy_pv"])
                if game_state["player"].ability != "warrior":
                    attacker.attack_target(game_state["enemy"])
                    return {"return": "again"}
            else:
                print(game_state["allies"][result - 1].name, "selected")
                attacker = game_state["allies"][result - 1]

            if self._ia == 0:
                play_card = str(
                    input(
                        "TARGET: Enter enemy minion number or 0 for chief : "
                    ))
            else:
                play_card = game_state["strategy"].target_choice(
                    game_state)
            sum_len = len(game_state["enemies"])
            try:
                result = int(play_card)
                if result < 0 or result > sum_len:
                    raise
            except Exception:
                return {"return": "wrong"}

            if result == 0:
                print(game_state["enemy"].name, "targeted")
                attacker.attack_target(game_state["enemy"])
            else:
                print(game_state["enemies"][result - 1].name, "targeted")
                attacker.attack_target(game_state["enemies"][result - 1])

        if ichoice == 3:
            return {"return": "success"}

        return {"return": "again"}

    def inject_attack(self, game_state: GameDict, front_pv: str) -> None:
        self.game_state: GameDict = game_state
        self.front_pv: str = front_pv

    def attack_target(self, target: Card) -> dict[str, str]:
        return self.attack(target)

    def attack(self, target: Card) -> dict[str, str]:
        game_state = self.game_state
        front_pv = self.front_pv

        match self.ability:
            case "warlock":
                print(self.name, "losed 6 pv and drawed a card")
                if front_pv == "pv":
                    game_state["e_hand"].append(
                        game_state["e_deck"].draw_card())
                    game_state["enemy_pv"] -= 6
                else:
                    game_state["hand"].append(game_state["deck"].draw_card())
                    game_state["pv"] -= 6
            case "priest":
                print(self.name, "gained 5 pv")
                if front_pv == "pv":
                    game_state["enemy_pv"] += 6
                else:
                    game_state["pv"] += 6

            case "warrior":
                print(target.name, "lose 5 pv")
                if isinstance(target, Player):
                    game_state[front_pv] -= 5
                else:
                    target.health -= 5
                    if target.health < 1:
                        target.state = False
                        print(target.name, "died")

        return {self.name: target.name}


class GameEngine:

    def __init__(self, player: Player, enemie: Player) -> None:
        self.game: GameDict = {"player": player, "mana": 0,
                               "enemy": enemie, "hand": [],
                               "e_hand": [], "deck": Deck, "e_deck": Deck,
                               "enemies": [], "allies": [],
                               "pv": 50, "enemy_pv": 50, "strategy": AggressiveStrategy}
        self.game["enemy"]._ia = 1

    def clear_field(self) -> None:
        for elem in self.game["allies"]:
            if elem.state is False:
                self.game["allies"].remove(elem)
        for elem in self.game["enemies"]:
            if elem.state is False:
                self.game["enemies"].remove(elem)
        if self.game["player"].health < 0:
            self.game["pv"] += self.game["player"].health
            self.game["player"].health = 0
        if self.game["enemy"].health < 0:
            self.game["enemy_pv"] += self.game["enemy"].health
            self.game["enemy"].health = 0

    def configure_engine(
            self, factory: CardFactory, strategy: GameStrategy) -> None:

        deck = factory.create_themed_deck(50)
        self.game.update({"deck": deck.get("deck")})
        self.strategy = strategy

        # ENEMY DECK CREATION ----
        total = deck["deck"].get_size()
        n_c = total // 2
        n_sa = n_c // 2
        if (n_c + n_sa * 2) < total:
            n_c += total - n_c - n_sa * 2
        Deck.invisibility = 1
        enemygen = FantasyCardFactory(
            "classic theme",
            [
                (FantasyCardFactory.create_creature,
                 n_c, CreatureCard, len(creature_set())),
                (FantasyCardFactory.create_spell,
                 n_sa, SpellCard, len(spell_set())),
                (FantasyCardFactory.create_artifact,
                 n_sa, ArtifactCard, len(artifact_set()))
            ])
        e_deck = enemygen.create_themed_deck(total)
        self.game.update({"e_deck": e_deck.get("deck")})

    def graphicprocess1(self, mana: int, e_mana: int) -> None:
        for elem in range(0, self.game["e_deck"].get_size()):
            print(end="[")
        print(self.game["e_deck"].get_size())
        print("                                                    MANA:",
              e_mana)
        for i in range(0, 20):
            print(end=" ")
        print(
            f"{self.game['enemy'].name} ( {self.game['enemy_pv']} )  ---   {self.game['enemy'].ability}")
        print("")
        for i in range(0, 22):
            print(end=" ")
        for elem in self.game["e_hand"]:
            print(end="[] ")
        print(end="\n               ")
        i: int = 0
        for elem in self.game["enemies"]:
            i += 1
            print(end=f"'({elem.health}){elem.name}.{i}' ")
        print("\n\n")
        print(end="\n               ")
        i = 0
        for elem in self.game["allies"]:
            i += 1
            print(end=f"'({elem.health}){elem.name}.{i}' ")
        print("")
        for i in range(0, 22):
            print(end=" ")
        for elem in self.game["hand"]:
            print(end="[] ")
        print("")
        for i in range(0, 20):
            print(end=" ")
        print(
            f"{self.game['player'].name} ( {self.game['pv']} )  ---   {self.game['player'].ability}")
        print("                                                    MANA:",
              mana)
        print(self.game["deck"].get_size(), end="")
        for elem in range(0, self.game["deck"].get_size()):
            print(end="]")
        print("")
        for i in range(0, 65):
            print(end="-")
        print("")

    def simulate_turn(self) -> dict[str, Any]:
        subprocess.run("clear")
        self.graphicprocess1(self.game["mana"], self.game["mana"])

        deck = cast(Deck, self.game.get("deck"))
        deck.shuffle()
        self.game["hand"].append(deck.draw_card())

        result: dict[str, str] = {"return": "start"}
        while 1:
            subprocess.run("clear")
            self.graphicprocess1(self.game["mana"], self.game["mana"])
            result = self.game["player"].play(cast(dict[Any, Any], self.game))
            if result["return"] == "success":
                print("--- TURN END ! ---")
                time.sleep(3)
                break
            if result["return"] == "wrong":
                print(" ! --- ! INVALID VALUE OCCURED ! --- ! ")
                time.sleep(2)
            else:
                time.sleep(5)
            self.clear_field()

        deck = cast(Deck, self.game.get("e_deck"))
        deck.shuffle()
        self.game["e_hand"].append(deck.draw_card())

        # self.game["enemy"].play(cast(dict[Any, Any], self.game))
        # prioritize_targets(self, available_targets: list) -> list:
        # execute_turn(self, hand: list, battlefield: list) -> dict:

        return {"TEEEEEEEEEEEEEEMP": "TEEEEEEEEEEEEEEEEEEEMP"}

    def exec() -> None:
        # while (1)
        # data = self.simulate_turn()
        #   if data.get("return") == "end"
        #        return
        pass

    def get_engine_status(self) -> dict[str, Any]:
        print(self.game)
        return {"status": self.game}
