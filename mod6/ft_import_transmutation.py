
def test1() -> None:
    import alchemy.elements
    print("Method 1 - Full module import:")
    print("alchemy.elements.create_fire()", alchemy.elements.create_fire())


def test2() -> None:
    print("\nMethod 2 -  Specific function import:")
    from alchemy.elements import create_water
    print("create_water():", create_water())


def test3() -> None:
    print("\nMethod 3 - Aliased import:")
    from alchemy.potions import healing_potion as heal
    print(heal())


def test4() -> None:
    from alchemy.elements import create_fire, create_water
    from alchemy.potions import strength_potion

    print("\nMethod 4 - Multiple imports:")
    print("create_fire():", create_fire())
    print("create_water():", create_water())
    print("strength_potion()", strength_potion())


if __name__ == "__main__":
    print("=== Import Transmutation Mastery ===\n")
    test1()
    test2()
    test3()
    test4()
    print("\nAll import transmutation methods mastered!")
