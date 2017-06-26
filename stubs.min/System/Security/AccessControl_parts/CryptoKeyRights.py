class CryptoKeyRights(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the cryptographic key operation for which an authorization rule controls access or auditing.
    
    enum (flags) CryptoKeyRights, values: ChangePermissions (262144), Delete (65536), FullControl (2032027), GenericAll (268435456), GenericExecute (536870912), GenericRead (-2147483648), GenericWrite (1073741824), ReadAttributes (128), ReadData (1), ReadExtendedAttributes (8), ReadPermissions (131072), Synchronize (1048576), TakeOwnership (524288), WriteAttributes (256), WriteData (2), WriteExtendedAttributes (16)
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

    ChangePermissions = None
    Delete = None
    FullControl = None
    GenericAll = None
    GenericExecute = None
    GenericRead = None
    GenericWrite = None
    ReadAttributes = None
    ReadData = None
    ReadExtendedAttributes = None
    ReadPermissions = None
    Synchronize = None
    TakeOwnership = None
    value__ = None
    WriteAttributes = None
    WriteData = None
    WriteExtendedAttributes = None

