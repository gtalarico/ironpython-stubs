class CableTrayType(MEPCurveType, IDisposable):
    """ This class represents a cable tray type in Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def IsValidBendMultiplier(self, bendMultiplier):
        """
        IsValidBendMultiplier(self: CableTrayType, bendMultiplier: float) -> bool
        
            Identifies if the input bend multiplier is valid.
        
            bendMultiplier: The bend multiplier to check.
            Returns: True if the value is acceptable, false otherwise.
        """
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

    BendMultiplier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bend multiplier.

Get: BendMultiplier(self: CableTrayType) -> float

Set: BendMultiplier(self: CableTrayType) = value
"""

    IsWithFitting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether this cable tray type is with fitting

Get: IsWithFitting(self: CableTrayType) -> bool

"""

    ShapeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Shape of this cable tray type.

Get: ShapeType(self: CableTrayType) -> CableTrayShape

"""


