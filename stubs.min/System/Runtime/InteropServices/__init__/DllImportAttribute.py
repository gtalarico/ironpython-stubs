class DllImportAttribute(Attribute, _Attribute):
    """
    Indicates that the attributed method is exposed by an unmanaged dynamic-link library (DLL) as a static entry point.
    
    DllImportAttribute(dllName: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, dllName):
        """ __new__(cls: type, dllName: str) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the DLL file that contains the entry point.

Get: Value(self: DllImportAttribute) -> str

"""


    BestFitMapping = None
    CallingConvention = None
    CharSet = None
    EntryPoint = None
    ExactSpelling = None
    PreserveSig = None
    SetLastError = None
    ThrowOnUnmappableChar = None

