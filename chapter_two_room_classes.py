import os
import platform


# allows me to clear the screen when playing
def clear():
    operating = platform.system()
    if operating == 'Linux' or operating == "Darwin":
        os.system("clear")
    elif operating == 'Windows':
        os.system('cls')


class ShopFunctions:
    """A class for giving shops the needed functions."""
    # class variables for print formatting
    bold = '''\033[1m'''
    end = '''\033[0;0m'''

    # general shop keeper function
    def shop_keeper(self):
        talking = True
        print("Welcome to my shop!")
        while talking:
            print("\nSell(s), Buy(b), or Quit(q)?")
            choice = input("").lower()
            clear()
            if choice == "s":
                self.sell_items()
            elif choice == "b":
                self.buy_items()
            elif choice == "q":
                print("Please come again.")
                talking = False
            else:
                print(f"What do you mean by {choice}.")

    # allows you to sell things
    def sell_items(self):
        talking = True
        while talking:
            if len(self.player_object.inventory) > 1:
                items_sell = []
                for item in self.player_object.inventory:
                    if item in self.player_object.sell_item_values:
                        items_sell.append(item)
                # if list is not empty allow selling
                if items_sell:
                    for number, item in enumerate(items_sell):
                        print(item, end=", ")
                        if (number + 1) % 4 == 0:
                            print("")
                    print("\n")
                    choice = input("\nSell what? q to quit. ").lower()
                    clear()
                    # if you do not have the thing you are trying to sell
                    if choice not in self.player_object.inventory and choice != "q":
                        print(f"You don't have a(n) {self.bold + choice + self.end} to sell")
                    # if the item has a value in game
                    elif choice in self.player_object.sell_item_values:
                        print("I'll take that. Thank you!")
                        # sells it
                        self.sell(choice)
                    elif choice == "q":
                        talking = False
                    else:
                        print(f"I don't want to buy a(n) {self.bold + choice + self.end}")
                else:
                    print("You don't have anything I want to buy.")
                    talking = False

            else:
                print("You don't have anything to sell.")
                talking = False

    # allows you to buy things
    def buy_items(self):
        talking = True
        while talking:
            if len(self.shop_inventory) > 0:
                for number, item in enumerate(self.shop_inventory):
                    print(item, end=", ")
                    if (number + 1) % 4 == 0:
                        print("")
                print("\n")
                choice = input("\nBuy what? q to quit. ").lower()
                clear()
                # if they have it to sell you
                if choice in self.shop_inventory:
                    # if you have enough money
                    if self.player_object.player_wallet >= self.player_object.buy_item_values.get(choice):
                        self.buy(choice)
                    else:
                        # if you are too poor
                        print(f"You can't afford the {self.bold + choice + self.end}. You need {self.player_object.buy_item_values.get(choice) - self.player_object.player_wallet}.")
                elif choice == "q":
                    talking = False
                else:
                    print(f"I don't have a(n) {self.bold + choice + self.end} to sell you.")
            else:
                print("I am totally out of things to sell you.")
                talking = False

    # controls selling items
    def sell(self, item):
        self.player_object.inventory.remove(item)
        if item in self.player_object.buy_item_values:
            self.shop_inventory.append(item)
        print(f"You sold the {self.bold + item + self.end}.")
        self.player_object.change_player_wallet(self.player_object.sell_item_values.get(item, 0))

    # controls buying items
    def buy(self, item):
        self.player_object.inventory.append(item)
        self.shop_inventory.remove(item)
        print(f"You bought the {self.bold + item + self.end}.")
        self.player_object.change_player_wallet(self.player_object.buy_item_values.get(item, 0))


# function class for inheritance.
class FunctionClass:
    """Never to be called. Only used for giving all other classes the same methods."""

    # class variables for print formatting
    bold = '''\033[1m'''
    end = '''\033[0;0m'''

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
                print(f"I can't look at the {look_at}.")

        else:
            print(f"I can't look at the {look_at}.")

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
                print(f"I can't operate the {operate}.")
        else:
            print(f"I can't operate the {operate}.")

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
                print(f"I can't go to {go}.")
        else:
            print(f"I can't go to {go}.")

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
                print(f"I can't find the {room_object}.")
        else:
            print(f"What is a(n) {room_object}.")

    # gives item to player
    def get_item(self, item):
        if item in self.inventory:
            print(f"I got the {self.bold + item + self.end}.")
            self.inventory.remove(item)
            self.player_object.inventory.append(item)
        else:
            print(f"There isn't a(n) {item} to get.")

    # dropping item back into room
    def drop_item(self, item):
        if item in self.player_object.inventory and item != "map":
            print(f"I dropped the {self.bold + item + self.end}.")
            self.inventory.append(item)
            self.player_object.inventory.remove(item)
        elif item in self.player_object.inventory and item != "map":
            print("I might need it, I'm not going to drop it.")
        else:
            print(f"I don't have a(n) {item} to drop.")

    # prints items and bolds them for effect.
    def print_items(self):
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) ", end="")
                print(self.bold, item, self.end)

    def print_look(self):
        if len(self.look_dict) > 0:
            print("I could look at...")
            print(f"There is a(n) ", end="")
            for location in self.look_dict:
                print(f"'{location}', ", end="")
            print("\n_________________________________________________")

    def print_locations(self):
        print("I could go to...")
        print(f"There is a(n) ", end="")
        for location in self.go_dict:
            print(f"'{location}', ", end="")
        print("\n______________________________________________________")


# town center rooms
class TownCenter(FunctionClass):
    """Starting room and center of town."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        # optional/only for shops
        # self.shop_inventory = []
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


class TownBar(FunctionClass, ShopFunctions):
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


class TownGenStore(FunctionClass, ShopFunctions):
    """town general store that acts as a shop and a puzzle hub."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        # things you can look at.
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
    """town gate house that allows or denies entry to mansion."""
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
    """town gate house that allows or denies entry to mansion."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.go_objects = ("town center", "ruined house", "ruined garage", "ruined office")
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


class RuinedGarage(FunctionClass):
    """town gate house that allows or denies entry to mansion."""
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
        print("A ruined garage.")
        print("__________________")
        self.print_look()
        self.print_locations()
        self.print_items()

    def go_ruined_street(self):
        self.player.location = "ruined street"


class RuinedOffice(FunctionClass):
    """town gate house that allows or denies entry to mansion."""
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


# mansion rooms
class MansionFoyer(FunctionClass):
    """Starting room and center of town."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"town center": self.go_town_center,
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

    def go_town_center(self):
        self.player.location = "town center"

    def go_mansion_kitchen(self):
        self.player.location = "kitchen"

    def go_mansion_hallway(self):
        self.player.location = "hallway"

    def go_mansion_sun_room(self):
        self.player.location = "sun room"


class MansionSunRoom(FunctionClass):
    """Starting room and center of town."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"foyer": self.go_mansion_foyer}
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


class MansionKitchen(FunctionClass):
    """Starting room and center of town."""
    def __init__(self, player_object):

        self.inventory = []
        self.player = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.look_dict = {"room": self.print_description_room}
        self.go_dict = {"foyer": self.go_mansion_foyer}
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


class MansionHallWay(FunctionClass):
    """Starting room and center of town."""
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
    """Starting room and center of town."""
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
