class MainPlaza:
    def __init__(self, items_contained=None, bool_list=(True, False, True, False, False)):
        if items_contained is None:
            items_contained = ["strange keys", "map"]
        self.inventory = items_contained

        self.exit_unlocked = bool_list[0]
        self.exit_opened = bool_list[1]
        self.upstairs_unlocked = bool_list[2]
        self.upstairs_opened = bool_list[3]
        self.map_gotten = bool_list[4]

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    def get_bools(self):
        return self.exit_unlocked, self.exit_opened, self.upstairs_unlocked, self.upstairs_opened, self.map_gotten

    # this prints a description along with a item list
    def print_description_room(self):
        print("It's a large Main Plaza of the mall. There is a path to the 'west wing' too.")
        if self.exit_opened:
            print("The 'exit' is open! I can get out.")
        else:
            print("The 'exit' is locked and I'm trapped.")
        if self.upstairs_opened:
            print("I can get 'upstairs' now at least.")
        else:
            print("The path 'upstairs' is shut for now.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    def print_description_car(self):
        print("It's an old beat up Nissan Laurel. Not that you know what that is. It's seen better days.")

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