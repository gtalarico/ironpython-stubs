class KeyboardEventArgs(InputEventArgs):
    """
    Provides data for keyboard-related events.
    
    KeyboardEventArgs(keyboard: KeyboardDevice, timestamp: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, keyboard, timestamp):
        """ __new__(cls: type, keyboard: KeyboardDevice, timestamp: int) """
        pass

    KeyboardDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the keyboard device associated with the input event.

Get: KeyboardDevice(self: KeyboardEventArgs) -> KeyboardDevice

"""


