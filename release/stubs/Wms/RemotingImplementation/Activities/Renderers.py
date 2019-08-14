# encoding: utf-8
# module Wms.RemotingImplementation.Activities.Renderers calls itself Renderers
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class MobileProgressBarRenderer:
    """ MobileProgressBarRenderer(current: Decimal, total: Decimal, title: str, enableDetails: bool, progressColor: str) """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return MobileProgressBarRenderer()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    def Dispose(self):
        """ Dispose(self: MobileProgressBarRenderer) """
        pass

    def Render(self):
        """ Render(self: MobileProgressBarRenderer) -> Array[Byte] """
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
    def __new__(self, current, total, title, enableDetails, progressColor):
        """ __new__(cls: type, current: Decimal, total: Decimal, title: str, enableDetails: bool, progressColor: str) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: MobileProgressBarRenderer) -> Decimal

Set: Current(self: MobileProgressBarRenderer) = value
"""

    EnableDetails = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnableDetails(self: MobileProgressBarRenderer) -> bool

Set: EnableDetails(self: MobileProgressBarRenderer) = value
"""

    ProgressColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProgressColor(self: MobileProgressBarRenderer) -> str

Set: ProgressColor(self: MobileProgressBarRenderer) = value
"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Title(self: MobileProgressBarRenderer) -> str

Set: Title(self: MobileProgressBarRenderer) = value
"""

    Total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Total(self: MobileProgressBarRenderer) -> Decimal

Set: Total(self: MobileProgressBarRenderer) = value
"""



