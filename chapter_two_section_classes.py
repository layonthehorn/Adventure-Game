import time
import chapter_two_room_classes as rooms


# Player Class
class PlayerClass:
    """This is the main player class. It holds the player inventory and score among other things."""

    # class variables for print formatting
    bold = '''\033[1m'''
    end = '''\033[0;0m'''

    # accepted locations where you can go
    accepted_locations = (
        "end", "exit",
        "town center", "general store", "gate house", "bath house", "bar",
        "ruined street", "ruined office", "ruined house", "ruined garage",
        "kitchen", "foyer", "sun room", "living room", "hallway",
        "tower entrance", "tower peak",
        "cellar entrance", "wine casks", "lab"
                          )
    accepted_sections = {"town": ("town center", "general store", "gate house", "bath house", "bar")
                         , "ruins": ("ruined street", "ruined office", "ruined house", "ruined garage")
                         , "mansion": ("kitchen", "foyer", "sun room", "living room", "hallway")
                         , "upstairs": ()
                         , "gen back rooms": ()
                         , "tower": ("tower entrance", "tower peak")
                         , "cellar": ("cellar entrance", "wine casks", "lab")
                         , "gardens": ()
                         }

    def __init__(self):

        self.inventory = ["self"]
        # neg
        self.buy_item_values = {"fish": -5,
                                "can": -3}
        # pos
        self.sell_item_values = {"fish": 4,
                                 "can": 2,
                                 "rock": 1}
        self.__location = "town center"
        self.__section = "town"
        self.__player_score = 0
        self.player_wallet = 0
        self.places = []
        self.map_dictionary = {}

        self.item_dictionary = {}

    def __str__(self):
        return f"""Inventory {self.inventory}\nLocation {self.__location}\nScore {self.__player_score}"""

    # enables changing player room for testing
    def debug_player(self):
        print("\nEnter location?\n")
        for number, place in enumerate(self.accepted_locations):
            print(f"{self.bold+place+self.end}", end=", ")
            if (number + 1) % 4 == 0:
                print("")
        print("")
        choice = input("").lower()
        self.location = choice

    @property
    def section(self):
        return self.__section

    @section.setter
    def section(self, new_sec):
        self.__section = new_sec

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        # makes sure that you do not enter a bad location.
        if location not in self.accepted_locations:
            print(f"Could not fine {location}... Possible missing spelling in code?")
            print("Could not find matching location. Canceling movement.")

        # makes sure not to print if you win or end game
        elif location != "end" and location != "exit":

            # checks if we need to update the section you are in
            if location not in self.accepted_sections.get(self.section):
                for key in self.accepted_sections:
                    if location in self.accepted_sections.get(key):
                        print(f"You have gone to the {location}, in the {key}.")
                        self.section = key
                        self.__location = location
                        break
                else:
                    print(f"Error, no good section found for {location}.")

            else:
                print(f"You have gone to the {location}.")
                self.__location = location

        # if you go to the exit or end, does not print anything
        else:
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
                    print(
                        f"{self.bold + item + self.end:<20}{self.item_dictionary.get(item, 'Error, Report me pls!'):<5}")

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
        print("Let me check my map.\n*Map crinkling sounds.*")
        time.sleep(1.5)
        if self.section == "town":
            print("""
                                                   +--------------------+
                                                   |     Town Area      |
                                                   +--------------------+     
                                                   |Legend:             |
                                                   |                    |
                                                   |Ruins Area:      RA |
                      TB                           |Mansion Area:    MA |
                      ||                           |Back Rooms Area: BA |
                  RA--TC--GH--MA                   |Town Center:     TC |
                      ||\\\\                         |Town Bar:        TB |
                      GS BH                        |General Store:   GS |
                     //                            |Bath House:      BH |
                     BA                            |Gate House:      GH |
                                                   |You: @@ in room  ?? |
                                                   +--------------------+ 
              """)
        elif self.section == "ruins":
            print("""
                                                   +--------------------+
                                                   |     Ruins Area     |
                                                   +--------------------+
                      RO                           |Legend:             |
                      ||                           |                    |
                      RS--TA                       |Town Area:       TA |
                      ||\\\\                         |Upstairs Area:   UA |
                  UA--MA RH                        |Ruined House:    RH |
                                                   |Ruined Garage:   RG |
                                                   |Ruined Office:   RO |
                                                   |Ruined Street:   RS |
                                                   |You: @@ in room  ?? |
                                                   +--------------------+
              """)
        elif self.section == "tower":
            print("""
                                                   +--------------------+
                                                   |     Tower Area     |
                                                   +--------------------+
                      TP                           |Legend:             |
                      ||                           |                    |
                      TE                           |Mansion Area:    MA |
                      ||                           |Tower Peak:      TP |
                      MA                           |Tower Entrance:  TE |
                                                   |You: @@ in room  ?? |
                                                   +--------------------+
              """)
        elif self.section == "mansion":
            print("""
                                                   +--------------------+
                                                   |    Mansion Area    |
                                                   +--------------------+
                                                   |Legend:             |
                      MT                           |                    |
                      ||                           |Town Area:       TA |
                      SR  LR                       |Mansion Tower:   MT |
                      ||  ||                       |Garden Area:     GA |
                  TA--MF--HW--GA                   |Mansion Foyer:   MF |
                      ||                           |Mansion Kitchen: MK |
                      MK                           |Hallway:         HW |
                      ||                           |Sun Room:        SR |
                      CA                           |Living Room:     LR |
                                                   |You: @@ in room  ?? |
                                                   +--------------------+
              """)
        elif self.section == "gardens":
            print("""
                                                   +--------------------+
                                                   |    Garden Area     |
                                                   +--------------------+
                                                   |Legend:             |
                                                   |                    |
                                                   |Mansion Area:    MA |
                                                   |Room One:        R1 |
                                                   |Room Two:        R2 |
                                                   |Room Three:      R3 |
                                                   |Room Four:       R4 |
                                                   |Room Five:       R5 |
                                                   |Room Six:        R6 |
                                                   |Room Seven:      R7 |
                                                   |You: @@ in room  ?? |
                                                   +--------------------+
              """)
        elif self.section == "cellar":
            print("""
                                                   +--------------------+
                                                   |    Cellar Area     |
                                                   +--------------------+
                                                   |Legend:             |
                      MA                           |                    |
                      ||                           |Mansion Area:    MA |
                      CE--LB                       |Lab:             LB |
                      ||                           |Wine Casks:      WC |
                      WC                           |Cellar Entrance: CE |
                                                   |You: @@ in room  ?? |
                                                   +--------------------+
              """)
        elif self.section == "gen back rooms":
            print("""
                                                   +--------------------+
                                                   |  Back Rooms Area   |
                                                   +--------------------+
                        TA                         |Legend:             |
                       //                          |                    |
              R3--R2--R1                           |Town Area:       TA |
                    \\\\||                           |Room One:        R1 |
                      R4                           |Room Two:        R2 |
                                                   |Room Three:      R3 |
                                                   |Room Four:       R4 |
                                                   |You: @@ in room  ?? |
                                                   +--------------------+
              """)
        elif self.section == "upstairs":
            print("""
                                                   +--------------------+
                                                   |   Upstairs Area    |
                                                   +--------------------+
                                                   |Legend:             |
                                                   |                    |
                      R1--RA                       |Ruins Area:      RA |
                    //  \\\\                         |Room One:        R1 |
                   R2----R3                        |Room Two:        R2 |
                                                   |Room Three:      R3 |
                                                   |You: @@ in room  ?? |
                                                   +--------------------+
              """)
        else:
            print("Error no match location found.")

    # looking at self
    def look_self(self):
        print("A nervous lion is what you are. Somehow still alive but for how long? Hopefully long enough.")


