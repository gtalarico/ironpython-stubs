class SymbolicCurve(CurveElement, IDisposable):
    """ A curve that provides information but is not intended to represent actual geometry in an element. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetVisibility(self):
        """
        GetVisibility(self: SymbolicCurve) -> FamilyElementVisibility
        
            Gets the visibility for the symbolic curve.
            Returns: A copy of visibility settings for the symbolic curve.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetVisibility(self, visibility):
        """
        SetVisibility(self: SymbolicCurve, visibility: FamilyElementVisibility)
            Sets the visibility for the symbolic curve.
        """
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

    IsDrawnInForeground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if this curve will be drawn in the foreground of the family instance.

Get: IsDrawnInForeground(self: SymbolicCurve) -> bool

Set: IsDrawnInForeground(self: SymbolicCurve) = value
"""

    ReferenceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates the type of reference.

Get: ReferenceType(self: SymbolicCurve) -> ReferenceType

Set: ReferenceType(self: SymbolicCurve) = value
"""

    Subcategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The subcategory.

Get: Subcategory(self: SymbolicCurve) -> GraphicsStyle

Set: Subcategory(self: SymbolicCurve) = value
"""


