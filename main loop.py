from player_class import VernLion
from starting_room_class import StartingRoom
from side_room_class import SideRoom
from main_plaza import MainPlaza
from small_den import SmallDen
from west_wing import WestWing
import re
import pickle
# these are my imports
# testing changes


class MainGame:
    def __init__(self):

        self.new_value_dictionary = {}
        self.use_pattern = re.compile(r"^use\s|\swith\s|\son\s")

        # building the rooms and player
        self.main_plaza_name = "main plaza"
        self.starting_room_name = "bunker"
        self.side_room_name = "side room"
        self.small_den_name = "small den"
        self.west_wing_name = "west wing"
        # Main classes
        # self.player - The player character class
        # self.starting_room - the bunker room class
        # self.side_room - the computer room to the side of the bunker class
        # self.main_plaza - the area outside the bunker class

        self.ascii_image = """                 ,  ,, ,
           , ,; ; ;;  ; ;  ;
        , ; ';  ;  ;; .-''\\ ; ;
     , ;  ;`  ; ,; . / /8b \\ ; ;
     `; ; .;'         ;,\\8 |  ;  ;
      ` ;/   / `_      ; ;;    ;  ; ;
         |/.'  /0)    ;  ; `    ;  ; ;
        ,/'   /       ; ; ;  ;   ; ; ; ;
       /_   /         ;    ;  `    ;  ;
      `R8P"  .      ;  ; ; ; ;     ;  ;;
      | ;  .:: `     ;; ; ;   `  ;  ;
      `' `--._      ;;  ;;  ; ;   ;   ;
       `-..__..--''   ; ;    ;;   ; ;   ;
                   ;    ; ; ;   ;     ;

"""

    def main_menu(self):
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
                choosing = False
            elif player_option == "L":
                # getting loaded settings
                new_value_dictionary = self.load_game_state("save game")
                if self.new_value_dictionary is None:
                    continue
                # getting saved settings
                # player data
                player_score = new_value_dictionary["player score"]
                player_inventory = new_value_dictionary["player inventory"]
                player_location = new_value_dictionary["player location"]
                player_bools = new_value_dictionary["player bools"]
                # bunker data
                starting_room_bools = new_value_dictionary["starting room bools"]
                starting_room_items = new_value_dictionary["starting room items"]
                # side room data
                side_room_bools = new_value_dictionary["side room bools"]
                side_room_items = new_value_dictionary["side room items"]
                # main plaza data
                main_plaza_bools = new_value_dictionary["main plaza bools"]
                main_plaza_items = new_value_dictionary["main plaza items"]
                # small den data
                small_den_item = new_value_dictionary["small den items"]
                small_den_bools = new_value_dictionary["small den bools"]
                # west wing data
                west_wing_items = new_value_dictionary["west wing items"]
                west_wing_bools = new_value_dictionary["west wing bools"]

                # loading saved settings
                self.player = VernLion(player_inventory, player_location, player_score,player_bools)
                self.starting_room = StartingRoom(starting_room_items, starting_room_bools)
                self.side_room = SideRoom(side_room_items, side_room_bools)
                self.main_plaza = MainPlaza(main_plaza_items, main_plaza_bools)
                self.small_den = SmallDen(small_den_item, small_den_bools)
                self.west_wing = WestWing(west_wing_items, west_wing_bools)
                choosing = False
            else:
                print(self.ascii_image)
                print("Welcome to my game!")
                continue

    # getting things
    def get_items(self, room, item):
        item = room.get_item(item)
        self.player.get_item(item)

    # drops items to a room
    def drop_items(self, room, item):
        if item in self.player.inventory:
            player_item = self.player.drop_item(item)
            room.give_item(player_item)
        else:
            print("I don't have a {0} to drop.".format(item))

    # loading saved game
    def load_game_state(self, file_name):
        try:
            with open(file_name, 'rb') as db_file:
                pickle_db = pickle.load(db_file)
                return pickle_db
        except FileNotFoundError:
            print("No save games found.")
            return None

    # saves games
    def save_game_state(self):
        value_dictionary = {"player inventory": self.player.get_inventory(),
                            "player score": self.player.get_score(),
                            "player location": self.player.get_location(),
                            "player bools": self.player.get_bools(),
                            "starting room bools": self.starting_room.get_bools(),
                            "starting room items": self.starting_room.get_inventory(),
                            "side room bools": self.side_room.get_bools(),
                            "side room items": self.side_room.get_inventory(),
                            "main plaza bools": self.main_plaza.get_bools(),
                            "main plaza items": self.main_plaza.get_inventory(),
                            "small den items": self.small_den.get_inventory(),
                            "small den bools": self.small_den.get_bools(),
                            "west wing items": self.west_wing.get_inventory(),
                            "west wing bools": self.west_wing.get_bools()
                            }
        try:
            with open("save game", 'wb+') as db_file:
                pickle.dump(value_dictionary, db_file)
        except IOError:
            print("Could not open file for saving...")

    # general actions that can be done anywhere
    def general_actions(self, action):
        general_list = action.split(" ", 1)
        # finds player location
        location = self.player.get_location()
        if location == self.starting_room_name:
            loc_name = self.starting_room
        elif location == self.side_room_name:
            loc_name = self.side_room
        elif location == self.main_plaza_name:
            loc_name = self.main_plaza
        elif location == self.small_den_name:
            loc_name = self.small_den
        elif location == self.west_wing_name:
            loc_name = self.west_wing
        else:
            print("no matching location found, defaulting to bunker.")
            loc_name = self.starting_room

        try:
            # prints inventory
            if action == "inv":
                self.player.check_inventory()
            # ends game
            elif action == "save":
                print("Game has been saved!")
                self.save_game_state()
                return "save"
            elif action == "end":
                save = input("Save game? ").lower()
                if save == 'y':
                    print('Saved!')
                    self.save_game_state()
                input("Goodbye!")
                return "end"
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
                self.drop_items(loc_name, general_list[1])
            except IndexError:
                print("Drop what?")

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
                    print("I don't know where {0} is.".format(p_list[1]))
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
                print(choice_list)
                if choice_list[0] == "fuse" and choice_list[1] == "box":
                    if not self.starting_room.fuse_box and "fuse" in self.player.inventory:
                        item = self.player.use_item("fuse")
                        self.starting_room.fix_fuse_box(item)
                        self.player.increase_score()
                    elif self.starting_room.fuse_box:
                        print("It's fixed. I don't need to worry about it now.")
                # using fuse to fix robot
                elif choice_list[0] == "wrench" and choice_list[1] == "robot":
                    if not self.starting_room.robot_fixed and "wrench" in self.player.inventory:
                        item = self.player.use_item("wrench")
                        self.starting_room.fix_robot(item)
                        self.player.increase_score()
                    elif self.starting_room.robot_fixed:
                        print("It's loose. I don't need to worry about it now.")
                    else:
                        print("I can't do that.")
                else:
                    print("I can't do that.")
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
                    print("I can't go to {0}.".format(p_list[1]))
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
                    print("I don't know where {0} is.".format(p_list[1]))
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
                    self.player.set_location("bunker")
                else:
                    print("(side)I can't go to {0}.".format(p_list[1]))
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
                    print("I don't know where {0} is.".format(p_list[1]))
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if p_list[1] == "bunker" and self.starting_room.door_opened:
                    self.player.set_location("bunker")
                elif p_list[1] == "west wing":
                    self.player.set_location("west wing")
                elif p_list[1] == "upstairs":
                    if self.main_plaza.upstairs_unlocked and self.main_plaza.upstairs_opened:
                        self.player.set_location("upstairs")
                    elif not self.main_plaza.upstairs_unlocked:
                        print("It's locked!")
                    elif not self.main_plaza.upstairs_opened:
                        print("Maybe I should open it first...")
                elif p_list[1] == "exit":
                    if self.main_plaza.exit_unlocked and self.main_plaza.exit_opened:
                        self.player.set_location("exit")
                    elif not self.main_plaza.exit_unlocked:
                        print("It's locked!")
                    elif not self.main_plaza.exit_opened:
                        print("Maybe I should open it first...")
                elif p_list[1] == "small den":
                    self.player.set_location("small den")
                else:
                    print("I can't go to {0}.".format(p_list[1]))
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
                    print("I don't know where {0} is.".format(p_list[1]))
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if p_list[1] == "main plaza":
                    self.player.set_location("main plaza")
                else:
                    print("I can't go to {0}.".format(p_list[1]))
            except IndexError:
                print("Go where?")

    # west wing actions
    def west_wing_area(self, player_choice):
        p_list = player_choice.split(" ", 1)
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.west_wing.print_description_room()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print("I don't know where {0} is.".format(p_list[1]))
            except IndexError:
                print("look at what?")

        # allows player to move around
        elif p_list[0] == "go":
            try:
                if p_list[1] == "main plaza":
                    self.player.set_location("main plaza")
                elif p_list[1] == "toy shop":
                    self.player.set_location("toy shop")
                elif p_list[1] == "cemetery":
                    self.player.set_location("cemetery")
                elif p_list[1] == "pet shop":
                    self.player.set_location("pet shop")
                else:
                    print("I can't go to {0}.".format(p_list[1]))
            except IndexError:
                print("Go where?")

    # toy shop actions
    def toy_shop_area(self, player_choice):
        pass

    # pet shot actions
    def pet_shop_area(self, player_choice):
        pass

    # cemetery actions
    def cemetery_area(self, player_choice):
        pass

    # main game loop
    def main_loop(self):
        playing = True
        print("""You, a young nervous lion wakes up, alone and afraid. Where did your friends go?
You'll have to figure out where you are first and then get to them.""")
        while playing:
            print("Verbs look, inv(entory), get, oper(ate), drop, use, go, save, end")
            player_choice = input("").lower()

            # general actions shared by rooms
            result = self.general_actions(player_choice)
            if result == "end":
                break
            elif result == "save":
                continue

            # actions available in some rooms only
            # for bunker
            if self.player.get_location() == self.starting_room_name:
                self.starting_area(player_choice)
                print("")
                continue
            # for computer room
            if self.player.get_location() == self.side_room_name:
                self.side_area(player_choice)
                print("")
                continue
            # for main plaza
            if self.player.get_location() == self.main_plaza_name:
                self.main_plaza_area(player_choice)
                print("")
                continue
            if self.player.get_location() == self.small_den_name:
                self.small_den_area(player_choice)
                print("")
                continue
            if self.player.get_location() == self.west_wing_name:
                self.west_wing_area(player_choice)
                print("")
                continue
            if self.player.get_location() == "exit":
                print("You escaped the mall! You are back with Johnson and Katie.")
                print("Maybe they can explain what happened to you.")
                playing = False
            else:
                print("You entered a un-built place. Ending game...")
                break


if __name__ == "__main__":
    menu = MainGame()
    menu.main_menu()
    menu.main_loop()
