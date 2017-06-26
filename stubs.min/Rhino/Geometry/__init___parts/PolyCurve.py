class PolyCurve(Curve, IDisposable, ISerializable):
    """ PolyCurve() """
    def Append(self, *__args):
        """
        Append(self: PolyCurve, curve: Curve) -> bool
        Append(self: PolyCurve, arc: Arc) -> bool
        Append(self: PolyCurve, line: Line) -> bool
        """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """ ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: Curve, disposing: bool) """
        pass

    def Duplicate(self):
        """ Duplicate(self: PolyCurve) -> GeometryBase """
        pass

    def DuplicatePolyCurve(self):
        """ DuplicatePolyCurve(self: PolyCurve) -> PolyCurve """
        pass

    def Explode(self):
        """ Explode(self: PolyCurve) -> Array[Curve] """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """ NonConstOperation(self: Curve) """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """ OnSwitchToNonConst(self: GeometryBase) """
        pass

    def PolyCurveParameter(self, segmentIndex, segmentCurveParameter):
        """ PolyCurveParameter(self: PolyCurve, segmentIndex: int, segmentCurveParameter: float) -> float """
        pass

    def RemoveNesting(self):
        """ RemoveNesting(self: PolyCurve) -> bool """
        pass

    def SegmentCurve(self, index):
        """ SegmentCurve(self: PolyCurve, index: int) -> Curve """
        pass

    def SegmentCurveParameter(self, polycurveParameter):
        """ SegmentCurveParameter(self: PolyCurve, polycurveParameter: float) -> float """
        pass

    def SegmentDomain(self, segmentIndex):
        """ SegmentDomain(self: PolyCurve, segmentIndex: int) -> Interval """
        pass

    def SegmentIndex(self, polycurveParameter):
        """ SegmentIndex(self: PolyCurve, polycurveParameter: float) -> int """
        pass

    def SegmentIndexes(self, subdomain, segmentIndex0, segmentIndex1):
        """ SegmentIndexes(self: PolyCurve, subdomain: Interval) -> (int, int, int) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    HasGap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasGap(self: PolyCurve) -> bool

"""

    IsNested = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNested(self: PolyCurve) -> bool

"""

    SegmentCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentCount(self: PolyCurve) -> int

"""


