class ConnectorType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all connector types for a connection
    
    enum ConnectorType, values: AllModes (16777215), AnyEnd (129), BlankEnd (128), Curve (2), End (1), EndSurface (17), Family (49), Invalid (0), Logical (4), MasterSurface (32), NodeReference (64), NonEnd (30), Physical (19), Reference (8), Surface (16)
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

    AllModes = None
    AnyEnd = None
    BlankEnd = None
    Curve = None
    End = None
    EndSurface = None
    Family = None
    Invalid = None
    Logical = None
    MasterSurface = None
    NodeReference = None
    NonEnd = None
    Physical = None
    Reference = None
    Surface = None
    value__ = None

