from abc import ABC, abstractmethod
from Chapter_Two.exception_class import ReadOnlyError
import os
import platform


# allows me to clear the screen when playing
def clear():
    operating = platform.system()
    if operating == 'Linux' or operating == "Darwin":
        os.system("clear")
    elif operating == 'Windows':
        os.system('cls')


# a shop class for inheritance
class ShopFunctions:
    """A class for giving shops the needed functions."""
    # class variables for print formatting
    bold = '''\033[1m'''
    end = '''\033[0;0m'''

    # general shop keeper function
    def shop_keeper(self, message="Welcome to my shop!"):
        talking = True
        print(message)
        while talking:
            print("\nSell(s), Buy(b), or Quit(q)?")
            choice = input("").lower()
            clear()
            if choice == "s":
                self.sell_items()
            elif choice == "b":
                self.buy_items()
            elif choice == "q":
                print("Please come again.")
                talking = False
            else:
                print(f"What do you mean by {choice}.")

    # allows you to sell things
    def sell_items(self):
        talking = True
        while talking:
            if len(self.player.inventory) > 1:
                items_sell = []
                for item in self.player.inventory:
                    if item in self.player.sell_item_values:
                        items_sell.append(item)
                # if list is not empty allow selling
                if items_sell:
                    for number, item in enumerate(items_sell):
                        print(item, end=", ")
                        if (number + 1) % 4 == 0:
                            print("")
                    print("\n")
                    choice = input("\nSell what? q to quit. ").lower()
                    clear()
                    # if you do not have the thing you are trying to sell
                    if choice not in self.player.inventory and choice != "q":
                        print(f"You don't have a(n) {self.bold + choice + self.end} to sell")
                    # if the item has a value in game
                    elif choice in self.player.sell_item_values:
                        print("I'll take that. Thank you!")
                        # sells it
                        self.sell(choice)
                    elif choice == "q":
                        talking = False
                    else:
                        print(f"I don't want to buy a(n) {self.bold + choice + self.end}")
                else:
                    print("You don't have anything I want to buy.")
                    talking = False

            else:
                print("You don't have anything to sell.")
                talking = False

    # allows you to buy things
    def buy_items(self):
        talking = True
        while talking:
            if len(self.shop_inventory) > 0:
                for number, item in enumerate(self.shop_inventory):
                    print(item, end=", ")
                    if (number + 1) % 4 == 0:
                        print("")
                print("\n")
                choice = input("\nBuy what? q to quit. ").lower()
                clear()
                # if they have it to sell you
                if choice in self.shop_inventory:
                    # if you have enough money
                    if self.player.player_wallet >= self.player.buy_item_values.get(choice):
                        self.buy(choice)
                    else:
                        # if you are too poor
                        print(f"You can't afford the {self.bold + choice + self.end}. You need {self.player.buy_item_values.get(choice) - self.player.player_wallet}.")
                elif choice == "q":
                    talking = False
                else:
                    print(f"I don't have a(n) {self.bold + choice + self.end} to sell you.")
            else:
                print("I am totally out of things to sell you.")
                talking = False

    # controls selling items
    def sell(self, item):
        self.player.inventory.remove(item)
        if item in self.player.buy_item_values:
            self.shop_inventory.append(item)
        print(f"You sold the {self.bold + item + self.end}.")
        self.player.change_player_wallet(self.player.sell_item_values.get(item, 0))

    # controls buying items
    def buy(self, item):
        self.player.inventory.append(item)
        self.shop_inventory.remove(item)
        print(f"You bought the {self.bold + item + self.end}.")
        self.player.change_player_wallet(self.player.buy_item_values.get(item, 0))


class NPC(ABC):
    """A base class to create NPCs from."""

    @abstractmethod
    def talk_to_npc(self):
        pass

    @abstractmethod
    def look_npc(self):
        pass

    @abstractmethod
    def check_move(self):
        pass

    @abstractmethod
    def use_item(self, item):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def position(self):
        pass

    @position.setter
    @abstractmethod
    def position(self, value):
        pass

    @property
    @abstractmethod
    def alive(self):
        pass

    @alive.setter
    @abstractmethod
    def alive(self, new_value):
        pass


