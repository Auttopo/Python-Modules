
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


class SunError(GardenError):
    """ sun class error for exceptions catch """

    def __init__(self, say: str = "Error occured") -> None:
        """ minimal init for error message """
        self.__say = say

    def __str__(self) -> str:
        """ return error message for the catch """
        return "SunError, " + self.__say


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

    def change_sun(self, sun: int) -> None:
        """ change the water value or catch an error """
        if sun < 0:
            raise SunError("Negative sun hours value, can't be set")
        self.__sun_hours = sun
        return None

    def set_name(self, name: str) -> None:
        """ change the name """
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


class GardenManager:
    """ basic Garden class """

    def __init__(self, name: str, water: int, sun: int) -> None:
        """ create the garden with a first plant """
        self.garden = []
        self.add(name, water, sun)

    def add(self, name: str, water: int, sun: int) -> None:
        """ add a plant to the garden """
        try:
            self.garden.append(
                            {"name": name, "plant": Plant(name, water, sun)})
        except GardenError as e:
            print(f"Error in add(): {e}")
            return
        print(name, "created")

    def find(self, target: str, nbr: int = 0) -> Plant:
        """return the n element with the chosen name and optional value"""

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

    @staticmethod
    def check_plant_health(plant: Plant) -> None:
        """ check the plant health , raise error if occured """

        if plant.get_name() is None:
            raise PlantError("none name")
        if plant.get_name() == "":
            raise PlantError("no name setted")
        if plant.get_water() < 1:
            raise WaterError(
                    str(plant.get_name()) + ", water lever < 1. current "
                    + str(plant.get_water()))
        if plant.get_water() > 10:
            raise WaterError(
                    str(plant.get_name()) + ", water lever > 10. current: "
                    + str(plant.get_water()))
        if plant.get_sun() < 2:
            raise PlantError(
                    str(plant.get_name()) + " sunlight, time < 2. current: "
                    + str(plant.get_sun()))
        if plant.get_sun() > 10:
            raise PlantError(
                    str(plant.get_name()) + " sunlight, time > 12. current: "
                    + str(plant.get_sun()))

    def check_all_health(self) -> None:
        """ check all plants health """

        print("\nHEALTH CHECKUP START -------------<")
        try:
            for plant in self.garden:
                try:
                    GardenManager.check_plant_health(plant.get("plant"))
                    print("All", plant.get("plant").get_name(), "datas are OK")
                except GardenError as e:
                    print(f"Error inside check_all_health(): {e}")
        except Exception as e:
            print(f"Error in check_all_health(): {e}")
        finally:
            print("HEALTH CHECKUP END ---------------<")

    def water_plants(self) -> None:
        """ water all plants """
        try:
            print("\nWatering START -------------<")
            for plant in self.garden:
                tmp = plant.get("plant")
                print("Watering", tmp.get_name(), ", gain +1 water stat")
                tmp.change_water(tmp.get_water() + 1)
        except GardenError as e:
            print(f"Error in water_plants() : {e}")
        finally:
            print("Watering END (cleaning) ----<")


def test_garden_management() -> None:
    """ test error in the garden manager """

    manager = GardenManager("tomato", 1, 2)
    manager.add("corn", 0, 4)
    manager.add("", 4, 4)
    manager.add("apple_tree", 6, 0)

    manager.check_all_health()
    manager.water_plants()
    manager.check_all_health()

    try:
        manager.find("apple_tree").change_sun(-5)
    except SunError as e:
        print(f"\nError when change_sun tried|: {e}")
    finally:
        try:
            manager.find("apple_tree").change_sun(5)
        finally:
            manager.check_all_health()

    print("\nthe function still runing")


if __name__ == "__main__":
    test_garden_management()
    print("the program still runing")
