import time


class VernLion:
    def __init__(self, player_inventory=None, player_start="bunker", score=0, player_misc=(False, 0)):

        if player_inventory is None:
            player_inventory = ["self"]

        self.inventory = player_inventory
        self.location = player_start
        self.player_score = score
        self.mane_brushed, self.fish_counter = player_misc

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
        self.item_dictionary = {
            "wrench": "Used for unstucking random things. Always handy with robots.",
            "fuse": "Lots of old world tech uses this to keep power flowing.",
            "bag of catnip": "Hey now. You need to stay sober.",
            "lion plush": "A cute lion plush. I wonder who left this here?",
            "keys": "These might be handy for reaching high places.",
            "strange keys": "For some reason you recognise them. Maybe they belong to a friend?",
            "meat": "Maybe something will want this?",
            "toy raygun": "It's flashing random colors. Not useful but fun!",
            "knife": "It cuts. I mean what else do you think it does?",
            "fur sample": "It's fur. Maybe you could use it to get in the pet store?",
            "map": "A map to the mall! Someone must have updated it recently.",
            "drugged meat": "This would knockout anything that eats it.",
            "battery": "This could be used to power something, or overpower it.",
            "mane brush": "You could use this on your mane. Not that you ever need it.",
            "self": "It's you... You should not see this item in your inventory. Please report it!",
            "cheetah keyring": "It's a cheetah keyring. Cute but not really useful to you right now.",
            "cat toy": "A lion plush stuff with catnip. You druggie...",
            "red fuse": "It's a red fuse. Much larger than the one from the bunker.",
            "green fuse": "It's a green fuse. Much larger than the one from the bunker.",
            "gold fuse": "It's a gold fuse. Much larger than the one from the bunker.",
            "blue fuse": "It's a blue fuse. Much larger than the one from the bunker.",
            "fish": "A very tasty if small fish. Should you?.. Eat it?",
            "bones": "Bones are all that's left of the little fish you ate. How could you?",
            "rope": "A length of rope. Might be useful to get somewhere lower.",
            "long rope": "A long length of rope. This should reach the bottom.",
            "soda": "An old flat soda. Not something you want to drink.",
            "shovel": "It's an old entrenching tool. Useful for digging and many other things.",
            "soldering iron": "It's used to repair wires and circuits.",
            "soldering wire": "Used to fix circuits and connections.",
            "capacitor": "A part to a circuit board, might be handy.",
            "circuit board": "A repaired part to a machine somewhere."
        }

    # returns his location
    def get_location(self):
        return self.location

    # returns a list of his inventory
    def get_inventory(self):
        return self.inventory

    def get_misc(self):
        return self.mane_brushed, self.fish_counter

    # returns the players score for saving
    def get_score(self):
        return self.player_score

    # prints your score
    def print_score(self):
        print(f"Your score is {self.player_score} out of 'Unknown Final Value'.")

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
            elif "lion plush" in item_list and "bag of catnip" in item_list:
                self.inventory.remove(item_1)
                self.inventory.remove(item_2)
                self.inventory.append("cat toy")
                print("I am so ashamed of myself for this...")
                return False
            # all using items on self reactions
            elif "self" in item_list and "cat toy" in item_list:
                self.inventory.remove("cat toy")
                print("purrrrr Mmmmm catnip.")
                return False
            elif "self" in item_list and "mane brush" in item_list:
                self.inventory.remove("mane brush")
                print("Hey, I'm looking better now. That's good too.")
                self.mane_brushed = True
                return True
            elif "self" in item_list and "drugs" in item_list:
                print("I'm not eating them...")
                return False
            elif "self" in item_list and "meat" in item_list:
                print("Nasty. I love meat but this is not appetizing at all.")
                return False
            elif "self" in item_list and "drugged meat" in item_list:
                print("Eating rotten meat is not any safer with medication in it.")
                return False
            elif "self" in item_list and "soda" in item_list:
                print("I hate sugary things...")
                return False
            elif "self" in item_list and "bag of catnip" in item_list:
                print("I need to stay sober right now... \nIf it was in a little cute toy I might... No, I better not.")
                return False
            elif "self" in item_list and "knife" in item_list:
                print("I don't think that's a great plan...")
                return False

            # small thing for player repeating the eat fish command
            elif "self" in item_list and "fish" in item_list:
                if self.fish_counter == 0:
                    print("I really shouldn't. Though it is tasty looking...")
                    self.fish_counter += 1
                    return False
                elif self.fish_counter == 1:
                    print("Still shouldn't eat it.")
                    self.fish_counter += 1
                    return False
                elif self.fish_counter == 2:
                    print("No, I need to get rid of it. I keep getting temped.")
                    self.fish_counter += 1
                    return False
                else:
                    print("Vern finally gives in and eats the little fish.")
                    print("Oh no! I couldn't resist anymore...")
                    print("Now all I have is a pile of bones.")
                    self.inventory.append("bones")
                    self.inventory.remove("fish")
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
        if "meat" in self.inventory or "drugged meat" in self.inventory:
            print("This meat smells awful...")
        if self.mane_brushed:
            print("At least I'm cleaned up now.")
