
class SecurePlant:

    __old = 0
    __time = 0

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
                print(end="your input is far larger than the stored value\n")
                if (input("enter (y) if you sur to applie :") != "y"):
                    return
            if (((value - self.__height) > 10) and (self.__height < value)):
                print(end="your input is far larger than the stored value\n")
                if (input("enter (y) if you sur to applie :") != "y"):
                    return
            self.__height = value
        else:
            print("incorrect value, not applied")

    def set_age(self, value: int) -> None:
        """ change the age value of the object, with security filter """
        if value >= 0:
            if (((self.__days - value) > 10) and (self.__days > value)):
                print(end="your input is far larger than the stored value\n")
                if (input("enter (y) if you sur to applie :") != "y"):
                    return
            if (((value - self.__days) > 10) and (self.__days < value)):
                print(end="your input is far larger than the stored value\n")
                if (input("enter (y) if you sur to applie :") != "y"):
                    return
            self.__days = value
        else:
            print("incorrect value, not applied")


if __name__ == "__main__":
    tulip = SecurePlant("tulip", 18, 19)
    print(tulip.get_age())
    tulip.set_age(-3)
    print(tulip.get_age())
    tulip.set_age(3)
    print(tulip.get_age())
