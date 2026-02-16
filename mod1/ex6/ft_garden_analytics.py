
class Plant:
    """Basic Plant class, store informations about a plant in your garden.
    Usefull methods are available for data management"""

    __time = 0

    def __init__(self, name: str, height: int, days: int) -> None:
        """init of the class with parameters (int same order)\
        : name:str, height:int, age:int"""

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
        self.__initial = height
        self.__days = days
        self.__olde = days
        self.__entry = self.__class__.__time * -1
        print(end="(Created) ")
        self.say()

    def grow_for_time(self) -> None:
        """ change the the height of a plant \
        depending of the time passed from the start """

        temp = self.__height
        if self.__entry + self.__class__.__time != 0:
            self.__height = (int(self.__initial +
                             ((self.__entry + self.__class__.__time) / 4)))
        if temp != self.__height:
            print(
                "\\/ this plant grow",
                self.__height - temp, "cm from your last passage"
            )

    def say(self) -> None:
        """display all basics informations of the plant (name, height, age)"""
        self.grow_for_time()
        self.__days = self.__olde + self.__entry + self.__class__.__time
        print(
            self.__name, ": ", self.__height, "cm, ",
            self.__days, " days old", sep=""
        )

    @classmethod
    def age(cls, time: int) -> None:
        """the time elapses according to the chosen value (in days)"""
        if time < 1:
            return
        cls.__time += time

    def get_age(self) -> int:
        """return the age value of the object"""
        return self.__days

    def get_height(self) -> int:
        """return the height value of the object"""
        return self.__height

    def set_height(self, value: int) -> None:
        """change the height value of the object, with security filter"""
        if value >= 0:
            if ((self.__height - value) > 10) and (self.__height > value):
                print(end="your input is far larger than the stored value")
                if input("enter (y) if you sur to applie :") != "y":
                    return
            if ((value - self.__height) > 10) and (self.__height < value):
                print(end="your input is far larger than the stored value")
                if input("enter (y) if you sur to applie :") != "y":
                    return
            self.__height = value
        else:
            print("incorrect value, not applied")

    def set_age(self, value: int) -> None:
        """change the age value of the object, with security filter"""
        if value >= 0:
            if ((self.__days - value) > 10) and (self.__days > value):
                print(end="your input is far larger than the stored value")
                if input("enter (y) if you sur to applie :") != "y":
                    return
            if ((value - self.__days) > 10) and (self.__days < value):
                print(end="your input is far larger than the stored value")
                if input("enter (y) if you sur to applie :") != "y":
                    return
            self.__days = value
        else:
            print("incorrect value, not applied")


class FloweringPlant(Plant):
    """child of the plant class, with flower stuff"""

    def __init__(
        self, name: str, height: int, days: int, stade: str = "Notbloomed"
    ) -> None:
        """init of the flower with parent like functioning"""
        self.__stade = stade
        super().__init__(name, height, days)

    def bloom(self) -> None:
        """bloom the flower whose the function is applied"""
        print("The flower you took care is now blooming...")
        print("Waw, what a beautiful flower it is now")
        self.__stade = "Bloomed"

    def say(self) -> None:
        """print the class bases and specificitys infos"""
        super().say()
        print("|", self.__stade)


class PrizeFlower(FloweringPlant):
    """child of the FloweringPlant class, with more flower stuff"""
    def __init__(
        self, name: str, height: int, days: int,
        prize: int = 0, stade: str = "Bloomed"
    ) -> None:
        """init of the prized flower with parent like functioning"""
        self.prize = prize
        super().__init__(name, height, days, stade)

    def say(self) -> None:
        """print the class bases and specificitys infos"""
        super().say()
        print("| prize points: ", self.prize)


def take_input(says: str, error: int) -> int:
    """take the input with security filter"""
    value = input(says)
    if value.isdigit():
        value = int(value)
        if value >= error:
            return value
    print("invalid number set to", error)
    value = int(error)
    return value


def plant_factory() -> Plant:
    """factory program to make large number of plant object
    using a while and take inputs"""

    total = take_input("How much plant do you want to create ? :", 1)
    plant_deposit = []
    i = 0
    print("Creation process start.")
    while i < total:
        print("plant", i + 1)
        name = str(input("name: "))
        height = take_input("height: ", 0)
        age = take_input("age: ", 0)

        print("types: (plant/blooming/bloomed/prized)")
        variant = str(input("enter type: "))
        if variant == "bloomed":
            plant_deposit.append(FloweringPlant(name, height, age, "Bloomed"))
        elif variant == "blooming":
            plant_deposit.append(FloweringPlant(name, height, age))
        elif variant == "prized":
            prize = take_input("prize points: ", 0)
            plant_deposit.append(PrizeFlower(name, height, age, prize))
        else:
            if variant != "plant":
                print("unknow type set as plant")
                plant_deposit.append(Plant(name, height, age))

        i += 1
    print("Creation process end.")
    return plant_deposit


