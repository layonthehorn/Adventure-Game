class UpstairsHallway:
    def __init__(self, items_contained=None, bool_list=(False, False)):
        if items_contained is None:
            items_contained = []
        self.inventory = items_contained

        self.book_looked, self.furniture_looked = bool_list

    # returns the items in the room.
    def get_inventory(self):
        return self.inventory

    # returns bools for saving
    def get_bools(self):
        return self.book_looked, self.furniture_looked

    # this prints a description along with a item list
    def print_description_room(self):
        print("You climb up the old escalator onto the upper plaza of the mall. It appears someone lived here for "
              "\nsome time, judging by the repurposed 'furniture' and empty food packaging all over the floor. Whoever "
              "\nlived here defended it fiercely, judging by all the old casings and bullet holes.")
        print("You can go to 'down stairs', 'shoe store', 'animal den', and 'bathroom'.")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"There is a(n) {item}")

    # for look furn
    def print_description_furniture(self):
        print("It's a bunch of stacked furniture made into a barricade. Someone was trying to defend this place.")
        if not self.furniture_looked:
            print("Hey, what is this this? A keyring?")
            self.inventory.append("cheetah keyring")
            self.furniture_looked = True
            print("And an old 'book' too...")
            if not self.book_looked:
                print("I wonder what's in it?")
        else:
            if "cheetah keyring" in self.inventory:
                print("What an odd keyring.")
            print("There is an old 'book'.")
            if not self.book_looked:
                print("I wonder what's in it?")

    # for look book
    def print_description_book(self):
        print("It's an old cracked 'book' that's stained with blood.")
        if not self.book_looked:
            print("I might want to read it. Maybe There's something useful inside.")

    # for oper book
    def read_book(self):
        reading = True
        if not self.book_looked:
            print("Time to take a look at this thing.")
            self.book_looked = True
        while reading:
            page = input("What page to read? (one, two, three, four, and end to quit reading.)\n")
            if page == "one":
                print("This page looks earlier than the rest.")
                print("Martha changed today. She's one of those felines now. \nWe had to lock the pet shop for her own "
                      "good. We had to lock it against exotic animals. \nI'm still surprised it had that functionality "
                      "built in.")
                print("She's still the same woman I fell in love with but still. It feels wrong she's supposed to be "
                      "a human.")
                print("I'll have to make sure the others don't hurt her. They are getting worried and I don't like "
                      "\nhow they are looking at her.")
                print("")
            elif page == "two":
                print("Things have gone well so far. I've helped Martha get used to not eating meat all the time again.")
                print("Poor sweetheart. She doesn't even remember being human at all.")
                print("What am I going to do?")
                print("")
            elif page == "three":
                print("Others are changing too now. This is getting out of hand.")
                print("I had convinced the others that Martha couldn't infect them but now they aren't listening to me.")
                print("I can't let them hurt her. We survived the end together and")
                print("The journal ends suddenly here...")
                print("")
            elif page == "four":
                print("This page is dated much older than the rest.")
                print("Hey, I found a sweet new place to live for a while. Gotta clean out all the old bodies first though.")
                print("Weird cat things. Everywhere they show up things go to shit.")
                # Vern talking to himself
                print("\nVern taps his foot on the ground and growls to himself.")
                print("Hey! jackass... Humans always seem to think themselves wonderful.")
                print("")
            elif page == "end":
                print("I guess that's all I need from it.")
                reading = False
            else:
                print(f"I can't find page {page}.")

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
