
from ex3.GameStrategy import GameStrate
from ex3.FantasyCardFactory import GameDict
from ex0.CreatureCard import CreatureCard


class AggressiveStrategy(GameStrate):  # type: ignore

    # Prioritizes attacking and dealing damage
    # Plays low-cost creatures first for board presence
    # Targets enemy creatures and player directly
    # Returns comprehensive turn execution results

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    def get_strategy_name(self) -> str:
        return str(self.__class__.__name__)

    def prioritize_targets(self, available_targets: list) -> list:
        pass

    @staticmethod
    def enter_choice(game_state: GameDict) -> str:

        for elem in game_state["e_hand"]:
            if isinstance(elem, CreatureCard):
                return "2"

        return "TEMPPPP"

    @staticmethod
    def card_choice(game_state: GameDict) -> str:
        return "TEMPPPP"

    @staticmethod
    def ability_choice(game_state: GameDict) -> str:
        return "TEMPPPP"

    @staticmethod
    def target_choice(game_state: GameDict) -> str:
        return "TEMPPPP"
