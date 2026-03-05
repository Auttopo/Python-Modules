from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Any
import random


def creature_set() -> list[CreatureCard]:
    return [

        CreatureCard("bun", 1, "common", 2, 10),
        CreatureCard("goat", 2, "common", 4, 10),
        CreatureCard("wolf", 3, "common", 6, 15),
        CreatureCard("mini golem", 3, "common", 2, 25),

        CreatureCard("dragon slayer", 6, "rare", 8, 35),
        CreatureCard("gobelin horde", 4, "rare", 15, 1),
        CreatureCard("unicorn", 5, "rare", 10, 20),

        CreatureCard("mega golem", 10, "legendary", 5, 120),
        CreatureCard("dragoon", 15, "legendary", 20, 100)
    ]


def spell_set() -> list[SpellCard]:
    return [
        SpellCard("bread powa", 5, "common", "heal"),
        SpellCard("water elfe infused", 5, "common", "get mana"),
        SpellCard("super Flower Rain", 5, "common", "magic rain"),
        SpellCard("fire strom", 5, "common", "fire wave")
    ]


def artifact_set() -> list[ArtifactCard]:
    return [
        ArtifactCard("heart of the mountain", 9, "rare", 3, "aoe"),
        ArtifactCard("shard of dragon anger", 11, "rare", 4, "direct"),
        ArtifactCard("cursed sword", 12, "legendary", 3, "single_random")
    ]


class Deck:

    invisibility: int = 0

    def __init__(self) -> None:
        self.deck: list[Card] = []

    def add_card(self, card: Card) -> None:
        if self.invisibility == 0:
            print(card.name, "added to the deck")
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        i = 0
        for elem in self.deck:
            if elem.name == card_name:
                self.deck.remove(elem)
                return True
            i += 1
        return False

    def shuffle(self) -> None:
        new: list[Card] = []
        for i in range(len(self.deck)):
            r = random.choice(self.deck)
            new.append(r)
            self.deck.remove(r)
        self.deck = new

    def draw_card(self) -> Card:
        r = random.choice(self.deck)
        self.deck.remove(r)
        return r

    def get_deck_stats(self) -> dict[str, Any]:
        data: dict[str, Any] = {}
        data.update({"deck size:": len(self.deck)})
        return data

    def show(self) -> None:
        print("[DECK]:")
        for elem in self.deck:
            print(elem.name)

    def get_size(self) -> int:
        return len(self.deck)


def create_deck(creatures_n: int, spells_n: int, artifact_n: int) -> Deck:
    i: int = 0
    deck = Deck()
    creatures = creature_set()
    spells = spell_set()
    artifacts = artifact_set()

    while i < creatures_n:
        deck.add_card(random.choice(creatures))
        i += 1
    i = 0
    while i < spells_n:
        deck.add_card(random.choice(spells))
        i += 1
    i = 0
    while i < artifact_n:
        deck.add_card(random.choice(artifacts))
        i += 1
    deck.shuffle()
    print("DECK CREATED -------------\n")
    return deck
