class ModelCurve(CurveElement, IDisposable):
    """ A model element that exists in 3D space and is visible in all views of a Revit project. """
    def ChangeToReferenceLine(self):
        """
        ChangeToReferenceLine(self: ModelCurve)
            Changes this curve to a reference curve.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetVisibility(self):
        """
        GetVisibility(self: ModelCurve) -> FamilyElementVisibility
        
            Gets the visibility for the model curve in a family document.
            Returns: A copy of visibility settings for the model curve in a family document.
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
        SetVisibility(self: ModelCurve, visibility: FamilyElementVisibility)
            Sets the visibility for the model curve in a family document.
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

    IsReferenceLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if this curve is a reference curve.

Get: IsReferenceLine(self: ModelCurve) -> bool

"""

    Subcategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The subcategory.

Get: Subcategory(self: ModelCurve) -> GraphicsStyle

Set: Subcategory(self: ModelCurve) = value
"""

    TrussCurveType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The truss curve type of this model curve.

Get: TrussCurveType(self: ModelCurve) -> TrussCurveType

Set: TrussCurveType(self: ModelCurve) = value
"""


