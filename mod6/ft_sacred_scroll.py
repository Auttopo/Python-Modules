
def test1() -> None:
    import alchemy

    print("alchemy.elements.create_fire()", alchemy.elements.create_fire())
    print("alchemy.elements.create_water()", alchemy.elements.create_water())
    print("alchemy.elements.create_earth()", alchemy.elements.create_earth())
    print("alchemy.elements.create_air()", alchemy.elements.create_air())


def test2() -> None:
    import alchemy.elements

    # exercice purpose
    print("alchemy.create_fire()", alchemy.create_fire())  # type: ignore
    print("alchemy.create_water()", alchemy.create_water())  # type: ignore
    try:
        # exercice purpose
        print("alchemy.create_earth()", alchemy.create_earth())  # type: ignore
    except AttributeError as e:
        print("error:", e)
    try:
        # exercice purpose
        print("alchemy.create_air()", alchemy.create_air())  # type: ignore
    except AttributeError as e:
        print("error:", e)


if __name__ == "__main__":
    import alchemy
    print("=== Sacred Scroll Mastery ===\n")
    test1()
    print("")
    test2()
    print("\nPackage metadata:")
    print("Author:", alchemy.__author__)
    print("Version", alchemy.__version__)
