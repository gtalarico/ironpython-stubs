class ResourceType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the defined native object types.
    
    enum ResourceType, values: DSObject (8), DSObjectAll (9), FileObject (1), KernelObject (6), LMShare (5), Printer (3), ProviderDefined (10), RegistryKey (4), RegistryWow6432Key (12), Service (2), Unknown (0), WindowObject (7), WmiGuidObject (11)
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

    DSObject = None
    DSObjectAll = None
    FileObject = None
    KernelObject = None
    LMShare = None
    Printer = None
    ProviderDefined = None
    RegistryKey = None
    RegistryWow6432Key = None
    Service = None
    Unknown = None
    value__ = None
    WindowObject = None
    WmiGuidObject = None

