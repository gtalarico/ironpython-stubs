class ProjectPosition(APIObject, IDisposable):
    """
    An object that is used to represent a geographical offset and rotation.
    
    ProjectPosition(ew: float, ns: float, elevation: float, angle: float)
    """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
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

    @staticmethod # known case of __new__
    def __new__(self, ew, ns, elevation, angle):
        """ __new__(cls: type, ew: float, ns: float, elevation: float, angle: float) """
        pass

    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Angle from True North

Get: Angle(self: ProjectPosition) -> float

Set: Angle(self: ProjectPosition) = value
"""

    EastWest = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """East/West offset

Get: EastWest(self: ProjectPosition) -> float

Set: EastWest(self: ProjectPosition) = value
"""

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Elevation above ground level.

Get: Elevation(self: ProjectPosition) -> float

Set: Elevation(self: ProjectPosition) = value
"""

    NorthSouth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """North/South offset

Get: NorthSouth(self: ProjectPosition) -> float

Set: NorthSouth(self: ProjectPosition) = value
"""


