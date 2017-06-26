class DispIdAttribute(Attribute, _Attribute):
    """
    Specifies the COM dispatch identifier (DISPID) of a method, field, or property.
    
    DispIdAttribute(dispId: int)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, dispId):
        """ __new__(cls: type, dispId: int) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the DISPID for the member.

Get: Value(self: DispIdAttribute) -> int

"""


