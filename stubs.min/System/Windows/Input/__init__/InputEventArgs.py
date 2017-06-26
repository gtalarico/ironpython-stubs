class InputEventArgs(RoutedEventArgs):
    """
    Provides data for input related events.
    
    InputEventArgs(inputDevice: InputDevice, timestamp: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, inputDevice, timestamp):
        """ __new__(cls: type, inputDevice: InputDevice, timestamp: int) """
        pass

    Device = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the input device that initiated this event.

Get: Device(self: InputEventArgs) -> InputDevice

"""

    Timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time when this event occurred.

Get: Timestamp(self: InputEventArgs) -> int

"""


