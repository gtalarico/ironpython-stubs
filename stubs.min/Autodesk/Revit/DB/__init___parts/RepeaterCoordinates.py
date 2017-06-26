class RepeaterCoordinates(object, IDisposable):
    """
    Represents coordinates in the array of repeating references in 0, 1, or 2 dimensions.
    
    RepeaterCoordinates(x: int, y: int)
    RepeaterCoordinates(x: int)
    RepeaterCoordinates()
    """
    def Dispose(self):
        """ Dispose(self: RepeaterCoordinates) """
        pass

    def GetCoordinate(self, dimension):
        """
        GetCoordinate(self: RepeaterCoordinates, dimension: int) -> int
        
            Returns the coordinate in the given dimension.
        
            dimension: The dimension.
            Returns: The coordinate.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RepeaterCoordinates, disposing: bool) """
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
    def __new__(self, x=None, y=None):
        """
        __new__(cls: type, x: int, y: int)
        __new__(cls: type, x: int)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    DimensionCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of dimensions of the coordinates (0, 1 or 2 for zero, one or two dimensional arrays.)

Get: DimensionCount(self: RepeaterCoordinates) -> int

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RepeaterCoordinates) -> bool

"""


