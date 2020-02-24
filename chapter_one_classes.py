import time


# function class for inheritance.
class FunctionClass:
    """Never to be called. Only used for giving all other classes the same methods."""

    # allows getting a print function form the look dictionary.
    def get_look_commands(self, look_at):
        # you have to enter at least three letters
        if len(look_at) >= 3:
            if len(self.look_dict) < 1:
                print(f"I can't look at {look_at}.")
            else:
                for key in self.look_dict:
                    if look_at in key:
                        look_command = self.look_dict.get(key)
                        look_command()
                        break
                else:
                    print(f"I can't look at {look_at}.")

        else:
            print(f"I can't go to {look_at}.")

    # allows getting operate commands
    def get_oper_commands(self, operate, player_bool):
        # you have to enter at least three letters
        if len(operate) >= 3:
            if len(self.oper_dict) < 1:
                print(f"I can't operate the {operate}.")
            else:
                for key in self.oper_dict:
                    if operate in key:
                        oper_command = self.oper_dict.get(key)
                        try:
                            oper_command()
                        except TypeError:
                            oper_command(player_bool)
                        break
                else:
                    print(f"I can't operate the {operate}.")
        else:
            print(f"I can't operate the {operate}.")

    # allows getting go commands
    def get_go_commands(self, player_object, go):
        # you have to enter at least three letters
        if len(go) >= 2:
            if len(self.go_dict) < 1:
                print(f"I can't go to {go}.")
            else:
                for key in self.go_dict:
                    if go in key:
                        go_command = self.go_dict.get(key)
                        go_command(player_object)
                        break
                else:
                    print(f"I can't go to {go}.")
        else:
            print(f"I can't go to {go}.")

    # allows using item on objects
    def get_use_commands(self, player_object, use_list):
        item = use_list[0]
        room_object = use_list[1]
        # you have to enter at least three letters
        if len(room_object) >= 3:
            if len(self.use_dict) < 1:
                print(f"I can't find the {room_object}.")
            for key in self.use_dict:
                if room_object in key:
                    use_command = self.use_dict.get(key)
                    if use_command(item):
                        player_object.use_item(item)
                        player_object.increase_score()
                    break
            else:
                print(f"I can't find the {room_object}.")
        else:
            print(f"What is a(n) {room_object}.")

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # returns item to room
    def get_item(self, item):
        location = self.inventory.index(item)
        return self.inventory.pop(location)

    # dropping item back into room
    def give_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)


# Player Class
class PlayerClass:
    """This is the main player class. It holds the player inventory and score among other things."""

    def __init__(self, player_inventory=None, player_start="bunker", score=0, player_misc=(False, 0)):

        if player_inventory is None:
            player_inventory = ["self"]

        self.inventory = player_inventory
        self.location = player_start
        self.player_score = score
        self.mane_brushed, self.fish_counter = player_misc

        self.map_of_building = """
          ---------MAP----------
                                               +--------------------+
                   SS                          |Legend:             |
                   ||                          |                    |
               AD--UP--RR                      |Main Plaza: MP      |
            C   SD ||                          |Upper Hall: UH      |
            ||   \\\\||                          |Pet Shop: PS        |
        PS--WW-----MP----EXIT                  |Shoe Store: SS      |
            ||     ||                          |Restroom: RR        |
            TS     FS--CR                      |Animal Den: AD      |
                                               |Small Den: SD       |
                                               |West wing: WW       |
                                               |Toy Shop: TS        |
                                               |Cemetery: C         |
                                               |Fallout Shelter: FS |
                                               |Computer Room: CR   |
                                               |                    |
                                               +--------------------+  
               """
        self.item_dictionary = {
            "wrench": "Used for unstucking random things. Always handy with robots.",
            "fuse": "Lots of old world tech uses this to keep power flowing.",
            "bag of catnip": "Hey now. You need to stay sober.",
            "lion plush": "A cute lion plush. I wonder who left this here?",
            "keys": "These might be handy for reaching high places.",
            "strange keys": "For some reason you recognise them. Maybe they belong to a friend?",
            "meat": "Maybe something will want this?",
            "toy raygun": "It's flashing random colors. Not useful but fun!",
            "knife": "It cuts. I mean what else do you think it does?",
            "fur sample": "It's fur. Maybe you could use it to get in the pet store?",
            "map": "A map to the mall! Someone must have updated it recently.",
            "drugged meat": "This would knockout anything that eats it.",
            "battery": "This could be used to power something, or overpower it.",
            "mane brush": "You could use this on your mane. Not that you ever need it.",
            "self": "It's you... You should not see this item in your inventory. Please report it!",
            "cheetah keyring": "It's a cheetah keyring. Cute but not really useful to you right now.",
            "cat toy": "A lion plush stuff with catnip. You druggie...",
            # in toy shop
            "red fuse": "It's a red fuse. Much larger than the one from the bunker.",
            # in side room
            "green fuse": "It's a green fuse. Much larger than the one from the bunker.",
            # in cemetery
            "gold fuse": "It's a gold fuse. Much larger than the one from the bunker.",
            # in ?
            "blue fuse": "It's a blue fuse. Much larger than the one from the bunker.",
            "fish": "A very tasty if small fish. Should you?.. Eat it?",
            "bones": "Bones are all that's left of the little fish you ate. How could you?",
            "rope": "A length of rope. Might be useful to get somewhere lower.",
            "long rope": "A long length of rope. This should reach the bottom.",
            "soda": "An old flat soda. Not something you want to drink.",
            "shovel": "It's an old entrenching tool. Useful for digging and many other things.",
            "soldering iron": "It's used to repair wires and circuits.",
            "soldering wire": "Used to fix circuits and connections.",
            "capacitor": "A part to a circuit board, might be handy.",
            "circuit board": "A repaired part to a machine somewhere.",
            "toy lion tail": "A toy tail for a child to wear. I guess even humans wanted to be lions...",
            "owl figurine": "A nice little owl toy. Has hoot hoot written on the bottom.",
            "coin": "Useful for just about nothing now that the human world has fallen.",
            "screw driver": "Useful for taking things apart and also breaking them open."
        }

    # returns his location
    def get_location(self):
        return self.location

    # returns a list of his inventory
    def get_inventory(self):
        return self.inventory

    def get_misc(self):
        return self.mane_brushed, self.fish_counter

    # returns the players score for saving
    def get_score(self):
        return self.player_score

    # prints your score
    def print_score(self):
        print(f"Your score is {self.player_score}.")

    # sets player score
    def increase_score(self):
        print("Your score went up!")
        self.player_score += 1

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
                    print("{:20}{:<5}".format(item, self.item_dictionary.get(item, "Error, Report me pls!")))

    # allows getting items into his inventory
    def get_item(self, item):

        if item in self.inventory:
            print("I don't need more of these.")
        else:
            self.inventory.append(item)
            print("I picked up the ", item)

    # returns if your mane has been brushed
    def is_mane_brushed(self):
        return self.mane_brushed

    # allows changing his location
    def set_location(self, room):
        self.location = room

    # getting item out of inventory
    def drop_item(self, item):
        if item in self.inventory:
            location = self.inventory.index(item)
            print("I dropped the ", item)
            return self.inventory.pop(location)

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
            if "meat" in item_list and "drugs" in item_list:
                self.inventory.remove(item_1)
                self.inventory.remove(item_2)
                self.inventory.append("drugged meat")
                print("I made drugged meat. Still nasty after that.")
                return True
            elif "lion plush" in item_list and "bag of catnip" in item_list:
                self.inventory.remove(item_1)
                self.inventory.remove(item_2)
                self.inventory.append("cat toy")
                print("I am so ashamed of myself for this...")
                return False
            # all using items on self reactions
            elif "self" in item_list and "cat toy" in item_list:
                self.inventory.remove("cat toy")
                print("purrrrr Mmmmm catnip.")
                return False
            elif "self" in item_list and "mane brush" in item_list:
                self.inventory.remove("mane brush")
                print("Hey, I'm looking better now. That's good too.")
                self.mane_brushed = True
                return True
            elif "self" in item_list and "drugs" in item_list:
                print("I'm not eating them...")
                return False
            elif "self" in item_list and "meat" in item_list:
                print("Nasty. I love meat but this is not appetizing at all.")
                return False
            elif "self" in item_list and "drugged meat" in item_list:
                print("Eating rotten meat is not any safer with medication in it.")
                return False
            elif "self" in item_list and "soda" in item_list:
                print("I hate sugary things...")
                return False
            elif "self" in item_list and "bag of catnip" in item_list:
                print("I need to stay sober right now... \nIf it was in a little cute toy I might... No, I better not.")
                return False
            elif "self" in item_list and "knife" in item_list:
                print("I don't think that's a great plan...")
                return False
            elif "self" in item_list and "toy lion tail" in item_list:
                print("I already have a tail thank you. Might save this for my daughter though.")
                return False

            # small thing for player repeating the eat fish command
            elif "self" in item_list and "fish" in item_list:
                if self.fish_counter == 0:
                    print("I really shouldn't. Though it is tasty looking...")
                    self.fish_counter += 1
                    return False
                elif self.fish_counter == 1:
                    print("Still shouldn't eat it.")
                    self.fish_counter += 1
                    return False
                elif self.fish_counter == 2:
                    print("No, I need to get rid of it. I keep getting temped.")
                    self.fish_counter += 1
                    return False
                else:
                    print("Vern finally gives in and eats the little fish.")
                    print("Oh no! I couldn't resist anymore...")
                    print("Now all I have is a pile of bones.")
                    self.inventory.append("bones")
                    self.inventory.remove("fish")
                    return True
            # no matches found
            else:
                print(f"I can't combine {item_1} and {item_2}.")
                return False

        # No matching items found
        else:
            print("I don't have all I need")
            return False

    # looking at map
    def look_player_map(self):
        if "map" in self.inventory:
            print("Let me check my map.\n*Map crinkling sounds.*")
            time.sleep(1.5)
            print(self.map_of_building)
        else:
            print("I don't have one.")

    # looking at self
    def look_self(self):
        print("A nervous lion is what you are. Somehow still alive but for how long? Hopefully long enough.")
        if "meat" in self.inventory or "drugged meat" in self.inventory:
            print("This meat smells awful...")
        if self.mane_brushed:
            print("At least I'm cleaned up now.")


