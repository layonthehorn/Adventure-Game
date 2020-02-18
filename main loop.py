import pickle
import re

from cemetery import Cemetery
from main_plaza import MainPlaza
from player_class import VernLion
from side_room_class import SideRoom
from small_den import SmallDen
from starting_room_class import StartingRoom
from west_wing import WestWing
from toy_shop import ToyShop
from pet_shop import PetShop
from upstairs_hallway import UpstairsHallway
from animal_den import AnimalDen
from bathroom import Bathroom
from shoe_store import ShoeStore
from basement_enter import BasementEnter
from basement_final_room import BasementGenRoom


# loading saved game
def load_game_state(file_name):
    try:
        with open(file_name, 'rb') as db_file:
            pickle_db = pickle.load(db_file)
            return pickle_db
    except FileNotFoundError:
        return None


def print_help():
    print("How to play.")
    print("look {item}: Looks at things. room, map, objects."
          "\ninv(entory): Checks your inventory and prints descriptions out."
          "\nget {item}: Gets items from room."
          "\noper(ate) {object}: How you use objects: doors, computers, etc."
          "\ncom(bine) {item} with/on {item}: allows you to combine items. Use 'self' to use an item on you."
          "\ndrop {item}: Allows you to get rid of an item."
          "\nscore: Allows the player to check current progress in-game."
          "\nuse {item} With/on {item}: how you use things with other things."
          "\ngo {location}: How you change rooms."
          "\nsave: How you save your game."
          "\nend: Exit game and will ask to save or not."
          "\nhelp: This menu.")


def print_loading():
    print("Game Loaded.")


def print_intro():
    print("""
You wake up, alone and afraid in an old fallout shelter, built some time in the past, but abandoned 
long ago. It appears a group had set themselves up here before the end, judging by the things that were left 
behind. The room smells of mould and rust. There is a disabled robot in the corner, an entry to a smaller 
room and there is a door that appears to be locked.
""")


