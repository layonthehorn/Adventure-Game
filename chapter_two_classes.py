import time


class FunctionClass:
    """Never to be called. Only used for giving all other classes the same methods."""

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
                print(f"I can't operate {operate}.")
        else:
            print(f"I can't go to {operate}.")

    # allows getting go commands
    def get_go_commands(self, player_object, go):
        # you have to enter at least three letters
        if len(go) >= 2:
            for key in self.go_dict:
                if go in key:
                    go_command = self.go_dict.get(key)
                    go_command(player_object)
                    break
            else:
                print(f"I can't go to {go}.")
        else:
            print(f"I can't go to {go}.")

    # allows using item on objects
    def get_use_commands(self, player_object, use_list):
        item = use_list[0]
        room_object = use_list[1]
        # you have to enter at least three letters
        if len(room_object) >= 3:
            for key in self.use_dict:
                if room_object in key:
                    use_command = self.use_dict.get(key)
                    if use_command(item):
                        player_object.use_item(item)
                        player_object.increase_score()
                    break
            else:
                print(f"I can't find the {room_object}.")
        else:
            print(f"What is a(n) {room_object}.")

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # returns item to room
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


class ExampleRoom(FunctionClass):
    """This is the bunker class. It acts as the starting room for the player."""
    def __init__(self, items_contained=None, bool_list=(False, False, False)):
        if items_contained is None:
            items_contained = ["temp"]
        self.inventory = items_contained
        self.bool_one, self.bool_two, self.bool_three = bool_list

        self.look_dict = {
            "room": self.print_description_room,
            "fuse box": self.print_description_box,
            "exit door": self.print_description_door
                         }

        self.go_dict = {
            "outside": self.go_outside,
            "side room": self.go_sideroom
        }
        self.oper_dict = {
            "door": self.operate_door,
            "fuse box": self.operate_fuse_box
                        }

        self.use_dict = {
            "fuse box": self.testing_using_items
        }

    def get_bools(self):
        return self.bool_one, self.bool_two, self.bool_three

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

    def go_outside(self, player_object):
        print("going outside")
        player_object.set_location("")

    def go_sideroom(self, player_object):
        print("going sideroom")
