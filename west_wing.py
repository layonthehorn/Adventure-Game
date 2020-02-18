class WestWing:
    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = []
        self.inventory = items_contained

        self.pet_shop_unlocked, self.vend_looked = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # returns bools for saving
    def get_bools(self):
        return self.pet_shop_unlocked, self.vend_looked

    # this prints a description along with a item list
    def print_description_room(self):
        print("To the west of the plaza sits the west wing. While it is quite dilapidated, it appears someone has "
              "\nmade an effort to clean the wing up a fair bit. There is a kiosk nearby and a vending machine.")
        if not self.pet_shop_unlocked:
            print("There is a kiosk in front of the pet shop.")
            print("It is asking for a pet to allow entry.")
        else:
            print("The kiosk is happy with your offering.")
        print("You can go to 'toy shop', 'main plaza', 'pet shop', and 'cemetery.")
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

    def go_pet_shop(self):
        if self.pet_shop_unlocked:
            return True
        else:
            print("The kiosk is demanding something.")
            return False

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
