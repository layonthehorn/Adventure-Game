class PetShop:
    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = ["mane brush"]
        self.inventory = items_contained

        self.bool_one, self.bool_two = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # returns bools for saving
    def get_bools(self):
        return (self.bool_one, self.bool_two)

    # this prints a description along with a item list
    def print_description_room(self):
        print("It's an old pet store. Lot's of useful things for a lion like you here. If you are not embarrassed to "
              "use them.")
        print("It’s an old pet shop. Humans would go here with their pets to buy care products for whatever animal "
              "they owned. While the pet displays are now empty and smashed to bits, there are still plenty of useful "
              "things for a lion like you. Though you aren’t too fond of having to go to a pet store to get anything "
              "even remotely useful for you. In the back room of the store there is a fish display tank. You seem "
              "oddly attracted to it...")

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