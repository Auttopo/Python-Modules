
from typing import Any
import sys
import os
import operator
import functools
from typing import Callable
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return functools.reduce(operator.add, spells)
    if operation == "multiply":
        return functools.reduce(operator.mul, spells)
    if operation == "max":
        return functools.reduce(max, spells)
    if operation == "min":
        return functools.reduce(min, spells)

    return 0


def powa(power: int, element: str, target: str) -> str:
    return f"{element} damage {power}pt to: {target}"


def partial_enchanter(
        base_enchantment: Callable[..., Any]
) -> dict[str, Callable[..., Any]]:
    return {
        "fire_enchant": functools.partial(
            base_enchantment, 50, "fire_enchant"),
        "ice_enchant": functools.partial(
            base_enchantment, 50, "ice_enchant"),
        "lightling_enchant": functools.partial(
            base_enchantment, 50, "lightling_enchant")
    }


@functools.lru_cache(maxsize=150)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @functools.singledispatch
    def dispatcher(data: Any) -> str:
        return "Nothing to do"

    @dispatcher.register(int)
    def _int_case(data: int) -> str:
        return f"{data * 8} big calculation, big brain"

    @dispatcher.register(str)
    def _str_case(data: str) -> str:
        return data + " : what a nice string it is"

    @dispatcher.register(list)
    def list_case(data: list[Any]) -> str:
        out = "mmmh... listing"
        for i, elem in enumerate(data, 1):
            out = f"{out}\n{i} | {elem}"
        return out

    return dispatcher


if __name__ == "__main__":
    from ex1.higher_magic import heal, fire_ball
    print("\nspell_reducer :")
    print(spell_reducer([heal(), fire_ball()], "add"))
    print(spell_reducer([heal(), fire_ball()], "multiply"))
    print(spell_reducer([heal(), fire_ball()], "max"))
    print(spell_reducer([heal(), fire_ball()], "min"))

    print("\npartial_enchanter :")
    enchants = partial_enchanter(powa)
    print(enchants["fire_enchant"]("goblin"))
    print(enchants["ice_enchant"]("goblin"))
    print(enchants["lightling_enchant"]("goblin"))

    print("\nmemoized_fibonacci :")
    for i in range(6):
        print(memoized_fibonacci(i))

    print("\nspell_dispatcher :")
    func = spell_dispatcher()
    print(func("coucou"))
    print(func(51))
    print(func([1, 91, 7, "ush", -12]))
