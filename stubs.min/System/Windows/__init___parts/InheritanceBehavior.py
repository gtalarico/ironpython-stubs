class InheritanceBehavior(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates the current mode of lookup for both property value inheritance, a resource lookup, and a RelativeSource FindAncestor lookup.
    
    enum InheritanceBehavior, values: Default (0), SkipAllNext (6), SkipAllNow (5), SkipToAppNext (2), SkipToAppNow (1), SkipToThemeNext (4), SkipToThemeNow (3)
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
    SkipAllNext = None
    SkipAllNow = None
    SkipToAppNext = None
    SkipToAppNow = None
    SkipToThemeNext = None
    SkipToThemeNow = None
    value__ = None

