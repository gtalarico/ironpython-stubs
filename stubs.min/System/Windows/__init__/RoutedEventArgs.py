class RoutedEventArgs(EventArgs):
    """
    Contains state information and event data associated with a routed event.
    
    RoutedEventArgs()
    RoutedEventArgs(routedEvent: RoutedEvent)
    RoutedEventArgs(routedEvent: RoutedEvent, source: object)
    """
    def InvokeEventHandler(self, *args): #cannot find CLR method
        """
        InvokeEventHandler(self: RoutedEventArgs, genericHandler: Delegate, genericTarget: object)
            When overridden in a derived class, provides a way to invoke event handlers in a type-specific way, which can increase efficiency over the base implementation.
        
            genericHandler: The generic handler / delegate implementation to be invoked.
            genericTarget: The target on which the provided handler should be invoked.
        """
        pass

    def OnSetSource(self, *args): #cannot find CLR method
        """
        OnSetSource(self: RoutedEventArgs, source: object)
            When overridden in a derived class, provides a notification callback entry point whenever the value of the System.Windows.RoutedEventArgs.Source property of an instance changes.
        
            source: The new value that System.Windows.RoutedEventArgs.Source is being set to.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, routedEvent=None, source=None):
        """
        __new__(cls: type)
        __new__(cls: type, routedEvent: RoutedEvent)
        __new__(cls: type, routedEvent: RoutedEvent, source: object)
        """
        pass

    Handled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates the present state of the event handling for a routed event as it travels the route.

Get: Handled(self: RoutedEventArgs) -> bool

Set: Handled(self: RoutedEventArgs) = value
"""

    OriginalSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the original reporting source as determined by pure hit testing, before any possible System.Windows.RoutedEventArgs.Source adjustment by a parent class.

Get: OriginalSource(self: RoutedEventArgs) -> object

"""

    RoutedEvent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.RoutedEventArgs.RoutedEvent associated with this System.Windows.RoutedEventArgs instance.

Get: RoutedEvent(self: RoutedEventArgs) -> RoutedEvent

Set: RoutedEvent(self: RoutedEventArgs) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a reference to the object that raised the event.

Get: Source(self: RoutedEventArgs) -> object

Set: Source(self: RoutedEventArgs) = value
"""


