
def garden_operations() -> None:
    """ demonstrate commons errors """

    try:
        i = float("coucou")
        i = i + 1
    except ValueError:
        print("ValueError occured")
    try:
        test = 1 / 0
        test = test + 1
    except ZeroDivisionError:
        print("ZeroDivisionError occured")
    try:
        file = open("blabliblou", "r")
        file.close()
    except FileNotFoundError:
        print("FileNotFoundError occured")
    try:
        vegetable = {"identifier": "banana", "color": "blue"}
        print(vegetable["location"])
    except KeyError:
        print("KeyError occured")


def test_error_types() -> None:
    """ show and catch differents errors """

    try:
        i = float("coucou")
        i = i + 1
    except ValueError:
        print("ValueError occured")
    try:
        test = 1 / 0
        test = test + 1
    except ZeroDivisionError:
        print("ZeroDivisionError occured")
    try:
        file = open("blabliblou", "r")
        file.close()
    except FileNotFoundError:
        print("FileNotFoundError occured")
    try:
        vegetable = {"identifier": "banana", "color": "blue"}
        print(vegetable["location"])
    except KeyError:
        print("KeyError occured")

    try:
        i2 = float("coucou")
        i2 = i2 + 1
        test2 = 1 / 0
        test2 = test2 + 1
        file2 = open("blabliblou", "r")
        file2.close()
        vegetable2 = {"identifier": "banana", "color": "blue"}
        print(vegetable2["location"])
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Error occured")
    print("\nthe function still runing")


if __name__ == "__main__":
    garden_operations()
    test_error_types()
    print("the program still runing")
