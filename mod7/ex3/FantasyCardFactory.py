
from typing import Any
from ex0.Card import Card
from ex3.CardFactory import CardFactory
from ex1.Deck import Deck, creature_set, spell_set, artifact_set
from collections.abc import Callable
import random


class FantasyCardFactory(CardFactory):  # type: ignore
    # Supports extensible card type registration

    def __init__(
        self, name: str,
        datas: list[
            tuple[Callable[[str | int | None], Card],
                  int, Card, int]
        ]
    ) -> None:
        """ first theme is the parameter """

        self.active_deck: str = name
        data_set: list[
            tuple[Callable[[str | int | None], Card],
                  int, Card, int]
        ] = []
        for elem in datas:
            data_set.append(elem)
        self.all = {name: data_set}

    def create_creature(self, name_or_power: str | int | None = None) -> Card:

        if name_or_power == "bun":
            return creature_set()[0]
        if name_or_power == "goat":
            return creature_set()[1]
        if name_or_power == "wolf":
            return creature_set()[2]
        if name_or_power == "mini golem":
            return creature_set()[3]
        if name_or_power == "dragon slayer":
            return creature_set()[4]
        if name_or_power == "gobelin horde":
            return creature_set()[5]
        if name_or_power == "unicorn":
            return creature_set()[6]
        if name_or_power == "mega golem":
            return creature_set()[7]
        if name_or_power == "dragoon":
            return creature_set()[8]
        else:
            return creature_set()[name_or_power]

    def create_spell(self, name_or_power: str | int | None = None) -> Card:

        if name_or_power == "bread powa":
            return spell_set()[0]
        if name_or_power == "water elfe infused":
            return spell_set()[1]
        if name_or_power == "super Flower Rain":
            return spell_set()[2]
        if name_or_power == "fire storm":
            return spell_set()[3]
        else:
            return spell_set()[name_or_power]

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:

        if name_or_power == "heart of the mountain":
            return artifact_set()[0]
        if name_or_power == "shard of dragon anger":
            return artifact_set()[1]
        if name_or_power == "cursed sword":
            return artifact_set()[2]
        else:
            return artifact_set()[name_or_power]

    def add_theme(self, name: str,
                  datas: list[
                      tuple[Callable[[str | int | None], Card],
                            int, Card, int]]
                  ) -> None:
        data_set: list[
            tuple[Callable[[str | int | None], Card],
                  int, Card, int]
        ] = []
        for elem in datas:
            data_set.append(elem)
        self.all.update({name: data_set})

    def set_active_them(self, theme: str) -> None:
        for name, elem in self.all.items():
            if name == theme:
                self.active_deck = theme
                return
        raise Exception("theme not exist")

    def create_themed_deck(self, size: int) -> dict[Any, Any]:

        deck: Deck = Deck()
        count: int = 0
        for name, elem in self.all.items():
            if name == self.active_deck:
                for composant in elem:
                    i: int = 0
                    while i < composant[1]:
                        deck.add_card(
                            composant[0](FantasyCardFactory,  # type: ignore
                                         random.randint(0, composant[3] - 1))
                        )
                        i += 1
                        count += 1
        if count != size:
            print(
                "Warning, the theme size is different than recommended"
            )
            print(count, size)

        return {"deck": deck}

    # Supports extensible card type registration
    def get_supported_types(self) -> dict[Any, Any]:
        types: set[str] = set()
        for name, elem in self.all.items():
            for composant in elem:
                types.update([str(composant[2].__name__)])

        return {"supported types": types}
