class PetShop:
    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = ["mane brush"]
        self.inventory = items_contained

        self.fish_looked, self.bool_two = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # returns bools for saving
    def get_bools(self):
        return self.fish_looked, self.bool_two

    # this prints a description along with a item list
    def print_description_room(self):
        print("It’s an old pet shop. Humans would go here with their pets to buy care products for whatever animal "
              "\nthey owned. While the pet displays are now empty and smashed to bits, there are still plenty of useful "
              "\nthings for a lion like you. Though you aren’t too fond of having to go to a pet store to get anything "
              "\neven remotely useful for you. In the back room of the store there is a fish display tank. You seem "
              "\noddly attracted to it...")
        if "mane brush" in self.inventory:
            print("I might need a clean up.")

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