class LayoutRuleFixedDistance(LayoutRule, IDisposable):
    """
    This class indicate the layout rule of a Beam System is Fixed-Distance.
    
    LayoutRuleFixedDistance(spacing: float, justifyType: BeamSystemJustifyType)
    """
    def Dispose(self):
        """ Dispose(self: LayoutRuleFixedDistance, A_0: bool) """
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
    def __new__(self, spacing, justifyType):
        """ __new__(cls: type, spacing: float, justifyType: BeamSystemJustifyType) """
        pass

    JustifyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the type of justification.

Get: JustifyType(self: LayoutRuleFixedDistance) -> BeamSystemJustifyType

Set: JustifyType(self: LayoutRuleFixedDistance) = value
"""

    Spacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set spacing of the Beam System.

Get: Spacing(self: LayoutRuleFixedDistance) -> float

Set: Spacing(self: LayoutRuleFixedDistance) = value
"""


