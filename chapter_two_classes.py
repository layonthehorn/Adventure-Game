import time


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
                print(f"I can't look at {look_at}.")

        else:
            print(f"I can't go to {look_at}.")

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

    # general shop keeper function
    def shop_keeper(self):
        talking = True
        print("Welcome to my shop!")
        while talking:
            print("Sell(s), Buy(b), or Quit(q)?")
            choice = input("").lower()
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
                    choice = input("Sell what? q to quit. ").lower()
                    # if you do not have the thing you are trying to sell
                    if choice not in self.player_object.inventory and choice != "q":
                        print(f"You don't have a(n) {choice} to sell")
                    # if the item has a value in game
                    elif choice in self.player_object.sell_item_values:
                        print("I'll take that. Thank you!")
                        # sells it
                        self.sell(choice)
                    elif choice == "q":
                        talking = False
                    else:
                        print(f"I don't want to buy a(n) {choice}")
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
                choice = input("Buy what? q to quit. ").lower()
                # if they have it to sell you
                if choice in self.shop_inventory:
                    # if you have enough money
                    if self.player_object.player_wallet >= self.player_object.buy_item_values.get(choice):
                        self.buy(choice)
                    else:
                        # if you are too poor
                        print(f"You can't afford the {choice}. You need {self.player_object.buy_item_values.get(choice) - self.player_object.player_wallet}.")
                elif choice == "q":
                    talking = False
                else:
                    print(f"I don't have a(n) {choice} to sell you.")
            else:
                print("I am totally out of things to sell you.")
                talking = False

    # controls selling items
    def sell(self, item):
        self.player_object.inventory.remove(item)
        if item in self.player_object.buy_item_values:
            self.shop_inventory.append(item)
        print(f"You sold the {item}.")
        self.player_object.change_player_wallet(self.player_object.sell_item_values.get(item, 0))

    # controls buying items
    def buy(self, item):
        self.player_object.inventory.append(item)
        self.shop_inventory.remove(item)
        print(f"You bought the {item}.")
        self.player_object.change_player_wallet(self.player_object.buy_item_values.get(item, 0))

    # prints items and bolds them for effect.
    def print_items(self):
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) ", end="")
                print(self.bold, item, self.end)