# Bunker Areas
class Bunker(FunctionClass):
    """This is the bunker class. It acts as the starting room for the player."""

    def __init__(self, items_contained=None, bool_list=(False, False, False)):
        if items_contained is None:
            items_contained = ["fuse"]
        self.inventory = items_contained
        self.fuse_box, self.door_opened, self.robot_fixed = bool_list
        self.look_dict = {
            "room": self.print_description_room,
            "fuse box": self.print_description_box,
            "exit door": self.print_description_door
        }

        self.go_dict = {
            "side room": self.go_sideroom,
            "outside": self.go_outside
        }
        self.oper_dict = {
            "door": self.open_door
        }

        self.use_dict = {
            "robot": self.fix_robot,
            "fuse box": self.fix_fuse_box
        }

    def get_bools(self):
        return self.fuse_box, self.door_opened, self.robot_fixed

    # this prints a description along with a item list
    def print_description_room(self):
        print("The room is dark and blasted out.")
        print("The room smells of mould and rust. There is a disabled 'robot' in the corner, an entry to \na side room "
              "\nand there is a 'door' that appears to be locked. Maybe it’s connected to that fuse 'box'?.")
        if self.door_opened:
            print("The door to 'outside' is open.")
        else:
            print("There is a old 'door' and a odd 'box' next to it.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    # this prints a description of the fuse box
    def print_description_box(self):
        if not self.fuse_box:
            print("It's an old fuse box....")
            time.sleep(1)
            print("And of course it's lacking a fuse.")
        else:
            print("Hey, it's working now!")

    def print_description_door(self):
        print("It's an old bunker door. Looks like it has a power lock.")
        if not self.fuse_box:
            print("I need to find a way to power it.")
        elif not self.door_opened:
            print("I need to open it I think now that it has power again.")
        else:
            print("I hope it stays working as long as I need it.")

    def look_robot(self):
        if not self.robot_fixed:
            print("It's a robot and it has a fuse!")
        elif 'fuse' in self.inventory and self.robot_fixed:
            print("I can get the fuse now.")
        else:
            print("I took the robots fuse.")

    # this pops off the items and returns it
    def get_item(self, item):

        if not self.robot_fixed and item == "fuse":
            print("The fuse is stuck. I need to get it loose first.")
            return None
        elif item in self.inventory:
            location = self.inventory.index(item)
            return self.inventory.pop(location)
        else:
            return None

    def go_outside(self, player_object):
        if self.door_opened:
            player_object.set_location("plaza")
        elif self.fuse_box and not self.door_opened:
            print("I need to open the door first.")
        elif not self.fuse_box:
            print("I need to power the door and open it first.")

    @staticmethod
    def go_sideroom(player_object):
        player_object.set_location("side room")

    # attempts to fix fuse box
    def fix_fuse_box(self, item):
        if not self.fuse_box:
            if item == "fuse":
                print("the fuse box is now working!")
                self.fuse_box = True
                return True
            else:
                print(f"I can't use {item} with the fuse box.")
                return False
        else:
            print("There is nothing else I need to do here.")
            return False

    # used to get fuse loose from robot
    def fix_robot(self, item):
        if not self.robot_fixed:
            if item == "wrench":
                print("The robot's fuse is loose!")
                self.robot_fixed = True
                return True
            else:
                print(f"I can't use {item} with the robot.")
                return False
        else:
            print("I don't have to mess with it anymore.")
            return False

    # tries to open door will fail if fuse box is not working.
    def open_door(self):
        if not self.fuse_box:
            print("The door is stuck. Looks like it's out of power.")
        elif self.door_opened:
            print("The door is already opened.")
        elif self.fuse_box and not self.door_opened:
            print("The door has opened! Now I can go outside!")
            self.door_opened = True


class ComputerRoom(FunctionClass):
    """The side room to the bunker."""

    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = ["wrench"]
        self.inventory = items_contained
        self.light_switch, self.safe_opened = bool_list

        self.look_dict = {
            "room": self.print_description_room,
            "light switch": self.print_description_light,
            "computer": self.print_description_computer,
            "safe": self.print_description_safe
        }

        self.go_dict = {
            "bunker": self.go_bunker
        }
        self.oper_dict = {
            "light switch": self.turn_on_switch,
            "computer": self.use_computer,
            "safe": self.operate_safe
        }

        self.use_dict = {}

    def get_bools(self):
        return self.light_switch, self.safe_opened

    # this prints a description along with a item list
    def print_description_room(self):
        if self.light_switch:
            print("You walk into a small room. It is dark and doesn’t smell any better than the rest of the bunker. "
                  "\nThere is a 'light' switch by the entryway. In the corner is an old 'computer' which appears to still "
                  "\nbe operational. You can get back to the 'bunker' too.")
            print("There is an old 'safe' of some sort too.")
            if len(self.inventory) > 0:
                for item in self.inventory:
                    print(f"There is a(n) {item}")
        else:
            print("There's a 'light switch' on the wall and an exit back to the 'bunker' \nbut otherwise it's too dark "
                  "to see.")

    def print_description_light(self):
        print("It's a light switch.")
        if self.light_switch:
            print("I hope there is power in here still.")
        else:
            print("I can't believe there is still power here.")

    def print_description_computer(self):
        if self.light_switch:
            print("An old but still working 'computer'.\nMaybe someone left some information on it.")
        else:
            print("It's too dark to see.")

    def print_description_safe(self):
        if self.light_switch:
            print("An old safe. Looks like it uses a biometric lock of some sort.")
            if not self.safe_opened:
                print("I wonder how I get into it?")
            elif "green fuse" in self.inventory:
                print("I might need that fuse.")
            else:
                print("I got the dumb thing open at least.")
        else:
            print("It's too dark to see.")

    @staticmethod
    def go_bunker(player_object):
        player_object.set_location("bunker")

    def operate_safe(self, mane_brushed):
        if self.light_switch:
            if not self.safe_opened:
                if mane_brushed:
                    print("I SUPPOSE YOU ARE CLEAN ENOUGH... FINE I'LL OPEN.\n")
                    print("Piece of junk... About damn time.")
                    self.inventory.append("green fuse")
                    self.safe_opened = True
                    return True
                else:
                    print("The safe buzzes and a voice barks out.")
                    print("HEY, A SCRUFFY THING LIKE YOU CAN'T OPEN ME.\n")
                    print("What The fuck?\n")
                    print("YES, YOU. CLEAN YOURSELF UP IF YOU WANT ME TO OPEN.\n")
                    print("Great a talking safe. Always happy to find new pains in my tail.")
                    return False
            else:
                print("It's already opened and I would prefer never to deal with it again.")
                return False
        else:
            print("It's too dark to see.")
            return False

    # turns on light switch
    def turn_on_switch(self):
        if not self.light_switch:
            print("The light is on now!")
            self.light_switch = True
        else:
            print("The switch is already on.")

    # uses computer in side room
    def use_computer(self):
        if self.light_switch:
            reading = True
            while reading:
                print("You have three emails. Select 1-4 and q to exit.")
                player_option = input("").lower()
                if player_option == "q":
                    reading = False
                elif player_option == "1":
                    print("""The only way to save messages on ths computer is to email them to myself.
                    Oh well, It's something to help pass the time as I try and stay human.""")
                elif player_option == "2":
                    print("""We've managed to keep those mutants out for the time being. 
                    I hope that we can continue to survive down here. It's going to be a rough couple of months 
                    before the radiation dies down up top.""")
                elif player_option == "3":
                    print("""The damn door fuse blew again. We only have a few left and the fuse box is not 
                    getting any younger. I hope that Mike returns before too long.""")
                elif player_option == "4":
                    print("""I've used the last fuse in that robot out there. You'll need so strong tools to remove it.
                    Hopefully we don't need it for the door.""")
                else:
                    print("I should select a usable option. Stupid computers.")
        else:
            print("You can't see anything to use it.")


# Main Plaza Areas
class MainPlaza(FunctionClass):
    """Main plaza class. Acts as the hub that connects all the other areas together."""

    def __init__(self, items_contained=None, bool_list=(False, False, False, False, False, False, False)):
        if items_contained is None:
            items_contained = ["map"]
        self.inventory = items_contained
        self.look_dict = {
            "room": self.print_description_room,
            "car": self.print_description_car,
            "desk": self.print_description_desk,
            "pay phone": self.print_description_phone,
            "gate": self.print_description_door
        }

        self.go_dict = {
            "bunker": self.go_bunker,
            "exit": self.go_exit,
            "upstairs": self.go_upstairs,
            "west wing": self.go_west_wing,
            "small den": self.go_small_den
        }

        self.oper_dict = {
            "car": self.operate_car
        }

        self.use_dict = {
            "desk": self.open_desk,
            "gate": self.unlock_gate,
            "pay phone": self.use_phone
        }

        self.exit_unlocked, self.upstairs_unlocked, self.map_gotten, self.car_looked, self.car_oper, self.desk_opened, self.phone_used = bool_list

    def get_bools(self):
        return self.exit_unlocked, self.upstairs_unlocked, self.map_gotten, self.car_looked, self.car_oper, self.desk_opened, self.phone_used

    def is_exit_unlocked(self):
        return self.exit_unlocked

    # this prints a description along with a item list
    def print_description_room(self):
        print("It's a large Main Plaza of the mall. There is a path to the 'west wing' too.")
        print("You emerge into the plaza of an old shopping mall. It is falling apart, "
              "\nwith much of the furnishings removed or smashed. Nature is starting to reclaim it too, judging by all "
              "\nthe foliage that’s popped up. There is an old 'car' parked nearby, for some strange reason."
              "\nThere is a 'desk' over by the main entrance near a 'payphone'.")
        if self.exit_unlocked:
            print("The 'exit' is open! I can get out.")
        else:
            print("The 'exit' is locked and I'm trapped.")
        if self.upstairs_unlocked:
            print("I can get 'upstairs' now at least. The 'gate' is unlocked now.")
        else:
            print("The path 'upstairs' is shut for now. The 'gate' is locked.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    def print_description_door(self):
        if not self.upstairs_unlocked:
            print("The gate is locked. You need to figure out how to open it.")
        elif self.upstairs_unlocked:
            print("You can go upstairs now at least.")
        else:
            print("It's open and you can go upstairs.")

    def print_description_desk(self):
        if not self.desk_opened:
            print("There's a old locked drawer here. I wonder how to get in.")
        elif "coin" in self.inventory:
            print("That coin is still there.")
        else:
            print("There's nothing else in the rotting desk.")

    def print_description_phone(self):
        if not self.phone_used:
            print("I wonder if it still works?")
        elif "blue fuse" in self.inventory:
            print("How did that get in there?")
        else:
            print("I know it does not work now...")

    def print_description_car(self):
        print("It's an old beat up Nissan Laurel. Not that you know what that is. It's seen better days.")
        if not self.car_looked:
            print("Hey this thing has a battery in it!")
            self.inventory.append("battery")
            self.car_looked = True
        elif "battery" in self.inventory:
            print("I should get the battery. Might come in handy.")
        else:
            print("I think I'm done messing with it.")

    def open_desk(self, item):
        if not self.desk_opened:
            if item == "screw driver":
                print("I got it open!")
                self.inventory.append("coin")
                self.desk_opened = True
                return True
            else:
                print(f"I can't open it with a(n) {item}.")
                return False
        else:
            print("It's already opened.")
            return False

    def use_phone(self, item):
        if not self.phone_used:
            if item == "coin":
                print("Hey, something fell out when I tried to use it!")
                self.inventory.append("blue fuse")
                self.phone_used = True
                return True

            else:
                print(f"I can use a(n) {item} with it.")
                return False
        else:
            print("It's not going to work all now.")
            return False

    def unlock_gate(self, item):
        if not self.upstairs_unlocked:
            if item == "keys":
                self.upstairs_unlocked = True
                return True
            else:
                print(f"I can't unlock it with {item}.")
                return False
        else:
            print("The gate is unlocked already.")
            return False

    def go_upstairs(self, player_object):
        if self.upstairs_unlocked:
            player_object.set_location("upstairs hallway")
        else:
            print("It's locked. I'll have to figure out how to get up there.")

    def go_exit(self, player_object):
        if self.exit_unlocked:
            player_object.set_location("exit")
        else:
            print("Right now the power is out, I'm trapped.")

    @staticmethod
    def go_west_wing(player_object):
        player_object.set_location("west wing")

    @staticmethod
    def go_small_den(player_object):
        player_object.set_location("small den")

    @staticmethod
    def go_bunker(player_object):
        player_object.set_location("bunker")

    def unlock_exit(self):
        self.exit_unlocked = True

    def operate_car(self):
        if not self.car_oper:
            print("It won't start but there are some odd keys in here.")
            self.inventory.append("strange keys")
            self.car_oper = True
        else:
            print("No point in trying to start it again.")

    # this pops off the items and returns it
    def get_item(self, item):

        if item in self.inventory:
            if item == "map" and not self.map_gotten:
                print("A map of the place! I should take a 'look'.")
                self.map_gotten = True
            location = self.inventory.index(item)
            return self.inventory.pop(location)
        else:
            return None


class SmallDen(FunctionClass):
    """A small animal pen that holds a dead animal and a workbench."""

    def __init__(self, items_contained=None, bool_list=(False, False, False, False), work_inventory=None):
        if items_contained is None:
            items_contained = []
        if work_inventory is None:
            work_inventory = []

        self.inventory = items_contained
        self.workbench_items_needed = ("soldering iron", "soldering wire", "capacitor")
        self.workbench_inventory = work_inventory
        self.animal_cut, self.barn_looked, self.tool_repaired, self.have_parts = bool_list

        self.look_dict = {
            "room": self.print_description_room,
            "barn": self.print_description_barn,
            "animal": self.print_description_animal_body,
            "work bench": self.print_description_workbench
        }

        self.go_dict = {
            "main plaza": self.go_main_plaza
        }
        self.oper_dict = {
            "work bench": self.operate_work_bench
        }

        self.use_dict = {"work bench": self.give_missing_part,
                         "animal": self.animal_cutting
                         }

    # returns bools for saving
    def get_bools(self):
        return self.animal_cut, self.barn_looked, self.tool_repaired, self.have_parts

    def get_parts(self):
        return self.workbench_inventory

    # this prints a description along with a item list
    def print_description_room(self):
        print(
            "It's some small den... or maybe a corral? It's not totally clear. \nThere is a exit back the 'main plaza'.")
        print("There is a small 'barn' of some kind built from old doors and scrap.")
        print("There is a dead body of an 'animal' here.")
        if self.barn_looked:
            print("And a 'work bench' too.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    # print description of dead body
    def print_description_animal_body(self):
        print("It's a dead body of some grazing animal. Not one I really recognize.")
        if not self.animal_cut:
            print("Could be useful if I cut some meat off it.")
        elif "meat" in self.inventory:
            print("I might need that meat. Though I don't want to touch it.")
        else:
            print("There's a chunk missing now.")

    # prints description of barn
    def print_description_barn(self):
        print("It's a old barn of some sort.")
        if not self.barn_looked:
            self.barn_looked = True
            print("Hey, there's an old 'work bench' here.\nI bet I could repair something on it.")
        else:
            print("I wonder what the 'work bench' was for.")

    # prints description of work bench
    def print_description_workbench(self):
        print("It's a work bench with assortment of tools and materials.")
        if not self.tool_repaired:

            if len(self.workbench_inventory) < 3:
                print("I wonder if I can fix that circuit board?")
                print("Looks like I need...")
                for item in self.workbench_items_needed:
                    if item not in self.workbench_inventory:
                        print(f"a(n) {item}")
            else:
                print("I can fix the board now!")
        elif "circuit board" in self.inventory:
            print("I repaired it.")
        else:
            print("I don't think there's anything else to do here.")

    # gets missing parts to work bench
    def give_missing_part(self, item):
        if len(self.workbench_inventory) < 3:
            if item in self.workbench_items_needed:
                print("That's one part of this.")
                self.workbench_inventory.append(item)
                if len(self.workbench_inventory) == 3:
                    print("Hey, that's all I need!")
                return True
            else:
                print(f"The {item} wouldn't help me.")
                return False
        else:
            print("It has everything it needs.")
            return False

    # if you have the parts you can repair the item
    def operate_work_bench(self):
        if not self.tool_repaired:
            if len(self.workbench_inventory) == 3:
                print("You fixed the board!")
                self.inventory.append("circuit board")
                self.tool_repaired = True
            else:
                print("I still need more parts.")
        else:
            print("The board is fixed now.")

    # player trying to get a chunk of meat
    def animal_cutting(self, item):
        if not self.animal_cut:
            if item == "knife":
                print("I cut off a chunk of meat. Gross...")
                self.inventory.append("meat")
                self.animal_cut = True
                return True
            else:
                print(f"I can't do any thing with the {item}.")
                return False
        else:
            print("It's already cut up. I'm done with it.")
            return False

    @staticmethod
    def go_main_plaza(player_object):
        player_object.set_location("plaza")


# West Wing Areas
class WestWing(FunctionClass):
    """A hallway that connects to the western rooms."""

    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = []
        self.inventory = items_contained

        self.pet_shop_unlocked, self.vend_looked = bool_list

        self.look_dict = {
            "room": self.print_description_room,
            "vending machine": self.print_description_vending,
            "kiosk": self.print_description_kiosk
        }

        self.go_dict = {
            "main plaza": self.go_main_plaza,
            "pet shop": self.go_pet_shop,
            "toy shop": self.go_toy_shop,
            "cemetery": self.go_cemetery
        }
        self.oper_dict = {
        }

        self.use_dict = {"kiosk": self.unlock_pet_shop
                         }

    # returns bools for saving
    def get_bools(self):
        return self.pet_shop_unlocked, self.vend_looked

    # this prints a description along with a item list
    def print_description_room(self):
        print("To the west of the plaza sits the west wing. While it is quite dilapidated, it appears someone has "
              "\nmade an effort to clean the wing up a fair bit. There is a 'kiosk' nearby and a 'vending machine'.")
        if not self.pet_shop_unlocked:
            print("There is a 'kiosk' in front of the pet shop.")
            print("It is asking for a pet to allow entry.")
        else:
            print("The 'kiosk' is happy with your offering.")
        print("You can go to 'toy shop', 'main plaza', 'pet shop', and 'cemetery.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    def print_description_kiosk(self):
        if not self.pet_shop_unlocked:
            print("It's a terminal to submit a pet for entering the shop. Old world store had theses a lot.")
            print("I usually just use my 'self' to fake my way past.")
        else:
            print("It's happy with the fur sample. Stupid thing...")

    def print_description_vending(self):
        print("It's a old and cracked machine. There is a flap on the front for getting things from it.")
        if not self.vend_looked:
            print("There's soda laying in it.")
            self.inventory.append("soda")
            self.vend_looked = True
        elif "soda" in self.inventory:
            print("That old soda is still here.")
        else:
            print("there's nothing else of value within it.")

    def go_pet_shop(self, player_object):
        if self.pet_shop_unlocked:
            player_object.set_location("pet shop")
        else:
            print("The 'kiosk' is demanding something.")
            return False

    @staticmethod
    def go_toy_shop(player_object):
        player_object.set_location("toy shop")

    @staticmethod
    def go_cemetery(player_object):
        player_object.set_location("cemetery")

    @staticmethod
    def go_main_plaza(player_object):
        player_object.set_location("plaza")

    def unlock_pet_shop(self, item):
        if not self.pet_shop_unlocked:
            if item == "fur sample":
                print("The shop accepted the sample as being a pet. You're in!")
                print("The doors slide open and allow you through.")
                self.pet_shop_unlocked = True
                return True
            elif item == "self":
                print("Error. Exotic pets are not allowed. Including but not limited too: lions, bears, etc...")
                print("I guess I will have to find something else to get in...")
                return False
            else:
                print(f"It doesn't like the {item}.")
                return False
        else:
            print("It's already unlocked.")
            return False


class PetShop(FunctionClass):
    """The petshop class. attached to the west wing."""

    def __init__(self, items_contained=None, bool_list=(False, False, False)):
        if items_contained is None:
            items_contained = ["mane brush"]
        self.inventory = items_contained

        self.fish_looked, self.rope_fixed, self.fridge_checked = bool_list
        self.look_dict = {
            "room": self.print_description_room,
            "fish": self.print_description_fish,
            "leash machine": self.print_description_leash_machine,
            "fridge": self.print_description_fridge,
            "shelves": self.print_description_selves
        }

        self.go_dict = {
            "west wing": self.go_west_wing
        }

        self.oper_dict = {}

        self.use_dict = {
            "leash machine": self.lengthen_rope
        }

    # returns bools for saving
    def get_bools(self):
        return self.fish_looked, self.rope_fixed, self.fridge_checked

    # this prints a description along with a item list
    def print_description_room(self):
        print("It’s an old pet shop. Humans would go here with their pets to buy care products for whatever animal "
              "\nthey owned. While the pet 'displays' are now empty and smashed to bits, there are still plenty of useful "
              "\nthings for a lion like you. Though you aren’t too fond of having to go to a pet store to get anything "
              "\neven remotely useful for you. In the back room of the store there is a fish display 'tank'. You seem "
              "\noddly attracted to it...")
        print("There is a 'leash machine' off in one of the corners and a small 'fridge'.")
        if "mane brush" in self.inventory:
            print("I might need a clean up and that brush looks handy.")

        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    def print_description_fish(self):
        if not self.fish_looked:
            self.inventory.append("fish")
            self.fish_looked = True
            print("Oh, there's a fish still alive in there.")
        elif "fish" in self.inventory:
            print("That fish looks tasty... No, Vern resist it.")
        else:
            print("I feel bad for taking the fish. Damn it.")

    def print_description_fridge(self):
        print("It's an old fridge and it's not very clean inside.")
        if not self.fridge_checked:
            print("Hey, what is this thing?")
            self.inventory.append("capacitor")
            print("And some catnip? uh on...")
            self.inventory.append("bag of catnip")
            self.fridge_checked = True

    @staticmethod
    def print_description_selves():
        print("They are ruined and there is nothing to get from them. Just old junk and random dog care products.")

    @staticmethod
    def go_west_wing(player_object):
        player_object.set_location("west wing")

    def print_description_leash_machine(self):
        print("It's a machine to repair leases.")
        if self.rope_fixed:
            print("It broke after extending my rope. It's no good now.")
        else:
            print("It looks like it's still working.")

    def lengthen_rope(self, item):
        if not self.rope_fixed:
            if item == "rope":
                print("Suddenly, the motor in the machine starts to struggle, and then with a large bang, ceases to "
                      "work.")
                print("Hey, I got a much longer rope now!")
                self.inventory.append("long rope")
                self.rope_fixed = True
                return True
            else:
                print(f"It rejected the {item}.")
                return False
        else:
            print("It's very broken and there's nothing else I can do with it.")
            return False


class ToyShop(FunctionClass):
    """The toyshop class. attached to the west wing."""

    def __init__(self, items_contained=None, bool_list=(False, False, False, False)):
        if items_contained is None:
            items_contained = ["soldering wire"]
        self.inventory = items_contained

        self.crane_fixed, self.crane_won, self.shelves_looked, self.locker_opened = bool_list
        self.look_dict = {
            "room": self.print_description_room,
            "crane": self.print_description_crane,
            "locker": self.print_description_locker,
            "shelves": self.print_description_shelves
        }

        self.go_dict = {
            "west wing": self.go_west_wing
        }

        self.oper_dict = {
            "crane": self.operate_crane
        }

        self.use_dict = {
            "locker": self.open_locker,
            "crane": self.fix_crane
        }

    # returns bools for saving
    def get_bools(self):
        return self.crane_fixed, self.crane_won, self.shelves_looked, self.locker_opened

    # this prints a description along with a item list
    def print_description_room(self):
        print("It’s an old toy shop, full of things a parent would buy for their children. It’s a mess with old toys "
              "\nstrewn across the floor and 'shelves', many of which are now broken. There is a 'crane' machine that’s still "
              "\noperational after so long. As well as an old 'locker' behind the registers.")
        if "soldering wire" in self.inventory:
            print("There's old wire used to repair things here too.")
        print("You can go back to the 'west wing' from here.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    def print_description_crane(self):
        print("It's an old crane machine.")
        if self.crane_won and "keys" not in self.inventory:
            print("You won the keys from it already.")
        elif "keys" in self.inventory:
            print("I should grab those keys.")
        else:
            print("There are a set of keys in the machine.")
        if self.crane_fixed:
            print("You have got the battery attached to it now.")
        elif not self.crane_won:
            print("There is a spot to attach things.")

    def print_description_shelves(self):
        print("There are a load of old toys and other bits and bobs.")
        print("What a pile of junk.")
        if not self.shelves_looked:
            print("There's a silly toy raygun. For some reason it makes you a little nervous.")
            self.inventory.append("toy raygun")
            self.shelves_looked = True
        elif "toy raygun" in self.inventory:
            print("That odd raygun is still here.")
        else:
            print("Just junk left now.")

    def print_description_locker(self):
        if not self.locker_opened:
            print("locked cabinet of sorts, with old toys from the old world, and there's a fuse in there")
        elif "red fuse" in self.inventory:
            print("I wonder what the fuse is for.")
        else:
            print("I beat the lock after all.")

    @staticmethod
    def go_west_wing(player_object):
        player_object.set_location("west wing")

    def open_locker(self, item):
        if not self.locker_opened:
            if item == "circuit board":
                print("Hey it opened up!")
                self.locker_opened = True
                self.inventory.append("red fuse")
                print("And a tail? What is this?")
                self.inventory.append("toy lion tail")
                return True
            else:
                print(f"This {item} is not helpful here.")
                return False
        else:
            print("It's already unlocked now.")
            return False

    def fix_crane(self, item):
        if not self.crane_fixed:
            if item == "battery":
                print("The crane is rigged to be won.\nNow I should try it again.")
                self.crane_fixed = True
                return True
            else:
                print(f"I can't fix it was a(n) {item}.")
                return False
        else:
            print("It's working for the moment.")
            return False

    def operate_crane(self):
        if not self.crane_won:
            if self.crane_fixed:
                print("The keys dropped into the pail in the front.")
                self.inventory.append("keys")
                self.crane_won = True
            else:
                print("You tried to get the keys out but the claw let them slip away.")
        else:
            print("There's nothing else in it you want.")


class Cemetery(FunctionClass):
    """The cemetery class. attached to the west wing."""

    def __init__(self, items_contained=None, bool_list=(False, False, False)):
        if items_contained is None:
            items_contained = ["lion plush"]
        self.inventory = items_contained

        self.first_entered, self.found_rope, self.grave_dug_up = bool_list

        self.look_dict = {
            "room": self.print_description_room,
            "graves": self.print_description_graves

        }

        self.go_dict = {
            "west wing": self.go_west_wing
        }

        self.oper_dict = {}

        self.use_dict = {
            "graves": self.dig_grave
        }

    # returns bools for saving
    def get_bools(self):
        return self.first_entered, self.found_rope, self.grave_dug_up

    # this prints a description along with a item list
    def print_description_room(self):
        print("You stumble into a makeshift cemetery. The atmosphere of the room makes you uneasy. At some point it "
              "\nused to be an outdoors food court, but it has become a 'grave' site for someone’s loved ones. The "
              "\nheadstones are made from old objects such as old car doors and hoods and signs.")
        print("You can go back to the 'west wing'.")
        if not self.first_entered:
            print("You don't think you should remove anything from here.")
            self.first_entered = True
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    def print_description_graves(self):
        print("There are a lot of different graves here. Seems a large community both lived and died here.")
        if "lion plush" in self.inventory:
            print("On a child's grave hangs a little lion plushy.")
        if not self.found_rope:
            print("Hey, there's an old 'rope' here. Might come in handy if you dare to steal from a graveyard.")
            self.inventory.append("rope")
            self.found_rope = True
        elif "rope" in self.inventory:
            print("That rope is still here. I wonder what it was from.")
        else:
            print("There's not much here of value now.")

    def dig_grave(self, item):
        if not self.grave_dug_up:
            if item == "shovel":
                print("Please forgive me for this.")
                print("digging sounds...")
                time.sleep(2)
                print("Hey, this is not a grave it's a cache!")
                print("A fuse!")
                self.inventory.append("gold fuse")
                self.grave_dug_up = True
                return True
            else:
                print(f"I can do anything with the {item}.")
                return False
        else:
            print("I have already dug that up.")
            return False

    @staticmethod
    def go_west_wing(player_object):
        player_object.set_location("west wing")


# Upstairs Areas
class UpstairsHallway(FunctionClass):
    """The upstairs hallway that connects to the animal den, shoe store, and bathroom."""

    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = []
        self.inventory = items_contained

        self.book_looked, self.furniture_looked = bool_list
        self.look_dict = {
            "room": self.print_description_room,
            "book": self.print_description_book,
            "furniture": self.print_description_furniture
        }

        self.go_dict = {
            "main plaza": self.go_main_plaza,
            "bathroom": self.go_bathroom,
            "shoe store": self.go_shoe_store,
            "animal den": self.go_animal_den
        }

        self.oper_dict = {
            "book": self.read_book}

        self.use_dict = {}

    # returns bools for saving
    def get_bools(self):
        return self.book_looked, self.furniture_looked

    # this prints a description along with a item list
    def print_description_room(self):
        print("You climb up the old escalator onto the upper plaza of the mall. It appears someone lived here for "
              "\nsome time, judging by the repurposed 'furniture' and empty food packaging all over the floor. Whoever "
              "\nlived here defended it fiercely, judging by all the old casings and bullet holes.")
        print("You can go to 'down stairs', 'shoe store', 'animal den', and 'bathroom'.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    # for look furn
    def print_description_furniture(self):
        print("It's a bunch of stacked furniture made into a barricade. Someone was trying to defend this place.")
        if not self.furniture_looked:
            print("Hey, what is this this? A keyring?")
            self.inventory.append("cheetah keyring")
            self.furniture_looked = True
            print("And an old 'book' too...")
            if not self.book_looked:
                print("I wonder what's in it?")
        else:
            if "cheetah keyring" in self.inventory:
                print("What an odd keyring.")
            print("There is an old 'book'.")
            if not self.book_looked:
                print("I wonder what's in it?")

    # for look book
    def print_description_book(self):
        print("It's an old cracked 'book' that's stained with blood.")
        if not self.book_looked:
            print("I might want to read it. Maybe There's something useful inside.")

    # for oper book
    def read_book(self):
        reading = True
        if not self.book_looked:
            print("Time to take a look at this thing.")
            self.book_looked = True
        while reading:
            page = input("What page to read? (one, two, three, four, and end to quit reading.)\n")
            if page == "one":
                print("This page looks earlier than the rest.")
                print("Martha changed today. She's one of those felines now. \nWe had to lock the pet shop for her own "
                      "good. We had to lock it against exotic animals. \nI'm still surprised it had that functionality "
                      "built in.")
                print("She's still the same woman I fell in love with but still. It feels wrong she's supposed to be "
                      "a human.")
                print("I'll have to make sure the others don't hurt her. They are getting worried and I don't like "
                      "\nhow they are looking at her.")
                print("")
            elif page == "two":
                print(
                    "Things have gone well so far. I've helped Martha get used to not eating meat all the time again.")
                print("Poor sweetheart. She doesn't even remember being human at all.")
                print("What am I going to do?")
                print("")
            elif page == "three":
                print("Others are changing too now. This is getting out of hand.")
                print(
                    "I had convinced the others that Martha couldn't infect them but now they aren't listening to me.")
                print("I can't let them hurt her. We survived the end together and")
                print("The journal ends suddenly here...")
                print("")
            elif page == "four":
                print("This page is dated much older than the rest.")
                print(
                    "Hey, I found a sweet new place to live for a while. Gotta clean out all the old bodies first though.")
                print("Weird cat things. Everywhere they show up things go to shit.")
                # Vern talking to himself
                print("\nVern taps his foot on the ground and growls to himself.")
                print("Hey! jackass... Humans always seem to think themselves wonderful.")
                print("")
            elif page == "end":
                print("I guess that's all I need from it.")
                reading = False
            else:
                print(f"I can't find page {page}.")

    @staticmethod
    def go_main_plaza(player_object):
        player_object.set_location("plaza")

    @staticmethod
    def go_shoe_store(player_object):
        player_object.set_location("shoe store")

    @staticmethod
    def go_animal_den(player_object):
        player_object.set_location("animal den")

    @staticmethod
    def go_bathroom(player_object):
        player_object.set_location("bathroom")


class AnimalDen(FunctionClass):
    """A upstairs animal den. Connected to the upstairs hallway."""

    def __init__(self, items_contained=None, bool_list=(False, False, False, False, False)):
        if items_contained is None:
            items_contained = ["meat"]
        self.inventory = items_contained

        self.animal_drugged, self.entered_after_drugged, self.found_fur, self.meat_just_taken, self.hole_tried = bool_list

        self.look_dict = {
            "room": self.print_description_room,
            "animal": self.print_description_animal,
            "hole": self.print_description_hole
        }

        self.go_dict = {
            "hallway": self.go_hallway,
            "hole": self.enter_hole
        }

        self.oper_dict = {}

        self.use_dict = {}

    # returns bools for saving
    def get_bools(self):
        return self.animal_drugged, self.entered_after_drugged, self.found_fur, self.meat_just_taken, self.hole_tried

    # this prints a description along with a item list
    def print_description_room(self):
        print("Once an old utility cabinet, it has now been claimed by some kind of animal. Judging by the sounds "
              "\ncoming from the den's 'hole' of a entrance, you feel you should probably avoid going in there directly.")
        if "meat" not in self.inventory and "drugged meat" not in self.inventory and not self.animal_drugged:
            print("With some sort of animal here I could lay a trap for it.")
        if not self.entered_after_drugged and self.animal_drugged:
            print("Hey, my trap worked!")
            self.entered_after_drugged = True
        if self.animal_drugged:
            print("Hey, looks like some sort of shaggy dog. Kinda fuzzy too, weird 'animal'.")
        elif self.meat_just_taken:
            print("It took my meat and left. I'll have to get more and use something on it.")
            self.meat_just_taken = False
        print("You can go back to the 'hallway'.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    # Vern talking about the odd hole in the wall
    def print_description_hole(self):
        if self.hole_tried:
            print("I'm never going in there again.")
        else:
            print("I wonder what's inside?")

    # talks about the animal
    def print_description_animal(self):
        if self.animal_drugged:
            print("it's a small animal. Pretty fuzzy too.")
            if not self.found_fur:
                print("Hey, that fur might help me out.")
                self.found_fur = True
        else:
            print("I'm sure it's around but I can't see it right now.")

    # Vern enters the hole once and never again
    def enter_hole(self, dummy):
        if self.hole_tried:
            print("Nope. Never again...")
        else:
            print("Well I need to try everything I can.")
            print("Vern enters the hole only for a lot of yelling and roaring to echo out of it.")
            print("You Died...")
            time.sleep(5)
            print("Suddenly Vern crawls from the hole and drops to the ground.")
            print("Wow, that thing was not nice. It's a good thing that us lions can fight.")
            self.hole_tried = True

    # if this returns true it does not add the meat item back to the other room.
    # if it returns false then it adds it for the player to try again.
    def drug_animal(self):
        if "meat" in self.inventory:
            print("I should see if something took my bate in the animal den.")
            self.inventory.remove("meat")
            self.meat_just_taken = True
            return "meat"
        elif "drugged meat" in self.inventory:
            print("I should check my trap in the animal den.")
            self.inventory.remove("drugged meat")
            self.inventory.append("fur sample")
            self.animal_drugged = True
            return "drugged"
        else:
            return "none"

    @staticmethod
    def go_hallway(player_object):
        player_object.set_location("upstairs hallway")


class Bathroom(FunctionClass):
    """A upstairs bathroom. Connected to the upstairs hallway."""

    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = ["knife"]
        self.inventory = items_contained

        self.looked_dryer, self.cabinet_looked = bool_list

        self.look_dict = {
            "room": self.print_description_room,
            "dryer": self.print_description_dryer,
            "graffiti": self.print_description_graffiti,
            "mirror": self.print_description_mirror,
            "medical cabinet": self.print_description_medical

        }

        self.go_dict = {
            "hallway": self.go_hallway,
        }

        self.oper_dict = {}

        self.use_dict = {}

    # returns bools for saving
    def get_bools(self):
        return self.looked_dryer, self.cabinet_looked

    # this prints a description along with a item list
    def print_description_room(self):
        print("It’s an old restroom. You can probably guess what "
              "\nwent on in here yourself. The old toilet blocks are heavily damaged and covered in 'graffiti'. The smell "
              "\nisn’t much better either. There is an old first aid 'cabinet' on the wall and a 'hand dryer' along side it. ")
        print("There is an old nasty looking 'mirror' on the wall.")
        print("You can go back to the 'hallway'.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    # bool will be if player has brushed mane
    @staticmethod
    def print_description_mirror(bool_val):
        print("It's an old cracked mirror. Kinda dirty too...")
        if bool_val:
            print("At least I look nicer than I thought I did.")
        else:
            print("My mane needs to be cleaned up pretty badly.")

    def print_description_dryer(self):
        if not self.looked_dryer:
            print("You look over the dryer and accidentally turn it on.")
            print("Yikes!")
            print("Vern's fur frizzes up and he jumps back.")
            time.sleep(1)
            print("Dumb thing...")
            self.looked_dryer = True
        else:
            print("I'm not messing with it again.")

    @staticmethod
    def print_description_graffiti():
        print("It's a lot of crudely drawn shapes and messages.")
        print("You look it and try to make something out.")
        time.sleep(1)
        print("I respect your political beliefs even if I do not share them.")
        print("You look nice today!\nAnd 404167")
        print("Huh? Much nicer than you'd think it would have been.")

    def print_description_medical(self):
        if not self.cabinet_looked:
            print("Lots of nasty old bandages and... wait!\nSome useful drugs remain.")
            self.inventory.append("drugs")
            self.cabinet_looked = True
        elif "drugs" in self.inventory:
            print("I should get those drugs. Might need them for something.")
        else:
            print("There's nothing else of value here.")

    @staticmethod
    def go_hallway(player_object):
        player_object.set_location("upstairs hallway")


class ShoeStore(FunctionClass):
    """A upstairs shoe store. Connected to the upstairs hallway."""

    def __init__(self, items_contained=None, bool_list=(False, False, False, False)):
        if items_contained is None:
            items_contained = ["owl figurine", "screw driver"]
        self.inventory = items_contained

        self.first_entered, self.elevator_opened, self.elevator_roped, self.weak_roped = bool_list

        self.look_dict = {
            "room": self.print_description_room,
            "elevator": self.print_description_elevator

        }

        self.go_dict = {
            "hallway": self.go_hallway,
            "elevator": self.go_elevator
        }

        self.oper_dict = {
            "elevator": self.operate_elevator_doors
        }

        self.use_dict = {
            "elevator": self.fix_elevator
        }

    # returns bools for saving
    def get_bools(self):
        return self.first_entered, self.elevator_opened, self.elevator_roped, self.weak_roped

    # this prints a description along with a item list
    def print_description_room(self):
        print("It’s an old shoe store. It smells of musty leather and fabric. It used to be where a human would go to "
              "\nget some footwear, but now it appears someone had turned it into a living space, judging by the mess "
              "they’ve left.")
        if "screw driver" in self.inventory:
            print("There's a screw driver on the old shelves around the place.")

        if self.elevator_opened:
            print("The 'elevator' shaft is opened now.")
            if self.elevator_roped:
                print("You can climb down it now.")
            elif "rope" in self.inventory and self.weak_roped:
                print("I used a rope on it but I don't think it's long enough.")
            else:
                print("There's no way down just yet. You'll have to figure that out.")
        else:
            print("There is an old 'elevator' shaft but the doors are closed.")
        if not self.first_entered:
            print("You doubt anything would fit your digitigrade feet from this place.")
            self.first_entered = True

        print("You can go back the the 'hallway' from here.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    def print_description_elevator(self):
        if not self.elevator_opened:
            print("It's closed right now. I wonder what's inside.")
        elif self.weak_roped:
            print("It's got a rope but I don't think it's long enough.")
        elif self.elevator_roped:
            print("I should be safe to go down now.")
        else:
            print("I need to figure out how to descend it.")

    # this pops off the items and returns it
    def get_item(self, item):
        if item in self.inventory:
            # if item is rope and you have used it on the elevator it flips that flag back to false
            if item == "rope" and self.weak_roped:
                print("I removed the short rope from the elevator.")
                self.weak_roped = False
            location = self.inventory.index(item)
            return self.inventory.pop(location)
        else:
            return None

    def operate_elevator_doors(self):
        if not self.elevator_opened:
            print("I got the doors opened now.")
            self.elevator_opened = True
        else:
            print("The doors are already opened.")

    # to fix the elevator
    # if you used the weak rope it adds it to the room inventory and flags you as having used the weak rope
    # if you use the strong rope it just removes the item and does marks you as having used the strong rope
    def fix_elevator(self, item):
        if not self.elevator_opened:
            print("I should open it first.")
            return False
        # if you have used either the weak or strong rope
        if self.weak_roped or self.elevator_roped:
            if self.weak_roped:
                print("I used a rope already but I should try and make the rope stronger.")
                return False
            else:
                print("It's ok for me to climb down now.")
                return False
        else:
            # if the item is the rope it adds to room inventory and flips the flag variable
            if item == "rope":
                print(f"I used the {item}. Maybe I can climb down.")
                self.inventory.append(item)
                self.weak_roped = True
                return True
            # if strong rope just flips the strong rope flag
            elif item == "long rope":
                print(f"I used the {item}. Maybe I can climb down now.")
                self.elevator_roped = True
                return True
            else:
                print(f"I can use the {item} on the elevator.")
                return False

    # tries to go down the shaft. Fails if the strong rope is not used
    def go_elevator(self, player_object):
        # if the elevator has not being opened fail
        if not self.elevator_opened:
            print("I should open it first.")
        # if weak rope has been used and
        if self.weak_roped:
            print("I'm not going down that rope. It's not safe at all.")
        # if you used the strong rope then you can go
        elif self.elevator_roped:
            print("Ok, it looks safe... Maybe not but here I go.")
            player_object.set_location("basement entry")
        else:
            print("I'll have to find a way to climb down it.")

    @staticmethod
    def go_hallway(player_object):
        player_object.set_location("upstairs hallway")


# Basement Areas
class BasementEntry(FunctionClass):
    """A basement room that is attached to the shoe store."""

    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = ["shovel"]
        self.inventory = items_contained

        self.door_unlocked, self.soda_used = bool_list

        self.look_dict = {
            "room": self.print_description_room,
            "note": self.print_description_note,
            "pad": self.print_description_pad

        }

        self.go_dict = {
            "shoe store up": self.go_shoe_store,
            "generator room": self.go_gen_room
        }

        self.oper_dict = {
            "pad": self.entering_code
        }

        self.use_dict = {
            "pad": self.entering_code
        }

    # returns bools for saving
    def get_bools(self):
        return self.door_unlocked, self.soda_used

    # this prints a description along with a item list
    def print_description_room(self):
        print("It's a dark basement lit only by emergency lights. There is a door with a electronic 'pad' lock across "
              "from you.")
        print("This place is not on the map... How strange.")
        if self.door_unlocked:
            print("The door is open and you can enter the 'generator room'.")
        else:
            print("You'll have to figure out how to open the door.")
        print("You can go back 'up' to the 'shoe store'.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    def print_description_pad(self):
        print("It's an old electronic lock of some kind.")
        print("There's a small 'note' near it.")
        if not self.door_unlocked:
            print("I can't believe I found that password.")
        elif self.door_unlocked and self.soda_used:
            print("It's open now and pretty gross from the soda.")
        else:
            print("It's asking for a password.")

    def print_description_note(self):
        print("It reads: Don't get anything on this new lock you morons.")
        print("I have replaced it, but next time it's on your paycheck.")
        if self.soda_used:
            print("The note is splattered with soda.")
            print("The soda worked... Who knew?")
        else:
            print("I wonder what that means.")

    def go_gen_room(self, player_object):
        if self.door_unlocked:
            player_object.set_location("basement generator room")
        else:
            print("The door is locked. I can't go there yet.")

    @staticmethod
    def go_shoe_store(player_object):
        player_object.set_location("shoe store")

    # tries to enter codes or items to bypass the door.
    def entering_code(self, item=None):

        # only allows attempting to unlock if door is locked.
        if not self.door_unlocked:
            # if no item is give it asks for a password
            if item is None:
                password = ""
                print("It's asking for a password.")
                while len(password) < 6:
                    number = input("")
                    # counts through the player input and makes sure are only numbers.
                    for digit in number:
                        if not digit.isdigit():
                            print("ERROR!")
                            print("Oops! Wrong button.")
                            break
                    else:
                        password += number

                if password == "404167":
                    print("That Password is accepted. The door is open now!")
                    self.door_unlocked = True
                else:
                    print("That was not accepted... I wonder what the code is?")
            # if they used a soda.
            elif item == "soda":
                print("You dump the soda on the code box.")
                print("It fizzles and sparks. The door opens.\nHuh? Can't believe that worked.")
                self.door_unlocked = True
                self.soda_used = True
                return True
            else:
                print("That doesn't help me...")
                return False
        else:
            print("It's open. I don't have to do anything else with it.")
            return False


class BasementGenRoom(FunctionClass):
    """A basement generator room that is attached to the shoe store."""

    def __init__(self, items_contained=None, generator_inv=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = ["soldering iron"]
        if generator_inv is None:
            generator_inv = []
        self.generator_inventory = generator_inv
        self.inventory = items_contained
        self.fuses_needed = ("green fuse", "red fuse", "blue fuse", "gold fuse")
        self.fuses_fixed, self.generator_working = bool_list

        self.look_dict = {
            "room": self.print_description_room,
            "generator": self.print_description_generator,
            "spec sheet": self.print_description_spec
        }

        self.go_dict = {
            "basement entry": self.go_basement_entry
        }

        self.oper_dict = {
            "generator": self.operate_generator
        }

        self.use_dict = {
            "generator": self.add_item_generator
        }

    # gets the number of fuses installed in the generator.
    def get_gen_inventory(self):
        return self.generator_inventory

    # returns bools for saving
    def get_bools(self):
        return self.fuses_fixed, self.generator_working

    # used for flags if generator is working.
    def is_generator_working(self):
        return self.generator_working

    # this prints a description along with a item list
    def print_description_room(self):
        print("This place is not on the map either... Maybe it just was not entered by the previous owners?.")
        print("Hey a large 'generator', maybe you can get it working?")
        print("There's a workbench with some scattered tools on it.")
        if "soldering iron" in self.inventory:
            print("That iron looks useful still.")
        if self.fuses_fixed:
            print("The power is on somewhere now. You should look around for it!")
        else:
            print("There is a large panel with spaces for four large fuses. You should get your eyes out for them.")
            print("There is a 'spec' sheet by it you might want to take note of.")
        print("You can go back to the 'basement entry'")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    def print_description_generator(self):
        print("It's a back up generator.")
        if self.generator_working:
            print("I got it working. I should check around and see what opened up. Maybe the exit is working again.")
        else:
            print("There are slots for four fuses. I need to find and insert them.")

    def print_description_spec(self):
        print("It lists the fuses I will need to fix the generator.")
        if len(self.generator_inventory) < 4:
            print("You still need:")
            for fuse in self.fuses_needed:
                if fuse not in self.generator_inventory:
                    print(f"A {fuse}")
        else:
            print("I got them all. Took long enough too...")

    def add_item_generator(self, item):
        if len(self.generator_inventory) < 4:
            if item in self.fuses_needed:
                if len(self.generator_inventory) < 3:
                    self.generator_inventory.append(item)
                    print(f"I added the {item} to the generator. Only {4 - len(self.generator_inventory)} Left to add.")
                else:
                    self.generator_inventory.append(item)
                    print(f"I added the {item} to the generator. That's the last one!")

                return True
            else:
                print("I can't use that on the generator.")
                return False
        else:
            print("It's got all it needs. You should run it now.")
            return False

    def operate_generator(self):
        if not self.generator_working and len(self.generator_inventory) == 4:
            print("You flip the massive switch and the generator roars to life!")
            self.generator_working = True
        elif not self.generator_working and len(self.generator_inventory) < 4:
            remainder = 4 - len(self.generator_inventory)
            print(f"It's missing {remainder} fuses still. You'll have to find them somewhere first.")
        else:
            print("It's already running.")

    @staticmethod
    def go_basement_entry(player_object):
        player_object.set_location("basement entry")
