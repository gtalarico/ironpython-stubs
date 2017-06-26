class SetComparisonResult(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all the relationship types between two sets of arbitrary nature.
    
    enum SetComparisonResult, values: BothEmpty (3), Disjoint (4), Equal (64), LeftEmpty (1), Overlap (8), RightEmpty (2), Subset (16), Superset (32)
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

    BothEmpty = None
    Disjoint = None
    Equal = None
    LeftEmpty = None
    Overlap = None
    RightEmpty = None
    Subset = None
    Superset = None
    value__ = None

