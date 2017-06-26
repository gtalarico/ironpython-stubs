class AttributeTargets(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the application elements on which it is valid to apply an attribute.
    
    enum (flags) AttributeTargets, values: All (32767), Assembly (1), Class (4), Constructor (32), Delegate (4096), Enum (16), Event (512), Field (256), GenericParameter (16384), Interface (1024), Method (64), Module (2), Parameter (2048), Property (128), ReturnValue (8192), Struct (8)
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

    All = None
    Assembly = None
    Class = None
    Constructor = None
    Delegate = None
    Enum = None
    Event = None
    Field = None
    GenericParameter = None
    Interface = None
    Method = None
    Module = None
    Parameter = None
    Property = None
    ReturnValue = None
    Struct = None
    value__ = None

