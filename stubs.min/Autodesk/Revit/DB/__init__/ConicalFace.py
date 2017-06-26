class ConicalFace(Face, IDisposable):
    """ A conical face of a 3d solid or open shell. """
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

    Axis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Axis of the surface.

Get: Axis(self: ConicalFace) -> XYZ

"""

    HalfAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Half angle of the surface.

Get: HalfAngle(self: ConicalFace) -> float

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Origin of the surface.

Get: Origin(self: ConicalFace) -> XYZ

"""


