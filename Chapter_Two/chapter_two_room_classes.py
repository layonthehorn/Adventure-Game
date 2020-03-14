import os
import random
import platform


# allows me to clear the screen when playing
def clear():
    operating = platform.system()
    if operating == 'Linux' or operating == "Darwin":
        os.system("clear")
    elif operating == 'Windows':
        os.system('cls')


# function class for inheritance
class FunctionClass:
    """Never to be called. Only used for giving all other classes the same methods."""

    # class variables for print formatting
    bold = '''\033[1m'''
    end = '''\033[0;0m'''
    look_at_remarks = ("I can't look at the {0}.", "What {0}?")
    oper_remarks = ("I can't operate the {0}.", "How would I operate the {0}?")
    go_to_remarks = ("I can't go to {0}.", "Where is {0}?")
    use_remarks = ("What is a(n) {0}.", "I can't do anything to the {0}")
    get_remarks = ("There isn't a(n) {0} to get.", "I can't find a(n) {0} to pick up.")
    drop_remarks = ("I don't have a(n) {0} to drop.", "I would need to have a(n) {0} to drop it.")

    # allows getting a print function form the look dictionary.
    def get_look_commands(self, look_at):
        # you have to enter at least three letters
        if len(look_at) >= 3:
            for key in self.look_dict:
                if look_at in key:
                    look_command = self.look_dict.get(key)
                    look_command()
                    break
            else:
                self.print_random_phrase(self.look_at_remarks, look_at)

        else:
            self.print_random_phrase(self.look_at_remarks, look_at)

    # allows getting operate commands
    def get_oper_commands(self, operate):
        # you have to enter at least three letters
        if len(operate) >= 3:
            for key in self.oper_dict:
                if operate in key:
                    oper_command = self.oper_dict.get(key)
                    oper_command()
                    break
            else:
                self.print_random_phrase(self.oper_remarks, operate)
        else:
            self.print_random_phrase(self.oper_remarks, operate)

    # allows getting go commands
    def get_go_commands(self, go):
        # you have to enter at least three letters
        if len(go) >= 2:
            for key in self.go_dict:
                if go in key:
                    go_command = self.go_dict.get(key)
                    go_command()
                    break
            else:
                self.print_random_phrase(self.go_to_remarks, go)
        else:
            self.print_random_phrase(self.go_to_remarks, go)

    # allows using item on objects
    def get_use_commands(self, use_list):
        item = use_list[0]
        room_object = use_list[1]
        # you have to enter at least three letters
        if len(room_object) >= 3:
            for key in self.use_dict:
                if room_object in key:
                    use_command = self.use_dict.get(key)
                    use_command(item)
                    break
            else:
                self.print_random_phrase(self.use_remarks, room_object)
        else:
            self.print_random_phrase(self.use_remarks, room_object)

    # gives item to player
    def get_item(self, item):
        if item in self.inventory:
            print(f"I got the {self.bold + item + self.end}.")
            self.inventory.remove(item)
            self.player_object.inventory.append(item)
        else:
            self.print_random_phrase(self.get_remarks, item)

    # dropping item back into room
    def drop_item(self, item):
        if item in self.player_object.inventory and item != "map":
            print(f"I dropped the {self.bold + item + self.end}.")
            self.inventory.append(item)
            self.player_object.inventory.remove(item)
        else:
            self.print_random_phrase(self.drop_remarks, item)

    # prints items and bolds them for effect.
    def print_items(self):
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) ", end="")
                print(self.bold, item, self.end)

    # prints what you can look at
    def print_look(self):
        look_list = ""
        print("I could look at...")
        for thing in self.look_dict:
            look_list += f"'{self.bold+ thing+ self.end}', "
        print(look_list)
        print("_" * len(look_list))

    # prints where you can go
    def print_locations(self):
        go_list = ""
        print("I could go to...")
        for location in self.go_dict:
            go_list += f"'{self.bold+ location+ self.end}', "
        print(go_list)
        print("_" * len(go_list))

    @staticmethod
    def print_random_phrase(selection_list, item):
        rand_phrase = random.choice(selection_list)
        print(rand_phrase.format(item))


