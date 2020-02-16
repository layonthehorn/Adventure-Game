class MainPlaza:
    def __init__(self, items_contained=None, bool_list=(False, False, False, False)):
        if items_contained is None:
            items_contained = ["strange keys", "map"]
        self.inventory = items_contained

        self.exit_unlocked, self.upstairs_unlocked, self.map_gotten, self.car_looked = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    def get_bools(self):
        return self.exit_unlocked, self.upstairs_unlocked, self.map_gotten, self.car_looked

    # this prints a description along with a item list
    def print_description_room(self):
        print("It's a large Main Plaza of the mall. There is a path to the 'west wing' too.")
        print("You emerge into the plaza of an old shopping mall. It is falling apart, "
              "with much of the furnishings removed or smashed. Nature is starting to reclaim it too, judging by all "
              "the foliage that’s popped up. There is an old car parked nearby, for some strange reason.")
        if self.exit_unlocked:
            print("The 'exit' is open! I can get out.")
        else:
            print("The 'exit' is locked and I'm trapped.")
        if self.upstairs_unlocked:
            print("I can get 'upstairs' now at least.")
        else:
            print("The path 'upstairs' is shut for now.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    def print_description_door(self):
        if not self.upstairs_unlocked:
            print("")
        else:
            print("It's open and you can go upstairs.")

    def print_description_car(self):
        print("It's an old beat up Nissan Laurel. Not that you know what that is. It's seen better days.")
        if not self.car_looked:
            print("Hey this thing has a battery in it!")
            self.inventory.append("battery")
            self.car_looked = True
        elif "battery" in self.inventory:
            print("I should get the battery. Might come in handy.")
        else:
            print("I think I'm done messing with it.")

    # this pops off the items and returns it
    def get_item(self, item):

        if item in self.inventory:
            if item == "map" and not self.map_gotten:
                print("A map of the place! I should take a 'look'.")
                self.map_gotten = True
            location = self.inventory.index(item)
            return self.inventory.pop(location)
        else:
            return None

    # dropping item back into room
    def give_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)