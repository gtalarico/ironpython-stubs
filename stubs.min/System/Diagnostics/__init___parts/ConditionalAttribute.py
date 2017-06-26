class ConditionalAttribute(Attribute, _Attribute):
    """
    Indicates to compilers that a method call or attribute should be ignored unless a specified conditional compilation symbol is defined.
    
    ConditionalAttribute(conditionString: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, conditionString):
        """ __new__(cls: type, conditionString: str) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    ConditionString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the conditional compilation symbol that is associated with the System.Diagnostics.ConditionalAttribute attribute.

Get: ConditionString(self: ConditionalAttribute) -> str

"""


