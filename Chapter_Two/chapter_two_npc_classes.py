from abc import ABC, abstractmethod


class NPC(ABC):
    """A base class to create NPCs from."""

    @abstractmethod
    def talk_to_npc(self):
        pass

    @abstractmethod
    def move_position(self, new_location):
        pass

    @abstractmethod
    def check_move(self):
        pass


class ScavengerNPC(NPC):
    """A scavenger that moves from the ruins to the general store and back."""
    def __init__(self, timer):
        self.clock = timer
        self.position = "ruined street"
        self.name = "scavenger"

    def move_position(self, new_location):
        pass

    def check_move(self):
        # to do, move around at certain times
        if 6 <= self.clock.timer <= 6.1:
            # move to town center
            self.position = "town center"
            return True
        elif 7 <= self.clock.timer <= 7.1:
            # move to general store
            self.position = "general store"
            return True
        elif 9 <= self.clock.timer <= 9.1:
            # move back to town center
            self.position = "town center"
            return True
        elif 11 <= self.clock.timer <= 11.1:
            # move to ruined street again
            self.position = "ruined street"
            return True
        else:
            return False

    def talk_to_npc(self):
        print("You should be able to talk to me. Hello!")
        print(f"My name is {self.name}, I'm in {self.position}, and it is {self.clock.timer}, {self.clock.am_pm}")
