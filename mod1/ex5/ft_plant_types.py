
class SecurePlant:

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
        self.__name = name
        self.__height = height
        self.__days = days
        self.__old = 0
        self.__time = 0

        print(end="(Created) ")
        self.say()

    def grow_for_time(self) -> None:
        """ applie the time passed to the height of the plant,
        this function have no utility outside the class
        because auto applied when necessary """
        if self.__time > 3:
            print(
                    "this plent grow", int(self.__time / 4),
                    "cm from your last passage")
            self.__height += int(self.__time / 4)
            self.__time -= int(self.__time % 4)

    def say(self) -> None:
        """ display all basics informations of the plant (name, height, age)"""
        print(
                self.__name, ": ",
                self.__height, "cm, ",
                self.__days, " days old", sep="")

    def age(self, time: int) -> None:
        """ the time elapses according to the chosen value (in days)"""
        if time < 1:
            return
        self.__days += time
        self.__old += time
        self.__time += time
        self.grow_for_time()

    def grow(self, size: int) -> None:
        """ grow the Plant for the chosen size (in cm) """
        if size < 1:
            return
        self.__height += size
        self.__days += size * 4
        self.__old += size * 4

    def get_info(self) -> None:
        """display all basics informations of the plant (name, height, age),
        like (say) method
        for more, display the time passed in the garden"""
        print("=== Day:", self.__old, "===")
        self.say()

    def get_age(self) -> int:
        """ return the age value of the object """
        return self.__days

    def get_height(self) -> int:
        """ return the height value of the object """
        return self.__height

    def set_height(self, value: int) -> None:
        """ change the height value of the object, with security filter """
        if value >= 0:
            if (((self.__height - value) > 10) and (self.__height > value)):
                print(end="your input is far larger than the stored value")
                if (input("enter (y) if you sur to applie :") != "y"):
                    return
            if (((value - self.__height) > 10) and (self.__height < value)):
                print(end="your input is far larger than the stored value")
                if (input("enter (y) if you sur to applie :") != "y"):
                    return
            self.__height = value
        else:
            print("incorrect value, not applied")

    def set_age(self, value: int) -> None:
        """ change the age value of the object, with security filter """
        if value >= 0:
            if (((self.__days - value) > 10) and (self.__days > value)):
                print(end="your input is far larger than the stored value")
                if (input("enter (y) if you sur to applie :") != "y"):
                    return
            if (((value - self.__days) > 10) and (self.__days < value)):
                print(end="your input is far larger than the stored value")
                if (input("enter (y) if you sur to applie :") != "y"):
                    return
            self.__days = value
        else:
            print("incorrect value, not applied")


class Flower(SecurePlant):

    """ child of the plant class, with flower stuff """

    def __init__(self, name: str, height: int, days: int, color: str) -> None:
        """ init of the folower with parent like functioning """
        super().__init__(name, height, days)
        self.__stade = "Notbloomed"
        self.color = color

    def bloom(self) -> None:
        """ bloom the flower whose the function is applied """
        print("The flower you took care is now blooming...")
        print("Waw, what a beautiful flower it is now")
        self.__stade = "Bloomed"

    def say_more(self) -> None:
        """ print the class bases and specificitys infos """
        super().say()
        print("| color:", self.color)
        print("|", self.__stade)


class Tree(SecurePlant):

    """ child of the plant class, with tree stuff """

    def __init__(self, name: str, height: int, days: int, trunk: int) -> None:
        """ init of the tree with parent like functioning """
        super().__init__(name, height, days)
        self.trunk_diameter = trunk

    def produce_shade(self) -> None:
        """ print a message to simulate tree shading """
        print("The tree is producing shade")

    def say_more(self) -> None:
        """ print the class bases and specificitys infos """
        super().say()
        print("| trunk diameter", self.trunk_diameter, "cm")


class Vegetable(SecurePlant):

    """ child of the plant class, with vegetable stuff """

    def __init__(
                    self, name: str, height: int, days: int,
                    season: str, nutriscore: str) -> None:
        """ init of the vegetable with parent like functioning """
        super().__init__(name, height, days)
        self.__nutritional_value = nutriscore
        self.__harvest_season = season

    def say_more(self) -> None:
        """ print the class bases and specificitys infos """
        super().say()
        print("| harvest season :", self.__harvest_season)
        print("| nutritional property:", self.__nutritional_value)


if __name__ == "__main__":
    flowa = Flower("rose", 2, 8, "blue")
    flowa2 = Flower("tulip", 8, 24, "yellow")
    print("")
    flowa.say_more()
    flowa2.say_more()
    print("")
    flowa.bloom()
    print("")
    flowa.say_more()
    print("")
    tree = Tree("just a tree", 260, 912, 23)
    tree2 = Tree("acacia", 56, 243, 12)
    print("")
    tree.produce_shade()
    print("")
    tree.say_more()
    tree2.say_more()
    print("")
    tomato = Vegetable("Tomato", 10, 121, "winter", "vitamine b12")
    not_tomato = Vegetable("Carrot", 5, 27, "summer", "rich in calcium")
    print("")
    tomato.say_more()
    not_tomato.say_more()
