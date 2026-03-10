
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")
    play_game = {"mana": 10, "name": "bidou", "allies": []}

    print("--- trying successfull play ------------------------------\n")
    obj = CreatureCard("wolf", 5, "common", 10, 50)
    enmy = CreatureCard("gobelin", 2, "common", 5, 10)

    obj.get_card_info()
    print("")
    obj.play(play_game)
    print("")
    obj.attack_target(enmy)

    print("\n--- trying unsuccessfull play ------------------------------\n")

    try:
        horse = CreatureCard("horse", 1, "common", -10, 5)
        print(horse.name)
    except Exception as e:
        print("error :", e)

    golem = CreatureCard("golem", 10, "rare", 25, 80)
    golem.play(play_game)
    golem.attack_target(obj)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("error :", e)
