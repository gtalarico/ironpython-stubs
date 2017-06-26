class MEPConnectorInfo(object, IDisposable):
    """ MEP connector information. """
    def Dispose(self):
        """ Dispose(self: MEPConnectorInfo) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: MEPConnectorInfo, disposing: bool) """
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

    IsPrimary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if this is the primary connector.

Get: IsPrimary(self: MEPConnectorInfo) -> bool

"""

    IsSecondary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if this is the secondary connector.

Get: IsSecondary(self: MEPConnectorInfo) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: MEPConnectorInfo) -> bool

"""

    LinkedConnector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The linked connector or ll if there is no linked connector

Get: LinkedConnector(self: MEPConnectorInfo) -> Connector

"""