# town center rooms
class TownCenter(FunctionClass):
    """Starting room and center of town."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"bar": self.go_bar,
                        "general store": self.go_gen_store,
                        "gate house": self.go_gate_house,
                        "bath house": self.go_bath_house,
                        "ruined street": self.go_ruined_street}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("The starting room.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_bar(self):
        self.player.location = "bar"

    def go_gen_store(self):
        self.player.location = "general store"

    def go_gate_house(self):
        self.player.location = "gate house"

    def go_bath_house(self):
        self.player.location = "bath house"

    def go_ruined_street(self):
        self.player.location = "ruined street"


class TownBar(FunctionClass):
    """Bar that acts as a shop and a meeting place."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.shop_inventory = []
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"town center": self.go_town_center}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("The town center bar.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_town_center(self):
        self.player.location = "town center"


class TownGenStore(FunctionClass):
    """town general store that acts as a shop and a puzzle hub."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.shop_inventory = []
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"town center": self.go_town_center}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("The town center general store.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def print_description_shop(self):
        print("It's a nice General store.", end=" ")
        if len(self.shop_inventory) > 0:
            print("Looks like there are things to buy.")
        else:
            print("He's all sold out of things I'd want.")

    def go_town_center(self):
        self.player.location = "town center"


class TownBathHouse(FunctionClass):
    """town bath house that acts as a small puzzle for getting cleaned up."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)

        self.shop_inventory = []
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"town center": self.go_town_center}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("The town center bath house.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_town_center(self):
        self.player.location = "town center"


class TownGateHouse(FunctionClass):
    """town gate house that allows or denies entry to mansion."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)

        self.shop_inventory = []
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"town center": self.go_town_center,
                        "mansion": self.go_mansion_foyer}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("The town center gate house.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_town_center(self):
        self.player.location = "town center"

    def go_mansion_foyer(self):
        self.player.location = "foyer"


# Ruined City rooms
class RuinedHouse(FunctionClass):
    """A ruined house in the city."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)

        self.shop_inventory = []
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"ruined street": self.go_ruined_street}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("A ruined city house")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_ruined_street(self):
        self.player.location = "ruined street"


