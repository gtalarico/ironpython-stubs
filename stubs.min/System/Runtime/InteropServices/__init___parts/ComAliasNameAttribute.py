class ComAliasNameAttribute(Attribute, _Attribute):
    """
    Indicates the COM alias for a parameter or field type.
    
    ComAliasNameAttribute(alias: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, alias):
        """ __new__(cls: type, alias: str) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the alias for the field or parameter as found in the type library when it was imported.

Get: Value(self: ComAliasNameAttribute) -> str

"""


