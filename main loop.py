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


# loading saved game
def load_game_state(file_name):
    try:
        with open(file_name, 'rb') as db_file:
            pickle_db = pickle.load(db_file)
            return pickle_db
    except FileNotFoundError:
        return None


class VernsAdventure:
    def __init__(self):

        self.use_pattern = re.compile(r"^use\s|\swith\s|\son\s")
        self.combine_pattern = re.compile(r"^com\s|\swith\s|\son\s")

        # building the rooms and player
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

        choosing = True
        print(self.ascii_image)
        print("Welcome to my game!")
        while choosing:
            player_option = input("Load(L) or Start New(S)?").upper()
            if player_option == "S":
                # leaves defaults
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

                choosing = False
            elif player_option == "L":
                # getting loaded settings
                new_value_dictionary = load_game_state("save game")
                if new_value_dictionary is None:
                    print("No save games found.")
                else:

                    # loading saved settings
                    # player data
                    self.player = VernLion(new_value_dictionary["player inventory"],
                                           new_value_dictionary["player location"],
                                           new_value_dictionary["player score"],
                                           new_value_dictionary["player bools"])
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
                    choosing = False
            else:
                print(self.ascii_image)
                print("Welcome to my game!")
                continue
        # location dictionary
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
            self.bathroom_name: self.bathroom
        }

        # action dictionary
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
            self.exit_name: self.exit_game,
            self.end_name: self.end_game
        }
        player_choice = ""
        print("""You, a young nervous lion wakes up, alone and afraid. Where did your friends go?
You'll have to figure out where you are first and then get to them.""")

        # main game play loop
        while self.playing:
            # if you reach the exit then don't ask for actions from player
            if self.player.location != self.exit_name:
                print("Verbs look, inv(entory), get, oper(ate), com(bine), drop, score, use, go, save, end")
                player_choice = input("").lower()
                # general actions shared by rooms
                self.general_actions(player_choice)

            # gets the room the player is in
            p_local = self.player.get_location()
            location_actions = self.location_dict.get(p_local, None)
            # if it does not find a room moves them to the main plaza
            if location_actions is None:
                print("You entered a un-built place. Moving to main plaza.")
                self.player.set_location(self.starting_room_name)
                location_actions = self.main_plaza_area
            if p_local != self.end_name and p_local != self.exit_name:
                # runs the players actions in the room they are in
                location_actions(player_choice)
                print("")
            elif p_local == self.end_name:
                # ends game after player asks to
                location_actions()
            else:
                # Winning game ending
                location_actions()

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
                            "player bools": self.player.get_bools(),
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
                            "shoe store bools": self.shoe_store.get_bools()
                            }
        try:
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

        general_list = action.split(" ", 1)
        try:
            # prints inventory
            if action == "inv":
                self.player.check_inventory()
            # ends game
            elif action == "save":
                print("Game has been saved!")
                self.save_game_state()
            elif action == "score":
                self.player.print_score()
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
        elif general_list[0] == "drop" and general_list[1] != "self":
            try:
                self.drop_items(loc_name, general_list[1])
            except IndexError:
                print("Drop what?")
        elif general_list[0] == "com":
            # attempting to unlock pet store
            choice_list = self.combine_pattern.split(action)
            try:
                choice_list.remove('')
            except ValueError:
                pass
            try:
                self.player.combine_items(choice_list[0], choice_list[1])

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
                elif p_list[1] == "box":
                    self.starting_room.print_description_box()
                elif p_list[1] == "robot":
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
                if choice_list[1] == "box":
                    if choice_list[0] in self.player.inventory:
                        if self.starting_room.fix_fuse_box(choice_list[0]):
                            self.player.use_item(choice_list[0])
                            self.player.increase_score()
                    else:
                        print(f"I don't have a(n) {choice_list[0]}")

                # attempt to fix robot
                elif choice_list[1] == "robot":
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
                if p_list[1] == "outside" and self.starting_room.door_opened:
                    self.player.set_location("outside")
                elif p_list[1] == "side room":
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
                elif p_list[1] == "computer":
                    self.side_room.print_description_computer()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("Look at what?")

        # player using things
        elif p_list[0] == "oper":
            try:
                if p_list[1] == "light switch":
                    if not self.side_room.light_switch:
                        self.player.increase_score()
                    self.side_room.turn_on_switch()
                elif p_list[1] == "computer":
                    self.side_room.use_computer()
                else:
                    print("I can't operate that.")
            except IndexError:
                print("Operate what?")

        # allows the player to leave
        elif p_list[0] == "go":
            try:
                if p_list[1] == "bunker":
                    print("I'm back in the bunker.")
                    self.player.set_location(self.starting_room_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

    # main plaza actions
    def main_plaza_area(self, player_choice):
        p_list = player_choice.split(" ", 1)
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.main_plaza.print_description_room()
                elif p_list[1] == "car":
                    self.main_plaza.print_description_car()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if p_list[1] == "bunker" and self.starting_room.door_opened:
                    self.player.set_location(self.starting_room_name)
                elif p_list[1] == "west wing":
                    self.player.set_location(self.west_wing_name)
                elif p_list[1] == "upstairs":
                    if self.main_plaza.upstairs_unlocked:
                        self.player.set_location(self.up_stairs_hallway_name)
                    else:
                        print("It's locked!")

                elif p_list[1] == "exit":
                    if self.main_plaza.exit_unlocked:
                        self.player.set_location(self.exit_name)
                    else:
                        print("It's locked!")

                elif p_list[1] == "small den":
                    self.player.set_location(self.small_den_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

    # small den actions
    def small_den_area(self, player_choice):
        p_list = player_choice.split(" ", 1)
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.small_den.print_description_room()
                elif p_list[1] == "animal":
                    self.small_den.print_description_animal_body()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if p_list[1] == "main plaza":
                    self.player.set_location(self.main_plaza_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

    # west wing actions
    def west_wing_area(self, player_choice):
        p_list = player_choice.split(" ", 1)
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.west_wing.print_description_room()
                elif p_list[1] == "kiosk":
                    self.west_wing.print_description_kiosk()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")
        elif p_list[0] == "use":
            # attempting to unlock pet store
            choice_list = self.use_pattern.split(player_choice)
            try:
                choice_list.remove('')
            except ValueError:
                pass
            try:
                # using an item on the kiosk
                if choice_list[1] == "kiosk":
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
                if p_list[1] == "main plaza":
                    self.player.set_location(self.main_plaza_name)
                elif p_list[1] == "toy shop":
                    self.player.set_location(self.toy_shop_name)
                elif p_list[1] == "cemetery":
                    self.player.set_location(self.cemetery_name)
                elif p_list[1] == "pet shop":
                    if self.west_wing.pet_shop_unlocked:
                        self.player.set_location(self.pet_shop_name)
                    else:
                        print("It wants me to unlock it first.")
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

    # toy shop actions
    def toy_shop_area(self, player_choice):
        p_list = player_choice.split(" ", 1)
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.toy_shop.print_description_room()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if p_list[1] == "west wing":
                    self.player.set_location(self.west_wing_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

    # pet shot actions
    def pet_shop_area(self, player_choice):
        p_list = player_choice.split(" ", 1)
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.pet_shop.print_description_room()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if p_list[1] == "west wing":
                    self.player.set_location(self.west_wing_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

    # cemetery actions
    def cemetery_area(self, player_choice):
        p_list = player_choice.split(" ", 1)
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.cemetery.print_description_room()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if p_list[1] == "west wing":
                    self.player.set_location(self.west_wing_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

    # upstairs hallway actions
    def up_stairs_hallway_area(self, player_choice):
        p_list = player_choice.split(" ", 1)
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
                if p_list[1] == "animal den":
                    self.player.set_location(self.animal_den_name)
                elif p_list[1] == "shoe store":
                    self.player.set_location(self.shoe_store_name)
                elif p_list[1] == "bathroom":
                    self.player.set_location(self.bathroom_name)
                elif p_list[1] == "down stairs":
                    self.player.set_location(self.main_plaza_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

    # animal den actions
    def animal_den_area(self, player_choice):
        pass
        p_list = player_choice.split(" ", 1)
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.animal_den.print_description_room()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if p_list[1] == "hallway":
                    self.player.set_location(self.up_stairs_hallway_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

    # bathroom actions
    def bathroom_area(self, player_choice):
        pass
        p_list = player_choice.split(" ", 1)
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.bathroom.print_description_room()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if p_list[1] == "hallway":
                    self.player.set_location(self.up_stairs_hallway_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

    # shoe store actions
    def shoe_store_area(self, player_choice):
        p_list = player_choice.split(" ", 1)
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.shoe_store.print_description_room()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if p_list[1] == "hallway":
                    self.player.set_location(self.up_stairs_hallway_name)
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")

    # a exit game function
    def exit_game(self):
        print("You escaped the mall! You are back with Johnson and Katie.")
        print("Maybe they can explain what happened to you.")
        input("Press enter to end game.\nThank you for playing!")
        self.playing = False

    # a end game function
    def end_game(self):
        self.playing = False


if __name__ == "__main__":
    VernsAdventure()
