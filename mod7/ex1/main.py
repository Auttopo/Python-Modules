from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck, create_deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard

if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===\n")

    game = {"pv": 50, "mana": 500, "player": "bob", "enemy_pv": 50}
    mydeck: Deck = create_deck(5, 3, 3)
    print(mydeck.get_deck_stats())
    card = mydeck.draw_card()
    print("card drawed:", card.name)

    goat = CreatureCard("goat", 2, "common", 2, 10)
    bun = CreatureCard("bun", 2, "common", 2, 10)

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
        ArtifactCard("heart of the mountain", 9, "rare", 3, "aoe"),
        ArtifactCard("shard of dragon anger", 11, "rare", 4, "direct"),
        ArtifactCard("cursed sword", 12, "legendary", 3, "single_random")
    ]
    print(end="\nPOLYMORFIC ARTIFACTS ")
    print("-------------------------------------------\n")
    # TURN SIMULATION
    for artifact in artifact_storage:
        artifact.play(game)
        print("")
    i: int = 0
    while i < 5:
        ArtifactCard.effects_update(game)
        i += 1