class RuinedStreet(FunctionClass):
    """The main street of the ruined city."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)

        self.shop_inventory = []
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"town center": self.go_town_center,
                        "ruined house": self.go_ruined_house,
                        "ruined garage": self.go_ruined_garage,
                        "ruined office": self.go_ruined_office}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("A ruined city street.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_town_center(self):
        self.player.location = "town center"

    def go_ruined_house(self):
        self.player.location = "ruined house"

    def go_ruined_garage(self):
        self.player.location = "ruined garage"

    def go_ruined_office(self):
        self.player.location = "ruined office"


class RuinedOffice(FunctionClass):
    """A ruined office building in the city."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)

        self.shop_inventory = []
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"ruined street": self.go_ruined_street}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("A ruined city offce.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_ruined_street(self):
        self.player.location = "ruined street"


class RuinedGarage(FunctionClass):
    """An old garage in the ruined city."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)

        self.shop_inventory = []
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"ruined street": self.go_ruined_street,
                        "upstairs": self.go_upstairs_break_room}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("A ruined garage.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_ruined_street(self):
        self.player.location = "ruined street"

    def go_upstairs_break_room(self):
        self.player.location = "break room"


# Garage Upstairs
class UpstairsBreakRoom(FunctionClass):
    """An upstairs break room in the garage."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)

        self.shop_inventory = []
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"ruined garage": self.go_ruined_garage,
                        "office": self.go_upstairs_office,
                        "balcony": self.go_upstairs_balcony}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("An upstairs break room attached to the garage.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_ruined_garage(self):
        self.player.location = "ruined garage"

    def go_upstairs_office(self):
        self.player.location = "managers office"

    def go_upstairs_balcony(self):
        self.player.location = "balcony"


class UpstairsBalcony(FunctionClass):
    """An upstairs balcony that overlooks the city street."""

    def __init__(self, player_object):
        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)

        self.shop_inventory = []
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"break room": self.go_upstairs_break_room,
                        "office": self.go_upstairs_office}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("An upstairs balcony overlooking the ruined street.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_upstairs_break_room(self):
        self.player.location = "break room"

    def go_upstairs_office(self):
        self.player.location = "managers office"


class UpstairsOffice(FunctionClass):
    """An upstairs office in the garage."""

    def __init__(self, player_object):
        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)

        self.shop_inventory = []
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"break room": self.go_upstairs_break_room,
                        "balcony": self.go_upstairs_balcony}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("An upstairs managers office attached to the garage.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_upstairs_break_room(self):
        self.player.location = "break room"

    def go_upstairs_balcony(self):
        self.player.location = "balcony"


# mansion rooms
class MansionFoyer(FunctionClass):
    """The entrance to the mansion."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"gate house": self.go_gate_house,
                        "kitchen": self.go_mansion_kitchen,
                        "hallway": self.go_mansion_hallway,
                        "sun room": self.go_mansion_sun_room}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("The mansion foyer.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_gate_house(self):
        self.player.location = "gate house"

    def go_mansion_kitchen(self):
        self.player.location = "kitchen"

    def go_mansion_hallway(self):
        self.player.location = "hallway"

    def go_mansion_sun_room(self):
        self.player.location = "sun room"


class MansionSunRoom(FunctionClass):
    """A warm sun room in the house."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"foyer": self.go_mansion_foyer,
                        "tower entrance": self.go_tower_entrance}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("The mansion sun room.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_mansion_foyer(self):
        self.player.location = "foyer"

    def go_tower_entrance(self):
        self.player.location = "tower entrance"


class MansionKitchen(FunctionClass):
    """A kitchen in the mansion."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"foyer": self.go_mansion_foyer,
                        "cellar": self.go_cellar_entrance}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("The mansion kitchen.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_mansion_foyer(self):
        self.player.location = "foyer"

    def go_cellar_entrance(self):
        self.player.location = "cellar entrance"


class MansionHallWay(FunctionClass):
    """A hallway in the mansion."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"foyer": self.go_mansion_foyer,
                        "living room": self.go_mansion_living_room}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("The mansion hallway.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_mansion_foyer(self):
        self.player.location = "foyer"

    def go_mansion_living_room(self):
        self.player.location = "living room"


class MansionLivingRoom(FunctionClass):
    """A living room in the mansion."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"hallway": self.go_mansion_hallway}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("The mansion foyer.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_mansion_hallway(self):
        self.player.location = "hallway"


# tower rooms
class TowerEntrance(FunctionClass):
    """The entrance to the mansion tower."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {
            "tower peak": self.go_tower_peak,
            "hallway": self.go_mansion_sun_room}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("The tower entrance.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_mansion_sun_room(self):
        self.player.location = "sun room"

    def go_tower_peak(self):
        self.player.location = "tower peak"


class TowerPeak(FunctionClass):
    """The top of the mansion tower."""

    def __init__(self, player_object):
        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"tower peak": self.go_tower_entrance}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("The tower entrance.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_tower_entrance(self):
        self.player.location = "tower entrance"


# cellar rooms
class CellarEntrance(FunctionClass):
    """Entrance to cellar of mansion."""

    def __init__(self, player_object):
        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"mansion": self.go_mansion_kitchen,
                        "wine casks": self.go_wine_casks,
                        "lab": self.go_lab}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("The cellar entrance.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_mansion_kitchen(self):
        self.player.location = "kitchen"

    def go_wine_casks(self):
        self.player.location = "wine casks"

    def go_lab(self):
        self.player.location = "lab"


class CellarWineCasks(FunctionClass):
    """Wine Casks in cellar of mansion."""

    def __init__(self, player_object):
        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"cellar entrance": self.go_cellar_entrance}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("The cellar wine casks.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_cellar_entrance(self):
        self.player.location = "cellar entrance"


class CellarLab(FunctionClass):
    """Secret lab in cellar of mansion."""

    def __init__(self, player_object):
        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"cellar entrance": self.go_cellar_entrance}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("The cellar secret lab.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_cellar_entrance(self):
        self.player.location = "cellar entrance"


# the general store's back rooms
class GeneralStorage(FunctionClass):
    def __init__(self, player_object):
        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"general store": self.go_general_store,
                        "work room": self.go_work_room,
                        "freezer": self.go_freezer}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("The General Store's storage.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_general_store(self):
        self.player.location = "general store"

    def go_work_room(self):
        self.player.location = "work room"

    def go_freezer(self):
        self.player.location = "freezer"


class WeaponsStorage(FunctionClass):
    def __init__(self, player_object):
        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"work room": self.go_work_room}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("The General Store's weapons storage.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_work_room(self):
        self.player.location = "work room"


class WorkRoom(FunctionClass):
    def __init__(self, player_object):
        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"weapon storage": self.go_weapon_storage,
                        "general storage": self.go_general_storage,
                        "freezer": self.go_freezer}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("The General Store's work room.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_weapon_storage(self):
        self.player.location = "weapons storage"

    def go_general_storage(self):
        self.player.location = "general storage"

    def go_freezer(self):
        self.player.location = "freezer"


class Freezer(FunctionClass):
    def __init__(self, player_object):
        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"general storage": self.go_general_storage,
                        "work room": self.go_work_room}
        self.oper_dict = {}
        self.use_dict = {}

    def print_description_room(self):
        print("The General Store's walk in freezer.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_general_storage(self):
        self.player.location = "general storage"

    def go_work_room(self):
        self.player.location = "work room"
