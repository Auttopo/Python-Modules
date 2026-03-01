
def test1() -> None:
    from alchemy.grimoire.validator import validate_ingredients
    print("Testing ingredient validation:")
    print('validate_ingredients("fire air")', validate_ingredients("fire air"))
    print('validate_ingredients("dragon scales")',
          validate_ingredients("dragon scales"))
    print("")


def test2() -> None:
    from alchemy.grimoire.spellbook import record_spell
    print("Testing spell recording with validation:")
    print('record_spell("Fireball", "fire air"):',
          record_spell("Fireball", "fire air"))
    print('record_spell("Dark Magic", "shadow"):',
          record_spell("Dark Magic", "shadow"))
    print("")


def test3() -> None:
    from alchemy.grimoire.spellbook import record_spell
    print("Testing late import technique:")
    print('record_spell("Lightning", "air"):',
          record_spell("Lightning", "air"))
    print("")


if __name__ == "__main__":
    print("=== Circular Curse Breaking ===\n")
    test1()
    test2()
    test3()
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")
