
import traceback
from ex3 import error_print
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    try:
        tournament = TournamentPlatform()
        obj1 = TournamentCard("Anduin", 2, "rare", "priest")
        tournament.register_card(obj1)
        tournament.register_card(TournamentCard(
            "Gul'dan", 2, "common", "warlock"))
        tournament.register_card(TournamentCard(
            "Garosh", 2, "common", "warrior"))
        tournament.register_card(TournamentCard(
            "Varian", 2, "rare", "warrior"))
        tournament.register_card(TournamentCard(
            "Ner zul", 2, "rare", "warlock"))
        tournament.register_card(TournamentCard(
            "boby", 2, "epic", "super bunny master"))
        tournament.register_card(TournamentCard("Velen", 2, "rare", "priest"))
        tournament.register_card(TournamentCard(
            "joakim", 2, "legendary", "intermitent du spéctacle"))
        tournament.register_card(TournamentCard(
            "kevin", 2, "mythic", "pancake summoner"))

        tournament.exec_real_tournament()

        print("\n=== DataDeck Tournament Platform ===\n")
        print(obj1.get_classement())
        print(obj1.get_rank_info())

        tournament.generate_tournament_report()
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


if __name__ == "__main__":
    main()
