def fibonacci(n: int) -> int:
    """create n of number of the fibonacci suit"""

    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibo_generator() -> int:
    """generate fibonacci numbers"""

    i = 0
    e = 1
    for i in iter(int, 1):
        yield fibonacci(e)
        e += 1


def fibo_event(r: int) -> None:
    """create n number of fobonacci suit with a generator"""
    #  for n in range(4):
    print(end="Generated Fibonacci suit :")
    t = fibo_generator()
    for i in range(r):
        print("", next(t), end="")
    print("")


def is_prime(nbr: int) -> bool:
    """return true if the number is prime"""

    i = 1
    e = 1
#    if nbr == 1:
#        return True
    for e in range(nbr):
        for i in range(nbr):
            if nbr == (i * e):
                return False
    return True


def prime_generator() -> int:
    """generate primes numbers"""

    i = 0
    e = 1
    for i in iter(int, 1):
        if is_prime(e) is True:
            yield e
        e += 1


def prime_event(r: int) -> None:
    """create n first prime numbers"""

    print(end="Generated Prime suit :")
    t = prime_generator()
    for i in range(r):
        print("", next(t), end="")
    print("")


def random_number(seed: int, range: int = 10) -> None:
    """create a random number"""

    r = seed
    plage = 4294967296
    multiple_chaos = 1664525
    jump = 1013904223
    for i in iter(int, 1):
        r = (r * multiple_chaos + jump) % plage
        yield r % range


def players_event(r: int) -> None:
    """prints randoms events and stats associed"""

    random_n = random_number(88, 3)

    players = {
        0: ["alice", 0],
        1: ["bob", 0],
        2: ["charlie", 0],
    }

    event_switch = {
        0: ["killed a monster", 0],
        1: ["found treasure", 0],
        2: ["leveled up", 0],
    }

    for i in range(r):
        n = next(random_n)
        n2 = next(random_n)
        if n2 == 2:
            players.get(n)[1] += 1
        event_switch.get(n2)[1] += 1
        print(
            players.get(n)[0],
            "{ level",
            players.get(n)[1],
            "}",
            event_switch.get(n2)[0],
        )

    print("\nMonster killed :", event_switch[0][1])
    print("Treasure events :", event_switch[1][1])
    print("Level-up events :", event_switch[2][1])

    high = players[1]
    for p in players.items():
        if p[1][1] > high[1]:
            high = p[1]
    print("Highest leveled player :", high[0], f"( {high[1]} )", "\n")


if __name__ == "__main__":
    players_event(1000)
    fibo_event(10)
    prime_event(10)
