class MouseAction(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies constants that define actions performed by the mouse.
    
    enum MouseAction, values: LeftClick (1), LeftDoubleClick (5), MiddleClick (3), MiddleDoubleClick (7), None (0), RightClick (2), RightDoubleClick (6), WheelClick (4)
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

    LeftClick = None
    LeftDoubleClick = None
    MiddleClick = None
    MiddleDoubleClick = None
    None = None
    RightClick = None
    RightDoubleClick = None
    value__ = None
    WheelClick = None

