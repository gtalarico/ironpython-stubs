class HitTestFilterBehavior(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the return behavior of a hit test in a hit test filter callback method.
    
    enum HitTestFilterBehavior, values: Continue (6), ContinueSkipChildren (2), ContinueSkipSelf (4), ContinueSkipSelfAndChildren (0), Stop (8)
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

    Continue = None
    ContinueSkipChildren = None
    ContinueSkipSelf = None
    ContinueSkipSelfAndChildren = None
    Stop = None
    value__ = None

