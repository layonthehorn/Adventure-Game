import time
import Chapter_Two.chapter_two_room_classes as rooms
import Chapter_Two.chapter_two_npc_classes as npc
from Chapter_Two.exception_class import ChangeLocationError, NPCLocationError


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

    def __init__(self, debug):

        self.inventory = ["self"]
        self.debug = debug
        # neg
        self.buy_item_values = {"fish": -5,
                                "can": -3}
        # pos
        self.sell_item_values = {"fish": 4,
                                 "can": 2,
                                 "rock": 1}
        self.__location = "town center"
        self.__section = "town"
        self.changed_location = True
        self.__score = 0
        self.player_wallet = 0
        self.places = []
        self.map_dictionary = {}

        self.item_dictionary = {"music sheet": "A piece of sheet music. Maybe someone would want this?",
                                "fish": "A tasty fish for testing only."}

    def __str__(self):
        return f"""Inventory {self.inventory}\nLocation {self.__location}\nSection {self.section}\nScore {self.__score}"""

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
            if not self.debug:
                print(f"Could not fine {location}... Possible missing spelling in code?")
                print("Could not find matching location. Canceling movement.")
            else:
                raise ChangeLocationError(location)

        # makes sure not to print if you win or end game
        elif location != "end" and location != "exit":

            # checks if we need to update the section you are in
            if location not in self.accepted_sections.get(self.section):
                for key in self.accepted_sections:
                    if location in self.accepted_sections.get(key):
                        print(f"You have gone to the {location}, in the {key}.")
                        self.changed_location = True
                        self.section = key
                        self.__location = location
                        break
                else:
                    print(f"Error, no good section found for {location}.")

            else:
                print(f"You have gone to the {location}.")
                self.changed_location = True
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
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_value):
        if new_value < 1:
            raise ValueError(f"Must be x >= 1, {new_value}.")
        else:
            print("You're score went up!")
            self.__score = new_value

    # prints your score
    def print_score(self):
        print(f"Your score is {self.score}.")

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
        if self.timer == 1200:
            self.am_pm = "PM"
        if (self.__timer + add_time)/2 > 2400:
            add_time = (self.__timer + add_time) % 2400
            self.am_pm = "AM"
        self.__timer = add_time

    def display_time_human(self):
        if self.timer >= 1300:
            clock_time = str(self.timer - 1200)
        else:
            clock_time = str(self.timer)

        # making sure it is always the right length for my string methods
        clock_time = clock_time.zfill(4)
        clock_time = clock_time[0:2] + ':' + clock_time[2:]
        # finds the human readable time
        minutes = str(int(int(clock_time[3:5]) * 3/5))
        clock_time = clock_time[0:3] + minutes.zfill(2)
        return f"The time is {clock_time}, {self.am_pm}"


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
        self.ruin_office = rooms.RuinedOffice(player)
        self.street = rooms.RuinedStreet(player)
        self.house = rooms.RuinedHouse(player)
        self.garage = rooms.RuinedGarage(player)
        # upstairs
        self.gar_office = rooms.UpstairsOffice(player)
        self.break_room = rooms.UpstairsBreakRoom(player)
        self.balcony = rooms.UpstairsBalcony(player)
        # tower rooms
        self.tow_entrance = rooms.TowerEntrance(player)
        self.peak = rooms.TowerPeak(player)
        # mansion rooms
        self.foyer = rooms.MansionFoyer(player)
        self.kitchen = rooms.MansionKitchen(player)
        self.hallway = rooms.MansionHallWay(player)
        self.sun_room = rooms.MansionSunRoom(player)
        self.living_room = rooms.MansionLivingRoom(player)
        # cellar rooms
        self.lab = rooms.CellarLab(player)
        self.cell_entrance = rooms.CellarEntrance(player)
        self.wine_casks = rooms.CellarWineCasks(player)

        # Loading NPCs
        self.scavenger = npc.ScavengerNPC(self.clock, player)
        self.organ_player = npc.OrganPlayer(self.clock, player)
        self.gen_shop_keeper = npc.GeneralStoreOwner(self.clock, player)

        # list NPCs to check if should be moved
        self.npc_roster = {
            # scavenger NPC.
            self.scavenger.name: self.scavenger,
            # organ player NPC
            self.organ_player.name: self.organ_player,
            # general store owner NPC
            self.gen_shop_keeper.name: self.gen_shop_keeper
            }

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
            "ruined office": self.ruin_office,
            "ruined house": self.house,
            "ruined garage": self.garage,

            # garage upstairs rooms and actions
            "break room": self.break_room,
            "managers office": self.gar_office,
            "balcony": self.balcony,

            # back rooms and actions
            "weapons storage": self.weapons_storage,
            "work room": self.work_room,
            "freezer": self.freezer,
            "general storage": self.general_storage,

            # tower rooms and actions
            "tower entrance": self.tow_entrance,
            "tower peak": self.peak,

            # mansion rooms and actions
            "foyer": self.foyer,
            "sun room": self.sun_room,
            "hallway": self.hallway,
            "kitchen": self.kitchen,
            "living room": self.living_room,

            # garden rooms and actions
            # "garden": self.rooms,

            # cellar rooms and actions
            "cellar entrance": self.cell_entrance,
            "wine casks": self.wine_casks,
            "lab": self.lab
        }

    # starts the NPCs where they should be
    def set_up_npc(self):
        for name in self.npc_roster:
            person = self.npc_roster.get(name)
            starting_point = self.switcher_dictionary.get(person.position)

            # errors if no matching location is found for starting point
            if starting_point is None:
                raise NPCLocationError(name, person.position)
            # added them to the rooms action dictionaries
            starting_point.look_dict[name] = person.look_npc
            starting_point.oper_dict[name] = person.talk_to_npc
            starting_point.use_dict[name] = person.use_item

    # moves NPCs around or removes them from the world
    def npc_movement_checker(self):
        npc_deletion = []
        # checks each NPC that can move
        for name in self.npc_roster:
            person = self.npc_roster.get(name)
            current_local = person.position
            if person.check_move() and person.alive:

                # add to new room
                new_room = self.switcher_dictionary.get(person.position)
                if name not in new_room.look_dict:
                    new_room.look_dict[name] = person.look_npc
                if name not in new_room.oper_dict:
                    new_room.oper_dict[name] = person.talk_to_npc
                if name not in new_room.use_dict:
                    new_room.use_dict[name] = person.use_item

                # delete from old room
                old_room = self.switcher_dictionary.get(current_local)
                if name in old_room.look_dict:
                    del old_room.look_dict[name]
                if name in old_room.oper_dict:
                    del old_room.oper_dict[name]
                if name in old_room.use_dict:
                    del old_room.use_dict[name]

            # if they are marked for deletion
            # we remove them from the game.
            elif not person.alive:
                current_room = self.switcher_dictionary.get(person.position)
                if name in current_room.look_dict:
                    del current_room.look_dict[name]
                if name in current_room.oper_dict:
                    del current_room.oper_dict[name]
                if name in current_room.use_dict:
                    del current_room.use_dict[name]
                npc_deletion.append(name)

        # actually removes them from the game
        for name in npc_deletion:
            try:
                del self.npc_roster[name]
            except KeyError:
                pass

        # counts clock up by a quarter hour
        self.clock.timer += 25
