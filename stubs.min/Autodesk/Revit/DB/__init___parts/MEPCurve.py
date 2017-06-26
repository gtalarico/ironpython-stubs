class MEPCurve(HostObject, IDisposable):
    """ A curve object for duct or pipe blend elements. """
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

    ConnectorManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connector manager of this MEP curve.

Get: ConnectorManager(self: MEPCurve) -> ConnectorManager

"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The diameter of the MEP curve.

Get: Diameter(self: MEPCurve) -> float

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The height of the MEP curve.

Get: Height(self: MEPCurve) -> float

"""

    LevelOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset of the MEP curve.

Get: LevelOffset(self: MEPCurve) -> float

Set: LevelOffset(self: MEPCurve) = value
"""

    MEPSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The system of the MEP curve.

Get: MEPSystem(self: MEPCurve) -> MEPSystem

"""

    ReferenceLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The reference level of the MEP curve.

Get: ReferenceLevel(self: MEPCurve) -> Level

Set: ReferenceLevel(self: MEPCurve) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The width of the MEP curve.

Get: Width(self: MEPCurve) -> float

"""


