import pickle
import re

from chapter_one_classes import PlayerClass, Bunker, ComputerRoom, MainPlaza, SmallDen, WestWing, ToyShop, PetShop, Cemetery, UpstairsHallway, AnimalDen, Bathroom, ShoeStore, BasementEntry, BasementGenRoom


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
          "\noper(ate) {object}: How you use/read objects: doors, computers, etc."
          "\ncom(bine) {item} with/on {item}: allows you to combine items. Use 'self' to use an item on you."
          "\ndrop {item}: Allows you to get rid of an item."
          "\nscore: Allows the player to check current progress in-game."
          "\nuse {item} With/on {item}: how you use things with other things."
          "\ngo {location}: How you change rooms."
          "\nsave: How you save your game."
          "\nend: Exit game and will ask to save or not."
          "\nhint: This will give you a hint on how to continue."
          "\nhelp: This menu.")


def print_intro():
    print("""
You wake up, alone and afraid in an old fallout shelter, built some time in the past, but abandoned 
long ago. It appears a group had set themselves up here before the end, judging by the things that were left 
behind. The room smells of mould and rust. There is a disabled robot in the corner, an entry to a smaller 
room and there is a door that appears to be locked.
""")


class ChapterOne:
    """This is a text adventure game, chapter one. All that is needed is to initialize it and the game will start."""
    def __init__(self):

        # pattern matching for actions
        self.use_pattern = re.compile(r"^use\s|\swith\s|\son\s")
        self.combine_pattern = re.compile(r"^com\s|\swith\s|\son\s")
        self.save_location = "saves/chapter_one.save"

        # building the rooms and player names
        self.player_name = "player"
        self.main_plaza_name = "plaza"
        self.starting_room_name = "bunker"
        self.side_room_name = "side room"
        self.small_den_name = "small den"
        self.west_wing_name = "west wing"
        self.cemetery_name = "cemetery"
        self.toy_shop_name = "toy shop"
        self.pet_shop_name = "pet shop"
        self.exit_name = "exit"
        self.end_name = "end"
        self.up_stairs_hallway_name = "upstairs hallway"
        self.animal_den_name = "animal den"
        self.shoe_store_name = "shoe store"
        self.bathroom_name = "bathroom"
        self.basement_entryway_name = "basement entry"
        self.basement_gen_room_name = "basement generator room"
        self.playing = True

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
        end_game = False
        while choosing:
            print("Chapter One: The Lost Mall")
            player_option = input("Load(L), Start New(S), Quit(Q), or How to play(H)?\n").lower()
            if player_option == "s":
                # Loads defaults in classes for game
                self.player = PlayerClass()
                self.starting_room = Bunker()
                self.side_room = ComputerRoom()
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
                self.basement_entryway = BasementEntry()
                self.basement_gen_room = BasementGenRoom()
                print_intro()
                choosing = False
            elif player_option == "q":
                choosing = False
                end_game = True
            elif player_option == "l":
                # getting loaded settings
                new_value_dictionary = load_game_state(self.save_location)
                # if the dictionary is none it can not load a game
                if new_value_dictionary is None:
                    print("No save games found.")
                else:

                    # loading saved settings for classes
                    # player data
                    self.player = new_value_dictionary.get(self.player_name)
                    # bunker data
                    self.starting_room = new_value_dictionary.get(self.starting_room_name)
                    # side room data
                    self.side_room = new_value_dictionary.get(self.side_room_name)
                    # main plaza data
                    self.main_plaza = new_value_dictionary.get(self.main_plaza_name)
                    # small den data
                    self.small_den = new_value_dictionary.get(self.small_den_name)
                    # west wing data
                    self.west_wing = new_value_dictionary.get(self.west_wing_name)
                    # cemetery data
                    self.cemetery = new_value_dictionary.get(self.cemetery_name)
                    # toy shop data
                    self.toy_shop = new_value_dictionary.get(self.toy_shop_name)
                    # pet shop data
                    self.pet_shop = new_value_dictionary.get(self.pet_shop_name)
                    # upstairs hallway data
                    self.up_stairs_hallway = new_value_dictionary.get(self.up_stairs_hallway_name)
                    # animal den data
                    self.animal_den = new_value_dictionary.get(self.animal_den_name)
                    # bathroom data
                    self.bathroom = new_value_dictionary.get(self.bathroom_name)
                    # shoe store data
                    self.shoe_store = new_value_dictionary.get(self.shoe_store_name)
                    # basement entryway data
                    self.basement_entryway = new_value_dictionary.get(self.basement_entryway_name)
                    # basement generator room data
                    self.basement_gen_room = new_value_dictionary.get(self.basement_gen_room_name)

                    # tells player it loaded the game
                    print("Loaded Game.")
                    print(f"You are in the {self.player.get_location()} area.")
                    choosing = False

            # prints instructions
            elif player_option == "H":
                print_help()

        # location dictionary
        # used for general actions to run player actions in any room.
        # if the player is going to actually play builds rest of game
        if not end_game:
            self.player_old_room = self.player.get_location()
            self.player_new_room = self.player_old_room
            self.switcher_dictionary = {
                # player only here for saving
                self.player_name: self.player,
                # rest here for saving and getting rooms
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

        # main game play loop
        while self.playing and not end_game:

            # if the generator is working and the exit is locked it opens the exit.
            if self.basement_gen_room.is_generator_working():
                if not self.main_plaza.is_exit_unlocked():
                    self.main_plaza.unlock_exit()

            # if they reached a new room announce it
            if self.player_old_room != self.player_new_room:
                print(f"You have gone to the {self.player_new_room}.")
                self.player_old_room = self.player_new_room

            # if you reach the exit then don't ask for actions from player
            if self.player.location != self.exit_name:
                print("Verbs look, inv(entory), get, oper(ate), com(bine), drop, score, use, go, save, end, help")
                player_choice = input("").lower()
                # general actions shared by rooms
                self.general_actions(player_choice)

            # gets the room the player is in
            p_local = self.player.get_location()
            if p_local != self.end_name and p_local != self.exit_name:

                # if the player is in the animal den it checks if it needs to run the
                # checking if they placed the meat in the animal den
                if p_local == self.up_stairs_hallway_name:
                    result = self.animal_den.drug_animal()
                    if result == "meat":
                        self.small_den.give_item("meat")
                    elif result == "drugged":
                        self.player.increase_score()

                # finds players new location to see if they changed rooms
                self.player_new_room = self.player.get_location()
                print("")
            elif p_local == self.end_name:
                # ends game after player asks to
                self.end_game()
            else:
                # Winning game ending
                self.exit_game()

    # saves games
    def save_game_state(self):

        try:
            # writes data to save file with pickle
            with open(self.save_location, 'wb+') as db_file:
                pickle.dump(self.switcher_dictionary, db_file)
        except IOError:
            print("Could not open file for saving...")

    # general actions that can be done anywhere
    def general_actions(self, action):
        # finds player location
        # this makes all your actions dependent on the room you are in
        loc_name = self.switcher_dictionary.get(self.player.get_location(), None)
        # if you reach an unbuilt area or somehow retrieve the player class
        if loc_name is None or self.player.get_location() == self.player_name:
            print("no matching location found, defaulting to bunker.")
            loc_name = self.starting_room
            self.player.set_location(self.starting_room_name)

        # splits the input on the first space
        general_list = action.split(" ", 1)
        # prints inventory
        if action == "inv":
            self.player.check_inventory()
        elif action == "hint":
            self.hint_system()
        # prints help page
        elif action == "help":
            print_help()
        # saves the game
        elif action == "save":
            print("Game has been saved!")
            self.save_game_state()
        # prints score
        elif action == "score":
            self.player.print_score()
        # in case input is blank
        elif action == "":
            print("Vern taps his foot on the ground. \n'I get so sick of waiting for something to happen.'")
        # ends game and asks to save
        elif action == "end":
            save = input("Save game? ").lower()
            if save == 'y':
                print('Saved!')
                self.save_game_state()
            input("Press enter to quit. Goodbye!")
            self.player.set_location(self.end_name)

        # looking at things
        elif general_list[0] == "look":
            try:
                if general_list[1] == "map":
                    self.player.look_player_map()
                # looks at self
                elif general_list[1] == "self":
                    self.player.look_self()
                else:
                    loc_name.get_look_commands(general_list[1], self.player.is_mane_brushed())
            except IndexError:
                print("Look at what?")

        # gets an item from the current room
        elif general_list[0] == "get":
            try:
                if general_list[1] in loc_name.get_inventory():
                    self.player.get_item(loc_name.get_item(general_list[1]))
                else:
                    print(f"There isn't a(n) {general_list[1]} to get.")
            except IndexError:
                print("Get what?")

        # drops item to current room
        elif general_list[0] == "drop":
            try:
                # if player tries to drop self print message.
                if general_list[1] != 'self':
                    if general_list[1] in self.player.get_inventory():
                        loc_name.give_item(self.player.drop_item(general_list[1]))
                    else:
                        print(f"I don't have a(n) {general_list[1]} to drop.")
                else:
                    print("Now how would I do that?")
            except IndexError:
                print("Drop what?")

        # combining items
        elif general_list[0] == "com":
            # tries to combine items
            choice_list = self.combine_pattern.split(action)
            try:
                choice_list.remove('')
            except ValueError:
                pass
            try:
                if self.player.combine_items(choice_list[0], choice_list[1]):
                    self.player.increase_score()

            except IndexError:
                print("Combine what with what?")

        # using items on objects
        elif general_list[0] == "use":
            try:
                choice_list = self.use_pattern.split(action)
                if '' in choice_list:
                    choice_list.remove('')
                loc_name.get_use_commands(self.player, choice_list)
            except IndexError:
                print("Use what with what?")

        # operating objects
        elif general_list[0] == "oper":
            try:
                loc_name.get_oper_commands(general_list[1], self.player.is_mane_brushed())

            except IndexError:
                print("Operate what?")

        # going to new areas.
        elif general_list[0] == "go":
            try:
                loc_name.get_go_commands(self.player, general_list[1])
            except IndexError:
                print("Go where?")
        else:
            print(f"I don't know how to {general_list[0]}.")

    # a winning game function
    def exit_game(self):
        print("You escaped the mall! You are back with Johnson and Katie.")
        print("Maybe they can explain what happened to you.")
        self.player.print_score()
        input("Press enter to end game.\nThank you for playing!")
        self.end_game()

    # a end game function
    def end_game(self):
        self.playing = False

    # hint system for cheaters
    def hint_system(self):
        if not self.starting_room.robot_fixed:
            print("You should find a way to get that fuse loose.")
        elif not self.starting_room.fuse_box:
            print("Keep playing for more hints.")
        elif not self.starting_room.door_opened:
            print("Keep playing for more hints.")
        elif not self.main_plaza.car_looked:
            print("You should look over that car.")
        elif not self.toy_shop.crane_fixed:
            print("Keep playing for more hints.")
        elif not self.toy_shop.crane_won:
            print("Keep playing for more hints.")
        elif not self.main_plaza.upstairs_unlocked:
            print("Maybe you have some keys that would help you now.")
        elif not self.small_den.animal_cut:
            print("Getting some meat would be a good idea.")
        elif not self.bathroom.cabinet_looked:
            print("Keep playing for more hints.")
        elif not self.animal_den.animal_drugged:
            print("Maybe place that meat somewhere?")
        elif not self.west_wing.pet_shop_unlocked:
            print("What can you use to unlock the pet store?")
        elif not self.cemetery.found_rope:
            print("Keep playing for more hints.")
        elif not self.pet_shop.rope_fixed:
            print("What is like a leash?")
        elif not self.shoe_store.elevator_opened:
            print("Keep playing for more hints.")
        elif not self.shoe_store.elevator_roped:
            print("What would help with getting down long falls?")
        elif not self.basement_entryway.door_unlocked:
            print("There's a code somewhere, or you could try and fry the lock.")
        elif len(self.basement_gen_room.get_gen_inventory()) < 4:
            print("You need to get four fuses to fix the generator")
            print("Check around the other places you have been before.")
        elif self.main_plaza.exit_unlocked:
            print("The exit is open now.")
        else:
            print("Keep playing for more hints.")


if __name__ == "__main__":
    ChapterOne()
