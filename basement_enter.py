class BasementEnter:
    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = ["shovel"]
        self.inventory = items_contained

        self.door_unlocked, self.soda_used = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # returns bools for saving
    def get_bools(self):
        return self.door_unlocked, self.soda_used

    # this prints a description along with a item list
    def print_description_room(self):
        print("It's a dark basement lit only by emergency lights. There is a door with a electronic 'pad' lock across "
              "from you.")
        print("This place is not on the map... How strange.")
        if self.door_unlocked:
            print("The door is open and you can enter.")
        else:
            print("You'll have to figure out how to open the door.")
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

    def go_gen_room(self):
        if self.door_unlocked:
            return True
        else:
            print("The door is locked. I can't go there yet.")
            return False

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
                        if digit not in "0123456789":
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
