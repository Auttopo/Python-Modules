from ex0.Card import Card
from typing import Any
import random


class Deck:

    def __init__(self) -> None:
        self.deck: list[Card] = []
        self.max = 30

    def add_card(self, card: Card) -> None:
        if len(self.deck) < self.max:
            print(card.name, "added to the deck")
            self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        i = 0
        for elem in self.deck:
            if elem.name == card_name:
                self.deck.remove[i]
                return True
            i += 1
        return False

    def shuffle(self) -> None:
        new: list[Card] = []
        for i in range(len(self.deck)):
            r = random.choice(self.deck)
            new.append(self.deck[r])
            self.deck.remove[r]

    def draw_card(self) -> Card:
        r = random.choice(self.deck)
        return self.deck[r]

    def get_deck_stats(self) -> dict[str, Any]:
        data: dict[str, Any] = {}
        data.update({"deck size:": len(self.deck)})
        return data
