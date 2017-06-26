class AnalyticalSupportPriority(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines how "highly" another Element is giving support for one Element.
    
    enum AnalyticalSupportPriority, values: FourthHigestPriority (4), HighestPriority (1), SecondHighestPriority (2), ThirdHighestPriority (3), UnknownPriority (0)
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

    FourthHigestPriority = None
    HighestPriority = None
    SecondHighestPriority = None
    ThirdHighestPriority = None
    UnknownPriority = None
    value__ = None

