
from ex2.EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":
    print("=== DataDeck Ability System ===\n")
    game = {"pv": 50, "mana": 500, "player": "bob", "enemy_pv": 50}
    magical_wyrm = EliteCard("Magical Wyrm", 20, "mythic", 100, 40, 80)
    mob: CreatureCard = CreatureCard("mini golem", 3, "common", 2, 25)
    mob2: CreatureCard = CreatureCard("bun", 1, "common", 1, 1)

    magical_wyrm.play(game)
    print("")

    magical_wyrm.show_stats()

    print("\nCombat phase: ---")
    magical_wyrm.attack(mob)
    magical_wyrm.defend(10)

    print("\nMagic phase: ---")
    magical_wyrm.cast_spell("fire storm", [mob, mob2])

    print("Multiple interface implementation successful!")