class ScavengerNPC(NPC):
    """A scavenger that moves from the ruins to the general store and back."""
    def __init__(self, timer, player):
        self.player = player
        self.clock = timer
        self.__position = "ruined street"
        self.__alive = True
        self.name = "scavenger"
        self.inventory = []

    def __str__(self):
        return f"My name is {self.name}, I'm in {self.position}, and it is {self.clock.display_human_time()}, {self.clock.am_pm}"

    @property
    def alive(self):
        return self.__alive

    @alive.setter
    def alive(self, new_value):
        if new_value is True or new_value is False:
            self.__alive = new_value
        else:
            print("Bad input, need a pure boolean value.")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if value in ("town center", "ruined street", "general store"):
            self.__position = value
        else:
            print("Error, Bad location to move.")

    def check_move(self):
        # 9:00 AM
        if self.clock.timer == 900:
            # move to town center
            self.position = "town center"
            return True
        # 10:00 AM
        elif self.clock.timer == 1000:
            # move to general store
            self.position = "general store"
            return True
        # 1:00 PM
        elif self.clock.timer == 1300:
            # move back to town center
            self.position = "town center"
            return True
        # 2:00 PM
        elif self.clock.timer == 1400:
            # move to ruined street again
            self.position = "ruined street"
            return True
        else:
            return False

    def use_item(self, item):
        print("It won't help.")
        return False

    def talk_to_npc(self):
        print("You should be able to talk to me. Hello!")

    def look_npc(self):
        print("It's a scavenger.")


class OrganPlayer(NPC):
    """An organ player that starts in the mansion and you can give items."""
    def __init__(self, timer, player):
        self.clock = timer
        self.player = player
        self.__position = "tower peak"
        self.__alive = True
        self.name = "organ player"
        self.inventory = []

    def __str__(self):
        return f"My name is {self.name}, I'm in {self.position}, and it is {self.clock.display_human_time()}, {self.clock.am_pm}"

    @property
    def alive(self):
        return self.__alive

    @alive.setter
    def alive(self, new_value):
        if new_value is True or new_value is False:
            self.__alive = new_value
        else:
            print("Bad input, need a pure boolean value.")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if value in ("tower peak", "tower entrance"):
            self.__position = value
        else:
            print("Error, Bad location to move.")

    def check_move(self):
        if "music sheet" in self.inventory and self.position == "tower peak":
            self.position = "tower entrance"
            return True
        else:
            return False

    def use_item(self, item):
        if item == "music sheet":
            print("That's what I needed! Thank you!")
            print("I must go and read it right away!")
            self.inventory.append(item)
            self.player.inventory.remove(item)
            self.player.score += 1
        else:
            print("No, no no. This won't do at all. I need music, my oddly furred man.")

    def talk_to_npc(self):
        if self.position == "tower peak":
            print("Hello I am playing music up here. Perfect for a puzzle, huh?")
            print(f"My name is {self.name}, I'm in {self.position}, and it is {self.clock.timer}, {self.clock.am_pm}")
        else:
            print("Think of them moving to this new location after I get what I want.")
            print(f"My name is {self.name}, I'm in {self.position}, and it is {self.clock.timer}, {self.clock.am_pm}")

    def look_npc(self):
        if self.position == "tower peak":
            print("It's a organ player. He is busy playing his organ.")
        else:
            print("It's a organ player. He's standing around waiting for something.")


class GeneralStoreOwner(NPC, ShopFunctions):
    """An organ player that starts in the mansion and you can give items."""
    def __init__(self, timer, player):
        self.clock = timer
        self.player = player
        self.__position = "general store"
        self.__alive = True
        self.name = "shop keeper"
        self.shop_inventory = []

    def __str__(self):
        return f"My name is {self.name}, I'm in {self.position}, and it is {self.clock.display_human_time()}, {self.clock.am_pm}"

    def look_npc(self):
        print("She's a friendly lioness shop keeper. Very attractive if I say so myself.", end=" ")
        if self.shop_inventory:
            print("Looks like there are thing to buy if I wanted.")
        else:
            print("She's all sold out of everything.")

    # she never moves
    def check_move(self):
        return False

    def talk_to_npc(self):

        while True:
            print("You want to 'talk' or 'shop'? (q to exit)")
            choice = input("").lower()
            clear()
            if choice == "talk":
                print("Some talking function here.")
            elif choice == "shop":
                self.shop_keeper("The lioness shows you her stock of goods.")
            elif choice == "q":
                break
            else:
                print("Do what now?")

    def use_item(self, item):
        print(f"She won't want the {item}.")

    @property
    def alive(self):
        return self.__alive

    @alive.setter
    def alive(self, new_value):
        # cannot be killed or removed from game
        raise ReadOnlyError(new_value)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        raise ReadOnlyError(value)
