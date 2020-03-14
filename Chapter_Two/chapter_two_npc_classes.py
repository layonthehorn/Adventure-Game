from abc import ABC, abstractmethod


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
        print(f"My name is {self.name}, I'm in {self.position}, and it is {self.clock.timer}, {self.clock.am_pm}")

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
            self.player.inventory.remove(item)
            self.player.increase_score()
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