def help_case() -> None:
    """ list all possibles commands """

    print("ALL POSSIBLE COMMANDS :\n")
    print("q / quit == quit th program")
    print(
        "create == create a garden with the factory\
 AND erase all data already exist")
    print("see == see all gardens repertoried with their index")
    print("see-garden == choose a garden and see all plants inside")
    print("tot-gardens == see number of registered gardens")
    print("tot-plants == see number of registered plants in a chosen garden")
    print("tot-all-plants == see total of registered plants")
    print("stats == see all gardens stats")
    print("elapse == pass the time of the chosen value in days")


def see_plants(data: list[Plant]) -> None:
    """ see all plants details inside a garden \
    (element of the gardens list) """

    i = -1
    if data:
        i = 0
        for Plant in data:
            data[i].say()
            i += 1
    else:
        print("this garden do not exist")


def see_garden(data: list[str]) -> None:
    """ see all gardens name with their index """
    i = 0
    if data:
        for str in data:
            print(data[i], "[", i + 1, "]")
            i += 1
    elif i == 0:
        print("no garden registered")


def safe_name(name: str) -> str:
    """ simple check of no str for garden name """
    if name == "":
        print("invalid name set to Garden")
        return "Garden"
    return name


def str_len(data: list[str]) -> int:
    """ return the size of the gardens name list """
    i = -1
    if data:
        i = 0
        for str in data:
            i += 1
    return i


def plant_len(data: list[Plant]) -> int:
    """ return the number of plants of a garden \
    (element of the gardens list) """
    i = 0
    if data:
        for Plant in data:
            i += 1
    return i


class GardenManager:
    """ create / manage / and see stats of garden(s) and plant(s) """

    gardens = []
    name_index = []

    class GardenStats:
        """ class with all stats utilities methods """

        @staticmethod
        def tot() -> None:
            """ show the total of gardens registered """
            tot = str_len(GardenManager.name_index)
            if tot > 0:
                print(tot)
            else:
                print("no garden registered")

        @staticmethod
        def tot_plants(index: int) -> None:
            """ show the total of plants registered in a chosen garden"""
            tot = plant_len(GardenManager.gardens[index])
            print(tot)

        @staticmethod
        def tot_all_plants() -> None:
            """ show the total of plants registered """
            i = 0
            tot = 0
            for Plant in GardenManager.gardens:
                tot += plant_len(GardenManager.gardens[i])
                i += 1
            print("total number of plants registered :", tot)

        @staticmethod
        def see() -> None:
            """ show all stats of all gardens """
            print("")
            total = str_len(GardenManager.name_index)
            if total < 0:
                total = 0
            print("gardens registered:", total)
            print("")
            i = 0
            while i < total:
                print("Garden name :", GardenManager.name_index[i])
                print("Plants possess: ", plant_len(GardenManager.gardens[i]))
                see_plants(GardenManager.gardens[i])
                i += 1
                print("")

    @classmethod
    def create_garden_network(cls) -> None:
        """ take inputs to manage the garden net_work """
        print("Welcome to Garden Analytic 1.0 - abenabde")
        print("enter (help) or (h) if you dont now what doing")
        while 1:
            todo = str(input())
            if todo == "q" or todo == "quit":
                return
            elif todo == "h" or todo == "help":
                help_case()
            elif todo == "create":
                cls.name_index.append(
                 safe_name(input("Choose a garden name: ")))
                cls.gardens.append(plant_factory())
            elif todo == "see":
                see_garden(cls.name_index)
            elif todo == "see-garden":
                tmp: int = int(take_input("garden index: ", -1)) - 1
                if tmp < str_len(cls.gardens) and tmp >= 0:
                    see_plants(cls.gardens[tmp])
                else:
                    print("invalid garden")
            elif todo == "stats":
                GardenManager.GardenStats.see()
            elif todo == "elapse":
                tmp = take_input("days to pass: ", 1)
                Plant.age(tmp)
            elif todo == "tot-gardens":
                GardenManager.GardenStats.tot()
            elif todo == "tot-plants":
                tmp: int = int(take_input("garden index: ", -1)) - 1
                if tmp < str_len(cls.gardens) and tmp >= 0:
                    GardenManager.GardenStats.tot_plants(tmp)
                else:
                    print("invalid garden")
            elif todo == "tot-all-plants":
                GardenManager.GardenStats.tot_all_plants()
            else:
                print("unknow command")


if __name__ == "__main__":
    GardenManager.create_garden_network()
