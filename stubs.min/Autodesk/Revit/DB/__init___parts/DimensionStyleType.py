class DimensionStyleType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type containing possible style types of dimensions.
    
    enum DimensionStyleType, values: Angular (1), ArcLength (3), Diameter (9), Linear (0), LinearFixed (7), Radial (2), SpotCoordinate (5), SpotElevation (4), SpotSlope (8)
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

    Angular = None
    ArcLength = None
    Diameter = None
    Linear = None
    LinearFixed = None
    Radial = None
    SpotCoordinate = None
    SpotElevation = None
    SpotSlope = None
    value__ = None

