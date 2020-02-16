import pickle

# this file is built to generate custom save games for testing.
value_dictionary = {
    # player data
    "player inventory": ["self", "bag of catnip", "lion plush", "keys"],
    "player score": 2,
    "player bools": False,
    "player location": "outside",
    # starting room data
    "starting room bools": (True, True, True),
    "starting room items": ["bag of catnip"],
    # computer room data
    "side room bools": (True, True),
    "side room items": [],
    # main plaza data
    "main plaza bools": (False, False, False, False),
    "main plaza items": ["strange keys", "map"],
    # small den data
    "small den bools": (False, False),
    "small den items": ["meat"],
    # west wing data
    "west wing bools": (False, False),
    "west wing items": [],
    # cemetery data
    "cemetery items": ["lion plush"],
    "cemetery bools": (False, False),
    # pet shop data
    "pet shop items": ["mane brush"],
    "pet shop bools": (False, False),
    # toy shop data
    "toy shop items": ["fur sample", "toy raygun"],
    "toy shop bools": (False, False),
    # bath room data
    "bathroom items": ["drugs"],
    "bathroom bools": (False, False),
    # animal den data
    "animal den items": ["meat"],
    "animal den bools": (False, False),
    # upstairs hallway data
    "upstairs hallway items": [],
    "upstairs hallway bools": (False, False),
    # shoe store data
    "shoe store items": [],
    "shoe store bools": (False, False)

}


def print_db_file(db):
    if db is None:
        print("nothing to do...")
    else:
        for key in db:
            print(key, " ", db[key])


def save_game_state(data, file_name):
    db_file = open(file_name, 'wb+')
    pickle.dump(data, db_file)
    db_file.close()


def load_game_state(file_name):
    try:
        with open(file_name, 'rb') as db_file:
            pickle_db = pickle.load(db_file)
            return pickle_db
    except FileNotFoundError:
        print("No save games found.")
        return None


if __name__ == "__main__":
    save_game_state(value_dictionary, "save game")
    item_dict = load_game_state("save game")
    print_db_file(item_dict)