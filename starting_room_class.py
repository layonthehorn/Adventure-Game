import time


class StartingRoom:
    def __init__(self, items_contained=None, bool_list=(False, False, False)):
        if items_contained is None:
            items_contained = ["fuse", "bag of catnip"]
        self.inventory = items_contained
        self.fuse_box, self.door_opened, self.robot_fixed = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    def get_bools(self):
        return (self.fuse_box, self.door_opened, self.robot_fixed)

    # this prints a description along with a item list
    def print_description_room(self):
        print("The room is dark and blasted out.")
        print("The room smells of mould and rust. There is a disabled robot in the corner, an entry to \na side room "
              "and there is a door that appears to be locked. Maybe it’s connected to that fuse box?.")
        if self.door_opened:
            print("The door to 'outside' is open.")
        else:
            print("There is a old door and a odd box next to it.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    # this prints a description of the fuse box
    def print_description_box(self):
        if not self.fuse_box:
            print("It's an old fuse box....")
            time.sleep(1)
            print("And of course it's lacking a fuse.")
        else:
            print("Hey, it's working now!")

    def look_robot(self):
        if not self.robot_fixed:
            print("It's a robot and it has a fuse!")
        else:
            print("I took the robots fuse.")

    # this pops off the items and returns it
    def get_item(self, item):

        if not self.robot_fixed and item == "fuse":
            print("The fuse is stuck. I need to get it loose first.")
            return None
        elif item in self.inventory:
            location = self.inventory.index(item)
            return self.inventory.pop(location)
        else:
            return None

    # dropping item back into room
    def give_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)

    # attempts to fix fuse box
    def fix_fuse_box(self, item):
        if not self.fuse_box:
            if item == "fuse":
                print("the fuse box is now working!")
                self.fuse_box = True
                return True
            else:
                print(f"I can't use {item} with the fuse box.")
                return False
        else:
            print("There is nothing else I need to do here.")
            return False

    # used to get fuse loose from robot
    def fix_robot(self, item):
        if not self.robot_fixed:
            if item == "wrench":
                print("The robot's fuse is loose!")
                self.robot_fixed = True
                return True
            else:
                print(f"I can't use {item} with the robot.")
                return False
        else:
            print("I don't have to mess with it anymore.")
            return False

    # tries to open door will fail if fuse box is not working.
    def open_door(self):
        if not self.fuse_box:
            print("The door is stuck. Looks like it's out of power.")
        elif self.door_opened:
            print("The door is already opened.")
        elif self.fuse_box and not self.door_opened:
            print("The door has opened! Now I can go outside!")
            self.door_opened = True