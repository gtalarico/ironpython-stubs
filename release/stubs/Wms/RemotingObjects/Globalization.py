from System.Collections.Generic import *
# encoding: utf-8
# module Wms.RemotingObjects.Globalization calls itself Globalization
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class SaveTranslationArgs():
    """ SaveTranslationArgs() """
    Instance = SaveTranslationArgs
    """hardcoded/returns an instance of the class"""
    LocaleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Langauge it is translated to

Get: LocaleId(self: SaveTranslationArgs) -> str

Set: LocaleId(self: SaveTranslationArgs) = value
"""

    ResourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Key for the translation

Get: ResourceId(self: SaveTranslationArgs) -> str

Set: ResourceId(self: SaveTranslationArgs) = value
"""

    ResourceSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Resource set, a way to group localizations together.
            Default: Portal

Get: ResourceSet(self: SaveTranslationArgs) -> str

Set: ResourceSet(self: SaveTranslationArgs) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The translation of the Wms.RemotingObjects.Globalization.SaveTranslationArgs.ResourceId in Wms.RemotingObjects.Globalization.SaveTranslationArgs.LocaleId.

Get: Value(self: SaveTranslationArgs) -> str

Set: Value(self: SaveTranslationArgs) = value
"""



class Translation():
    """ Translation() """
    Instance = Translation
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def LoadFromRegistry():
        """ LoadFromRegistry() -> str """
        pass

    @staticmethod
    def SaveToRegistry(culture):
        """ SaveToRegistry(culture: str) """
        pass

    def ToString(self):
        """ ToString(self: Translation) -> str """
        pass

    Culture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Culture(self: Translation) -> str

Set: Culture(self: Translation) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: Translation) -> str

Set: Name(self: Translation) = value
"""

    Resources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Resources(self: Translation) -> Dictionary[str, object]

Set: Resources(self: Translation) = value
"""

    ResourseSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ResourseSet(self: Translation) -> str

Set: ResourseSet(self: Translation) = value
"""



class Translations(List):
    """ Translations() """
    Instance = Translations
    """hardcoded/returns an instance of the class"""
    def Add(self, *__args):
        """ Add(self: Translations, culture: str, resourseSet: str) """
        pass

    def ToString(self):
        """ ToString(self: Translations) -> str """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


