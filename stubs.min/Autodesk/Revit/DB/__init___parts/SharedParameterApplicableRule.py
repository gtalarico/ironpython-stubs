class SharedParameterApplicableRule(FilterRule, IDisposable):
    """
    Tests whether an element supports a shared parameter.
    
    SharedParameterApplicableRule(parameterName: str)
    """
    def Dispose(self):
        """ Dispose(self: FilterRule, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FilterRule, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, parameterName):
        """ __new__(cls: type, parameterName: str) """
        pass

    ParameterName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the parameter that an element must support to pass this rule.

Get: ParameterName(self: SharedParameterApplicableRule) -> str

Set: ParameterName(self: SharedParameterApplicableRule) = value
"""


