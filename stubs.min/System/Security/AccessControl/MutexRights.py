class MutexRights(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the access control rights that can be applied to named system mutex objects.
    
    enum (flags) MutexRights, values: ChangePermissions (262144), Delete (65536), FullControl (2031617), Modify (1), ReadPermissions (131072), Synchronize (1048576), TakeOwnership (524288)
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
    Modify = None
    ReadPermissions = None
    Synchronize = None
    TakeOwnership = None
    value__ = None

