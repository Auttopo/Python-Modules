
from typing import Any
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card


class EliteCard (Card, Combatable, Magical):  # type: ignore

    def __init__(
            self, name: str, cost: str, rarity: str,
            health: int, mana: int, stamina: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.health = health
        self.mana = mana
        self.stamina = stamina
        self.tank_pt = 0

    # FROM MAGICAL ------------------------------------------------------------

    def cast_spell(
            self, spell_name: str, targets: list[Any]) -> dict[Any, Any]:
        if self.mana < 10:
            return {
                "action": "spell",
                "user": self.__class__.__name__,
                "state": "failed"
            }
        print(self.name, "initiate", spell_name, "...")
        for elem in targets:
            print(f"{elem.name} take 10 damage from", spell_name)
            elem.health -= 10
        self.mana -= 10
        return {
            "action": "spell",
            "user": self.__class__.__name__,
            "state": "success"
        }

    def channel_mana(self, amount: int) -> dict[Any, Any]:
        print(self.name, "regenerate 10 mana")
        self.mana += 10
        return {
            "action": "chanel mana",
            "user": self.__class__.__name__,
            "state": "success"
        }

    def get_magic_stats(self) -> dict[Any, Any]:
        print(self.mana, ": mana points")
        return {
            "action": "magic info",
            "user": self.__class__.__name__,
            "state": "success"
        }

    # FROM COMBAT_ -----------------------------------------------------------

    def attack(self, target: CreatureCard) -> dict[Any, Any]:
        if self.stamina < 5:
            return {
                "action": "attack",
                "user": self.__class__.__name__,
                "state": "failed"
            }

        print(f"{target.name} take 10 damage from {self.name} attack")
        target.health -= 7
        self.stamina -= 5
        return {
            "action": "attack",
            "user": self.__class__.__name__,
            "state": "success"
        }

    def defend(self, incoming_damage: int) -> dict[Any, Any]:
        if self.stamina < 6:
            return {
                "action": "defence",
                "user": self.__class__.__name__,
                "state": "failled"
            }
        print(self.name, "raise his shield to prevent next 5 damage")
        self.stamina -= 6
        self.tank_pt += 5
        self.damage(incoming_damage)
        return {
            "action": "defence",
            "user": self.__class__.__name__,
            "state": "success"
        }

    def get_combat_stats(self) -> dict[Any, Any]:
        print(self.stamina, ": stamina points")
        print(self.tank_pt, ": shield points")
        return {
            "action": "combat info",
            "user": self.__class__.__name__,
            "state": "success"
        }

    # FROM CARD___ -----------------------------------------------------------

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        if not self.is_playable(game_state.get("mana")):
            return {
                "action": "play",
                "user": self.__class__.__name__,
                "state": "failled"
            }
        enemies = game_state.get("ennemies")
        if enemies is None:
            enemies = []
        enemies.append(self)
        game_state.update({"ennemies": enemies})
        print(self.name, "summoned to the battlefield")
        return {
            "action": "play",
            "user": self.__class__.__name__,
            "state": "success"
        }

    # FROM LOCAL__ -----------------------------------------------------------

    def damage(self, damage: int) -> None:
        if damage < 1:
            return
        untank = self.tank_pt - damage
        if untank < 0:
            print(self.tank_pt, "damage tanked")
            print(untank * -1, "PV losed")
            self.health += untank
            self.tank_pt = 0
        else:
            self.tank_pt -= damage
            print(damage, "damage tanked")

        if self.health < 1:
            print(self.name, "died")

    def show_stats(self) -> None:
        self.get_card_info()
        self.get_combat_stats()
        self.get_magic_stats()
