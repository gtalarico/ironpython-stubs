class DoubleParameterValue(ParameterValue, IDisposable):
    """
    A class that holds a Double value of a parameter element.
    
    DoubleParameterValue(value: float)
    DoubleParameterValue()
    """
    def Dispose(self):
        """ Dispose(self: ParameterValue, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ParameterValue, disposing: bool) """
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
    def __new__(self, value=None):
        """
        __new__(cls: type, value: float)
        __new__(cls: type)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The stored value

Get: Value(self: DoubleParameterValue) -> float

Set: Value(self: DoubleParameterValue) = value
"""


