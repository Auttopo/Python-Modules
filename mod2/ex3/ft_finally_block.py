
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
        """ set name plant with security """
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
        if self.__name:
            return self.__name
        raise PlantError("Plant name never setted (= None)")

    def broke_the_plant(self) -> None:
        """ change name plant to none """
        self.__name = None


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
        raise GardenError(target, "This plant do not exist")


def water_plants(plant_list: list[tuple[str: str, str: Plant]]) -> None:
    """ water plants and do not crash """
    try:
        print("\nWatering START --------------<")
        for plant in plant_list:
            tmp = plant.get("plant")
            print("Watering", tmp.get_name())
    except Exception as e:
        print(f"Error catched: {e}")
    finally:
        print("Watering END (cleaning)------<")


def test_watering_system() -> None:
    """ test the finnaly key word """

    print("--Garden Watering System--")
    try:
        garden = Garden("tomato", 0)
        garden.add("letuce", 1)
        water_plants(garden.garden)
    except Exception as e:
        print(f"Error catched: {e}")
    finally:
        try:
            broken_garden = Garden("corn", 0)
            broken_garden.add("parsnip", 1)
            broken_garden.add("glitched_plant", 1)
            broken_garden.find("glitched_plant").broke_the_plant()
            water_plants(broken_garden.garden)
        except Exception as e:
            print(f"Error catched: {e}")
        finally:
            print("function ending properly")


if __name__ == "__main__":
    test_watering_system()
