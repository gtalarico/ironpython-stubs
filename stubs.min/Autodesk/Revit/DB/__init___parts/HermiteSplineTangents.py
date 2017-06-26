class HermiteSplineTangents(object, IDisposable):
    """
    This class indicates tangency at the start, the end, or both ends of the curve.
    
    HermiteSplineTangents()
    """
    def Dispose(self):
        """ Dispose(self: HermiteSplineTangents) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: HermiteSplineTangents, disposing: bool) """
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

    EndTangent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The tangent vector at the end of the curve.

Get: EndTangent(self: HermiteSplineTangents) -> XYZ

Set: EndTangent(self: HermiteSplineTangents) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: HermiteSplineTangents) -> bool

"""

    StartTangent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The tangent vector at the start of the curve.

Get: StartTangent(self: HermiteSplineTangents) -> XYZ

Set: StartTangent(self: HermiteSplineTangents) = value
"""


