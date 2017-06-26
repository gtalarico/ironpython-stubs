class MouseButtonEventArgs(MouseEventArgs):
    """
    Provides data for mouse button related events.
    
    MouseButtonEventArgs(mouse: MouseDevice, timestamp: int, button: MouseButton)
    MouseButtonEventArgs(mouse: MouseDevice, timestamp: int, button: MouseButton, stylusDevice: StylusDevice)
    """
    @staticmethod # known case of __new__
    def __new__(self, mouse, timestamp, button, stylusDevice=None):
        """
        __new__(cls: type, mouse: MouseDevice, timestamp: int, button: MouseButton)
        __new__(cls: type, mouse: MouseDevice, timestamp: int, button: MouseButton, stylusDevice: StylusDevice)
        """
        pass

    ButtonState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the state of the button associated with the event.

Get: ButtonState(self: MouseButtonEventArgs) -> MouseButtonState

"""

    ChangedButton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the button associated with the event.

Get: ChangedButton(self: MouseButtonEventArgs) -> MouseButton

"""

    ClickCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of times the button was clicked.

Get: ClickCount(self: MouseButtonEventArgs) -> int

"""


