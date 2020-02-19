class BasementGenRoom:
    def __init__(self, items_contained=None, generator_inv=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = []
        if generator_inv is None:
            generator_inv = []
        self.generator_inventory = generator_inv
        self.inventory = items_contained
        self.fuses_needed = ("green fuse", "red fuse", "blue fuse", "gold fuse")
        self.fuses_fixed, self.generator_working = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # gets the number of fuses installed in the generator.
    def get_gen_inventory(self):
        return self.generator_inventory

    # returns bools for saving
    def get_bools(self):
        return self.fuses_fixed, self.generator_working

    # this prints a description along with a item list
    def print_description_room(self):
        print("This place is not on the map either... Maybe it just was not entered by the previous owners?.")
        print("Hey a large 'generator', maybe you can get it working?")
        if self.fuses_fixed:
            print("The power is on somewhere now. You should look around for it!")
        else:
            print("There is a large panel with spaces for four large fuses. You should get your eyes out for them.")
            print("There is a 'spec' sheet by it you might want to take note of.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    def print_description_generator(self):
        print("It's a back up generator.")
        if self.generator_working:
            print("I got it working. I should check around and see what opened up. Maybe the exit is working again.")
        else:
            print("There are slots for four fuses. I need to find and insert them.")

    def print_description_spec(self):
        print("It lists the fuses I will need to fix the generator.")
        if len(self.generator_inventory) < 4:
            print("You still need:")
            for fuse in self.fuses_needed:
                if fuse not in self.generator_inventory:
                    print(f"A {fuse}")
        else:
            print("I got them all. Took long enough too...")

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

    def add_item_generator(self, item):
        if len(self.generator_inventory) < 4:
            if item in self.fuses_needed:
                if len(self.generator_inventory) < 3:
                    self.generator_inventory.append(item)
                    print(f"I added the {item} to the generator. Only {4 - len(self.generator_inventory)} Left to add.")
                else:
                    self.generator_inventory.append(item)
                    print(f"I added the {item} to the generator. That's the last one!")

                return True
            else:
                print("I can't use that on the generator.")
                return False
        else:
            print("It's got all it needs. You should run it now.")
            return False

    def operate_generator(self):
        if not self.generator_working and len(self.generator_inventory) == 4:
            print("You flip the massive switch and the generator roars to life!")
            self.generator_working = True
        elif not self.generator_working and len(self.generator_inventory) < 4:
            remainder = 4 - len(self.generator_inventory)
            print(f"It's missing {remainder} fuses still. You'll have to find them somewhere first.")
        else:
            print("It's already running.")
