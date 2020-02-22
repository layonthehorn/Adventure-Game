class ToyShop:
    def __init__(self, items_contained=None, bool_list=(False, False, False, False)):
        if items_contained is None:
            items_contained = ["soldering wire"]
        self.inventory = items_contained

        self.crane_fixed, self.crane_won, self.shelves_looked, self.locker_opened = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

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
