
from ex3.FantasyCardFactory import FantasyCardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import creature_set, spell_set, artifact_set
from ex3.GameEngine import GameEngine, Player
from ex3.AggressiveStrategy import AggressiveStrategy
import time

if __name__ == "__main__":
    factory = FantasyCardFactory(
        "basic theme",
        [
            (FantasyCardFactory.create_creature,
             12, CreatureCard, len(creature_set())),
            (FantasyCardFactory.create_spell, 3, SpellCard, len(spell_set())),
            (FantasyCardFactory.create_artifact,
             2, ArtifactCard, len(artifact_set()))
        ])
    factory.add_theme(
        "classic theme",
        [
            (FantasyCardFactory.create_creature,
             30, CreatureCard, len(creature_set())),
            (FantasyCardFactory.create_spell, 10, SpellCard, len(spell_set())),
            (FantasyCardFactory.create_artifact,
             10, ArtifactCard, len(artifact_set()))
        ])

    factory.set_active_them("classic theme")

    mystr = factory.get_supported_types()
    print(mystr)

    print(end="BASIC SETUP FINISHED")
    print("------------------------------------------------------------------")

    player = Player("bob", 2, "commun", "warlock")
    enemie = Player("doofenshmirtz", 2, "rare", "warrior")

    game = GameEngine(player, enemie)
    game.configure_engine(factory, AggressiveStrategy)

    print(end="GAME CONFIGURATION FINISHED")
    print("------------------------------------------------------------------")

    time.sleep(2)
    game.simulate_turn()
    game.simulate_turn()
