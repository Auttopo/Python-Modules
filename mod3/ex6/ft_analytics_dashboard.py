from typing import Generator


def case_0(
    who: int,
    players: dict[int, list[str, int, int]],
    who2: int,
) -> None:
    """event:  killed a monster"""

    players[who][1] += 0.1  # xp
    players[who][2] += 5  # golds


def case_1(
    who: int,
    players: dict[int, list[str, int, int]],
    who2: int,
) -> None:
    """event: found a chest"""

    players[who][2] += 10  # golds


def case_2(
    who: int,
    players: dict[int, list[str, int, int]],
    who2: int,
) -> None:
    """event: finish a quest"""

    players[who][1] += 0.4  # xp
    players[who][2] += 10  # golds


def case_3(
    who: int,
    players: dict[int, list[str, int, int]],
    who2: int,
) -> None:
    """event: sell an item"""

    players[who][2] += 60  # golds
    players[who2][2] -= 65  # golds


def case_4(
    who: int,
    players: dict[int, list[str, int, int]],
    who2: int,
) -> None:
    """event: found treasure"""

    players[who][2] += 50  # golds


def case_5(
    who: int,
    players: dict[int, list[str, int, int]],
    who2: int,
) -> None:
    """event: killed a player"""

    players[who][3].add("player_killer")

    players[who][1] += 0.2  # xp

    players[who2][1] -= 0.1  # xp
    players[who2][2] -= 5  # golds


def case_6(
    who: int,
    players: dict[int, list[str, int, int]],
    who2: int,
) -> None:
    """event: finish a dungeon"""

    players[who][3].add("boss_slayer")
    players[who2][3].add("boss_slayer")

    players[who][1] += 1  # xp
    players[who][2] += 55  # golds

    players[who2][1] += 1  # xp
    players[who2][2] += 55  # golds


def case_7(
    who: int,
    players: dict[int, list[str, int, int]],
    who2: int,
) -> None:
    """event: found a Legendary treasure"""

    players[who][3].add("collector")

    players[who][1] += 0.1  # xp
    players[who][2] += 100  # golds


def random_number(seed: int, range: int = 10) -> Generator[int, None, None]:
    """create a random number"""

    r = seed
    plage = 4294967296
    multiple_chaos = 1664525
    jump = 1013904223
    for i in iter(int, 1):
        r = (r * multiple_chaos + jump) % plage
        yield r % range


def event_gen(what_gen: Generator[int, None, None]) -> int:
    """generate a random event"""

    key = next(what_gen)

    if key >= 0 and key <= 19:
        key = 0  # "killed a monster"
    elif key >= 20 and key <= 39:
        key = 1  # "found a chest"
    elif key >= 40 and key <= 54:
        key = 2  # "finish a quest"
    elif key >= 55 and key <= 69:
        key = 3  # "sell an item"
    elif key >= 70 and key <= 79:
        key = 4  # "found treasure"
    elif key >= 80 and key <= 89:
        key = 5  # "killed a player"
    elif key >= 90 and key <= 99:
        key = 6  # "finish a dungeon"
    else:
        key = 7  # "found a Legendary weapon"
    return key


def print_event(
    who: int,
    event: int,
    players: dict[int, list[str, int, int]],
    event_switch: dict[int, list[str, int]],
    who2: int,
) -> None:
    """print the event occured"""
    print(
        players.get(who)[0],
        "{ level",
        int(players.get(who)[1]),
        "}",
        event_switch.get(event)[0],
        end="",
    )
    if event == 5:
        print(f' nammed "{players.get(who2)[0]}"', end="")
    elif event == 6:
        print(f' with "{players.get(who2)[0]}"', end="")
    print("")


def set_last_achievements(
    players: dict[int, list[str, int, int]],
) -> None:
    """give achievements based on statistics"""

    best = players[0]

    # for the richest
    player = 0
    while player < 5:
        if players[player][2] > best[2]:
            best = players[player]
        player += 1
    best[3].add("true_dragon")

    # for the highest leveled
    player = 0
    while player < 5:
        if players[player][1] > best[1]:
            best = players[player]
        if players[player][1] > 60:
            players[player][3].add("level_60_!")
        player += 1
    best[3].add("speed_demon")


def is_unique(
    players: dict[int, list[str, int, int]],
    data: str
) -> bool:
    i = 0
    for player in players.items():
        if data in player[1][3]:
            i += 1
    if i != 1:
        return False
    return True


def summary(
    players: dict[int, list[str, int, int]],
    event_switch: dict[int, list[str, int]],
    gen_n: int,
) -> None:
    """summarize all stats and print it"""

    print("=== Game Analytics Dashboard ===")
    print("\nTotal Generations:", gen_n)

    print("\nEvery Players Lasts Stats:")
    player = 0
    while player < 5:
        print(
            players[player][0].capitalize(),
            "level:",
            int(players[player][1]),
            "golds:",
            players[player][2],
            ", achievements:",
            players[player][3],
        )
        player += 1

    events_count = {name: nbr for name, nbr, *oth in event_switch.values()}
    print("\nEvents Occured:")
    for event, nbr in events_count.items():
        print(event, ":", nbr)

    all_achievements = {ach for player_data in players.values()
                        for ach in player_data[3] if is_unique(players, ach)}
    print("\nUnique achievement(s)", all_achievements)

    players_investment = [[name, level / gold, gold / level]
                          for name, level, gold, *oth in players.values()]
    print("\nInvestment of players :")
    for player in players_investment:
        print(
            f"{player[0]}, {player[1]:.3f} level per gold, \
{player[2]:.2f} gold per level ")

    print("\nData Répartition:")
    print(
        "events : set | elements of events : list |\
elements of events list : dénominator str, totals, function associed"
    )
    print(
        "players : set | elements of players : list | elements of player list \
: dénominator str, level, gold, and achievement | achievement : dict"
    )


def players_event(r: int, seed: int) -> None:
    """prints randoms events and stats associed"""

    what_gen = random_number(seed, 101)
    who_gen = random_number(seed, 5)
    gen_n = 0

    players = {
        0: ["alice", 0, 0, set()],
        1: ["bob", 0, 0, set()],
        2: ["charlie", 0, 0, set()],
        3: ["luther", 0, 0, set()],
        4: ["jaina", 0, 0, set()],
    }

    event_switch = {
        0: ["killed a monster", 0, case_0],
        1: ["found a chest", 0, case_1],
        2: ["finish a quest", 0, case_2],
        3: ["sell an item", 0, case_3],
        4: ["found treasure", 0, case_4],
        5: ["killed a player", 0, case_5],
        6: ["finish a dungeon", 0, case_6],
        7: ["found a Legendary treasure", 0, case_7],
    }

    for i in range(r):
        event = event_gen(what_gen)
        event_switch[event][1] += 1
        who = next(who_gen)
        with_who = next(who_gen)
        gen_n += 3
        while who == with_who:
            with_who = next(who_gen)
            gen_n += 1

        event_switch[event][2](who, players, with_who)
        print_event(who, event, players, event_switch, with_who)
    print("The game closed.\n")

    set_last_achievements(players)
    summary(players, event_switch, gen_n)


if __name__ == "__main__":
    players_event(1000, 971)
