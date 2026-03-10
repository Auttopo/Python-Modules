from __future__ import annotations

from ex2.Combatable import Combatable
from ex3.GameEngine import Player
from ex0.CreatureCard import CreatureCard
from ex4.Rankable import Rankable
from typing import Any


class TournamentCard (Player, Combatable, Rankable):  # type: ignore

    ranking: list[TournamentCard] = []

    def __init__(
            self, name: str, cost: int, rarity: str, ability: str
    ) -> None:
        super().__init__(name, cost, rarity, ability)
        self.health: int = 0
        self._ia: int = 0
        self.charge: int = 1
        self.wins: int = 0
        self.losses: int = 0
        TournamentCard.ranking.append(self)

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict[Any, Any]:
        return {
            "name": self.name,
            "ability": self.ability,
            "wins": self.wins,
            "losses": self.losses,
            "rank": self.calculate_rating()
        }

    def play(self, game_state: dict[str, Any]) -> dict[str, str]:
        out: dict[str, str] = super().play(game_state)
        return out

    def attack(self, target: Combatable | CreatureCard) -> dict[str, str]:
        out: dict[str, str] = super().attack(target)
        return out

    def calculate_rating(self) -> int:

        rank: int = 1000 + self.wins * 10 - self.losses * 8
        if rank < 1:
            rank = 1
        return rank

    @classmethod
    def get_classement(cls) -> list[str]:
        rank_list: list[TournamentCard] = []

        for i in range(0, len(cls.ranking)):
            higher = cls.ranking[0]
            for elem in cls.ranking:
                if higher.calculate_rating() < elem.calculate_rating():
                    higher = elem
            rank_list.append(higher)
            cls.ranking.remove(higher)
        cls.ranking = rank_list

        out: list[str] = []
        for elem in rank_list:
            out.append(elem.name + " rank: " +
                       str(elem.calculate_rating()))
        return out

    def get_tournament_stats(self) -> dict[str, list[TournamentCard]]:
        return {"ranking": TournamentCard.ranking}
