class SolidCurveIntersectionOptions(object, IDisposable):
    """
    This class contains the options used to calculate the intersection between a solid and a curve.
    
    SolidCurveIntersectionOptions()
    """
    def Dispose(self):
        """ Dispose(self: SolidCurveIntersectionOptions) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: SolidCurveIntersectionOptions, disposing: bool) """
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

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: SolidCurveIntersectionOptions) -> bool

"""

    ResultType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of results expected by the calculation.  The default is CurveSegmentsInside.

Get: ResultType(self: SolidCurveIntersectionOptions) -> SolidCurveIntersectionMode

Set: ResultType(self: SolidCurveIntersectionOptions) = value
"""