# Player Class
class PlayerClass:
    """This is the main player class. It holds the player inventory and score among other things."""

    # class variables for print formatting
    bold = '''\033[1m'''
    end = '''\033[0;0m'''

    def __init__(self):

        self.inventory = ["self"]
        self.started = True
        # neg
        self.buy_item_values = {"fish": -5,
                                "can": -3}
        # pos
        self.sell_item_values = {"fish": 4,
                                 "can": 2,
                                 "rock": 1}
        self.__location = "bunker"
        self.__player_score = 0
        self.player_wallet = 0
        #
        # mp, up, pet, shoe, rest, ani, den, west, toy, cem, fall, com = (
        #     "MP", "UH", 'PS', 'SS', 'RR', 'AD', 'SD', 'WW', 'TS', 'C ', 'FS', 'CR')
        self.places = []
        self.map_dictionary = {
            "plaza": "MP",
            "bunker": "FS",
            "side room": "CR",
            "small den": "SD",
            "west wing": "WW",
            "cemetery": "C ",
            "toy shop": "TS",
            "pet shop": "PS",
            "upstairs hallway": "UH",
            "animal den": "AD",
            "shoe store": "SS",
            "bathroom": "RR",
        }

        self.item_dictionary = {
            "temp": "Temporary item...",

        }

    def __str__(self):
        return f"""Inventory {self.inventory}\nLocation {self.__location}\nScore {self.__player_score}"""

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        if location not in ():
            print("Could not find matching location. Moving to None.")
            print(f"Could not fine {location}... Possible missing spelling in code?")
            location = None
        else:
            print(f"You have gone to the {location}.")
        self.__location = location

    def change_player_wallet(self, new_value):
        if new_value < 0:
            print(f"You lost {abs(new_value)} coins.")
        elif new_value > 0:
            print(f"You got {new_value} coins!")
        else:
            print("Error somehow got 0 dollars.")
        self.player_wallet += new_value
        print(f"You have {self.player_wallet} coins total now.")

    @property
    def player_score(self):
        return self.__player_score

    @player_score.setter
    def player_score(self, new_value):
        if new_value < 1:
            new_value = 1
            print("You're score went up!")
            self.__player_score += new_value
        else:
            print("You're score went up!")
            self.__player_score = new_value

    # prints your score
    def print_score(self):
        print(f"Your score is {self.player_score}.")

    # prints his inventory
    def check_inventory(self):
        # if self is some how removed it will be added back.
        # just in case.
        if "self" not in self.inventory:
            self.inventory.append("self")
        if len(self.inventory) == 1:
            print("My pockets are empty it seems.")
        else:
            print("I have...")
            for item in self.inventory:
                # should not be shown to player as being an item.
                if item != "self":
                    print(f"{self.bold + item + self.end:<20}{self.item_dictionary.get(item, 'Error, Report me pls!'):<5}")

    def drop_item(self, item):
        # prevents dropping the map.
        if item in self.inventory and item == "map":
            print("I might need it, I'm not going to drop it.")
        # otherwise if the item is in your inventory allows you to drop it
        elif item in self.inventory:
            location = self.inventory.index(item)
            print("I dropped the ", item)
            return self.inventory.pop(location)

    # removes items from player
    def use_item(self, item):
        # never removes self from inventory.
        if item != "self":
            print("I used the ", item)
            self.inventory.remove(item)
        else:
            print("I used myself?")

    # combines items
    def combine_items(self, item_1, item_2):
        # debugging line to check the items being used.
        # print(item_1, " ", item_2)
        if item_1 in self.inventory and item_2 in self.inventory:
            # a list to make checking for contents easier
            item_list = (item_1, item_2)

            # item crafting results
            if "" in item_list and "" in item_list:
                self.inventory.remove(item_1)
                self.inventory.remove(item_2)
                self.inventory.append("")
                print("Replace me!")
                return True
            # no matches found
            else:
                print(f"I can't combine {item_1} and {item_2}.")
                return False

        # No matching items found
        else:
            print("I don't have all I need.")
            return False

    # looking at map
    def look_player_map(self):
        if "map" in self.inventory:
            print("Let me check my map.\n*Map crinkling sounds.*")
            time.sleep(1.5)
            rooms = []
            p_local = "??"
            for room in self.places:
                if self.map_dictionary.get(self.location,"") == room:

                    # if the player is on the map it changes that room to the player symbol
                    rooms.append("@@")
                    # then puts the room symbol in the legend
                    p_local = room
                else:
                    # other wise just puts rooms there normally
                    rooms.append(room)
            print("Map not made yet.")
            # print(f"""
            #   ---------MAP----------
            #                                        +--------------------+
            #            {rooms[3]}                          |Legend:             |
            #            ||                          |                    |
            #        {rooms[5]}--{rooms[1]}--{rooms[4]}                      |Main Plaza: MP      |
            #     {rooms[9]}  {rooms[6]} ||                          |Upper Hall: UH      |
            #     ||   \\\\||                          |Pet Shop: PS        |
            # {rooms[2]}--{rooms[7]}-----{rooms[0]}----EXIT                  |Shoe Store: SS      |
            #     ||     ||                          |Restroom: RR        |
            #     {rooms[8]}     {rooms[10]}--{rooms[11]}                      |Animal Den: AD      |
            #                                        |Small Den: SD       |
            #                                        |West wing: WW       |
            #                                        |Toy Shop: TS        |
            #                                        |Cemetery: C         |
            #                                        |Fallout Shelter: FS |
            #                                        |Computer Room: CR   |
            #                                        |You: @@ in room {p_local}  |
            #                                        +--------------------+
            #        """)
        else:
            print("I don't have one.")

    # looking at self
    def look_self(self):
        print("A nervous lion is what you are. Somehow still alive but for how long? Hopefully long enough.")


class ExampleRoom(FunctionClass):
    """Example class."""
    def __init__(self, player_object):

        self.inventory = ["temp"]
        self.player_object = player_object
        self.bool_one, self.bool_two, self.bool_three = (False, False, False)
        self.shop_inventory = []
        self.look_dict = {}
        self.go_dict = {}
        self.oper_dict = {}
        self.use_dict = {}

    # this prints a description along with a item list
    def print_description_room(self):
        print("It's an example room. use temp with box.")
        print("go outside should work too but only print something."
              "")
        self.print_items()

    def print_description_box(self):
        print("its a box")

    def print_description_door(self):
        print("it's a door")

    def operate_door(self):
        if not self.bool_one:
            self.bool_one = True
            self.player_object.increase_score()
            print("switched to new value door")
        else:
            print("stays the same door")

    def operate_fuse_box(self):
        if not self.bool_two:
            self.bool_two = True
            self.player_object.increase_score()
            print("switched to new value box")
        else:
            print("stays the same box")

    def testing_using_items(self, item):
        if not self.bool_one:
            if item == "temp":
                print("Worked with temp item")
                self.bool_one = False
                self.player_object.use_item(item)
                self.player_object.increase_score()

            else:
                print("Wrong item")
        else:
            print("Already used.")

    def go_outside(self):
        self.player_object.location = "Place"

    def go_sideroom(self):
        self.player_object.location = "home"


if __name__ == "__main__":
    # for testing shops
    player = PlayerClass()
    room = ExampleRoom(player)
    # room.shop_inventory.append("")
    player.inventory.append("rock")
    player.inventory.append("stone")
    player.inventory.append("fish")
    room.shop_keeper()
