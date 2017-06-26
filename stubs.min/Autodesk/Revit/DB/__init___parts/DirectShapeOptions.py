class DirectShapeOptions(object, IDisposable):
    """ This class is used to control behavior of a DirectShape or a DirectShapeType object. """
    def Dispose(self):
        """ Dispose(self: DirectShapeOptions) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: DirectShapeOptions, disposing: bool) """
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

Get: IsValidObject(self: DirectShapeOptions) -> bool

"""

    ReferencingOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether or not the geometry stored in a DirectShape or DirectShapeType object may be referenced.

Get: ReferencingOption(self: DirectShapeOptions) -> DirectShapeReferencingOption

Set: ReferencingOption(self: DirectShapeOptions) = value
"""

    RoomBoundingOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies whether the DirectShape supports an option for the "Room Bounding" parameter to permit participation in room boundary calculations.

Get: RoomBoundingOption(self: DirectShapeOptions) -> DirectShapeRoomBoundingOption

"""


