class Line(Curve, IDisposable):
    """ A line in space. """
    @staticmethod
    def CreateBound(endpoint1, endpoint2):
        """
        CreateBound(endpoint1: XYZ, endpoint2: XYZ) -> Line
        
            Creates a new instance of a bound linear curve.
        
            endpoint1: The first line endpoint.
            endpoint2: The second line endpoint.
            Returns: The new bound line.
        """
        pass

    @staticmethod
    def CreateUnbound(origin, direction):
        """
        CreateUnbound(origin: XYZ, direction: XYZ) -> Line
        
            Creates a new instance of an unbound linear curve.
        
            origin: The origin of the unbound line.
            direction: The direction of the unbound line.
            Returns: The new unbound line.
        """
        pass

    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: GeometryObject) """
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

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the direction of the line.

Get: Direction(self: Line) -> XYZ

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the origin of the line.

Get: Origin(self: Line) -> XYZ

"""


