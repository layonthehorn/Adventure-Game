import time


class AnimalDen:
    def __init__(self, items_contained=None, bool_list=(False, False, False, False, False)):
        if items_contained is None:
            items_contained = ["meat"]
        self.inventory = items_contained

        self.animal_drugged, self.entered_after_drugged, self.found_fur, self.meat_just_taken, self.hole_tried = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # returns bools for saving
    def get_bools(self):
        return self.animal_drugged, self.entered_after_drugged, self.found_fur, self.meat_just_taken,self.hole_tried

    # this prints a description along with a item list
    def print_description_room(self):
        print("Once an old utility cabinet, it has now been claimed by some kind of animal. Judging by the sounds "
              "\ncoming from the den's 'hole' of a entrance, you feel you should probably avoid going in there directly.")
        if "meat" not in self.inventory and "drugged meat" not in self.inventory and not self.animal_drugged:
            print("With some sort of animal here I could lay a trap for it.")
        if not self.entered_after_drugged and self.animal_drugged:
            print("Hey, my trap worked!")
            self.entered_after_drugged = True
        if self.animal_drugged:
            print("Hey, looks like some sort of shaggy dog. Kinda fuzzy too, weird 'animal'.")
        elif self.meat_just_taken:
            print("It took my meat and left. I'll have to get more and use something on it.")
            self.meat_just_taken = False
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

    # Vern talking about the odd hole in the wall
    def print_description_hole(self):
        if self.hole_tried:
            print("I'm never going in there again.")
        else:
            print("I wonder what's inside?")

    # Vern enters the hole once and never again
    def enter_hole(self):
        if self.hole_tried:
            print("Nope. Never again...")
        else:
            print("Well I need to try everything I can.")
            print("Vern enters the hole only for a lot of yelling and roaring to echo out of it.")
            print("You Died...")
            time.sleep(5)
            print("Suddenly Vern crawls from the hole and drops to the ground.")
            print("Wow, that thing was not nice. It's a good thing that us lions can fight.")
            self.hole_tried = True

    # talks about the animal
    def print_description_animal(self):
        if self.animal_drugged:
            print("it's a small animal. Pretty fuzzy too.")
            if not self.found_fur:
                self.inventory.append("fur sample")
                print("Hey, that fur might help me out.")
                self.found_fur = True
        else:
            print("I'm sure it's around but I can't see it right now.")

    # if this returns true it does not add the meat item back to the other room.
    # if it returns false then it adds it for the player to try again.
    def drug_animal(self):
        if "meat" in self.inventory:
            print("I should see if something took my bate in the animal den.")
            self.inventory.remove("meat")
            self.meat_just_taken = True
            return False
        elif "drugged meat" in self.inventory:
            print("I should check my trap in the animal den.")
            self.inventory.remove("drugged meat")
            self.animal_drugged = True
            return True
