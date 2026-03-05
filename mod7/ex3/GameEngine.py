from __future__ import annotations

from ex0.Card import Card
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrate as GameStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck, creature_set, spell_set, artifact_set
from ex2.Combatable import Combatable
from typing import TypedDict, Any, cast, Literal
import subprocess
import time
import sys
import random


# FROM THE FUTURE

# TournamentCard (Multiple Inheritance: Card + Combatable + Rankable)
# def calculate_rating(self) -> int:
# get_tournament_stats(self) -> dict:

# FROM STRATEGY

# def execute_turn(self, hand: list, battlefield: list) -> dict:
# def get_strategy_name(self) -> str:
# def prioritize_targets(self, available_targets: list) -> list:


class GameDict(TypedDict):
    player: Player
    enemy: Player
    mana: int
    hand: list[Card]
    e_hand: list[Card]
    enemies: list[CreatureCard]
    allies: list[CreatureCard]
    deck: Deck
    e_deck: Deck
    pv: int
    enemy_pv: int
    strategy: GameStrategy
    effects: list[ArtifactCard]
    enemy_effects: list[ArtifactCard]


class Player(Card, Combatable):  # type: ignore

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

    def __init__(
            self, name: str, cost: int, rarity: str, ability: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.ability = ability
        self.health = 0
        self._ia = 0
        self.charge = 1

    def get_combat_stats(self) -> None:
        print("hero ability :", self.ability)
        print("is an ia", self._ia)

    def defend(self, incoming_damage: int) -> dict[Any, Any]:
        true_damage = (incoming_damage - 10)
        if true_damage > 0:
            self.health -= true_damage
        print(self.name, "taken", true_damage,
              "deffend with 10 tanking damage shield")
        return {"damages": true_damage}

    def set_ia(self) -> None:
        self._ia = 1

    def who_is_playing(self, player: str) -> None:
        if player == "player":
            self.player: Literal["player", "enemy"] = "player"
            self.pv: Literal["pv", "enemy_pv"] = "pv"
            self.hand: Literal["hand", "e_hand"] = "hand"
            self.allies: Literal["allies", "enemies"] = "allies"

            self.enemy: Literal["enemy", "player"] = "enemy"
            self.e_hand: Literal["e_hand", "hand"] = "e_hand"
            self.enemy_pv: Literal["enemy_pv", "pv"] = "enemy_pv"
            self.enemies: Literal["enemies", "allies"] = "enemies"
            self.effects: Literal["effects", "enemy_effects"] = "effects"

        if player == "enemy":
            self.player = "enemy"
            self.pv = "enemy_pv"
            self.hand = "e_hand"
            self.allies = "enemies"

            self.enemy = "player"
            self.enemy_pv = "pv"
            self.enemies = "allies"

            self.effects = "enemy_effects"

    def play(self, game_state: dict[str, Any]) -> dict[str, str]:
        # game: GameDict = cast(GameDict, game_state)

        if self._ia == 0:
            print(end="\nHAND: ")
            i: int = 0
            for elem in game_state["hand"]:
                i += 1
                print(end=f"[{i}:")
                if isinstance(elem, CreatureCard):
                    print(end=f"{{{elem.attack}}}.")
                elif isinstance(elem, SpellCard):
                    print(end="$.")
                elif isinstance(elem, ArtifactCard):
                    print(end="@.")
                print(end=f"{elem.name}")
                if isinstance(elem, CreatureCard):
                    print(end=f".({elem.health})")
                print(end=f"[{elem.cost}]]  ")
            print("\n")
            choice: str = str(input(
                "For play, ENTER:-- 1: play a card | \
                    2 play ability | 3 end turn --: "))
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
                play_card = game_state["strategy"].card_choice(game_state)
            hand_len = len(game_state[self.hand])
            try:
                result = int(play_card)
                if result < 1 or result > hand_len or hand_len == 0:
                    raise
            except Exception:
                return {"return": "wrong"}
            info = game_state[self.hand][result - 1].play(game_state)
            if info["state"] == "True":
                game_state[self.hand].pop(result - 1)

        if ichoice == 2:

            if self._ia == 0:
                play_card = str(
                    input(
                        "PLAY ABILITY : \
Enter allie minion number or 0 for chief: "
                    ))
            else:
                play_card = game_state["strategy"].ability_choice(
                    game_state)

            sum_len = len(game_state[self.allies])
            try:
                result = int(play_card)
                if result < 0 or result > sum_len:
                    raise
                if result == 0 and game_state[self.player].charge == 0:
                    print(game_state[self.player].name,
                          ". unit Already Attacked (one per turn)")
                    raise
                elif result != 0 and \
                        game_state[self.allies][result - 1].charge == 0:
                    print(game_state[self.allies][result - 1].name,
                          "this unit Already Attacked (one per turn)")
                    raise
            except Exception:
                return {"return": "wrong"}

            if result == 0:
                print(game_state[self.player].name, "selected")
                attacker = game_state[self.player]
                self.inject_attack(cast(GameDict, game_state), self.enemy_pv)
                if game_state[self.player].ability != "warrior":
                    attacker.attack_target(game_state[self.enemy])
                    return {"return": "again"}
            else:
                print(game_state[self.allies][result - 1].name, "selected")
                attacker = game_state[self.allies][result - 1]

            if self._ia == 0:
                play_card = str(
                    input(
                        "TARGET: Enter enemy minion number or 0 for chief : "
                    ))
            else:
                play_card = game_state["strategy"].target_choice(
                    game_state)
            sum_len = len(game_state[self.enemies])
            try:
                result = int(play_card)
                if result < 0 or result > sum_len:
                    raise
            except Exception:
                return {"return": "wrong"}

            if result == 0:
                print(game_state[self.enemy].name, "targeted")
                attacker.attack_target(game_state[self.enemy])
            else:
                print(game_state[self.enemies][result - 1].name, "targeted")
                attacker.attack_target(game_state[self.enemies][result - 1])

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
        self.charge = 0

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
                    game_state[front_pv] -= 5  # type: ignore
                else:
                    target.health -= 5
                    if target.health < 1:
                        target.state = False
                        print(target.name, "died")

        return {self.name: target.name}

    def effects_update(self, game_state: GameDict) -> None:
        artifacts = game_state[self.effects]
        if not artifacts:
            return
        print(f"FROM [{self.name}] --- ")
        for artifact in artifacts:
            print(artifact.name, end="affect the game ! ")
            match artifact.effect:
                case "aoe":
                    print("gravels falls into the battle cry")
                    for elem in game_state[self.enemies]:
                        print(elem.name, "take 5 damage")
                        elem.damage(5)

                case "single_random":
                    rnd: int = random.randint(1, 3)
                    if rnd == 1:
                        if not len(game_state[self.allies]):
                            print("no active allied to attack")
                        else:
                            print(end="allied ")
                            rnd = random.randint(
                                0, len(game_state[self.allies]) - 1)
                            print(game_state[self.allies][rnd].name,
                                  "designed, lose 15 pv")
                            game_state[self.allies][rnd].damage(15)
                    else:
                        if not len(game_state[self.enemies]):
                            print("no active enemy to attack")
                        else:
                            print(end="enemy ")
                            rnd = random.randint(
                                0, len(game_state[self.enemies]) - 1)
                            print(game_state[self.enemies][rnd].name,
                                  "designed, lose 15 pv")
                            game_state[self.enemies][rnd].damage(15)
                case "direct":
                    print("the enemy take 5 damage")
                    game_state[self.enemy_pv] -= 5
            artifact.durability -= 1
            if artifact.durability == 0:
                game_state[self.effects].remove(artifact)
            time.sleep(3)


class GameEngine:

    def __init__(self, player: Player, enemie: Player) -> None:
        from ex3.AggressiveStrategy import AggressiveStrategy

        self.game: GameDict = {"player": player, "mana": 0,
                               "enemy": enemie, "hand": [],
                               "e_hand": [], "deck": Deck, "e_deck": Deck,
                               "enemies": [], "allies": [],
                               "pv": 50, "enemy_pv": 50,
                               "strategy": AggressiveStrategy,
                               "effects": [], "enemy_effects": []}
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
        for elem in self.game["e_deck"].deck:
            if isinstance(elem, (CreatureCard, SpellCard)):
                elem.set_allies("enemies")
            if isinstance(elem, ArtifactCard):
                elem.set_allies("enemy_effects")

        self.game["player"].who_is_playing("player")
        self.game["enemy"].who_is_playing("enemy")

    def graphicprocess1(self, player: Card) -> None:
        for i in range(0, self.game["e_deck"].get_size()):
            print(end="[")
        print(self.game["e_deck"].get_size())
        print("")
        for i in range(0, 20):
            print(end=" ")
        print(
            f"{self.game['enemy'].name} ( {self.game['enemy_pv']} )  \
---   {self.game['enemy'].ability}")
        print("")
        for i in range(0, 22):
            print(end=" ")
        for elem in self.game["e_hand"]:
            print(end="[] ")
        print(end="\n               ")
        i = 0
        for elem in self.game["enemies"]:
            i += 1
            print(end=f"'({elem.health}){elem.name}.{i}' ")
        print("\n\n\n")
        print("                                                    MANA:",
              self.game["mana"])
        print("\n")
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
            f"{self.game['player'].name} ( {self.game['pv']} )  \
---   {self.game['player'].ability}")
        print("")
        print(self.game["deck"].get_size(), end="")
        for elem in range(0, self.game["deck"].get_size()):
            print(end="]")
        print("")
        for i in range(0, 65):
            print(end="-")
        print("\n", player.name.capitalize(), "TURN --/")
        print("")

    def simulate_turn(self) -> dict[str, Any]:

        self.game["mana"] += 1

        subprocess.run("clear")
        self.graphicprocess1(self.game["player"])

        deck = cast(Deck, self.game.get("deck"))
        deck.shuffle()
        self.game["hand"].append(deck.draw_card())

        result: dict[str, str] = {"return": "start"}
        while 1:
            subprocess.run("clear")
            self.graphicprocess1(self.game["player"])
            result = self.game["player"].play(cast(dict[Any, Any], self.game))
            if result["return"] == "success":
                self.game["player"].effects_update(self.game)
                self.clear_field()
                for elem in self.game["allies"]:
                    elem.charge = 1
                self.game["player"].charge = 1
                print("--- PLAYER TURN END ! ---")
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
        while 1:
            subprocess.run("clear")
            self.graphicprocess1(self.game["enemy"])
            result = self.game["enemy"].play(cast(dict[Any, Any], self.game))
            if result["return"] == "success":
                break
            time.sleep(4)
        self.game["enemy"].effects_update(self.game)
        self.clear_field()
        for elem in self.game["enemies"]:
            elem.charge = 1
        self.game["enemy"].charge = 1
        print("--- ENEMY TURN END ! ---")
        time.sleep(4)

        return {"TEEEEEEEEEEEEEEMP": "TEEEEEEEEEEEEEEEEEEEMP"}

    def exec(self) -> None:
        while (1):
            data = self.simulate_turn()
            if data.get("return") == "end":
                return

    def get_engine_status(self) -> dict[str, Any]:
        print(self.game)
        return {"status": self.game}
