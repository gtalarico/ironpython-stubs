class RoutedEventHandlerInfo(object):
    """ Provides special handling information to inform event listeners whether specific handlers should be invoked. """
    def Equals(self, *__args):
        """
        Equals(self: RoutedEventHandlerInfo, handlerInfo: RoutedEventHandlerInfo) -> bool
        
            Determines whether the specified System.Windows.RoutedEventHandlerInfo is equivalent to the current System.Windows.RoutedEventHandlerInfo.
        
            handlerInfo: The System.Windows.RoutedEventHandlerInfo to compare to the current System.Windows.RoutedEventHandlerInfo.
            Returns: true if the specified System.Windows.RoutedEventHandlerInfo is equivalent to the current System.Windows.RoutedEventHandlerInfo; otherwise, false.
        Equals(self: RoutedEventHandlerInfo, obj: object) -> bool
        
            Determines whether the specified object is equivalent to the current System.Windows.RoutedEventHandlerInfo.
        
            obj: The object to compare to the current System.Windows.RoutedEventHandlerInfo.
            Returns: true if the specified object is equivalent to the current System.Windows.RoutedEventHandlerInfo; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: RoutedEventHandlerInfo) -> int
        
            Returns a hash code for the current System.Windows.RoutedEventHandlerInfo.
            Returns: A hash code for the current System.Windows.RoutedEventHandlerInfo.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Handler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the event handler.

Get: Handler(self: RoutedEventHandlerInfo) -> Delegate

"""

    InvokeHandledEventsToo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the event handler is invoked when the routed event is marked handled.

Get: InvokeHandledEventsToo(self: RoutedEventHandlerInfo) -> bool

"""


