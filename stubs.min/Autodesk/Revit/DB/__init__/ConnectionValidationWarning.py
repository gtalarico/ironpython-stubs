class ConnectionValidationWarning(object, IDisposable):
    """
    Contains information about a specific connection validation problem.
    
    ConnectionValidationWarning(resolution: ConnectionResolution, reason: ConnectionWarning, part1: ElementId, part2: ElementId)
    """
    def Dispose(self):
        """ Dispose(self: ConnectionValidationWarning) """
        pass

    def GetParts(self):
        """
        GetParts(self: ConnectionValidationWarning) -> ISet[ElementId]
        
            Get ElementIds of affected parts.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ConnectionValidationWarning, disposing: bool) """
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

    @staticmethod # known case of __new__
    def __new__(self, resolution, reason, part1, part2):
        """ __new__(cls: type, resolution: ConnectionResolution, reason: ConnectionWarning, part1: ElementId, part2: ElementId) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ConnectionValidationWarning) -> bool

"""

    Reason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enumeration for reason of warning.

Get: Reason(self: ConnectionValidationWarning) -> ConnectionWarning

"""

    Resolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enumeration for resolution that was applied.

Get: Resolution(self: ConnectionValidationWarning) -> ConnectionResolution

"""


