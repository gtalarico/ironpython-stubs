class ViewOrientation3D(object, IDisposable):
    """
    Container for the point and vectors which define View3D's orientation.
    
    ViewOrientation3D(eyePosition: XYZ, upDirection: XYZ, forwardDirection: XYZ)
    """
    def Dispose(self):
        """ Dispose(self: ViewOrientation3D) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ViewOrientation3D, disposing: bool) """
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
    def __new__(self, eyePosition, upDirection, forwardDirection):
        """ __new__(cls: type, eyePosition: XYZ, upDirection: XYZ, forwardDirection: XYZ) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    EyePosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The eye position point

Get: EyePosition(self: ViewOrientation3D) -> XYZ

"""

    ForwardDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The forward direction vector

Get: ForwardDirection(self: ViewOrientation3D) -> XYZ

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ViewOrientation3D) -> bool

"""

    UpDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The up direction vector

Get: UpDirection(self: ViewOrientation3D) -> XYZ

"""


