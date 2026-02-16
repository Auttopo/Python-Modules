
class Plant:

    """ Basic Plant class, store informations about a plant in your garden.
    Usefull methods are available for data management """

    def __init__(self, name, height: int, age: int) -> None:
        """ init of the class with parameters (int same order)
        : name:str, height:int, age:int """
        self.name = name
        self.height = height
        self.age = age

    def say(self) -> None:
        """ diplay basics informations of the object """
        print(
                self.name, ": ",
                self.height, "cm, ",
                self.age, " days old", sep="")


if __name__ == "__main__":
    tulip = Plant("Tulip", 8, 27)
    sunflower = Plant("Sunflower", 12, 62)
    hydrangea = Plant("Hydrangea", 3, 9)
    tulip.say()
    sunflower.say()
    hydrangea.say()
