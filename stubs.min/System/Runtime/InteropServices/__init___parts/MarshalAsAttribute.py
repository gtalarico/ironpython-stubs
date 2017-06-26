class MarshalAsAttribute(Attribute, _Attribute):
    """
    Indicates how to marshal the data between managed and unmanaged code.
    
    MarshalAsAttribute(unmanagedType: UnmanagedType)
    MarshalAsAttribute(unmanagedType: Int16)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, unmanagedType):
        """
        __new__(cls: type, unmanagedType: UnmanagedType)
        __new__(cls: type, unmanagedType: Int16)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Runtime.InteropServices.UnmanagedType value the data is to be marshaled as.

Get: Value(self: MarshalAsAttribute) -> UnmanagedType

"""


    ArraySubType = None
    IidParameterIndex = None
    MarshalCookie = None
    MarshalType = None
    MarshalTypeRef = None
    SafeArraySubType = None
    SafeArrayUserDefinedSubType = None
    SizeConst = None
    SizeParamIndex = None

