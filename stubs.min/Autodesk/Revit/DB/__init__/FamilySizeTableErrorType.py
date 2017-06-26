class FamilySizeTableErrorType(Enum, IComparable, IFormattable, IConvertible):
    """
    The set of errors that can be returned when importing a FamilySizeTable from a CSV file.
    
    enum FamilySizeTableErrorType, values: CannotOpenFile (1), CannotParseColumnHeader (4), CannotReadFile (2), FileNotFound (0), IncorrectNumberOfColumns (5), InvalidHeaderSeparator (3), Undefined (-1)
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

    CannotOpenFile = None
    CannotParseColumnHeader = None
    CannotReadFile = None
    FileNotFound = None
    IncorrectNumberOfColumns = None
    InvalidHeaderSeparator = None
    Undefined = None
    value__ = None

