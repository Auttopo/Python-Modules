
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

    def __init__(self, name: str, water: int, sun: int) -> None:
        """ minimal init for plant with water value """
        self.__water = water
        self.__sun_hours = sun
        self.__name = None
        self.set_name(name)

    def change_water(self, water: int) -> None:
        """ change the water value or catch an error """
        if water < 0:
            raise WaterError("Negative water value, can't be set")
        self.__water = water
        return None

    def set_name(self, name: str) -> None:
        """ set the flower name with security """
        if name:
            if name != "":
                self.__name = name
                return
        raise PlantError("No name chosen, can't be set")

    def get_water(self) -> int:
        """ return the water value """
        return self.__water

    def get_sun(self) -> int:
        """ return the water value """
        return self.__sun_hours

    def get_name(self) -> str:
        """ return the name string """
        return self.__name

    def broke_the_plant(self) -> None:
        """ change the name to none """
        self.__name = None


class Garden:
    """ basic Garden class """

    def __init__(self, name: str, water: int, sun: int) -> None:
        """ create the garden with a first plant """
        self.garden = []
        self.garden.append({"name": name, "plant": Plant(name, water, sun)})

    def add(self, name: str, water: int, sun: int) -> None:
        """ add a plant to the garden """
        self.garden.append({"name": name, "plant": Plant(name, water, sun)})

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
        raise GardenError(target, "This plant do not exist")


def check_plant_health(
                    plant_name: str, water_level: int,
                    sunlight_hours: int) -> None:
    """ check the plant health , raise error if occured """

    if plant_name is None:
        raise ValueError("none name")
    if plant_name == "":
        raise ValueError("no name setted")
    if water_level < 1:
        raise ValueError("water lever < 1. current " + str(water_level))
    if water_level > 10:
        raise ValueError("water lever > 10. current: " + str(water_level))
    if sunlight_hours < 2:
        raise ValueError("sunlight time < 2. current: " + str(sunlight_hours))
    if sunlight_hours > 10:
        raise ValueError("sunlight time > 12. current: " + str(sunlight_hours))
    print("All", plant_name, "datas are good")


def test_plant_checks() -> None:
    """ test plants datas"""

    try:
        tomato = Plant("tomato", 2, 5)
        check_plant_health(
                        tomato.get_name(),
                        tomato.get_water(), tomato.get_sun())
    except ValueError as e:
        print(f"Error catched: {e}")
    try:
        corn = Plant("corn", 0, 4)
        check_plant_health(corn.get_name(), corn.get_water(), corn.get_sun())
    except ValueError as e:
        print(f"Error catched: {e}")
    try:
        basilica = Plant("basilica", 2, 32)
        check_plant_health(
                        basilica.get_name(),
                        basilica.get_water(), basilica.get_sun())
    except ValueError as e:
        print(f"Error catched: {e}")
    try:
        simple_plant = Plant("glitched_plant", 2, 32)
        simple_plant.broke_the_plant()
        check_plant_health(
                        simple_plant.get_name(),
                        simple_plant.get_water(), simple_plant.get_sun())
    except ValueError as e:
        print(f"Error catched: {e}")


if __name__ == "__main__":
    test_plant_checks()
