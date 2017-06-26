class FaceSecondDerivatives(object, IDisposable):
    """ Contains second partial derivatives of a face at a specified point. """
    def Dispose(self):
        """ Dispose(self: FaceSecondDerivatives) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FaceSecondDerivatives, disposing: bool) """
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

Get: IsValidObject(self: FaceSecondDerivatives) -> bool

"""

    MixedDerivative = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mixed derivative.

Get: MixedDerivative(self: FaceSecondDerivatives) -> XYZ

"""

    UUDerivative = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The second derivative with respect to U.

Get: UUDerivative(self: FaceSecondDerivatives) -> XYZ

"""

    VVDerivative = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The second derivative with respect to V.

Get: VVDerivative(self: FaceSecondDerivatives) -> XYZ

"""


