class ImportedFromTypeLibAttribute(Attribute, _Attribute):
    """
    Indicates that the types defined within an assembly were originally defined in a type library.
    
    ImportedFromTypeLibAttribute(tlbFile: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, tlbFile):
        """ __new__(cls: type, tlbFile: str) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the original type library file.

Get: Value(self: ImportedFromTypeLibAttribute) -> str

"""


