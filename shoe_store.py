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
            print("The 'elevator' shaft is opened now.")
            if self.elevator_roped:
                print("You can climb down it now.")
            elif "rope" in self.inventory and self.weak_roped:
                print("I used a rope on it but I don't think it's strong enough.")
            else:
                print("There's no way down just yet. You'll have to figure that out.")
        else:
            print("There is an old 'elevator' shaft but the doors are closed.")
        if not self.first_entered:
            print("You doubt anything would fit your digitigrade feet from this place.")
            self.first_entered = True

        print("You can go back the the 'hallway' from here.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    def print_description_elevator(self):
        if not self.elevator_opened:
            print("It's closed right now. I wonder what's inside.")
        elif self.weak_roped:
            print("It's got a rope but I don't think it's safe enough.")
        elif self.elevator_roped:
            print("I should be safe to go down now.")
        else:
            print("I need to figure out how to descend it.")

    # this pops off the items and returns it
    def get_item(self, item):
        if item in self.inventory:
            # if item is rope and you have used it on the elevator it flips that flag back to false
            if item == "rope" and self.weak_roped:
                print("I removed the weak rope from the elevator.")
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
    # if you used the weak rope it adds it to the room inventory and flags you as having used the weak rope
    # if you use the strong rope it just removes the item and does marks you as having used the strong rope
    def fix_elevator(self, item):
        if not self.elevator_opened:
            print("I should open it first.")
            return False
        # if you have used either the weak or strong rope
        if self.weak_roped or self.elevator_roped:
            if self.weak_roped:
                print("I used a rope already but I should try and make the rope stronger.")
                return False
            else:
                print("It's ok for me to climb down now.")
                return False
        else:
            # if the item is the rope it adds to room inventory and flips the flag variable
            if item == "rope":
                print(f"I used the {item}. Maybe I can climb down")
                self.inventory.append(item)
                self.weak_roped = True
                return True
            # if strong rope just flips the strong rope flag
            elif item == "strong rope":
                print(f"I used the {item}. Maybe I can climb down now.")
                self.elevator_roped = True
                return True
            else:
                print(f"I can use the {item} on the elevator.")
                return False

    # tries to go down the shaft. Fails if the strong rope is not used
    def go_elevator(self):
        # if the elevator has not being opened fail
        if not self.elevator_opened:
            print("I should open it first.")
            return False
        # if weak rope has been used and
        if self.weak_roped:
            print("I'm not going down that rope. It's not safe at all.")
            return False
        # if you used the strong rope then you can go
        elif self.elevator_roped:
            print("Ok, it looks safe... Maybe not but here I go.")
            return True
        else:
            print("I'll have to find a way to climb down it.")
            return False
