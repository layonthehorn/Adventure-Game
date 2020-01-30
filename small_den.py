class SmallDen:
    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = ["meat"]
        self.inventory = items_contained

        self.bool_one = bool_list[0]
        self.bool_two = bool_list[1]

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # returns bools for saving
    def get_bools(self):
        return (self.bool_one, self.bool_two)

    # this prints a description along with a item list
    def print_description_room(self):
        print("It's some small den... or maybe a corral? It's not totally clear.\nThere is a exit back the 'main plaza'.")
        print("There is a dead body of an animal here.")

    # print description of dead body
    def print_description_animal_body(self):
        print("It's a dead body of some grazing animal. Not one you really recognize")

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
