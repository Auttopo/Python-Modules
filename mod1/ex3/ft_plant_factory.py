
class Plant:
    time = 0
    old = 0

    """ Basic Plant class, store informations about a plant in your garden.
    Usefull methods are available for data management """

    def __init__(self, name: str, height: int, days: int) -> None:
        """ init of the class with parameters (int same order)
        : name:str, height:int, age:int """
        if days < 0:
            print("invalid age set to 0")
            days = 0
        if height < 0:
            print("invalid height set to 0")
            height = 0
        if name == "":
            print("invalid name set to (Plant)")
            name = "Plant"
        self.name = name
        self.height = height
        self.days = days
        self.old = 0
        print(end="(Created) ")
        self.say()

    def grow_for_time(self) -> None:
        """ applie the time passed to the height of the plant,
        this function have no utility outside the class
        because auto applied when necessary """
        if self.time > 3:
            print(
                "this plent grow", int(self.time / 4),
                "cm from your last passage")
            self.height += int(self.time / 4)
            self.time -= int(self.time % 4)

    def say(self) -> None:
        """ display all basics informations of the plant (name, height, age)"""
        print(
            self.name, ": ",
            self.height, "cm, ",
            self.days, " days old", sep="")

    def age(self, time: int) -> None:
        """ the time elapses according to the chosen value (in days)"""
        if time < 1:
            return
        self.days += time
        self.old += time
        self.time += time
        self.grow_for_time()

    def grow(self, size: int) -> None:
        """ grow the Plant for the chosen size (in cm) """
        if size < 1:
            return
        self.height += size
        self.days += size * 4
        self.old += size * 4

    def get_info(self) -> None:
        """display all basics informations of the plant (name, height, age),
        like (say) method
        for more, display the time passed in the garden"""
        print("=== Day:", self.old, "===")
        self.say()


def take_input(says: str) -> int:
    """ take the input with security filter """
    value = input(says)
    if value.isdigit():
        value = int(value)
    else:
        value = int(0)
    return value


def plant_factory(data: list[tuple[str, int, int]]) -> list[Plant]:
    """ factory program to make large number of plants object
    using a while with the parameter"""

    plant_deposit = []
    i = 0
    print("Creation process start.")
    for elem in data:
        print("plant", i + 1)
        plant_deposit.append(Plant(*elem))
        i += 1
    print("Creation process end.")
    return plant_deposit


if __name__ == "__main__":
    plants_spec = [
        ("rose", 15, 10), ("larkspur", 2, 2), ("tulip", 2, 4),
        ("sunflower", 102, 153), ("abutilon", 9, 21)]
    deposit = plant_factory(plants_spec)

    print("\nPlant deposit summary:")
    i = 0
    for elem in deposit:
        deposit[i].say()
        i += 1
