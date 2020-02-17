class ShoeStore:
    def __init__(self, items_contained=None, bool_list=(False, False, False, False)):
        if items_contained is None:
            items_contained = []
        self.inventory = items_contained

        self.first_entered, self.elevator_opened, self.elevator_roped, self.weak_roped = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # returns bools for saving
    def get_bools(self):
        return self.first_entered, self.elevator_opened, self.elevator_roped, self.weak_roped

    # this prints a description along with a item list
    def print_description_room(self):
        print("It’s an old shoe store. It smells of musty leather and fabric. It used to be where a human would go to "
              "\nget some footwear, but now it appears someone had turned it into a living space, judging by the mess "
              "\nthey’ve left.")

        if self.elevator_opened:
            print("The elevator shaft is opened now.")
            if self.elevator_roped:
                print("You can climb down it now.")
            elif "rope" in self.inventory and self.weak_roped:
                print("I used a rope on it but I don't think it's strong enough.")
            else:
                print("There's no way down just yet. You'll have to figure that out.")
        else:
            print("There is an old elevator shaft but the doors are closed.")
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
            if item is "rope":
                self.weak_roped = False
            location = self.inventory.index(item)
            return self.inventory.pop(location)
        else:
            return None

    # dropping item back into room
    def give_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)

    def operate_elevator_doors(self):
        if not self.elevator_opened:
            print("I got the doors opened now.")
            self.elevator_opened = True
        else:
            print("The doors are already opened.")

    # to fix the elevator
    def fix_elevator(self, item):
        if not self.elevator_opened:
            print("I should open it first.")
            return False
        if "rope" in self.inventory or self.elevator_roped:
            if "rope" in self.inventory:
                print("I used a rope already but I should try and make the rope stronger.")
                return False
            else:
                print("It's ok for me to climb down now.")
                return False
        else:
            if item == "rope":
                print(f"I used the {item}. Maybe I can climb down")
                self.inventory.append(item)
                self.weak_roped = True
                return True
            elif item == "strong rope":
                print(f"I used the {item}. Maybe I can climb down now.")
                self.elevator_roped = True
                return True
            else:
                print(f"I can use the {item} on the elevator.")
                return False

    def go_elevator(self):
        if not self.elevator_opened:
            print("I should open it first.")
            return False
        if "rope" in self.inventory:
            print("I'm not going down that rope. It's not safe at all.")
            return False
        elif "strong rope" in self.inventory:
            print("Ok, it looks safe... Maybe not but here I go.")
            return True
        else:
            print("I'll have to find a way to climb down it.")
            return False
