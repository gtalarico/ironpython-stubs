class DividedPath(Element, IDisposable):
    """ An element that consists of a set of points distributed along a path which consists of a connected set of curves and edges. """
    @staticmethod
    def AreCurveReferencesConnected(document, curveReferences):
        """ AreCurveReferencesConnected(document: Document, curveReferences: IList[Reference]) -> bool """
        pass

    @staticmethod
    def Create(document, curveReferences, intersectors=None):
        """
        Create(document: Document, curveReferences: IList[Reference]) -> DividedPath
        Create(document: Document, curveReferences: IList[Reference], intersectors: ICollection[ElementId]) -> DividedPath
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def Flip(self):
        """
        Flip(self: DividedPath)
            Toggle the flipped value
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetIntersectingElements(self):
        """
        GetIntersectingElements(self: DividedPath) -> ICollection[ElementId]
        
            Get the elements whose intersection with path produces points.
        """
        pass

    @staticmethod
    def IsCurveReferenceValid(document, curveReference):
        """
        IsCurveReferenceValid(document: Document, curveReference: Reference) -> bool
        
            This returns true if the reference represents a curve or edge that can be used 
             to create a divided path.
        
        
            document: The document.
            curveReference: The reference.
            Returns: True if the reference can be used to create a divided path, false otherwise.
        """
        pass

    @staticmethod
    def IsIntersectorValidForCreation(document, intersector):
        """
        IsIntersectorValidForCreation(document: Document, intersector: ElementId) -> bool
        
            This returns true if the intersector is an element that can be used to 
             intersect with a newly created divided path.
        
        
            document: The document.
            intersector: The intersector.
            Returns: True if the reference can be used to create a divided path, false otherwise.
        """
        pass

    def IsIntersectorValidForDividedPath(self, intersector):
        """
        IsIntersectorValidForDividedPath(self: DividedPath, intersector: ElementId) -> bool
        
            This returns true if the intersector is an element that can be used to 
             intersect with the divided path.
        
        
            intersector: The intersector.
            Returns: True if the reference can be used to create a divided path, false otherwise.
        """
        pass

    def IsValidBeginningIndent(self, beginningIndent):
        """
        IsValidBeginningIndent(self: DividedPath, beginningIndent: float) -> bool
        
            Checks that the indent value does not cause the beginningIndent and endIndent 
             to overlop
        """
        pass

    def IsValidEndIndent(self, endIndent):
        """
        IsValidEndIndent(self: DividedPath, endIndent: float) -> bool
        
            Checks that the indent value does not cause the beginningIndent and endIndent 
             to overlop
        """
        pass

    @staticmethod
    def IsValidFixedNumberOfPoints(fixedNumberOfPoints):
        """
        IsValidFixedNumberOfPoints(fixedNumberOfPoints: int) -> bool
        
            Identifies if the indicated number of points is valid for assignment
           to a 
             DividedPath with a layout type 'FixedNumber'.
        """
        pass

    def IsValidMeasurementType(self, measurementType):
        """
        IsValidMeasurementType(self: DividedPath, measurementType: DividedPathMeasurementType) -> bool
        
            Checks that the measurement type enumeration value is valid
        """
        pass

    def IsValidSpacingRuleJustification(self, justification):
        """
        IsValidSpacingRuleJustification(self: DividedPath, justification: SpacingRuleJustification) -> bool
        
            Checks that the justification enumeration value is valid
        """
        pass

    def IsValidSpacingRuleLayout(self, layout):
        """
        IsValidSpacingRuleLayout(self: DividedPath, layout: SpacingRuleLayout) -> bool
        
            Checks that the spacing rule layout enumeration value is valid
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    @staticmethod
    def SeparateReferencesIntoConnectedReferences(document, curveReferences):
        """ SeparateReferencesIntoConnectedReferences(document: Document, curveReferences: IList[Reference]) -> IList[IList[Reference]] """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetIntersectingElements(self, intersectors):
        """ SetIntersectingElements(self: DividedPath, intersectors: ICollection[ElementId]) """
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

    BeginningIndent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The beginningIndent is an offset distance from the beginning of the
   first curve that determines the beginning of the range over which
   the layout is applied.
   The measurement type determines how the distance is measured.

Get: BeginningIndent(self: DividedPath) -> float

Set: BeginningIndent(self: DividedPath) = value
"""

    DisplayNodeNumbers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Controls whether the node numbers are shown when the divided path is selected

