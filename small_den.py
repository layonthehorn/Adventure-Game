class SmallDen:
    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = ["meat"]
        self.inventory = items_contained
        self.animal_cut, self.meat_added = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # returns bools for saving
    def get_bools(self):
        return self.animal_cut, self.meat_added

    # this prints a description along with a item list
    def print_description_room(self):
        print("It's some small den... or maybe a corral? It's not totally clear. \nThere is a exit back the 'main plaza'.")
        print("There is a dead body of an 'animal' here.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    # print description of dead body
    def print_description_animal_body(self):
        print("It's a dead body of some grazing animal. Not one you really recognize.")
        if not self.animal_cut:
            print("Could be useful if I cut some meat off it.")
        elif not self.meat_added:
            print("There's chuck of 'meat' loose now.")
            self.inventory.append("meat")
            self.meat_added = True
        elif "meat" in self.inventory:
            print("I might need that meat. Though I don't want to touch it.")
        else:
            print("There's a chunk missing now.")

    def animal_cutting(self, item):
        if not self.animal_cut:
            if item == "knife":
                print("I cut off a chunk of meat. Gross...")
                self.animal_cut = True
                return True
            else:
                print(f"I can't do any thing with the {item}.")
                return False
        else:
            print("It's already cut up. I'm done with it.")
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
