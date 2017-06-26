class FamilyPlacementType(Enum, IComparable, IFormattable, IConvertible):
    """
    The type of placement required for a given family.
    
    enum FamilyPlacementType, values: Adaptive (8), CurveBased (5), CurveBasedDetail (6), CurveDrivenStructural (7), Invalid (9), OneLevelBased (0), OneLevelBasedHosted (1), TwoLevelsBased (2), ViewBased (3), WorkPlaneBased (4)
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

    Adaptive = None
    CurveBased = None
    CurveBasedDetail = None
    CurveDrivenStructural = None
    Invalid = None
    OneLevelBased = None
    OneLevelBasedHosted = None
    TwoLevelsBased = None
    value__ = None
    ViewBased = None
    WorkPlaneBased = None

