import time
import Chapter_Two.chapter_two_room_classes as rooms
import Chapter_Two.chapter_two_npc_classes as npc


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
        "cellar entrance", "wine casks", "lab",
        "manager office", "break room", "balcony",
        "weapon storage", "work room", "general storage", "freezer"
                          )
    # sections of the map, changes how your map looks.
    accepted_sections = {"town": ("town center", "general store", "gate house", "bath house", "bar")
                         , "ruins": ("ruined street", "ruined office", "ruined house", "ruined garage")
                         , "mansion": ("kitchen", "foyer", "sun room", "living room", "hallway")
                         , "upstairs": ("manager office", "break room", "balcony")
                         , "gen back rooms": ("weapon storage", "work room", "general storage", "freezer")
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
        print("Add item or change location?")
        pick = input("").lower()

        # debug for changing rooms
        if pick in "location":
            print("\nEnter location?\n")
            for number, place in enumerate(self.accepted_locations):
                print(f"{self.bold+place+self.end}", end=", ")
                if (number + 1) % 4 == 0:
                    print("")
            print("")
            choice = input("").lower()
            self.location = choice

        # debug for adding items to inventory
        elif pick in "item":
            print("\nEnter item?\n")
            for number, place in enumerate(self.item_dictionary):
                print(f"{self.bold+place+self.end}", end=", ")
                if (number + 1) % 4 == 0:
                    print("")
            print("")
            choice = input("").lower()
            if choice in self.item_dictionary:
                self.inventory.append(choice)
            else:
                print("No matching item to add.")
        else:
            print("Not an acceptable action.")

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
              WS--WR--GS                           |Town Area:       TA |
                    \\\\||                           |General Storage: GS |
                      FR                           |Work Room:       WR |
                                                   |Freezer:         FR |
                                                   |Weapons Storage: WS |
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
                   MO-BR-RA                        |Ruins Area:      RA |
                    \\\\//                           |Break Room:      BR |
                     GB                            |Managers Office: MO |
                                                   |Garage Balcony:  GB |
                                                   |You: @@ in room  ?? |
                                                   +--------------------+
              """)
        else:
            print("Error no match location found.")

    # looking at self
    def look_self(self):
        print("A nervous lion is what you are. Somehow still alive but for how long? Hopefully long enough.")


class TimeKeeper:
    def __init__(self):
        self.__timer = 0
        self.__am_pm = "AM"

    @property
    def am_pm(self):
        return self.__am_pm

    @am_pm.setter
    def am_pm(self, value):
        if value in ("AM", "PM"):
            self.__am_pm = value
        else:
            print("Error, bad value in AM/PM switcher.")

    @property
    def timer(self):
        return self.__timer

    @timer.setter
    def timer(self, add_time):
        if 12 <= self.timer < 13:
            self.am_pm = "PM"
        if (self.__timer + add_time)/2 > 24:
            add_time = (self.__timer + add_time) % 24
            self.am_pm = "AM"
        self.__timer = add_time


# class NPCMovement:
#     """Controls NPC movement across rooms."""
#     def __init__(self, town, ruins):
#         # locations for NPCs to move
#         self.town = town
#         self.ruins = ruins
#
#     # checks if it needs to move NPCs
#     def check_npc_move(self):
#         self.move_npc_scavenger()

    # def move_npc_scavenger(self):
    #     if self.scavenger.check_move:
    #         # move to town
    #         if self.scavenger_move_count == 0:
    #             self.scavenger_move_count += 1
    #             self.move_npc_actions(self.scavenger, self.town.center, self.ruins.ruined_street)
    #         # move to general store
    #         elif self.scavenger_move_count == 1:
    #             self.scavenger_move_count += 1
    #             self.move_npc_actions(self.scavenger, self.town.gen_store, self.ruins.center)
    #         # move to town
    #         elif self.scavenger_move_count == 2:
    #             self.scavenger_move_count += 1
    #             self.move_npc_actions(self.scavenger, self.ruins.center, self.town.gen_store)
    #         # move to ruined street again
    #         elif self.scavenger_move_count == 3:
    #             self.move_npc_actions(self.scavenger, self.town.town_center, self.ruins.ruined_street)
    #             self.scavenger_move_count = 0
    #
    # @staticmethod
    # def move_npc_actions(npc, new_room, old_room):
    #     pass


class RoomSystem:
    """This starts all the rooms.
    It also will track NPC movements and cross room changes."""

    def __init__(self, player):
        self.clock = TimeKeeper()
        # back rooms
        self.weapons_storage = rooms.WeaponsStorage(player)
        self.general_storage = rooms.GeneralStorage(player)
        self.freezer = rooms.Freezer(player)
        self.work_room = rooms.WorkRoom(player)
        # town center
        self.center = rooms.TownCenter(player)
        self.bar = rooms.TownBar(player)
        self.gen_store = rooms.TownGenStore(player)
        self.bath_house = rooms.TownBathHouse(player)
        self.gate_house = rooms.TownGateHouse(player)
        # ruins
        self.office = rooms.RuinedOffice(player)
        self.street = rooms.RuinedStreet(player)
        self.house = rooms.RuinedHouse(player)
        self.garage = rooms.RuinedGarage(player)
        # upstairs
        self.office = rooms.UpstairsOffice(player)
        self.break_room = rooms.UpstairsBreakRoom(player)
        self.balcony = rooms.UpstairsBalcony(player)
        # tower rooms
        self.entrance = rooms.TowerEntrance(player)
        self.peak = rooms.TowerPeak(player)
        # mansion rooms
        self.foyer = rooms.MansionFoyer(player)
        self.kitchen = rooms.MansionKitchen(player)
        self.hallway = rooms.MansionHallWay(player)
        self.sun_room = rooms.MansionSunRoom(player)
        self.living_room = rooms.MansionLivingRoom(player)
        # cellar rooms
        self.lab = rooms.CellarLab(player)
        self.entrance = rooms.CellarEntrance(player)
        self.wine_casks = rooms.CellarWineCasks(player)
        self.scavenger = npc.ScavengerNPC(self.clock)
        # npc_list = (npc.ScavengerNPC(self.clock))
        # name_list = ("scavenger")

        # list NPCs to check if should be moved
        self.npc_roster = {"scavenger": self.scavenger}

        # lists possible rooms to move to
        self.switcher_dictionary = {
            # town center rooms and actions
            "town center": self.center,
            "bar": self.bar,
            "bath house": self.bath_house,
            "general store": self.gen_store,
            "gate house": self.gate_house,

            # ruins rooms and actions
            "ruined street": self.street,
            "ruined office": self.office,
            "ruined house": self.house,
            "ruined garage": self.garage,

            # garage upstairs rooms and actions
            "break room": self.break_room,
            "managers office": self.office,
            "balcony": self.balcony,

            # back rooms and actions
            "weapons storage": self.weapons_storage,
            "work room": self.work_room,
            "freezer": self.freezer,
            "general storage": self.general_storage,

            # tower rooms and actions
            "tower entrance": self.entrance,
            "tower peak": self.peak,

            # mansion rooms and actions
            "foyer": self.foyer,
            "sun room": self.sun_room,
            "hallway": self.hallway,
            "kitchen": self.kitchen,

            # garden rooms and actions
            # "garden": self.rooms,

            # cellar rooms and actions
            "cellar entrance": self.entrance,
            "wine casks": self.wine_casks,
            "lab": self.lab
        }

    # starts the NPCs where they should be
    def set_up_npc(self):
        for key in self.npc_roster:
            person = self.npc_roster.get(key)
            starting_point = self.switcher_dictionary.get(person.position)
            starting_point.look_dict[key] = person.look_npc
            starting_point.oper_dict[key] = person.talk_to_npc
            starting_point.use_dict[key] = person.use_item

    def npc_movement_checker(self):
        for key in self.npc_roster:
            person = self.npc_roster.get(key)
            current_local = person.position
            if person.check_move():
                # add to new room
                new_room = self.switcher_dictionary.get(person.position)
                new_room.look_dict[key] = person.look_npc
                new_room.oper_dict[key] = person.talk_to_npc
                new_room.use_dict[key] = person.use_item

                # delete from old room
                old_room = self.switcher_dictionary.get(current_local)
                if key in old_room.look_dict:
                    del old_room.look_dict[key]
                if key in old_room.oper_dict:
                    del old_room.oper_dict[key]
                if key in old_room.use_dict:
                    del old_room.use_dict[key]

        self.clock.timer += .5
