
def test1() -> None:
    from alchemy.transmutation import basic
    print("Testing Absolute Imports (from basic.py):")
    print(basic.lead_to_gold())
    print(basic.stone_to_gem(), "\n")


def test2() -> None:
    from alchemy.transmutation import advanced
    print("Testing Relative Imports (from advanced.py):")
    print(advanced.philosophers_stone())
    print(advanced.elixir_of_life(), "\n")


def test3() -> None:
    import alchemy
    try:
        print("Testing Package Access:")
        print("alchemy.transmutation.lead_to_gold():",
              alchemy.transmutation.lead_to_gold())
        print("alchemy.transmutation.philosophers_stone():",
              alchemy.transmutation.philosophers_stone(), "\n")
    except Exception as e:
        print("error occured:", e)


if __name__ == "__main__":
    print("=== Pathway Debate Mastery ===\n")
    test1()
    test2()
    test3()
    print("Both pathways work! Absolute: clear, Relative: concise")
