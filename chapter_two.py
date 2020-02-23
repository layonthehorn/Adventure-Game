import re
import pickle
from chapter_two_classes import PlayerClass, ExampleRoom


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
Not Yet built.
""")


class ChapterTwo:
    """This is a text adventure game, chapter two. All that is needed is to initialize it and the game will start."""
    def __init__(self):

        # pattern matching for actions
        self.use_pattern = re.compile(r"^use\s|\swith\s|\son\s")
        self.combine_pattern = re.compile(r"^com\s|\swith\s|\son\s")
        self.save_location = "saves/chapter_two.save"

        # building the rooms and player names
        self.example_name = "example"
        self.exit_name = "exit"
        self.end_name = "end"

        self.playing = True
        choosing = True
        end_game = False
        while choosing:
            print("Chapter Two: Vern in the Big City")
            player_option = input("Load(L), Start New(S), Quit(Q), or How to play(H)?\n").lower()
            if player_option == "s":
                # Loads defaults in classes for game
                self.player = PlayerClass()
                self.example = ExampleRoom()
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
                    # player data
                    self.player = PlayerClass(new_value_dictionary["player inventory"],
                                              new_value_dictionary["player location"],
                                              new_value_dictionary["player score"],
                                              new_value_dictionary["player misc"])

                    # example room data
                    self.example = ExampleRoom(new_value_dictionary["example room items"],
                                               new_value_dictionary["example room bools"])

                    print("Loaded Game.")
                    choosing = False

            # prints instructions
            elif player_option == "H":
                print_help()

        if not end_game:
            self.player_old_room = self.player.get_location()
            self.player_new_room = self.player_old_room
            self.switcher_dictionary = {
                self.example_name: self.example,
            }

            # action dictionary for each of the rooms special actions
            # also holds the end and exit game functions
            self.location_dict = {
                self.example_name: self.example_area,
                self.exit_name: self.exit_game,
                self.end_name: self.end_game
            }

        player_choice = ""
        # main game play loop
        while self.playing and not end_game:

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
            location_actions = self.location_dict.get(p_local, None)

            # if it does not find a room moves them to the main plaza
            if location_actions is None:
                print("You entered a un-built place. Moving to example place.")
                self.player.set_location(self.example_name)
                location_actions = self.example_area
            if p_local != self.end_name and p_local != self.exit_name:
                # runs the players actions in the room they are in

                location_actions(player_choice)

                # finds players new location to see if they changed rooms
                self.player_new_room = self.player.get_location()
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

    # general actions that can be done anywhere
    def general_actions(self, action):

        # finds player location
        loc_name = self.switcher_dictionary.get(self.player.get_location(), None)
        if loc_name is None:
            print("no matching location found, defaulting to bunker.")
            loc_name = self.example

        # splits the input on the first space
        general_list = action.split(" ", 1)
        try:
            # prints inventory
            if action == "inv":
                self.player.check_inventory()
            # prints actions that can be taken
            elif action == "hint":
                self.hint_system()
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

    # saves games
    def save_game_state(self):
        value_dictionary = {
            # player data
            "player inventory": self.player.get_inventory(),
            "player score": self.player.get_score(),
            "player location": self.player.get_location(),
            "player misc": self.player.get_misc(),
            # example room data
            "example room items": self.example.get_inventory(),
            "example room bools": self.example.get_bools()
        }
        try:
            # writes data to save file with pickle
            with open(self.save_location, 'wb+') as db_file:
                pickle.dump(value_dictionary, db_file)
        except IOError:
            print("Could not open file for saving...")

    # a winning game function
    def exit_game(self):
        print("")
        print("")
        self.player.print_score()
        input("")
        self.end_game()

    # a end game function
    def end_game(self):
        self.playing = False

    # hint system for cheaters
    def hint_system(self):
        print("Keep playing for more hints.")

    def example_area(self, player_choice):
        # looking at things
        p_list = player_choice.split(" ", 1)
        if p_list[0] == "look":
            try:
                if p_list[1] == "room":
                    self.example.print_description_room()
                elif p_list[1] != "self" and p_list[1] != "map":
                    print(f"I don't know where {p_list[1]} is.")
            except IndexError:
                print("Look at what?")

        # opens door
        elif p_list[0] == "oper":
            try:
                if p_list[1] == "door":
                    print("testing operating")
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
                        if self.example.testing_using_items(choice_list[0]):
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
                if p_list[1] == "outside":
                    print("tesing going outside.")
                else:
                    print(f"I can't go to {p_list[1]}.")
            except IndexError:
                print("Go where?")
