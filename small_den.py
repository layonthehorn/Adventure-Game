class SmallDen:
    def __init__(self, items_contained=None, bool_list=(False, False, False, False), work_inventory=None):
        if items_contained is None:
            items_contained = ["meat"]
        if work_inventory is None:
            work_inventory = []

        self.inventory = items_contained
        self.workbench_items_needed = ("", "", "")
        self.workbench_inventory = work_inventory
        self.animal_cut, self.barn_looked, self.tool_repaired, self.have_parts = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # returns bools for saving
    def get_bools(self):
        return self.animal_cut, self.barn_looked, self.tool_repaired, self.have_parts

    def get_parts(self):
        return self.workbench_inventory

    # this prints a description along with a item list
    def print_description_room(self):
        print("It's some small den... or maybe a corral? It's not totally clear. \nThere is a exit back the 'main plaza'.")
        print("There is a small 'barn' of some kind built from old doors and scrap.")
        print("There is a dead body of an 'animal' here.")
        if self.barn_looked:
            print("And a 'work bench' too.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    # print description of dead body
    def print_description_animal_body(self):
        print("It's a dead body of some grazing animal. Not one I really recognize.")
        if not self.animal_cut:
            print("Could be useful if I cut some meat off it.")
        elif "meat" in self.inventory:
            print("I might need that meat. Though I don't want to touch it.")
        else:
            print("There's a chunk missing now.")

    # prints description of barn
    def print_description_barn(self):
        print("It's a old barn of some sort.")
        if not self.barn_looked:
            self.barn_looked = True
            print("Hey, there's an old 'work bench' here.\nI bet I could repair something on it.")
        else:
            print("I wonder what the 'work bench' was for.")

    # prints description of work bench
    def print_description_workbench(self):
        print("It's a work bench with assortment of tools and materials.")
        if not self.tool_repaired:
            print("I wonder if I can fix that, .")
        elif "tool" in self.inventory:
            print("I repaired it.")
        else:
            print("I don't think there's anything else to do here.")

    # gets missing parts to work bench
    def give_missing_part(self, item):
        return False

    # if you have the parts you can repair the item
    def operate_work_bench(self):
        pass

    # player trying to get a chunk of meat
    def animal_cutting(self, item):
        if not self.animal_cut:
            if item == "knife":
                print("I cut off a chunk of meat. Gross...")
                self.inventory.append("meat")
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
