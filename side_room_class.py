
class SideRoom:
    def __init__(self, items_contained=None, bool_list=(False)):
        if items_contained is None:
            items_contained = ["wrench"]
        self.inventory = items_contained
        self.light_switch = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    def get_bools(self):
        return (self.light_switch)

    # this prints a description along with a item list
    def print_description_room(self):
        if self.light_switch:
            print("It's a small 'side room'. There is a 'computer' running some had left logged in. "
                  "\nThere is an exit back to the 'bunker'.")
            print("It's cramped with very little room to move. They did not spend much on this room.")
            if len(self.inventory) > 0:
                for item in self.inventory:
                    print(f"There is a(n) {item}")
        else:
            print("There's a 'light switch' on the wall and an exit back to the 'bunker' but otherwise it's too dark to "
                  "see.")

    def print_description_computer(self):
        if self.light_switch:
            print("An old but still working 'computer'.\nMaybe someone left some information on it.")
        else:
            print("It's too dark to see.")

    # this pops off the items and returns it
    def get_item(self, item):

        if item in self.inventory:
            location = self.inventory.index(item)
            return self.inventory.pop(location)
        else:
            return None

    # dropping item back into room
    def give_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)

    # turns on light switch
    def turn_on_switch(self):
        if not self.light_switch:
            print("The light is on now!")
            self.light_switch = True
        else:
            print("The switch is already on.")

    # uses computer in side room
    def use_computer(self):
        if not self.light_switch:
            print("You can't see anything to use it.")
        else:
            reading = True
            while reading:
                print("You have three emails. Select 1-4 and -1 to exit.")
                player_option = input("")
                if player_option == "-1":
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