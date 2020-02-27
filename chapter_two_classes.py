from chapter_one_classes import FunctionClass
import time


# Player Class
class PlayerClass:
    """This is the main player class. It holds the player inventory and score among other things."""

    def __init__(self):

        self.inventory = ["self"]
        self.started = True
        self.location = "bunker"
        self.player_score = 0
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
        return f"""Inventory {self.inventory}\nLocation {self.location}\nScore {self.player_score}"""

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        # prevents printing the message when you start the game.
        if self.started:
            self.started = False
        elif location not in ():
            print("Could not find matching location. Moving to None.")
            location = None
        else:
            print(f"You have gone to the {location}.")
        self.__location = location

    # prints your score
    def print_score(self):
        print(f"Your score is {self.player_score}.")

    # sets player score
    def increase_score(self):
        print("Your score went up!")
        self.player_score += 1

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
                    print("{:20}{:<5}".format(item, self.item_dictionary.get(item, "Error, Report me pls!")))

    # allows getting items into his inventory
    def get_item(self, item):

        if item in self.inventory:
            print("I don't need more of these.")
        # if item is not false or none
        elif item:
            self.inventory.append(item)
            print("I picked up the ", item)

    # getting item out of inventory
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
    """This is the bunker class. It acts as the starting room for the player."""
    def __init__(self, items_contained=None, bool_list=(False, False, False)):
        if items_contained is None:
            items_contained = ["temp"]
        self.inventory = items_contained
        self.bool_one, self.bool_two, self.bool_three = bool_list

        self.look_dict = {}

        self.go_dict = {}
        self.oper_dict = {}

        self.use_dict = {}

    # this prints a description along with a item list
    def print_description_room(self):
        print("It's an example room. use temp with box.")
        print("go outside should work too but only print something."
              "")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    def print_description_box(self):
        print("its a box")

    def print_description_door(self):
        print("it's a door")

    def operate_door(self):
        if not self.bool_one:
            self.bool_one = True
            print("switched to new value door")
        else:
            print("stays the same door")

    def operate_fuse_box(self):
        if not self.bool_two:
            self.bool_two = True
            print("switched to new value box")
        else:
            print("stays the same box")

    def testing_using_items(self, item):
        if not self.bool_one:
            if item == "temp":
                print("Worked with temp item")
                self.bool_one = False
                return True
            else:
                print("Wrong item")
                return False
        else:
            print("Already used.")
            return False

    @staticmethod
    def go_outside(player_object):
        print("going outside")
        player_object.location = ""

    def go_sideroom(self, player_object):
        print("going sideroom")
