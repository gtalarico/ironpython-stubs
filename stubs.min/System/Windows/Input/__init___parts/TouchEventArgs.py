class TouchEventArgs(InputEventArgs):
    """
    Provides data for touch input events.
    
    TouchEventArgs(touchDevice: TouchDevice, timestamp: int)
    """
    def GetIntermediateTouchPoints(self, relativeTo):
        """
        GetIntermediateTouchPoints(self: TouchEventArgs, relativeTo: IInputElement) -> TouchPointCollection
        
            Returns all touch points that were collected between the most recent and previous touch events.
        
            relativeTo: The element that defines the coordinate space.
            Returns: All touch points that were collected between the most recent and previous touch events.
        """
        pass

    def GetTouchPoint(self, relativeTo):
        """
        GetTouchPoint(self: TouchEventArgs, relativeTo: IInputElement) -> TouchPoint
        
            Returns the current position of the touch device relative to the specified element.
        
            relativeTo: The element that defines the coordinate space.
            Returns: The current position of the touch device relative to the specified element.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, touchDevice, timestamp):
        """ __new__(cls: type, touchDevice: TouchDevice, timestamp: int) """
        pass

    TouchDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the touch that generated the event.

Get: TouchDevice(self: TouchEventArgs) -> TouchDevice

"""


