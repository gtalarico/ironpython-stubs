class FamilyPointPlacementReference(APIObject, IDisposable):
    """
    This object represents data corresponding to the placement references in a
    certain types of Family Instances (see examples listed below).
    """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def getCDA(self, *args): #cannot find CLR method
        """ getCDA(self: FamilyPointPlacementReference) -> ControlledDocAccess* """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The location of the point.

Get: Location(self: FamilyPointPlacementReference) -> Transform

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the corresponding reference point in the Family document.

Get: Name(self: FamilyPointPlacementReference) -> str

"""

    PointReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The reference on which the point depends on.

Get: PointReference(self: FamilyPointPlacementReference) -> Reference

"""


