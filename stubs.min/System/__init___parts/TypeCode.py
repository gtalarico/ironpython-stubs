class TypeCode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of an object.
    
    enum TypeCode, values: Boolean (3), Byte (6), Char (4), DateTime (16), DBNull (2), Decimal (15), Double (14), Empty (0), Int16 (7), Int32 (9), Int64 (11), Object (1), SByte (5), Single (13), String (18), UInt16 (8), UInt32 (10), UInt64 (12)
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

    Boolean = None
    Byte = None
    Char = None
    DateTime = None
    DBNull = None
    Decimal = None
    Double = None
    Empty = None
    Int16 = None
    Int32 = None
    Int64 = None
    Object = None
    SByte = None
    Single = None
    String = None
    UInt16 = None
    UInt32 = None
    UInt64 = None
    value__ = None

