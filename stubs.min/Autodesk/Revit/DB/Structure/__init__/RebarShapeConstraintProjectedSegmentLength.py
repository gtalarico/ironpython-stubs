class RebarShapeConstraintProjectedSegmentLength(RebarShapeConstraint, IDisposable):
    """
    A constraint that measures the length of a segment as measured by projecting onto a direction
       that is not parallel to the segment.
    
    RebarShapeConstraintProjectedSegmentLength(paramId: ElementId, direction: UV, tripleProductSign: int, refType0: RebarShapeSegmentEndReferenceType, refType1: RebarShapeSegmentEndReferenceType)
    """
    def Dispose(self):
        """ Dispose(self: RebarShapeConstraint, A_0: bool) """
        pass

    def GetSegmentEndReferenceType(self, index):
        """
        GetSegmentEndReferenceType(self: RebarShapeConstraintProjectedSegmentLength, index: int) -> RebarShapeSegmentEndReferenceType
        
            Choice of two possibilities for the start and end references of the length 
             constraint.
        
        
            index: Which reference on the constraint. Either 0 or 1.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeConstraint, disposing: bool) """
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
    def __new__(self, paramId, direction, tripleProductSign, refType0, refType1):
        """ __new__(cls: type, paramId: ElementId, direction: UV, tripleProductSign: int, refType0: RebarShapeSegmentEndReferenceType, refType1: RebarShapeSegmentEndReferenceType) """
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A vector specifying the direction of the constraint. The direction is fixed,
   and the shape is always constructed so that the segment
   direction has a positive dot product with this vector.

Get: Direction(self: RebarShapeConstraintProjectedSegmentLength) -> UV

"""

    TripleProductSign = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sign of the z-coordinate of the cross
   product of the Direction property with the segment vector.
   TripleProductSign is 1 if the segment direction is to be on the left of
   the constraint direction,
   or -1 if the segment direction is to be on the right.

Get: TripleProductSign(self: RebarShapeConstraintProjectedSegmentLength) -> int

"""