# town center and starting section for player
class TownCenter:
    NPC_Roster = {}
    """This starts all the rooms in the town center.
    It also will track NPC movements and cross room changes."""

    def __init__(self, player):
        self.center = rooms.TownCenter(player)
        self.bar = rooms.TownBar(player)
        self.gen_store = rooms.TownGenStore(player)
        self.bath_house = rooms.TownBathHouse(player)
        self.gate_house = rooms.TownGateHouse(player)


class BackRooms:
    """This starts all the rooms in the general store back rooms.
    It also will track NPC movements and cross room changes."""
    NPC_Roster = {}

    def __init__(self, player):
        pass


# ruins outside the town, good for scavenging
class Ruins:
    """This starts all the rooms in the ruins.
    It also will track NPC movements and cross room changes."""
    NPC_Roster = {}

    def __init__(self, player):
        self.office = rooms.RuinedOffice(player)
        self.street = rooms.RuinedStreet(player)
        self.house = rooms.RuinedHouse(player)
        self.garage = rooms.RuinedGarage(player)


class Upstairs:
    """This starts all the rooms in the ruins upstairs section.
    It also will track NPC movements and cross room changes."""
    NPC_Roster = {}

    def __init__(self, player):
        pass


# a tower to the house
class Tower:
    """This starts all the rooms in the mansion tower.
    It also will track NPC movements and cross room changes."""
    NPC_Roster = {}

    def __init__(self, player):
        self.entrance = rooms.TowerEntrance(player)
        self.peak = rooms.TowerPeak(player)


class Mansion:
    """This starts all the rooms in the mansion.
    It also will track NPC movements and cross room changes."""
    NPC_Roster = {}

    def __init__(self, player):
        self.foyer = rooms.MansionFoyer(player)
        self.kitchen = rooms.MansionKitchen(player)
        self.hallway = rooms.MansionHallWay(player)
        self.sun_room = rooms.MansionSunRoom(player)
        self.living_room = rooms.MansionLivingRoom(player)


class Gardens:
    """This starts all the rooms in the mansion gardens.
    It also will track NPC movements and cross room changes."""
    NPC_Roster = {}

    def __init__(self, player):
        pass


class Cellar:
    """This starts all the rooms in the cellar.
    It also will track NPC movements and cross room changes."""
    NPC_Roster = {}

    def __init__(self, player):
        self.lab = rooms.CellarLab(player)
        self.entrance = rooms.CellarEntrance(player)
        self.wine_casks = rooms.CellarWineCasks(player)
