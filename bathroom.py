class Bathroom:
    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = ["drugs"]
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
        print("It’s an old restroom. You can probably guess what "
              "went on in here yourself. The old toilet blocks are heavily damaged and covered in graffiti. The smell "
              "isn’t much better either. There is an old first aid cabinet on the wall. ")
        print("You can go back to the 'hallway'.")
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
