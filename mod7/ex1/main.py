from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck, create_deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


def main() -> None:
    print("=== DataDeck Deck Builder ===\n")

    pomdapi = CreatureCard("pomdapi", 2, "common", 2, 10)
    goat = CreatureCard("mega goat", 2, "common", 2, 100)
    bun = CreatureCard("bunny", 2, "common", 2, 10)
    game = {"pv": 50, "mana": 500, "player": "bob", "enemy_pv": 50}
    mydeck: Deck = create_deck(5, 3, 3)
    print(mydeck.get_deck_stats())
    mydeck.add_card(pomdapi)
    card = mydeck.draw_card()
    print("card drawed:", card.name)
    mydeck.remove_card("pomdapi")
    mydeck.show()

    mydeck.remove_card("")

    spell_book = [
        SpellCard("Fire strom", 5, "common", "fire wave"),
        SpellCard("Super Flower Rain", 5, "common", "magic rain"),
        SpellCard("bread powa", 5, "common", "heal"),
        SpellCard("water elfe infused", 5, "common", "get mana")
    ]

    game.update({"enemies": [goat]})
    game.update({"allies": [bun]})

    print(end="\nPOLYMORFIC BOOK: ")
    print("-------------------------------------------")
    for spell in spell_book:
        print("")
        spell.play(game)

    artifact_storage = [
        ArtifactCard("heart of the mountain", 9, "rare", 1, "aoe"),
        ArtifactCard("shard of dragon anger", 11, "rare", 1, "direct"),
        ArtifactCard("cursed sword", 12, "legendary", 2, "single_random")
    ]
    print(end="\nPOLYMORFIC ARTIFACTS ")
    print("-------------------------------------------\n")
    # TURN SIMULATION
    for artifact in artifact_storage:
        artifact.play(game)
        artifact.is_active()
    print("")
    i: int = 0
    while i < 5:
        i += 1
        print("L", i)
        ArtifactCard.effects_update(game)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("error occured", e)
