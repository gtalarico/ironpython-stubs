class TextMarkerStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the appearance of a list item's bullet style.
    
    enum TextMarkerStyle, values: Box (4), Circle (2), Decimal (9), Disc (1), LowerLatin (7), LowerRoman (5), None (0), Square (3), UpperLatin (8), UpperRoman (6)
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

    Box = None
    Circle = None
    Decimal = None
    Disc = None
    LowerLatin = None
    LowerRoman = None
    None = None
    Square = None
    UpperLatin = None
    UpperRoman = None
    value__ = None

