
import math


def distance(pos1: tuple[int, int, int], pos2: tuple[int, int, int]) -> int:
    """ calcul 3d distance """
    return math.sqrt(
                    (pos2[0] - pos1[0]) ** 2 +
                    (pos2[1] - pos1[1]) ** 2 +
                    (pos2[2] - pos1[2]) ** 2)


def parser(data: str) -> tuple[int, int, int]:
    """ yes i know this function is complicated for nothing """

    n = [0, 0, 0]
    i = 0
    sign = 0
    for c in data:
        if sign == 0:
            if c == '-':
                sign = -1
                continue
            else:
                sign = 1
        if c.isdigit():
            n[i] *= 10
            n[i] += int(c)
        elif c == ',' and i < 2:
            n[i] *= sign
            i += 1
            sign = 0
        else:
            raise Exception("invalid coordinates occured")
            return
    pos = (n[0], n[1], n[2] * sign)
    print(pos, "<- position parsed and created --")
    return pos


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    try:
        pos1 = parser("0,5,3")
        pos2 = parser("10,20,3")
        print("distances beetwin pos1 and pos2 :", distance(pos1, pos2))
        t = parser("1r23,-666,554")
        print(t)
    except Exception as e:
        print(f"{e}")

    unvrapx, unvrapy, unvrapz = pos1
    print(f"pos1 unvraped x:{unvrapx}, y:{unvrapy}, z:{unvrapz}")
