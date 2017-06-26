class LoaderOptimizationAttribute(Attribute, _Attribute):
    """
    Used to set the default loader optimization policy for the main method of an executable application.
    
    LoaderOptimizationAttribute(value: Byte)
    LoaderOptimizationAttribute(value: LoaderOptimization)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value):
        """
        __new__(cls: type, value: Byte)
        __new__(cls: type, value: LoaderOptimization)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current System.LoaderOptimization value for this instance.

Get: Value(self: LoaderOptimizationAttribute) -> LoaderOptimization

"""


