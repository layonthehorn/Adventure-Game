from player_class import VernLion
from starting_room_class import StartingRoom
from side_room_class import SideRoom
# from main_plaza import MainPlaza
import re


# getting things
def get_items(room, item):
    item = room.get_item(item)
    player.get_item(item)


def drop_items(room, item):
    if item in player.inventory:
        player_item = player.drop_item(item)
        room.give_item(player_item)
    else:
        print("I don't have a {0} to drop.".format(item))


# function for doing things in the starting room
def starting_area(player_choice, use_pattern):
    # looking at things
    p_list = player_choice.split(" ", 1)
    if p_list[0] == "look":
        if len(p_list) < 2:
            return None
        if p_list[1] == "room":
            starting_room.print_description_room()
        elif p_list[1] == "box":
            starting_room.print_description_box()
        elif p_list[1] == "self":
            player.look_self()
        elif p_list[1] == "robot":
            starting_room.look_robot()
        elif p_list[1] == "map":
            player.look_player_map()
        else:
            print("I don't know where {0} is.".format(p_list[1]))

    # getting things
    elif p_list[0] == "get":
        if len(p_list) < 2:
            return None
        get_items(starting_room, p_list[1])

    # dropping things
    elif p_list[0] == "drop":
        if len(p_list) < 2:
            return None
        drop_items(starting_room, p_list[1])

    # checks inventory
    elif player_choice == "inv":
        player.check_inventory()

    # opens door
    elif p_list[0] == "oper":
        if len(p_list) < 2:
            return None
        if p_list[1] == "door":
            starting_room.open_door()
        else:
            print("I can't use that.")

    elif p_list[0] == "use":
        # using fuse to fix door
        choice_list = use_pattern.split(player_choice)
        choice_list.remove('')
        # print(choice_list)
        if choice_list[0] == "fuse" and choice_list[1] == "box":
            if not starting_room.fuse_box and "fuse" in player.inventory:
                item = player.use_item("fuse")
                starting_room.fix_fuse_box(item)
                player.increase_score()
            elif starting_room.fuse_box:
                print("It's fixed. I don't need to worry about it now.")
        # using fuse to fix robot
        elif choice_list[0] == "wrench" and choice_list[1] == "robot":
            if not starting_room.robot_fixed and "wrench" in player.inventory:
                item = player.use_item("wrench")
                starting_room.fix_robot(item)
                player.increase_score()
            elif starting_room.robot_fixed:
                print("It's loose. I don't need to worry about it now.")
            else:
                print("I can't do that.")
        else:
            print("I can't do that. test")

    # allows the player to leave
    elif p_list[0] == "go":
        if len(p_list) < 2:
            return None
        if p_list[1] == "outside" and starting_room.door_opened:
            player.set_location("outside")
        elif p_list[1] == "side room":
            print("What a small room.")
            player.set_location("side room")
        else:
            print("I can't go to {0}.".format(p_list[1]))


def side_area(player_choice):
    # looking at things
    p_list = player_choice.split(" ", 1)
    if p_list[0] == "look":
        if len(p_list) < 2:
            return None
        if p_list[1] == "room":
            side_room.print_description_room()
        elif p_list[1] == "computer":
            side_room.print_description_computer()
        elif p_list[1] == "map":
            player.look_player_map()
        elif p_list[1] == "self":
            player.look_self()
        else:
            print("I don't know where {0} is.".format(p_list[1]))

    # getting things
    elif p_list[0] == "get":
        if len(p_list) < 2:
            return None
        get_items(side_room, p_list[1])

    # dropping things
    elif p_list[0] == "drop":
        if len(p_list) < 2:
            return None
        drop_items(side_room, p_list[1])

    # checks inventory
    elif player_choice == "inv":
        player.check_inventory()

    elif p_list[0] == "oper":
        if len(p_list) < 2:
            return None
        if p_list[1] == "light switch":
            if not side_room.light_switch:
                player.increase_score()
            side_room.turn_on_switch()
        elif p_list[1] == "computer":
            side_room.use_computer()
        else:
            print("I can't operate that.")

    # allows the player to leave
    elif p_list[0] == "go":
        if len(p_list) < 2:
            return None
        if p_list[1] == "bunker":
            print("I'm back in the bunker.")
            player.set_location("bunker")
        else:
            print("(side)I can't go to {0}.".format(p_list[1]))


# building item lists
player_inventory = []
starting_room_bools = (False, False, False)
starting_room_items = ["fuse", "bag of catnip"]
side_room_bools = [False]
side_room_items = ["wrench"]

# areas of the program
starting_room_name = "bunker"
outside_name = "outside"
side_room_name = "side room"
use_pattern = re.compile(r"^use\s|\swith\s|\son\s")

# building the rooms and player
player = VernLion(player_inventory, starting_room_name)
starting_room = StartingRoom(starting_room_items,starting_room_name,starting_room_bools)
side_room = SideRoom(side_room_items, side_room_name, side_room_bools)

# testing loop
playing = True
print("""You, a young nervous lion wakes up, alone and afraid. Where did your friends go?
You'll have to figure out where you are first and then get to them.""")
while playing:
    if player.get_location() == outside_name:
        print("")
        print("You won for now.")
        nope = input("Press Enter to Quit...")
        break
    print("Verbs look, inv(entory), get, oper(ate), drop, use, go")
    player_choice = input("").lower()
    if player.get_location() == starting_room_name:
        starting_area(player_choice, use_pattern)
        print("")
        continue
    if player.get_location() == side_room_name:
        side_area(player_choice)
        print("")
        continue

