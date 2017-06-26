class AceFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the inheritance and auditing behavior of an access control entry (ACE).
    
    enum (flags) AceFlags, values: AuditFlags (192), ContainerInherit (2), FailedAccess (128), InheritanceFlags (15), Inherited (16), InheritOnly (8), None (0), NoPropagateInherit (4), ObjectInherit (1), SuccessfulAccess (64)
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

    AuditFlags = None
    ContainerInherit = None
    FailedAccess = None
    InheritanceFlags = None
    Inherited = None
    InheritOnly = None
    None = None
    NoPropagateInherit = None
    ObjectInherit = None
    SuccessfulAccess = None
    value__ = None

