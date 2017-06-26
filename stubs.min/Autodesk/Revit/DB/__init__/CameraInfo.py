class CameraInfo(object, IDisposable):
    """ An object holding information about the projection mapping of a 3D view. """
    def Dispose(self):
        """ Dispose(self: CameraInfo) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: CameraInfo, disposing: bool) """
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

    FarDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance from eye point to far plane of view frustum along the view direction.

Get: FarDistance(self: CameraInfo) -> float

"""

    HorizontalExtent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance between left and right planes on the target plane.

Get: HorizontalExtent(self: CameraInfo) -> float

"""

    IsPerspective = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies whether the projection is orthographic or perspective

Get: IsPerspective(self: CameraInfo) -> bool

"""

    IsPespective = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies whether the projection is orthographic or perspective

Get: IsPespective(self: CameraInfo) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: CameraInfo) -> bool

"""

    NearDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance from eye point to near plane of view frustum along the view direction.

Get: NearDistance(self: CameraInfo) -> float

"""

    RightOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance that the target plane is offset towards the right
   where right is normal to both Up direction and View direction.
   This offset shifts both left and right planes.

Get: RightOffset(self: CameraInfo) -> float

"""

    TargetDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance from eye point along view direction to target plane.

Get: TargetDistance(self: CameraInfo) -> float

"""

    UpOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance that the target plane is offset in the direction of
   the Up direction. This offset shifts both top and bottom planes.

Get: UpOffset(self: CameraInfo) -> float

"""

    VerticalExtent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance between top and bottom planes on the target plane.

Get: VerticalExtent(self: CameraInfo) -> float

"""


