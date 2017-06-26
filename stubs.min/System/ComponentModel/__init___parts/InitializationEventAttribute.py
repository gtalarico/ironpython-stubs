class InitializationEventAttribute(Attribute, _Attribute):
    """
    Specifies which event is raised on initialization. This class cannot be inherited.
    
    InitializationEventAttribute(eventName: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, eventName):
        """ __new__(cls: type, eventName: str) """
        pass

    EventName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the initialization event.

Get: EventName(self: InitializationEventAttribute) -> str

"""


