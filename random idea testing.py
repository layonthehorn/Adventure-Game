def general_actions(self, action):
    # finds player location
    loc_name = self.switcher_dictionary.get(self.player.get_location(), None)
    if loc_name is None:
        print("no matching location found, defaulting to bunker.")
        loc_name = self.example

    # splits the input on the first space
    general_list = action.split(" ", 1)
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
    elif general_list[0] == "look":
        try:
            if general_list[1] == "map":
                self.player.look_player_map()
            # looks at self
            elif general_list[1] == "self":
                self.player.look_self()
            else:
                if not loc_name.get_look_commands(general_list[1]):
                    print(f"I can't look at the {general_list[1]}.")
        except IndexError:
            print("Look at what?")

    # gets an item from the current room
    elif general_list[0] == "get":
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
    elif general_list[0] == "use":
        try:
            pass
        except IndexError:
            print("Use what with what?")
    elif general_list[0] == "oper":
        try:
            pass
        except IndexError:
            print("Operate what?")
    else:
        print(f"I don't know how to {general_list[0]} something.")
