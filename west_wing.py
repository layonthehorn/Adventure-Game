class WestWing:
    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = []
        self.inventory = items_contained

        self.pet_shop_unlocked, self.bool_two = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # returns bools for saving
    def get_bools(self):
        return (self.pet_shop_unlocked, self.bool_two)

    # this prints a description along with a item list
    def print_description_room(self):
        print("It's a small hallway that leads to new areas.\nThere is a exit back the 'main plaza'.")
        print("You can go to 'toy shop', 'pet shop', and 'cemetery.")
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

    def print_description_kiosk(self):
        if not self.pet_shop_unlocked:
            print("It's a terminal to submit a pet for entering the shop. Old world store had theses a lot.")
            print("I usually just use my 'self' to fake my way past.")
        else:
            print("It's happy with the fur sample. Stupid thing...")

    def unlock_pet_shop(self, item):
        if not self.pet_shop_unlocked:
            if item == "fur sample":
                print("The shop accepted the sample as being a pet. You're in!")
                self.pet_shop_unlocked = True
                return True
            elif item == "self":
                print("Error. Exotic pets are not allowed. Including but not excluded too: lions, bears, etc...")
                print("I guess I will have to find something else to get in...")
                return False
            else:
                print(f"It doesn't like the {item}.")
                return False
        else:
            print("It's already unlocked.")
            return False
