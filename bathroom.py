import time


class Bathroom:
    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = []
        self.inventory = items_contained

        self.looked_dryer, self.cabinet_looked = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # returns bools for saving
    def get_bools(self):
        return (self.looked_dryer, self.cabinet_looked)

    # this prints a description along with a item list
    def print_description_room(self):
        print("It’s an old restroom. You can probably guess what "
              "\nwent on in here yourself. The old toilet blocks are heavily damaged and covered in graffiti. The smell "
              "\nisn’t much better either. There is an old first aid cabinet on the wall and a hand drier along side it. ")
        print("You can go back to the 'hallway'.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    def print_description_dryer(self):
        if not self.looked_dryer:
            print("You look over the dryer and accidentally turn it on.")
            print("Yikes!")
            print("Vern's fur frizzes up and he jumps back.")
            time.sleep(1)
            print("Dumb thing...")
            self.looked_dryer = True
        else:
            print("I'm not messing with it again.")

    def print_description_graffiti(self):
        print("It's a lot of crudely drawn shapes and messages.")
        print("You look it and try to make something out.")
        time.sleep(1)
        print("I respect your political beliefs even if I do not share them.")
        print("You look nice today! and\n404167")
        print("Huh? Much nicer than you'd think it would have been.")

    def print_description_medical(self):
        if not self.cabinet_looked:
            print("Lots of nasty old bandages and... wait!\nSome useful drugs remain.")
            self.inventory.append("drugs")
            self.cabinet_looked = True
        elif "drugs" in self.inventory:
            print("I should get those drugs. Might need them for something.")
        else:
            print("There's nothing else of value here.")

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
