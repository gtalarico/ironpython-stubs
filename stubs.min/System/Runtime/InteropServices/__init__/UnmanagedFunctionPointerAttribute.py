class UnmanagedFunctionPointerAttribute(Attribute, _Attribute):
    """
    Controls the marshaling behavior of a delegate signature passed as an unmanaged function pointer to or from unmanaged code. This class cannot be inherited.
    
    UnmanagedFunctionPointerAttribute(callingConvention: CallingConvention)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, callingConvention):
        """ __new__(cls: type, callingConvention: CallingConvention) """
        pass

    CallingConvention = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of the calling convention.

Get: CallingConvention(self: UnmanagedFunctionPointerAttribute) -> CallingConvention

"""


    BestFitMapping = None
    CharSet = None
    SetLastError = None
    ThrowOnUnmappableChar = None

