class ListType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type indicating the style of list item
       for paragraphs that are part of ordered or unordered lists
       in FormattedText.
    
    enum ListType, values: ArabicNumbers (3), Bullet (2), LowerCaseLetters (4), Mixed (0), None (1), UpperCaseLetters (5)
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

    ArabicNumbers = None
    Bullet = None
    LowerCaseLetters = None
    Mixed = None
    None = None
    UpperCaseLetters = None
    value__ = None

