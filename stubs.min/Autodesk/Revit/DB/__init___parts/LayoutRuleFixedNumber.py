class LayoutRuleFixedNumber(LayoutRule, IDisposable):
    """
    This class indicate the layout rule of a Beam System is Fixed-Number.
    
    LayoutRuleFixedNumber(numberOfLines: int)
    """
    def Dispose(self):
        """ Dispose(self: LayoutRuleFixedNumber, A_0: bool) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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
    def __new__(self, numberOfLines):
        """ __new__(cls: type, numberOfLines: int) """
        pass

    NumberOfLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the number of the beams in a beam system.

Get: NumberOfLines(self: LayoutRuleFixedNumber) -> int

Set: NumberOfLines(self: LayoutRuleFixedNumber) = value
"""


