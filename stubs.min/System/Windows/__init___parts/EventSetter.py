class EventSetter(SetterBase):
    """
    Represents an event setter in a style. Event setters invoke the specified event handlers in response to events.
    
    EventSetter()
    EventSetter(routedEvent: RoutedEvent, handler: Delegate)
    """
    @staticmethod # known case of __new__
    def __new__(self, routedEvent=None, handler=None):
        """
        __new__(cls: type)
        __new__(cls: type, routedEvent: RoutedEvent, handler: Delegate)
        """
        pass

    Event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the particular routed event that this System.Windows.EventSetter responds to.

Get: Event(self: EventSetter) -> RoutedEvent

Set: Event(self: EventSetter) = value
"""

    HandledEventsToo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that determines whether the handler assigned to the setter should still be invoked, even if the event is marked handled in its event data.

Get: HandledEventsToo(self: EventSetter) -> bool

Set: HandledEventsToo(self: EventSetter) = value
"""

    Handler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the reference to a handler for a routed event in the setter.

Get: Handler(self: EventSetter) -> Delegate

Set: Handler(self: EventSetter) = value
"""


