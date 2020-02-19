class PetShop:
    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = ["mane brush", "bag of catnip"]
        self.inventory = items_contained

        self.fish_looked, self.rope_fixed = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # returns bools for saving
    def get_bools(self):
        return self.fish_looked, self.rope_fixed

    # this prints a description along with a item list
    def print_description_room(self):
        print("It’s an old pet shop. Humans would go here with their pets to buy care products for whatever animal "
              "\nthey owned. While the pet 'displays' are now empty and smashed to bits, there are still plenty of useful "
              "\nthings for a lion like you. Though you aren’t too fond of having to go to a pet store to get anything "
              "\neven remotely useful for you. In the back room of the store there is a fish display 'tank'. You seem "
              "\noddly attracted to it...")
        print("There is a 'leash repairing' machine off in one of the corners.")
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

    def print_description_selves(self):
        print("They are ruined and there is nothing to get from them. Just old junk and random dog care products.")

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