class ShoeStore:
    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = ["drugs"]
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
        print("It's a small place. Use to sell shoes and wears like that. Now"
              " it's just a wreck and all too messy.")
        if not self.first_entered:
            print("You doubt anything would fit your digitigrade feet from this place.")
            self.first_entered = True
        print("You can go back the the 'hallway' from here.")
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