class VernsAdventure:
    def __init__(self):

        # pattern matching for actions
        self.use_pattern = re.compile(r"^use\s|\swith\s|\son\s")
        self.combine_pattern = re.compile(r"^com\s|\swith\s|\son\s")

        # building the rooms and player names
        self.main_plaza_name = "outside"
        self.starting_room_name = "bunker"
        self.side_room_name = "side room"
        self.small_den_name = "small den"
        self.west_wing_name = "west wing"
        self.cemetery_name = "cemetery"
        self.toy_shop_name = "toy shop"
        self.pet_shop_name = "pet shop"
        self.exit_name = "exit"
        self.end_name = "end"
        self.up_stairs_hallway_name = "upstairs"
        self.animal_den_name = "animal den"
        self.shoe_store_name = "shoe store"
        self.bathroom_name = "bathroom"
        self.basement_entryway_name = "basement entry"
        self.basement_gen_room_name = "basement generator"
        self.playing = True

        # Temporary ascii art from https://ascii.co.uk/art/lion
        self.ascii_image = """                 ,  ,, ,
                   , ,; ; ;;  ; ;  ;
                , ; ';  ;  ;; .-''\\ ; ;
             , ;  ;`  ; ,; . / /8b \\ ; ;
             `; ; .;'         ;,\\8 |  ;  ;
              ` ;/   / `_      ; ;;    ;  ; ;
                 |/.'  /0)    ;  ; `    ;  ; ;
                ,/'   /       ; ; ;  ;   ; ; ; ;
               /_   /         ;    ;  `    ;  ;
              `?8P"  .      ;  ; ; ; ;     ;  ;;
              | ;  .:: `     ;; ; ;   `  ;  ;
              `' `--._      ;;  ;;  ; ;   ;   ;
               `-..__..--''   ; ;    ;;   ; ;   ;
                           ;    ; ; ;   ;     ;

        """
        # Main Classes
        # These are loaded below as to not load them twice.
        # self.player - The player character class
        # self.starting_room - the bunker room class
        # self.side_room - the computer room to the side of the bunker class
        # self.main_plaza - the area outside the bunker # self.cemetery - the area north of the west wing.
        # self.west_wing - a side area used to reach more places
        # self.toy_shop - the toy shop off of the west wing
        # self.pet_shop - A pet shot off of the west wing
        # self.up_stairs_hallway - the upstairs hallway
        # self.animal_den - the upstairs den
        # self.shoe_store - the shoe store up stairs
        # self.bathroom - the bathroom upstairs
        # self.basement_entry - where you have to go to finish the game
        # self.basement_gen_room - where you turn on the power.

        choosing = True
        print(self.ascii_image)
        print("Welcome to my game!")
        while choosing:
            player_option = input("Load(L), Start New(S), or How to play(H)?").upper()
            if player_option == "S":
                # Loads defaults in classes for game
                self.player = VernLion()
                self.starting_room = StartingRoom()
                self.side_room = SideRoom()
                self.main_plaza = MainPlaza()
                self.small_den = SmallDen()
                self.west_wing = WestWing()
                self.cemetery = Cemetery()
                self.toy_shop = ToyShop()
                self.pet_shop = PetShop()
                self.up_stairs_hallway = UpstairsHallway()
                self.animal_den = AnimalDen()
                self.shoe_store = ShoeStore()
                self.bathroom = Bathroom()
                self.basement_entryway = BasementEnter()
                self.basement_gen_room = BasementGenRoom()
                print_intro()
                choosing = False
            elif player_option == "L":
                # getting loaded settings
                new_value_dictionary = load_game_state("save game")
                # if the dictionary is none it can not load a game
                if new_value_dictionary is None:
                    print("No save games found.")
                else:

                    # loading saved settings for classes
                    # player data
                    self.player = VernLion(new_value_dictionary["player inventory"],
                                           new_value_dictionary["player location"],
                                           new_value_dictionary["player score"],
                                           new_value_dictionary["player misc"])
                    # bunker data
                    self.starting_room = StartingRoom(new_value_dictionary["starting room items"],
                                                      new_value_dictionary["starting room bools"])
                    # side room data
                    self.side_room = SideRoom(new_value_dictionary["side room items"],
                                              new_value_dictionary["side room bools"])
                    # main plaza data
                    self.main_plaza = MainPlaza(new_value_dictionary["main plaza items"],
                                                new_value_dictionary["main plaza bools"])
                    # small den data
                    self.small_den = SmallDen(new_value_dictionary["small den items"],
                                              new_value_dictionary["small den bools"])
                    # west wing data
                    self.west_wing = WestWing(new_value_dictionary["west wing items"],
                                              new_value_dictionary["west wing bools"])
                    # cemetery data
                    self.cemetery = Cemetery(new_value_dictionary["cemetery items"],
                                             new_value_dictionary["cemetery bools"])
                    # toy shop data
                    self.toy_shop = ToyShop(new_value_dictionary["toy shop items"],
                                            new_value_dictionary["toy shop bools"])
                    # pet shop data
                    self.pet_shop = PetShop(new_value_dictionary["pet shop items"],
                                            new_value_dictionary["pet shop bools"])
                    # upstairs hallway data
                    self.up_stairs_hallway = UpstairsHallway(new_value_dictionary["upstairs hallway items"],
                                                             new_value_dictionary["upstairs hallway bools"])
                    # animal den data
                    self.animal_den = AnimalDen(new_value_dictionary["animal den items"],
                                                new_value_dictionary["animal den bools"])
                    # bathroom data
                    self.bathroom = Bathroom(new_value_dictionary["bathroom items"],
                                             new_value_dictionary["bathroom bools"])
                    # shoe store data
                    self.shoe_store = ShoeStore(new_value_dictionary["shoe store items"],
                                                new_value_dictionary["shoe store bools"])

                    # basement entryway data
                    self.basement_entryway = BasementEnter(new_value_dictionary["basement entry items"],
                                                           new_value_dictionary["basement entry bools"])

                    # basement generator room data
                    self.basement_gen_room = BasementGenRoom(new_value_dictionary["basement gen items"],
                                                             new_value_dictionary["basement gen inv"],
                                                             new_value_dictionary["basement gen bools"])
                    # tells player it loaded the game
                    print_loading()
                    print(f"You are in the {self.player.get_location()} room.")
                    choosing = False

            # prints instructions
            elif player_option == "H":
                print_help()
            else:
                #
                print(self.ascii_image)
                print("Welcome to my game!")
                continue

        # location dictionary
        # used for general actions to run player actions in any room.
        self.switcher_dictionary = {
            self.starting_room_name: self.starting_room,
            self.side_room_name: self.side_room,
            self.main_plaza_name: self.main_plaza,
            self.west_wing_name: self.west_wing,
            self.cemetery_name: self.cemetery,
            self.pet_shop_name: self.pet_shop,
            self.toy_shop_name: self.toy_shop,
            self.small_den_name: self.small_den,
            self.up_stairs_hallway_name: self.up_stairs_hallway,
            self.shoe_store_name: self.shoe_store,
            self.animal_den_name: self.animal_den,
            self.bathroom_name: self.bathroom,
            self.basement_gen_room_name: self.basement_gen_room,
            self.basement_entryway_name: self.basement_entryway
        }

        # action dictionary for each of the rooms special actions
        self.location_dict = {
            self.starting_room_name: self.starting_area,
            self.side_room_name: self.side_area,
            self.main_plaza_name: self.main_plaza_area,
            self.small_den_name: self.small_den_area,
            self.west_wing_name: self.west_wing_area,
            self.cemetery_name: self.cemetery_area,
            self.pet_shop_name: self.pet_shop_area,
            self.toy_shop_name: self.toy_shop_area,
            self.up_stairs_hallway_name: self.up_stairs_hallway_area,
            self.bathroom_name: self.bathroom_area,
            self.animal_den_name: self.animal_den_area,
            self.shoe_store_name: self.shoe_store_area,
            self.basement_entryway_name: self.basement_entryway_area,
            self.basement_gen_room_name: self.basement_gen_area,
            self.exit_name: self.exit_game,
            self.end_name: self.end_game
        }
        player_choice = ""
        self.player_old_room = self.player.get_location()
        self.player_new_room = self.player_old_room
        # main game play loop
        while self.playing:
            # if you reach the exit then don't ask for actions from player
            if self.player_old_room != self.player_new_room:
                print(f"You have gone to the {self.player_new_room} outside.")
                self.player_old_room = self.player_new_room
            if self.player.location != self.exit_name:
                print("Verbs look, inv(entory), get, oper(ate), com(bine), drop, score, use, go, save, end, help")
                player_choice = input("").lower()
                # general actions shared by rooms
                self.general_actions(player_choice)

            # gets the room the player is in
            p_local = self.player.get_location()
            self.player_new_room = p_local
            location_actions = self.location_dict.get(p_local, None)
            # if it does not find a room moves them to the main plaza
            if location_actions is None:
                print("You entered a un-built place. Moving to main plaza.")
                self.player.set_location(self.starting_room_name)
                location_actions = self.main_plaza_area
            if p_local != self.end_name and p_local != self.exit_name:
                # runs the players actions in the room they are in

                # if the player is in the animal den it checks if it needs to run the
                # checking if they placed the meat in the animal den
                if p_local == self.up_stairs_hallway_name:
                    if not self.animal_den.drug_animal():
                        self.small_den.give_item("meat")
                    else:
                        self.player.increase_score()
                location_actions(player_choice)
                print("")
            elif p_local == self.end_name:
                # ends game after player asks to
                self.end_game()
            else:
                # Winning game ending
                self.exit_game()

    # getting things
    def get_items(self, room, item):
        self.player.get_item(room.get_item(item))

    # drops items to a room
    def drop_items(self, room, item):
        if item in self.player.inventory:
            room.give_item(self.player.drop_item(item))
        else:
            print(f"I don't have a(n) {item} to drop.")

    # saves games
    def save_game_state(self):
        value_dictionary = {
                            # player data
                            "player inventory": self.player.get_inventory(),
                            "player score": self.player.get_score(),
                            "player location": self.player.get_location(),
                            "player misc": self.player.get_misc(),
                            # starting room data
                            "starting room bools": self.starting_room.get_bools(),
                            "starting room items": self.starting_room.get_inventory(),
                            # side/computer room data
                            "side room bools": self.side_room.get_bools(),
                            "side room items": self.side_room.get_inventory(),
                            # main plaza data
                            "main plaza bools": self.main_plaza.get_bools(),
                            "main plaza items": self.main_plaza.get_inventory(),
                            # small den data
                            "small den items": self.small_den.get_inventory(),
                            "small den bools": self.small_den.get_bools(),
                            # west wing data
                            "west wing items": self.west_wing.get_inventory(),
                            "west wing bools": self.west_wing.get_bools(),
                            # cemetery data
                            "cemetery items": self.cemetery.get_inventory(),
                            "cemetery bools": self.cemetery.get_bools(),
                            # toy shop data
                            "toy shop items": self.toy_shop.get_inventory(),
                            "toy shop bools": self.toy_shop.get_bools(),
                            # pet shop data
                            "pet shop items": self.toy_shop.get_inventory(),
                            "pet shop bools": self.toy_shop.get_bools(),
                            # bathroom data
                            "bathroom items": self.bathroom.get_inventory(),
                            "bathroom bools": self.bathroom.get_bools(),
                            # animal den data
                            "animal den items": self.animal_den.get_inventory(),
                            "animal den bools": self.animal_den.get_bools(),
                            # upstairs hallway data
                            "upstairs hallway items": self.up_stairs_hallway.get_inventory(),
                            "upstairs hallway bools": self.up_stairs_hallway.get_bools(),
                            # shoe store data
                            "shoe store items": self.shoe_store.get_inventory(),
                            "shoe store bools": self.shoe_store.get_bools(),
                            # basement entryway data
                            "basement entry items": self.basement_entryway.get_inventory(),
                            "basement entry bools": self.basement_entryway.get_bools(),
                            # basement generator room data
                            "basement gen items": self.basement_gen_room.get_inventory(),
                            "basement gen bools": self.basement_gen_room.get_bools(),
                            "basement gen inv": self.basement_gen_room.get_gen_inventory()
                            }
        try:
            # writes data to save file with pickle
            with open("save game", 'wb+') as db_file:
                pickle.dump(value_dictionary, db_file)
        except IOError:
            print("Could not open file for saving...")

    # general actions that can be done anywhere
    def general_actions(self, action):

        # finds player location
        loc_name = self.switcher_dictionary.get(self.player.get_location(), None)
        if loc_name is None:
            print("no matching location found, defaulting to bunker.")
            loc_name = self.starting_room

        # splits the input on the first space
        general_list = action.split(" ", 1)
        try:
            # prints inventory
            if action == "inv":
                self.player.check_inventory()
            # prints actions that can be taken
            elif action == "help":
                print_help()
            # ends game
            elif action == "save":
                print("Game has been saved!")
                self.save_game_state()
            # prints score
            elif action == "score":
                self.player.print_score()
            # in case input is blank
            elif action == "":
                print("Vern taps his foot on the ground. \n'I get so sick of waiting for something to happen.'")
            # ends game asks to save
            elif action == "end":
                save = input("Save game? ").lower()
                if save == 'y':
                    print('Saved!')
                    self.save_game_state()
                input("Press enter to quit. Goodbye!")
                self.player.set_location(self.end_name)

            # looks at player map
            elif general_list[0] == "look" and general_list[1] == "map":
                self.player.look_player_map()
            # looks at self
            elif general_list[0] == "look" and general_list[1] == "self":
                self.player.look_self()
        except IndexError:
            pass
        # gets an item from the current room
        if general_list[0] == "get":
            try:
                self.get_items(loc_name, general_list[1])
            except IndexError:
                print("Get what?")
        # drops item to current room
        elif general_list[0] == "drop":
            try:
                # if player tries to drop self print message.
                if general_list[1] != 'self':
                    self.drop_items(loc_name, general_list[1])
                else:
                    print("Now how would I do that?")
            except IndexError:
                print("Drop what?")
        elif general_list[0] == "com":
            # tries to combine items
            choice_list = self.combine_pattern.split(action)
            try:
                choice_list.remove('')
            except ValueError:
                pass
            try:
                # if the player makes the drugged meat it increases your score
                if self.player.combine_items(choice_list[0], choice_list[1]):
                    self.player.increase_score()

            except IndexError:
                print("Combine what with what?")

    # commands for bunker area
    def starting_area(self, player_choice):
        # looking at things
        p_list = player_choice.split(" ", 1)
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.starting_room.print_description_room()
                elif "box" in p_list[1]:
                    self.starting_room.print_description_box()
                elif "robot" in p_list[1]:
                    self.starting_room.look_robot()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("Look at what?")

        # opens door
        elif p_list[0] == "oper":
            try:
                if p_list[1] == "door":
                    self.starting_room.open_door()
                else:
                    print("I can't use that.")
            except IndexError:
                print("Operate what?")

        # player fixing objects
        elif p_list[0] == "use":
            # using fuse to fix door
            choice_list = self.use_pattern.split(player_choice)
            try:
                choice_list.remove('')
            except ValueError:
                pass
            try:
                # attempt to fix fuse box
                if "box" in choice_list[1]:
                    if choice_list[0] in self.player.inventory:
                        if self.starting_room.fix_fuse_box(choice_list[0]):
                            self.player.use_item(choice_list[0])
                            self.player.increase_score()
                    else:
                        print(f"I don't have a(n) {choice_list[0]}")

                # attempt to fix robot
                elif "robot" in choice_list[1]:
                    if choice_list[0] in self.player.inventory:
                        if self.starting_room.fix_robot(choice_list[0]):
                            self.player.use_item(choice_list[0])
                            self.player.increase_score()
                    else:
                        print(f"I don't have a(n) {choice_list[0]}")
                else:
                    print(f"I can't do anything to {choice_list[1]}")

            except IndexError:
                print("Use what with what?")

        # allows the player to leave
        elif p_list[0] == "go":
            try:
                if p_list[1] == "outside" or "plaza" in p_list[1]:
                    if self.starting_room.go_outside():
                        self.player.set_location("outside")
                elif "side" in p_list[1]:
                    print("What a small room.")
                    self.player.set_location("side room")
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

    # actions for the side room
    def side_area(self, player_choice):
        # looking at things
        p_list = player_choice.split(" ", 1)
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.side_room.print_description_room()
                elif "pc" in p_list[1] or "computer" in p_list[1]:
                    self.side_room.print_description_computer()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("Look at what?")

        # player using things
        elif p_list[0] == "oper":
            try:
                if "light" in p_list[1] or "switch" in p_list[1]:
                    if not self.side_room.light_switch:
                        self.player.increase_score()
                    self.side_room.turn_on_switch()
                elif "pc" in p_list[1] or "computer" in p_list[1]:
                    self.side_room.use_computer()
                else:
                    print("I can't operate that.")
            except IndexError:
                print("Operate what?")

        # allows the player to leave
        elif p_list[0] == "go":
            try:
                if "bunker" in p_list[1]:
                    print("I'm back in the bunker.")
                    self.player.set_location(self.starting_room_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

        # allows the player to use items on objects
        elif p_list[0] == "use":
            choice_list = self.use_pattern.split(player_choice)
            try:
                choice_list.remove('')
            except ValueError:
                pass
            try:
                # place holding in case player attempts to use an item on an object here.
                if choice_list[1] is None:
                    if choice_list[0] in self.player.inventory:
                        pass
                        # if self.starting_room.fix_fuse_box(choice_list[0]):
                        #     self.player.use_item(choice_list[0])
                        #     self.player.increase_score()
                    else:
                        print(f"I don't have a(n) {choice_list[0]}")
                else:
                    print(f"I can't do anything to {choice_list[1]}")

            except IndexError:
                print("Use what with what?")

    # main plaza actions
    def main_plaza_area(self, player_choice):
        p_list = player_choice.split(" ", 1)

        # allows player to look at things
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.main_plaza.print_description_room()
                elif "car" in p_list[1]:
                    self.main_plaza.print_description_car()
                elif "gate" in p_list[1]:
                    self.main_plaza.print_description_door()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to leave
        elif p_list[0] == "go":
            try:
                if p_list[1] == "bunker":
                    self.player.set_location(self.starting_room_name)
                elif "west" in p_list[1]:
                    self.player.set_location(self.west_wing_name)
                elif "up" in p_list[1]:
                    if self.main_plaza.go_upstairs():
                        self.player.set_location(self.up_stairs_hallway_name)

                elif "exit" in p_list[1]:
                    if self.main_plaza.go_exit():
                        self.player.set_location(self.exit_name)

                elif "den" in p_list[1]:
                    self.player.set_location(self.small_den_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

        # allows the player to operate things. Placeholder
        elif p_list[0] == "oper":
            try:
                if p_list[1] is None:
                    pass
                else:
                    print("I can't use that.")
            except IndexError:
                print("Operate what?")

        # allows the player to use items with objects
        elif p_list[0] == "use":
            choice_list = self.use_pattern.split(player_choice)
            try:
                choice_list.remove('')
            except ValueError:
                pass
            try:
                if "gate" in choice_list[1]:
                    if choice_list[0] in self.player.inventory:
                        if self.main_plaza.unlock_gate(choice_list[0]):
                            self.player.use_item(choice_list[0])
                            self.player.increase_score()
                    else:
                        print(f"I don't have a(n) {choice_list[0]}")
                else:
                    print(f"I can't do anything to {choice_list[1]}")

            except IndexError:
                print("Use what with what?")

    # small den actions
    def small_den_area(self, player_choice):
        p_list = player_choice.split(" ", 1)

        # player looking at things
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.small_den.print_description_room()
                elif "animal" in p_list[1]:
                    self.small_den.print_description_animal_body()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if "plaza" in p_list[1] or p_list[1] == "outside":
                    self.player.set_location(self.main_plaza_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

        # allows player to operate things. Placeholder
        elif p_list[0] == "oper":
            try:
                if p_list[1] is None:
                    pass
                else:
                    print("I can't use that.")
            except IndexError:
                print("Operate what?")

        # allows player to use items with objects
        elif p_list[0] == "use":
            choice_list = self.use_pattern.split(player_choice)
            try:
                choice_list.remove('')
            except ValueError:
                pass
            try:
                # asks for knife to get meat from animal.
                if "animal" in choice_list[1]:
                    if choice_list[0] in self.player.inventory:
                        if self.small_den.animal_cutting(choice_list[0]):
                            self.player.increase_score()
                    else:
                        print(f"I don't have a(n) {choice_list[0]}")
                else:
                    print(f"I can't do anything to {choice_list[1]}")

            except IndexError:
                print("Use what with what?")

    # west wing actions
    def west_wing_area(self, player_choice):
        p_list = player_choice.split(" ", 1)

        # player looking at objects
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.west_wing.print_description_room()
                elif "kiosk" in p_list[1]:
                    self.west_wing.print_description_kiosk()
                elif "vend" in p_list[1] or "mach" in p_list[1]:
                    self.west_wing.print_description_vending()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to use items on objects
        elif p_list[0] == "use":
            # attempting to unlock pet store
            choice_list = self.use_pattern.split(player_choice)
            try:
                choice_list.remove('')
            except ValueError:
                pass
            try:
                # using an item on the kiosk
                if "kiosk" in p_list[1]:
                    if choice_list[0] in self.player.inventory:
                        if self.west_wing.unlock_pet_shop(choice_list[0]):
                            self.player.use_item(choice_list[0])
                            self.player.increase_score()
                    else:
                        print(f"I don't have a(n) {choice_list[0]}")

            except IndexError:
                print("Use what with what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if "plaza" in p_list[1] or p_list[1] == "outside":
                    self.player.set_location(self.main_plaza_name)
                elif "toy" in p_list[1]:
                    self.player.set_location(self.toy_shop_name)
                elif "cem" in p_list[1]:
                    self.player.set_location(self.cemetery_name)
                elif "pet" in p_list[1]:
                    if self.west_wing.go_pet_shop():
                        self.player.set_location(self.pet_shop_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

        # allows player to operate things. Placeholder
        elif p_list[0] == "oper":
            try:
                if p_list[1] is None:
                    pass
                else:
                    print("I can't use that.")
            except IndexError:
                print("Operate what?")

    # toy shop actions
    def toy_shop_area(self, player_choice):
        p_list = player_choice.split(" ", 1)

        # allows player to look at things
        if p_list[0] == "look":
            try:
                if "room" in p_list[1]:
                    self.toy_shop.print_description_room()
                elif "shelve" in p_list[1]:
                    self.toy_shop.print_description_shelves()
                elif "crane" in p_list[1]:
                    self.toy_shop.print_description_crane()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if "west" in p_list[1]:
                    self.player.set_location(self.west_wing_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

        # allows player to operate things
        elif p_list[0] == "oper":
            try:
                if "crane" in p_list[1]:
                    self.toy_shop.operate_crane()
                else:
                    print("I can't use that.")
            except IndexError:
                print("Operate what?")

        # allows player to use items on objects
        elif p_list[0] == "use":
            choice_list = self.use_pattern.split(player_choice)
            try:
                choice_list.remove('')
            except ValueError:
                pass
            try:
                if "crane" in choice_list[1]:
                    if choice_list[0] in self.player.inventory:
                        if self.toy_shop.fix_crane(choice_list[0]):
                            self.player.use_item(choice_list[0])
                            self.player.increase_score()
                    else:
                        print(f"I don't have a(n) {choice_list[0]}")
                else:
                    print(f"I can't do anything to {choice_list[1]}")

            except IndexError:
                print("Use what with what?")

    # pet shot actions
    def pet_shop_area(self, player_choice):
        p_list = player_choice.split(" ", 1)

        # allows the player to look at things
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.pet_shop.print_description_room()
                elif "fish" in p_list[1]:
                    self.pet_shop.print_description_fish()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if "west" in p_list[1]:
                    self.player.set_location(self.west_wing_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

        # allows player to operate things
        elif p_list[0] == "oper":
            try:
                if p_list[1] is None:
                    pass
                else:
                    print("I can't use that.")
            except IndexError:
                print("Operate what?")

        # allows player to use items with objects
        elif p_list[0] == "use":
            choice_list = self.use_pattern.split(player_choice)
            try:
                choice_list.remove('')
            except ValueError:
                pass
            try:
                if choice_list[1] is None:
                    if choice_list[0] in self.player.inventory:
                        pass
                        # if self.starting_room.fix_fuse_box(choice_list[0]):
                        #     self.player.use_item(choice_list[0])
                        #     self.player.increase_score()
                    else:
                        print(f"I don't have a(n) {choice_list[0]}")
                else:
                    print(f"I can't do anything to {choice_list[1]}")

            except IndexError:
                print("Use what with what?")

    # cemetery actions
    def cemetery_area(self, player_choice):
        p_list = player_choice.split(" ", 1)

        # allows player to look at things
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.cemetery.print_description_room()
                elif "grave" in p_list[1]:
                    self.cemetery.print_description_graves()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if "west" in p_list[1]:
                    self.player.set_location(self.west_wing_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

        # allows player to operate things. Placeholder
        elif p_list[0] == "oper":
            try:
                if p_list[1] is None:
                    pass
                else:
                    print("I can't use that.")
            except IndexError:
                print("Operate what?")

        # allows player to use items on objects. Placeholder
        elif p_list[0] == "use":
            choice_list = self.use_pattern.split(player_choice)
            try:
                choice_list.remove('')
            except ValueError:
                pass
            try:
                if choice_list[1] == "":
                    if choice_list[0] in self.player.inventory:
                        pass
                        # if self.starting_room.fix_fuse_box(choice_list[0]):
                        #     self.player.use_item(choice_list[0])
                        #     self.player.increase_score()
                    else:
                        print(f"I don't have a(n) {choice_list[0]}")
                else:
                    print(f"I can't do anything to {choice_list[1]}")

            except IndexError:
                print("Use what with what?")

    # upstairs hallway actions
    def up_stairs_hallway_area(self, player_choice):
        p_list = player_choice.split(" ", 1)

        # allows player to look around
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.up_stairs_hallway.print_description_room()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if "den" in p_list[1]:
                    self.player.set_location(self.animal_den_name)
                elif "shoe" in p_list[1]:
                    self.player.set_location(self.shoe_store_name)
                elif "bath" in p_list[1]:
                    self.player.set_location(self.bathroom_name)
                elif "down" in p_list[1] or "plaza" in p_list[1] or p_list[1] == "outside":
                    self.player.set_location(self.main_plaza_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

        # allows player to operate things. Placeholder
        elif p_list[0] == "oper":
            try:
                if p_list[1] is None:
                    pass
                else:
                    print("I can't use that.")
            except IndexError:
                print("Operate what?")

        # allows player to use items on objects. Placeholder
        elif p_list[0] == "use":
            choice_list = self.use_pattern.split(player_choice)
            try:
                choice_list.remove('')
            except ValueError:
                pass
            try:
                if choice_list[1] is None:
                    if choice_list[0] in self.player.inventory:
                        pass
                        # if self.starting_room.fix_fuse_box(choice_list[0]):
                        #     self.player.use_item(choice_list[0])
                        #     self.player.increase_score()
                    else:
                        print(f"I don't have a(n) {choice_list[0]}")
                else:
                    print(f"I can't do anything to {choice_list[1]}")

            except IndexError:
                print("Use what with what?")

    # animal den actions
    def animal_den_area(self, player_choice):
        pass
        p_list = player_choice.split(" ", 1)
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.animal_den.print_description_room()
                elif "animal" in p_list[1]:
                    self.animal_den.print_description_animal()
                elif "hole" in p_list[1]:
                    self.animal_den.print_description_hole()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if "hall" in p_list[1]:
                    self.player.set_location(self.up_stairs_hallway_name)
                elif "hole" in p_list[1]:
                    self.animal_den.enter_hole()
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

        # allows player to operate things. Placeholder
        elif p_list[0] == "oper":
            try:
                if p_list[1] is None:
                    pass
                else:
                    print("I can't use that.")
            except IndexError:
                print("Operate what?")

        # allows player to use items on objects. Placeholder
        elif p_list[0] == "use":
            choice_list = self.use_pattern.split(player_choice)
            try:
                choice_list.remove('')
            except ValueError:
                pass
            try:
                if choice_list[1] is None:
                    if choice_list[0] in self.player.inventory:
                        pass
                        # if self.starting_room.fix_fuse_box(choice_list[0]):
                        #     self.player.use_item(choice_list[0])
                        #     self.player.increase_score()
                    else:
                        print(f"I don't have a(n) {choice_list[0]}")
                else:
                    print(f"I can't do anything to {choice_list[1]}")

            except IndexError:
                print("Use what with what?")

    # bathroom actions
    def bathroom_area(self, player_choice):
        pass
        p_list = player_choice.split(" ", 1)

        # allows player to look at things
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.bathroom.print_description_room()
                elif "mirror" in p_list[1]:
                    self.bathroom.print_description_mirror(self.player.is_mane_brushed())
                elif "graffiti" in p_list[1]:
                    self.bathroom.print_description_graffiti()
                elif "cabinet" in p_list[1]:
                    self.bathroom.print_description_medical()
                elif "dryer" in p_list[1]:
                    self.bathroom.print_description_dryer()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if "hall" in p_list[1]:
                    self.player.set_location(self.up_stairs_hallway_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

        # allows player to operate things. Placeholder
        elif p_list[0] == "oper":
            try:
                if p_list[1] is None:
                    pass
                else:
                    print("I can't use that.")
            except IndexError:
                print("Operate what?")

        # allows player to use things. Placeholder
        elif p_list[0] == "use":
            choice_list = self.use_pattern.split(player_choice)
            try:
                choice_list.remove('')
            except ValueError:
                pass
            try:
                if choice_list[1] is None:
                    if choice_list[0] in self.player.inventory:
                        pass
                        # if self.starting_room.fix_fuse_box(choice_list[0]):
                        #     self.player.use_item(choice_list[0])
                        #     self.player.increase_score()
                    else:
                        print(f"I don't have a(n) {choice_list[0]}")
                else:
                    print(f"I can't do anything to {choice_list[1]}")

            except IndexError:
                print("Use what with what?")

    # shoe store actions
    def shoe_store_area(self, player_choice):
        p_list = player_choice.split(" ", 1)
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.shoe_store.print_description_room()
                elif "ele" in p_list[1]:
                    self.shoe_store.print_description_elevator()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if "hall" in p_list[1]:
                    self.player.set_location(self.up_stairs_hallway_name)
                elif "ele" in p_list[1]:
                    if self.shoe_store.go_elevator():
                        self.player.set_location(self.basement_entryway_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

        # opens door
        elif p_list[0] == "oper":
            try:
                if "ele" in p_list[1]:
                    self.shoe_store.operate_elevator_doors()
                else:
                    print("I can't use that.")
            except IndexError:
                print("Operate what?")

        elif p_list[0] == "use":
            choice_list = self.use_pattern.split(player_choice)
            try:
                choice_list.remove('')
            except ValueError:
                pass
            try:
                if "ele" in choice_list[1]:
                    if choice_list[0] in self.player.inventory:
                        if self.shoe_store.fix_elevator(choice_list[0]):
                            if choice_list[0] == "strong rope":
                                self.player.use_item(choice_list[0])
                                self.player.increase_score()
                            else:
                                self.player.use_item(choice_list[0])
                    else:
                        print(f"I don't have a(n) {choice_list[0]}")
                else:
                    print(f"I can't do anything to {choice_list[1]}")

            except IndexError:
                print("Use what with what?")

    # basement entryway actions
    def basement_entryway_area(self, player_choice):
        p_list = player_choice.split(" ", 1)
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.basement_entryway.print_description_room()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if "up" in p_list[1]:
                    self.player.set_location(self.shoe_store_name)
                elif "gen" in p_list[1]:
                    if self.basement_entryway.go_gen_room():
                        self.player.set_location(self.basement_gen_room_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

        # opens door
        elif p_list[0] == "oper":
            try:
                if "pad" in p_list[1]:
                    self.basement_entryway.entering_code()
                else:
                    print("I can't use that.")
            except IndexError:
                print("Operate what?")

        elif p_list[0] == "use":
            choice_list = self.use_pattern.split(player_choice)
            try:
                choice_list.remove('')
            except ValueError:
                pass
            try:
                if "pad" in choice_list[1]:
                    if choice_list[0] in self.player.inventory:
                        if self.basement_entryway.entering_code(choice_list[0]):
                            self.player.use_item(choice_list[0])
                            self.player.increase_score()
                    else:
                        print(f"I don't have a(n) {choice_list[0]}")
                else:
                    print(f"I can't do anything to {choice_list[1]}")

            except IndexError:
                print("Use what with what?")

    # basement generator actions
    def basement_gen_area(self, player_choice):
        p_list = player_choice.split(" ", 1)
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.basement_gen_room.print_description_room()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if "entry" in p_list[1]:
                    self.player.set_location(self.basement_entryway_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

        # opens door
        elif p_list[0] == "oper":
            try:
                if "gen" in p_list[1]:
                    self.basement_gen_room.operate_generator()
                else:
                    print("I can't use that.")
            except IndexError:
                print("Operate what?")

        elif p_list[0] == "use":
            choice_list = self.use_pattern.split(player_choice)
            try:
                choice_list.remove('')
            except ValueError:
                pass
            try:
                if "gen" in choice_list[1]:
                    if choice_list[0] in self.player.inventory:
                        if self.basement_gen_room.add_item_generator(choice_list[0]):
                            self.player.use_item(choice_list[0])
                            self.player.increase_score()
                    else:
                        print(f"I don't have a(n) {choice_list[0]}")
                else:
                    print(f"I can't do anything to {choice_list[1]}")

            except IndexError:
                print("Use what with what?")

    # a winning game function
    def exit_game(self):
        print("You escaped the mall! You are back with Johnson and Katie.")
        print("Maybe they can explain what happened to you.")
        input("Press enter to end game.\nThank you for playing!")
        self.end_game()

    # a end game function
    def end_game(self):
        self.playing = False


if __name__ == "__main__":
    VernsAdventure()
