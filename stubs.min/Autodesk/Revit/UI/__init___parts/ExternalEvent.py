class ExternalEvent(object, IDisposable):
    """ A class that represent an external event. """
    @staticmethod
    def Create(handler):
        """
        Create(handler: IExternalEventHandler) -> ExternalEvent
        
            Creates an instance of external event.
        
            handler: An instance of IExternalEventHandler which will execute the event.
            Returns: An instance of ExternalEvent class, which will be used to invoke the event
        """
        pass

    @staticmethod
    def CreateJournalable(handler):
        """
        CreateJournalable(handler: IExternalEventHandler) -> ExternalEvent
        
            Creates an instance of external event which will have the ability to record its 
             executions in the journal.
        
        
            handler: An instance of IExternalEventHandler which will execute the event.
            Returns: An instance of ExternalEvent class, which will be used to invoke the event
        """
        pass

    def Dispose(self):
        """ Dispose(self: ExternalEvent) """
        pass

    def getNativeObject(self, *args): #cannot find CLR method
        """ getNativeObject(self: ExternalEvent) -> ExternalEvent* """
        pass

    def Raise(self):
        """
        Raise(self: ExternalEvent) -> ExternalEventRequest
        
            Instructing Revit to raise (signal) the external event.
            Returns: The result of event raising request. If the request is 'Accepted',
           the 
             event would be added to the event queue and its handler will
           be executed in 
             the next event-processing cycle.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ExternalEvent, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsPending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checking whether an event has been raised but not yet executed.

Get: IsPending(self: ExternalEvent) -> bool

"""


