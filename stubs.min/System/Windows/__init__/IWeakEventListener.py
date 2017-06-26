class IWeakEventListener:
    """ Provides event listening support for classes that expect to receive events through the WeakEvent pattern and a System.Windows.WeakEventManager. """
    def ReceiveWeakEvent(self, managerType, sender, e):
        """
        ReceiveWeakEvent(self: IWeakEventListener, managerType: Type, sender: object, e: EventArgs) -> bool
        
            Receives events from the centralized event manager.
        
            managerType: The type of the System.Windows.WeakEventManager calling this method.
            sender: Object that originated the event.
            e: Event data.
            Returns: true if the listener handled the event. It is considered an error by the System.Windows.WeakEventManager handling in WPF�to register a listener for an event that the listener does not handle. Regardless, 
             the method should return false if it receives an event that it does not recognize or handle.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

