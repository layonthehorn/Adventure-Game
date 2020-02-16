class ToyShop:
    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = ["toy raygun", "fur sample"]
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
        print("It’s an old toy shop, full of things a parent would buy for their children. It’s a mess with old toys "
              "strewn across the floor, many of which are now broken. There is a claw machine that’s still "
              "operational after so long.")
        print("You can go back to the west wing from here.")
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