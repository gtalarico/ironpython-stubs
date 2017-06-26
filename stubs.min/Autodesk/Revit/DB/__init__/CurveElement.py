class CurveElement(Element, IDisposable):
    """ Class representing curve elements. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetAdjoinedCurveElements(self, end):
        """
        GetAdjoinedCurveElements(self: CurveElement, end: int) -> ISet[ElementId]
        
            Returns elements that are joining with this curve element at the given end 
             point.
        
        
            end: Id of one the curve's end. Value '0' indicates start and '1' indicates the end 
             of the curve, respectively.
        
            Returns: Collection of Ids of Curve Elements.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetLineStyleIds(self):
        """
        GetLineStyleIds(self: CurveElement) -> ICollection[ElementId]
        
            Ids of all line style Elements that are applicable to this curve element.
            Returns: A collection of Ids of line style elements.
        """
        pass

    def GetTangentLock(self, end, other):
        """
        GetTangentLock(self: CurveElement, end: int, other: ElementId) -> bool
        
            Returns the state of a tangent join between this and another curve element at 
             the given end-point.
        
        
            end: Index of one of the curve's end. Values '0' and '1' indicate the start or end 
             point, respectively.
        
            other: ElementId of another Curve Element from the same document.
            Returns: Returns True if this curve element has a tangent joint with the other input 
             element and the join is curently locked; returns False otherwise.
        """
        pass

    def HasTangentJoin(self, end, other):
        """
        HasTangentJoin(self: CurveElement, end: int, other: ElementId) -> bool
        
            Tests whether this curve element and the input curve element have common 
             tangent join at the given end-point.
        
        
            end: Index of one of the curve's end. Values '0' and '1' indicate the start or end 
             point, respectively.
        
            other: ElementId of another Curve Element from the same document.
            Returns: Returns True if the two curve elements have a tangent join at the given 
             end-point.
        """
        pass

    def HasTangentLocks(self, end):
        """
        HasTangentLocks(self: CurveElement, end: int) -> bool
        
            Tests whether this curve element has any locked tangent joins at the given 
             end-point.
        
        
            end: Index of one of the curve's end. Values '0' and '1' indicate the start or end 
             point, respectively.
        
            Returns: Returns True if the curve element is tangentially locked to at least one other 
             curve element at the given end-point; returns False otherwise.
        """
        pass

    def IsAdjoinedCurveElement(self, end, other):
        """
        IsAdjoinedCurveElement(self: CurveElement, end: int, other: ElementId) -> bool
        
            This method tests whether this and the given curve elements are joined at the 
             given end.
        
        
            end: Index of one of the curve's end. Values '0' and '1' indicate the start or end 
             point, respectively.
        
            other: ElementId of another Curve Element from the same document.
            Returns: Returns True if the input curve element joins This curve element at the given 
             end-point; returns False otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetGeometryCurve(self, curve, overrideJoins):
        """
        SetGeometryCurve(self: CurveElement, curve: Curve, overrideJoins: bool)
            Sets the geometry of the curve element.
        After the curve geometry is set, other 
             nearby curves may join to the new curve geometry.
        
        
            curve: The new curve.
            overrideJoins: An option to specify whether or not existing joins will affect setting the 
             geometry of the CurveElement.
        Setting this parameter to false is essentially 
             the same as directly setting the Autodesk.Revit.DB.CurveElement.GeometryCurve 
             property.
        """
        pass

    def SetSketchPlaneAndCurve(self, sketchPlane, curve):
        """
        SetSketchPlaneAndCurve(self: CurveElement, sketchPlane: SketchPlane, curve: Curve)
            Sets the sketch plane and the curve for this CurveElement.
        
            sketchPlane: The new sketch plane.
            curve: The new curve.
        """
        pass

    def SetTangentLock(self, end, other, state):
        """
        SetTangentLock(self: CurveElement, end: int, other: ElementId, state: bool)
            Sets a new status for an existing tangent join with another curve element at 
             the given end-point.
        
        
            end: Index of one of the curve's ends. Values '0' and '1' indicate the start or end 
             point, respectively.
        
            other: ElementId of another Curve Element from the same document.
            state: Requested new state of the lock; True to lock it, False to unlock it.
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

    CenterPointReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Centerpoint reference of curve element.  Curves such as circles, arcs, ellipses, and partial ellipses support this property.

Get: CenterPointReference(self: CurveElement) -> Reference

"""

    CurveElementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of the curve element.

Get: CurveElementType(self: CurveElement) -> CurveElementType

"""

    GeometryCurve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Geometry curve of the curve element.

Get: GeometryCurve(self: CurveElement) -> Curve

Set: GeometryCurve(self: CurveElement) = value
"""

    LineStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The line style of this curve element.

Get: LineStyle(self: CurveElement) -> Element

Set: LineStyle(self: CurveElement) = value
"""

    SketchPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sketch plane the curve element lies in.

Get: SketchPlane(self: CurveElement) -> SketchPlane

Set: SketchPlane(self: CurveElement) = value
"""

    SupportsTangentLocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether or not this curve element can have a locked tangent
   join at either of its end-points shared with another curve element.

Get: SupportsTangentLocks(self: CurveElement) -> bool

"""


