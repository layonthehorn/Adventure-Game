class Cemetery:
    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = ["lion plush"]
        self.inventory = items_contained

        self.first_entered, self.found_rope = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # returns bools for saving
    def get_bools(self):
        return self.first_entered, self.found_rope

    # this prints a description along with a item list
    def print_description_room(self):
        print("You stumble into a makeshift cemetery. The atmosphere of the room makes you uneasy. At some point it "
              "\nused to be an outdoors food court, but it has become a 'grave' site for someone’s loved ones. The "
              "\nheadstones are made from old objects such as old car doors and hoods and signs.")
        print("You can go back to the 'west wing'.")
        if not self.first_entered:
            print("You don't think you should remove anything from here.")
            self.first_entered = True
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    def print_description_graves(self):
        print("There are a lot of different graves here. Seems a large community both lived and died here.")
        if "lion plush" in self.inventory:
            print("On a child's grave hangs a little lion plushy.")
        if not self.found_rope:
            print("Hey, there's an old 'rope' here. Might come in handy if you dare to steal from a graveyard.")
            self.inventory.append("rope")
            self.found_rope = True
        elif "rope" in self.inventory:
            print("That rope is still here. I wonder what it was from.")
        else:
            print("There's not much here of value now.")

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
