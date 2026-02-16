
def check_temperature(temp_str: str = None) -> int:
    """ check the str input and asign the temperature if it's valide """

    if temp_str is None:
        temp_str = input("What is the tempereature ? : ")

    if temp_str.isdigit():
        value = int(temp_str)
        if value >= 0 and value <= 40:
            print(temp_str, "is valid\n")
            return value
    print("invalid number not returned\n")


def test_temperature_input() -> None:
    """ test the temperature with differents inputs """
    print(check_temperature("25"), ":result with 25\n")
    print(check_temperature("abc"), ":result with abc\n")
    print(check_temperature("100"), ":result with 100\n")
    print(check_temperature("-50"), ":result with -50\n")
    print(check_temperature(""), ":result with nothing\n")


if __name__ == "__main__":
    check_temperature()
    test_temperature_input()
    print("the program still runing")
