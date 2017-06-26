class CurveElementType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing the curve element types that can be used when filtering elements
       (via CurveElementFilter).
    
    enum CurveElementType, values: AreaSeparation (7), Cloud (11), CurveByPoints (8), DetailCurve (2), Insulation (10), Invalid (0), ModelCurve (1), ReferenceLine (4), RepeatingDetail (9), RoomSeparation (6), SpaceSeparation (5), SymbolicCurve (3)
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

    AreaSeparation = None
    Cloud = None
    CurveByPoints = None
    DetailCurve = None
    Insulation = None
    Invalid = None
    ModelCurve = None
    ReferenceLine = None
    RepeatingDetail = None
    RoomSeparation = None
    SpaceSeparation = None
    SymbolicCurve = None
    value__ = None

