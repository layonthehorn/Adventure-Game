

class Error(Exception):
    """Base class for exceptions."""
    pass


class ReadOnlyError(Error):
    """Throws error if attempting to set a read only variable."""
    def __init__(self, item):
        super().__init__(f"Failed to set read only variable to {item}")


class ChangeLocationError(Error):
    """Throws this error if attempting to move to unknown place."""
    def __init__(self, area):
        super().__init__(f"Failed to find matching area for {area}.")


class NPCLocationError(Error):
    """Throws this error if attempting to place NPC in unknown place."""
    def __init__(self, name, area):
        super().__init__(f"Failed to find matching area for {area} when setting up {name}.")


class ChangeNPCLocationError(Error):
    """An error to tell me that I messed up naming a room correctly when moving."""
    def __init__(self, name, area):
        super().__init__(f"Failed to find matching area for {area} when moving {name}.")
