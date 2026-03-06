
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform

if __name__ == "__main__":
    obj1 = TournamentCard("jack", 5, "rare", "warlock")
    obj2 = TournamentCard("jackno", 5, "rare", "warlock")
    obj3 = TournamentCard("jackson", 5, "rare", "warlock")

    obj1.update_wins(6)
    obj2.update_losses(3)
    obj3.update_losses(2)
    obj3.update_wins(5)
    print(obj1.get_classement())

    tournament = TournamentPlatform()
    tournament.programm_main()
