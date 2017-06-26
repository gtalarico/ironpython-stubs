class CurtainGridLine(HostObject, IDisposable):
    """ Represents a CurtainGridLine within Autodesk Revit. """
    def AddAllSegments(self):
        """
        AddAllSegments(self: CurtainGridLine)
            All the segments on this grid line will be added.
        """
        pass

    def AddMullions(self, segment, mullionType, oneSegmentOnly):
        """
        AddMullions(self: CurtainGridLine, segment: Curve, mullionType: MullionType, oneSegmentOnly: bool) -> ElementSet
        
            Add mullions on the specified segments of a grid. If any segment already has a 
             mullion, no change is made to that segment.
        
        
            segment: Curve of the segment.
            mullionType: The type of the mullion to add.
            oneSegmentOnly: If true, add one mullion to the specified segment, otherwise add mullions to 
             all the segments of the matching grid line.
        
            Returns: If operation succeeds, the created mullions will be returned.
        """
        pass

    def AddSegment(self, curve):
        """
        AddSegment(self: CurtainGridLine, curve: Curve)
            Add a segment based on the specified segment curve of the gridline.
        
            curve: The curve used to locate the segment to be removed. This function will invoke 
             regeneration.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveSegment(self, curve):
        """
        RemoveSegment(self: CurtainGridLine, curve: Curve)
            Remove the segment specified by the input curve.
        
            curve: The curve used to locate the segment to be removed.
        """
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

    AllSegmentCurves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve the curves of all segments.

Get: AllSegmentCurves(self: CurtainGridLine) -> CurveArray

"""

    ExistingSegmentCurves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve all the existing segment curves of the grid line.

Get: ExistingSegmentCurves(self: CurtainGridLine) -> CurveArray

"""

    FullCurve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve the geometry curve of the curtain grid line.

Get: FullCurve(self: CurtainGridLine) -> Curve

"""

    IsUGridLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve the direction of a grid line.If it is true,we say it is a UGridLine,otherwise it is VGridLine

Get: IsUGridLine(self: CurtainGridLine) -> bool

"""

    Lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves or changes the lock state of the curtain grid line.

Get: Lock(self: CurtainGridLine) -> bool

Set: Lock(self: CurtainGridLine) = value
"""

    SkippedSegmentCurves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve all the removed segment curves of the grid line.

Get: SkippedSegmentCurves(self: CurtainGridLine) -> CurveArray

"""


