class CursorType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the built in cursor types.
    
    enum CursorType, values: AppStarting (3), Arrow (2), ArrowCD (27), Cross (4), Hand (14), Help (5), IBeam (6), No (1), None (0), Pen (15), ScrollAll (18), ScrollE (22), ScrollN (19), ScrollNE (24), ScrollNS (16), ScrollNW (23), ScrollS (20), ScrollSE (26), ScrollSW (25), ScrollW (21), ScrollWE (17), SizeAll (7), SizeNESW (8), SizeNS (9), SizeNWSE (10), SizeWE (11), UpArrow (12), Wait (13)
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

    AppStarting = None
    Arrow = None
    ArrowCD = None
    Cross = None
    Hand = None
    Help = None
    IBeam = None
    No = None
    None = None
    Pen = None
    ScrollAll = None
    ScrollE = None
    ScrollN = None
    ScrollNE = None
    ScrollNS = None
    ScrollNW = None
    ScrollS = None
    ScrollSE = None
    ScrollSW = None
    ScrollW = None
    ScrollWE = None
    SizeAll = None
    SizeNESW = None
    SizeNS = None
    SizeNWSE = None
    SizeWE = None
    UpArrow = None
    value__ = None
    Wait = None

