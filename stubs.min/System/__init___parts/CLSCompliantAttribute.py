class CLSCompliantAttribute(Attribute, _Attribute):
    """
    Indicates whether a program element is compliant with the Common Language Specification (CLS). This class cannot be inherited.
    
    CLSCompliantAttribute(isCompliant: bool)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, isCompliant):
        """ __new__(cls: type, isCompliant: bool) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    IsCompliant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Boolean value indicating whether the indicated program element is CLS-compliant.

Get: IsCompliant(self: CLSCompliantAttribute) -> bool

"""


