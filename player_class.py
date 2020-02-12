from item_descriptions_class import ItemDictionary
from map_class import MapOfBuilding


class VernLion:
    def __init__(self, player_inventory=None, player_start="bunker", score=0, player_bools=False):

        if player_inventory is None:
            player_inventory = ["self"]

        self.inventory = player_inventory
        self.dictionary = ItemDictionary()
        self.location = player_start
        self.map_building = MapOfBuilding()
        self.player_score = score
        self.made_drugged_meat = player_bools

    # returns his location
    def get_location(self):
        return self.location

    # returns a list of his inventory
    def get_inventory(self):
        return self.inventory

    def get_bools(self):
        return self.made_drugged_meat

    # returns the players score for saving
    def get_score(self):
        return self.player_score

    # prints your score
    def check_score(self):
        print("Your score is {self.player_score}.")

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
                    print("{:20}{:<5}".format(item, self.dictionary.get_description(item)))

    # allows getting items into his inventory
    def get_item(self, item):

        if item in self.inventory:
            print("I don't need more of these.")
        elif item is None:
            pass
        else:
            self.inventory.append(item)
            print("I picked up the ", item)

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
        location = self.inventory.index(item)
        print("I used the ", item)
        self.inventory.remove(location)

    # combines items
    def combine_items(self, item_1, item_2):
        if item_1 in self.inventory and item_2 in self.inventory:
            if item_1 == "meat" and item_2 == "drugs" or item_1 == "drugs" and item_2 == "meat":
                self.inventory.remove(item_1)
                self.inventory.remove(item_2)
                self.inventory.append("drugged meat")
                print("I made drugged meat. Still nasty after that.")
                self.made_drugged_meat = True
            elif item_1 == "" and item_2 == "" or item_1 == "" and item_2 == "":
                pass
        else:
            print("I don't have all I need")


    # looking at map
    def look_player_map(self):
        if "map" in self.inventory:
            self.map_building.print_map()
        else:
            print("I don't have one.")

    # looking at self
    def look_self(self):
        print("A nervous lion is what you are. Somehow still alive but for how long? Hopefully long enough.")