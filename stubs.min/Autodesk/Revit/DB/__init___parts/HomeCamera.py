class HomeCamera(object, IDisposable):
    """
    A structure that contains information about the camera and view for the Home view orientation stored in the model.
    
    HomeCamera(other: HomeCamera)
    """
    def Dispose(self):
        """ Dispose(self: HomeCamera) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: HomeCamera, disposing: bool) """
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
    def __new__(self, other):
        """ __new__(cls: type, other: HomeCamera) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BottomAngleOfFieldOfView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The bottom angle of the field of view.

Get: BottomAngleOfFieldOfView(self: HomeCamera) -> float

"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The zoom or orbit center.

Get: Center(self: HomeCamera) -> XYZ

"""

    EyePosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The eye position point.

Get: EyePosition(self: HomeCamera) -> XYZ

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: HomeCamera) -> bool

"""

    LeftAngleOfFieldOfView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The left angle of the field of view.

Get: LeftAngleOfFieldOfView(self: HomeCamera) -> float

"""

    OrthogonalProjectionHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The height of orthogonal projection view volume.

Get: OrthogonalProjectionHeight(self: HomeCamera) -> float

"""

    OrthogonalProjectionWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The width of orthogonal projection view volume.

Get: OrthogonalProjectionWidth(self: HomeCamera) -> float

"""

    Pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The pivot point.

Get: Pivot(self: HomeCamera) -> XYZ

"""

    RightAngleOfFieldOfView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The right angle of the field of view.

Get: RightAngleOfFieldOfView(self: HomeCamera) -> float

"""

    TopAngleOfFieldOfView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The top angle of the field of view.

Get: TopAngleOfFieldOfView(self: HomeCamera) -> float

"""

    UpDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The up direction vector.

Get: UpDirection(self: HomeCamera) -> XYZ

"""

    ViewId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the view which is associated to this document's Home view orientation.

Get: ViewId(self: HomeCamera) -> ElementId

"""


