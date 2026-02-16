
def unique(localset1: set, localset2: set, localset3: set) -> None:
    "look for unique set element in the first argument"
    d = localset1 - localset2.union(localset3)
    if d:
        print(d, end="")


def compare(s1: str, s2: str, set1: set, set2: set) -> None:
    """ compare data of two sets"""
    s0 = "| " + s1 + " vs " + s2 + " |"
    print("-" * len(s0))
    print(s0)
    print("| common :", set1.intersection(set2))
    print("|", s1, "uniques :", set1 - set2)
    print("|", s2, "uniques :", set2 - set1)
    print("|")


if __name__ == "__main__":

    allset = {
            "boss_slayer", "collector", "first_kill",
            "level_10", "perfectionist",
            "speed_demon", "treasure_hunter"}
    aliceset = {
            "first_kill", "level_10",
            "treasure_hunter", "speed_demon"}
    bobset = {
            "first_kill", "level_10",
            "boss_slayer", "collector"}
    charlieset = {
                "level_10", "treasure_hunter",
                "boss_slayer", "speed_demon",
                "perfectionist"}

    print("=== Achievement Tracker System ===\n")

    print("All achievements :", allset)

    print("\nalice achievements:", aliceset)
    print("bob achievements:", bobset)
    print("charlie achievements:", charlieset)

    print("\nCommon to all :", charlieset.intersection(aliceset, bobset))
    print(end="Rare achievements:")
    unique(aliceset, charlieset, bobset)
    unique(bobset, aliceset, charlieset)
    unique(charlieset, aliceset, bobset)
    print("\n")
    compare("Alice", "Bob", aliceset, bobset)
    compare("Alice", "Charlie", aliceset, charlieset)
    compare("Bob", "charlie", bobset, charlieset)
