import re
import pickle


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

        self.playing = True
        choosing = True
        end_game = False
        while choosing:
            print("Chapter Two: Vern in the Big City")
            player_option = input("Load(L), Start New(S), Quit(Q), or How to play(H)?\n").lower()
            if player_option == "s":
                # Loads defaults in classes for game

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

                    print("Loaded Game.")
                    choosing = False

            # prints instructions
            elif player_option == "H":
                print_help()
