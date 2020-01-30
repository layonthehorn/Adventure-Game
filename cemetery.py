class Cemetery:
    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = ["lion plush"]
        self.inventory = items_contained

        self.first_entered = bool_list[0]
        self.bool_two = bool_list[1]

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # returns bools for saving
    def get_bools(self):
        return (self.first_entered, self.bool_two)

    # this prints a description along with a item list
    def print_description_room(self):
        print("It's a make-shift cemetery. There is an exit back to the 'west wing'")
        if not self.cemetery.first_entered:
            print("You don't think you should remove anything from here.")
            self.cemetery.first_entered = True

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