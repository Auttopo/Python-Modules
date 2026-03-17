
from typing import Callable, TypedDict


class MemoryDict(TypedDict):
    store: Callable[[str, int], None]
    recall: Callable[[str], int | None]


def mage_counter() -> Callable[[], int]:
    i = [0]

    def magic() -> int:
        i[0] += 1
        return i[0]
    return magic


def spell_accumulator(initial_power: int) -> Callable[[], int]:
    i = [initial_power]

    def magic() -> int:
        i[0] += initial_power
        return i[0]
    return magic


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def magic(item: str) -> str:
        return item + " " + enchantment_type
    return magic


def memory_vault(

) -> MemoryDict:
    storage = {}

    def store(key: str, value: int) -> None:
        storage.update({key: value})

    def recall(key: str) -> int | None:
        return storage.get(key)

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("\nmage_counter :")
    func = mage_counter()
    print(func())
    print(func())
    print(func())

    print("\nspell_accumulator :")
    func2 = spell_accumulator(11)
    print(func2())
    print(func2())
    print(func2())

    print("\nenchantment_factory :")
    func3 = enchantment_factory("PoerMegaMaxed")
    print(func3("sword"))

    print("\nmemory_vault :")
    funcs4 = memory_vault()
    funcs4["store"]("poulet", 5)
    funcs4["store"]("chicken", 18)
    print(funcs4["recall"]("poulet"))
    print(funcs4["recall"]("chicken"))
