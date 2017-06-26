class PointOnCurveMeasurementType(Enum, IComparable, IFormattable, IConvertible):
    """
    Point on curve measurement type
       Defines the types of measurements that may be used when placing a point at a designated distance along a curve.
    
    enum PointOnCurveMeasurementType, values: Angle (6), ChordLength (5), NonNormalizedCurveParameter (1), NormalizedCurveParameter (2), NormalizedSegmentLength (4), SegmentLength (3)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Angle = None
    ChordLength = None
    NonNormalizedCurveParameter = None
    NormalizedCurveParameter = None
    NormalizedSegmentLength = None
    SegmentLength = None
    value__ = None

