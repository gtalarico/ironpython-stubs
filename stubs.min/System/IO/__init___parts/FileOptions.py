class FileOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents additional options for creating a System.IO.FileStream object.
    
    enum (flags) FileOptions, values: Asynchronous (1073741824), DeleteOnClose (67108864), Encrypted (16384), None (0), RandomAccess (268435456), SequentialScan (134217728), WriteThrough (-2147483648)
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

    Asynchronous = None
    DeleteOnClose = None
    Encrypted = None
    None = None
    RandomAccess = None
    SequentialScan = None
    value__ = None
    WriteThrough = None

