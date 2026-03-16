
from typing import Callable


def spell_combiner(
        spell1: Callable[[], int | float], spell2: Callable[[], int | float]
) -> Callable[[], tuple[int | float, int | float]]:
    def spell() -> tuple[int | float, int | float]:
        return (spell1(), spell2())
    return spell


def power_amplifier(
        base_spell: Callable[[], int | float], multiplier: int
) -> Callable[[], int | float]:
    def spell() -> int | float:
        return (base_spell() * multiplier)
    return spell


def conditional_caster(
        condition: Callable[
            [int | float], bool], spell: Callable[[], int | float
                                                  ]
) -> Callable[[], str]:

    if condition(spell()):
        def new_spell() -> str:
            return spell.__name__
    else:
        def new_spell() -> str:
            return "Spell fizzled"
    return new_spell


def spell_sequence(
        spells: list[Callable[[], int | float]]
) -> Callable[[], list[int | float]]:

    new_data: list[int | float] = []
    for elem in spells:
        new_data.append(elem())

    def new_spell() -> list[int | float]:
        return new_data
    return new_spell


def fire_ball() -> int:
    return -15


def heal() -> int:
    return 12


def condition(data: int | float) -> bool:
    return data >= 10


if __name__ == "__main__":
    print("\nspell_combiner")
    func1 = spell_combiner(fire_ball, heal)
    print(func1())
    print("\npower_amplifier")
    func2 = power_amplifier(fire_ball, 3)
    print(func2())
    print("\nconditional_caster, damage=-15 >= 20")
    func3 = conditional_caster(condition, fire_ball)
    print(func3())
    print("\nconditional_caster, heal=12 >= 10")
    func3 = conditional_caster(condition, heal)
    print(func3())
    print("\nspell_sequence")
    func4 = spell_sequence([fire_ball, heal])
    print(func4())
