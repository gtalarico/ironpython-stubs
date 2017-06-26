class DataExchangeMessageId(Enum, IComparable, IFormattable, IConvertible):
    """
    Predefined message ids for DataExchangeLog.
    
    enum DataExchangeMessageId, values: EmptyObject (10), GenericError (6), InvalidDataSet (5), InvalidRenderingStyle (9), InvalidSourceObject (4), None (0), ObjectCreated (2), ObjectNotConverted (8), ObjectNotSupported (7), UnexpectedResult (3), UnitOfProgressCompleted (1)
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

    EmptyObject = None
    GenericError = None
    InvalidDataSet = None
    InvalidRenderingStyle = None
    InvalidSourceObject = None
    None = None
    ObjectCreated = None
    ObjectNotConverted = None
    ObjectNotSupported = None
    UnexpectedResult = None
    UnitOfProgressCompleted = None
    value__ = None

