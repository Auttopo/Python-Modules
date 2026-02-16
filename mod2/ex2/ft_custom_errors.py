
class GardenError(Exception):
    """ garden class error for exceptions catch """

    def __init__(self, say: str = "Error occured") -> None:
        """ minimal init for error message """
        self.__say = say

    def __str__(self) -> str:
        """ return error message for the catch """
        return "GardenError, " + self.__say


class PlantError(GardenError):
    """ plant class error for exceptions catch """

    def __init__(self, say: str = "Error occured") -> None:
        """ minimal init for error message """
        self.__say = say

    def __str__(self) -> str:
        """ return error message for the catch """
        return "PlantError, " + self.__say


class WaterError(GardenError):
    """ water class error for exceptions catch """

    def __init__(self, say: str = "Error occured") -> None:
        """ minimal init for error message """
        self.__say = say

    def __str__(self) -> str:
        """ return error message for the catch """
        return "WaterError, " + self.__say


class Plant:
    """ basic plant class with stored water value """

    def __init__(self, name: str, water: int) -> None:
        """ minimal init for plant with water value """
        self.__water = water
        self.__name = None
        self.set_name(name)

    def change_water(self, water: int) -> None:
        """ change the water value or catch an error """
        if water < 0:
            raise WaterError("Negative water value, can't be set")
        self.__water = water
        return None

    def set_name(self, name: str) -> None:
        if name:
            if name != "":
                self.__name = name
                return
        raise PlantError("No name chosen, can't be set")

    def get_water(self) -> int:
        """ return the water value """
        return self.__water

    def get_name(self) -> str:
        """ return the name string """
        return self.__name


class Garden:
    """ basic Garden class """

    def __init__(self, name: str, water: int) -> None:
        """ create the garden with a first plant """
        self.garden = []
        self.garden.append({"name": name, "plant": Plant(name, water)})

    def add(self, name: str, water: int) -> None:
        """ add a plant to the garden """
        self.garden.append({"name": name, "plant": Plant(name, water)})

    def find(self, target: str, nbr: int = 0) -> Plant:
        """return the fist element with the chosen name and optional value"""

        i = 0
        found = None
        for elem in self.garden:
            if elem.get("name") == target:
                if i == nbr:
                    found = elem
                i += 1
        if found:
            return found.get("plant")
        raise GardenError("This plant do not exist")


def error_catcher_exemple() -> None:
    """ demonstate my customs exceptions catching """

    garden = Garden("tulip", 2)
    garden.add("sunflower", 3)

    try:
        tmp = garden.find("flower")
        print(tmp.get_name())
    except GardenError as e:
        print(f"Garden except catched : {e}")
    try:
        garden.add("", 2)
    except PlantError as e:
        print(f"Plant except catched : {e}")
    try:
        garden.find("sunflower").change_water(2)
        print("water changed to", garden.find("sunflower").get_water())
        garden.find("sunflower").change_water(-2)
        print("water changed to", garden.find("sunflower").get_water())
    except WaterError as e:
        print(f"Water except catched : {e}")

    try:
        tmp = garden.find("flower")
        print(tmp.get_name())
    except GardenError as e:
        print(f"Garden except catched : {e}")
    try:
        garden.add("", 2)
    except GardenError as e:
        print(f"Garden except catched : {e}")
    try:
        garden.find("sunflower").change_water(2)
        print("water changed to", garden.find("sunflower").get_water())
        garden.find("sunflower").change_water(-2)
        print("water changed to", garden.find("sunflower").get_water())
    except GardenError as e:
        print(f"Garden except catched : {e}")


if __name__ == "__main__":
    error_catcher_exemple()
