class IFCVersion(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing available IFC file versions into which a file may be exported.
    
    enum IFCVersion, values: Default (0), IFC2x2 (9), IFC2x3 (10), IFC2x3BFM (27), IFC2x3CV2 (21), IFC2x3FM (24), IFC4 (23), IFC4DTV (26), IFC4RV (25), IFCBCA (8), IFCCOBIE (17)
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

    Default = None
    IFC2x2 = None
    IFC2x3 = None
    IFC2x3BFM = None
    IFC2x3CV2 = None
    IFC2x3FM = None
    IFC4 = None
    IFC4DTV = None
    IFC4RV = None
    IFCBCA = None
    IFCCOBIE = None
    value__ = None

