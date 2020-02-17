class Cemetery:
    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = ["lion plush"]
        self.inventory = items_contained

        self.first_entered, self.bool_two = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # returns bools for saving
    def get_bools(self):
        return (self.first_entered, self.bool_two)

    # this prints a description along with a item list
    def print_description_room(self):
        print("You stumble into a makeshift cemetery. The atmosphere of the room makes you uneasy. At some point it "
              "\nused to be an outdoors food court, but it has become a burial site for someone’s loved ones. The "
              "\nheadstones are made from old objects such as old car doors and hoods and signs.")
        print("You can go back to the 'west wing'.")
        if not self.first_entered:
            print("You don't think you should remove anything from here.")
            self.first_entered = True
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