class EventRoute(object):
    """
    Represents the container for the route to be followed by a routed event.
    
    EventRoute(routedEvent: RoutedEvent)
    """
    def Add(self, target, handler, handledEventsToo):
        """
        Add(self: EventRoute, target: object, handler: Delegate, handledEventsToo: bool)
            Adds the specified handler for the specified target to the route.
        
            target: Specifies the target object of which the handler is to be added to the route.
            handler: Specifies the handler to be added to the route.
            handledEventsToo: Indicates whether or not the listener detects events that have already been handled.
        """
        pass

    def PeekBranchNode(self):
        """
        PeekBranchNode(self: EventRoute) -> object
        
            Returns the top-most element on the event route stack at which two logical trees diverge.
            Returns: The top-most element on the event route stack at which two logical trees diverge.
        """
        pass

    def PeekBranchSource(self):
        """
        PeekBranchSource(self: EventRoute) -> object
        
            Returns the source for the top-most element on the event route stack at which two logical trees diverge.
            Returns: The source for the top-most element on the event route stack at which two logical trees diverge.
        """
        pass

    def PopBranchNode(self):
        """
        PopBranchNode(self: EventRoute) -> object
        
            Returns the top-most node on the event route stack at which two logical trees diverge.
            Returns: The top-most node on the event route stack at which two logical trees diverge.
        """
        pass

    def PushBranchNode(self, node, source):
        """
        PushBranchNode(self: EventRoute, node: object, source: object)
            Adds the top-most node to the event route stack at which two logical trees diverge.
        
            node: The top-most element on the event route stack at which two logical trees diverge.
            source: The source for the top-most element on the event route stack at which two logical trees diverge.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, routedEvent):
        """ __new__(cls: type, routedEvent: RoutedEvent) """
        pass

