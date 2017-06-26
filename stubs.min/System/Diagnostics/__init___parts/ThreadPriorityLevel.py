class ThreadPriorityLevel(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the priority level of a thread.
    
    enum ThreadPriorityLevel, values: AboveNormal (1), BelowNormal (-1), Highest (2), Idle (-15), Lowest (-2), Normal (0), TimeCritical (15)
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

    AboveNormal = None
    BelowNormal = None
    Highest = None
    Idle = None
    Lowest = None
    Normal = None
    TimeCritical = None
    value__ = None

