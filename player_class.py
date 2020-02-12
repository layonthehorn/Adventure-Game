import time

from item_descriptions_class import ItemDictionary


class VernLion:
    def __init__(self, player_inventory=None, player_start="bunker", score=0, player_bools=False):

        if player_inventory is None:
            player_inventory = ["self"]

        self.inventory = player_inventory
        self.dictionary = ItemDictionary()
        self.location = player_start
        self.player_score = score
        self.made_drugged_meat = player_bools
        self.map_of_building = """
          ---------MAP----------
                                               +--------------------+
                   SS                          |Legend:             |
                   ||                          |                    |
               AD--UP--RR                      |Main Plaza: MP      |
            C   SD ||                          |Upper Hall: UH      |
            ||   \\\\||                          |Pet Shop: PS        |
        PS--WW-----MP----EXIT                  |Shoe Store: SS      |
            ||     ||                          |Restroom: RR        |
            TS     FS--CR                      |Animal Den: AD      |
                                               |Small Den: SD       |
                                               |West wing: WW       |
                                               |Toy Shop: TS        |
                                               |Cemetery: C         |
                                               |Fallout Shelter: FS |
                                               |Computer Room: CR   |
                                               |                    |
                                               +--------------------+  
               """

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
        # never removes self from inventory.
        if item != "self":
            location = self.inventory.index(item)
            print("I used the ", item)
            self.inventory.remove(location)
        else:
            print("I used myself?")

    # combines items
    def combine_items(self, item_1, item_2):
        if item_1 in self.inventory and item_2 in self.inventory:
            if item_1 == "meat" and item_2 == "drugs" or item_1 == "drugs" and item_2 == "meat":
                self.inventory.remove(item_1)
                self.inventory.remove(item_2)
                self.inventory.append("drugged meat")
                print("I made drugged meat. Still nasty after that.")
                self.made_drugged_meat = True
            elif item_1 == "bag of catnip" and item_2 == "lion plush" or item_1 == "lion plush" and item_2 == "bag of catnip":
                self.inventory.remove(item_1)
                self.inventory.remove(item_2)
                self.inventory.append("cat toy")
                print("I am so ashamed of myself for this...")
            else:
                print(f"I can't combine {item_1} and {item_2}.")
        else:
            print("I don't have all I need")

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