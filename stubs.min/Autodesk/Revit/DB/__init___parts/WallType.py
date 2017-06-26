class WallType(HostObjAttributes, IDisposable):
    """ Represents a specific type of wall, such as 'Generic -8" '. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    Function = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The wall function.

Get: Function(self: WallType) -> WallFunction

Set: Function(self: WallType) = value
"""

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The nature of the wall.

Get: Kind(self: WallType) -> WallKind

"""

    ThermalProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The calculated and settable thermal properties of the WallType

Get: ThermalProperties(self: WallType) -> ThermalProperties

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The overall thickness of this type of wall.

Get: Width(self: WallType) -> float

"""