Get: DisplayNodeNumbers(self: DividedPath) -> bool

Set: DisplayNodeNumbers(self: DividedPath) = value
"""

    DisplayNodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Controls whether the points of the divided path are visible

Get: DisplayNodes(self: DividedPath) -> bool

Set: DisplayNodes(self: DividedPath) = value
"""

    DisplayReferenceCurves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Controls whether the curves in the path are visible

Get: DisplayReferenceCurves(self: DividedPath) -> bool

Set: DisplayReferenceCurves(self: DividedPath) = value
"""

    Distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The distance between points that are distributed along the path according to the selected layout.
   When the layout is set to 'FixedDistance' this value can be set to desired distance.
   The measurement type determines how the distance is measured.

Get: Distance(self: DividedPath) -> float

Set: Distance(self: DividedPath) = value
"""

    EndIndent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The endIndent is an offset distance from the end of the
   last curve that determines the end of the range over which
   the layout is applied.
   The measurement type determines how the distance is measured.

Get: EndIndent(self: DividedPath) -> float

Set: EndIndent(self: DividedPath) = value
"""

    FixedNumberOfPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of points used when the layout is set to 'FixedNumber'.

Get: FixedNumberOfPoints(self: DividedPath) -> int

Set: FixedNumberOfPoints(self: DividedPath) = value
"""

    Flipped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If the divided path is flipped the nodes are numbered in the reverse order.
   It also switches the ends from which beginningIndent and endIndent are measured from.

Get: Flipped(self: DividedPath) -> bool

"""

    IsClosedLoop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether or not the path forms a closed loop.

Get: IsClosedLoop(self: DividedPath) -> bool

"""

    IsCyclical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the first and last point coincide
   False otherwise.

Get: IsCyclical(self: DividedPath) -> bool

"""

    MaximumDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum distance is used when the layout is set to 'MaximumSpacing'.
   When that layout rule is used the distance between points will not exceed this value.
   The measurement type determines how the distance is measured.

Get: MaximumDistance(self: DividedPath) -> float

Set: MaximumDistance(self: DividedPath) = value
"""

    MeasurementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The measurement type determines how distances are calculated.
   Either along a straight line between two points ('ChordLength')
   or along the segment of the path that connects them. ('SegmentLength').

Get: MeasurementType(self: DividedPath) -> DividedPathMeasurementType

Set: MeasurementType(self: DividedPath) = value
"""

    MinimumDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The minimum distance is used when the layout is set to 'MinimumSpacing'.
   When that layout rule is used the distance between points will not fall below this value.
   The measurement type determines how the distance is measured.

Get: MinimumDistance(self: DividedPath) -> float

Set: MinimumDistance(self: DividedPath) = value
"""

    NumberOfPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total number of points of the divided surface.
   This combines the layout points and the intersection points.

Get: NumberOfPoints(self: DividedPath) -> int

"""

    SpacingRuleJustification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When the layout is set to 'FixedDistance' the points may not cover the
   entire range of the path.  The justification determines whether
   the points are centered on the range, or shifted towards the start or end of the range.

Get: SpacingRuleJustification(self: DividedPath) -> SpacingRuleJustification

Set: SpacingRuleJustification(self: DividedPath) = value
"""

    SpacingRuleLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The layout determines how points are distributed along the path.

Get: SpacingRuleLayout(self: DividedPath) -> SpacingRuleLayout

Set: SpacingRuleLayout(self: DividedPath) = value
"""

    TotalPathLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sum of the curve lengths.

Get: TotalPathLength(self: DividedPath) -> float

"""


