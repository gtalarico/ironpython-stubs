# encoding: utf-8
# module Wms.RemotingImplementation.Razor calls itself Razor
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BasePage:
    # no doc
    def ResolveLayout(self, *args): #cannot find CLR method
        """ ResolveLayout(self: TemplateBase[TModel], name: str) -> ITemplate """
        pass

    def T(self, key):
        """ T(self: BasePage[TModel], key: str) -> object """
        pass

    def Translate(self, key):
        """ Translate(self: BasePage[TModel], key: str) -> object """
        pass

    def TryTranslatePortal(self, key):
        """ TryTranslatePortal(self: BasePage[TModel], key: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    HasDynamicModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _context = None

    Instance = BasePage()
    """hardcoded/returns an instance of the class"""

class ILocalizeable:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CultureInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CultureInfo(self: ILocalizeable) -> CultureInfo

Set: CultureInfo(self: ILocalizeable) = value
"""


    Instance = ILocalizeable()
    """hardcoded/returns an instance of the class"""

