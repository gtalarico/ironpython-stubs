class LCIDConversionAttribute(Attribute, _Attribute):
    """
    Indicates that a method's unmanaged signature expects a locale identifier (LCID) parameter.
    
    LCIDConversionAttribute(lcid: int)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, lcid):
        """ __new__(cls: type, lcid: int) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the position of the LCID argument in the unmanaged signature.

Get: Value(self: LCIDConversionAttribute) -> int

"""


