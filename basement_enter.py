import time


class BasementEnter:
    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = []
        self.inventory = items_contained

        self.door_unlocked, self.bool_two = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # returns bools for saving
    def get_bools(self):
        return (self.door_unlocked, self.bool_two)

    # this prints a description along with a item list
    def print_description_room(self):
        print("It's a dark basement lit only by emergency lights. There is a door with a pad lock across from you.")
        if self.door_unlocked:
            print("The door is open and you can enter.")
        else:
            print("You'll have to figure out how to open it.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

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

    # tries to enter codes or items to bypass the door.
    def entering_code(self, item=None):

        if not self.door_unlocked:
            if item is None:
                password = ""
                print("It's asking for a password.")
                while len(password) < 6:
                    number = input("")
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
                    return False
                else:
                    print("That was not accepted... I wonder what the code is?")
                    return False
            elif item == "soda":
                print("You dump the soda on the code box.")
                print("It fizzles and sparks. The door opens.\nHuh? Can't believe that worked.")
                self.door_unlocked = True
                return True
            else:
                print("That doesn't help me...")
                return False
        else:
            print("It's open. I don't have to do anything else with it.")
            return False
