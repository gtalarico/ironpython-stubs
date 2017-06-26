class FamilyPointLocation(APIObject, IDisposable):
    """ Data corresponding to the point locations in certain types of Family Symbols. """
    def Dispose(self):
        """ Dispose(self: FamilyPointLocation, A_0: bool) """
        pass

    def GetLocation(self):
        """
        GetLocation(self: FamilyPointLocation) -> Transform
        
            Gets the location of the point.
            Returns: The location of the point.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FamilyPointLocation, disposing: bool)ReleaseUnmanagedResources(self: APIObject) """
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

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FamilyPointLocation) -> bool

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The location of the point.

Get: Location(self: FamilyPointLocation) -> Transform

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the corresponding reference point in the Family document.

Get: Name(self: FamilyPointLocation) -> str

"""


