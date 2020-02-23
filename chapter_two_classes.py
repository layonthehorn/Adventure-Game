import time


class PlayerClass:
    """This is the main player class. It holds the player inventory and score among other things."""
    def __init__(self, player_inventory=None, player_start="example", score=0, player_misc=(False, 0)):

        if player_inventory is None:
            player_inventory = ["self"]

        self.inventory = player_inventory
        self.location = player_start
        self.player_score = score
        self.bool_one, self.misc_counter = player_misc

        self.map_of_building = """

               """
        self.item_dictionary = {
            "temp": "Used for holding a place for real items.",

        }

    # returns his location
    def get_location(self):
        return self.location

    # returns a list of his inventory
    def get_inventory(self):
        return self.inventory

    def get_misc(self):
        return self.bool_one, self.misc_counter

    # returns the players score for saving
    def get_score(self):
        return self.player_score

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
        elif item is None:
            pass
        else:
            self.inventory.append(item)
            print("I picked up the ", item)

    # returns if your mane has been brushed
    def is_mane_brushed(self):
        return self.mane_brushed

    # allows changing his location
    def set_location(self, room):
        self.location = room

    # getting item out of inventory
    def drop_item(self, item):
        if item in self.inventory:
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
            if "meat" in item_list and "drugs" in item_list:
                self.inventory.remove(item_1)
                self.inventory.remove(item_2)
                self.inventory.append("drugged meat")
                print("I made drugged meat. Still nasty after that.")
                return True

            # no matches found
            else:
                print(f"I can't combine {item_1} and {item_2}.")
                return False

        # No matching items found
        else:
            print("I don't have all I need")
            return False

    # looking at map
    def look_player_map(self):
        if "map" in self.inventory:
            print("Let me check my map.\n*Map crinkling sounds.*")
            time.sleep(1.5)
            print(self.map_of_building)
        else:
            print("I don't have one.")

    # looking at self
    def look_self(self):
        print("A nervous lion is what you are. Somehow still alive but for how long? Hopefully long enough.")


class ExampleRoom:
    """This is the bunker class. It acts as the starting room for the player."""
    def __init__(self, items_contained=None, bool_list=(False, False, False)):
        if items_contained is None:
            items_contained = ["temp"]
        self.inventory = items_contained
        self.bool_one, self.bool_two, self.bool_three = bool_list

        self.look_dict = {
            ("room", "place"): self.print_description_room,
            ("box", "fuse"): self.print_description_box,
            ("door", "exit"): self.print_description_door
                         }

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    def get_bools(self):
        return self.bool_one, self.bool_two, self.bool_three

    # allows getting a print function form the look dictionary.
    def get_look_commands(self, look_at):
        for key in self.look_dict:
            for name in key:
                if look_at in name:
                    look_command = self.look_dict.get(key)
                    look_command()
                    return True
        return False

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

    # this pops off the items and returns it
    def get_item(self, item):
        if item in self.inventory:
            location = self.inventory.index(item)
            return self.inventory.pop(location)
        else:
            return None

    # dropping item back into room
    def give_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)

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
