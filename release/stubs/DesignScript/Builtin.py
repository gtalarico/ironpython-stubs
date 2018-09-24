# encoding: utf-8
# module DesignScript.Builtin calls itself Builtin
# from DesignScriptBuiltin, Version=2.0.1.5055, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Dictionary(object):
    # no doc
    @staticmethod
    def ByKeysValues(keys, values):
        """ ByKeysValues(keys: IList[str], values: IList[object]) -> Dictionary """
        pass

    def Components(self):
        """ Components(self: Dictionary) -> IDictionary[str, object] """
        pass

    def RemoveKeys(self, keys):
        """ RemoveKeys(self: Dictionary, keys: IList[str]) -> Dictionary """
        pass

    def SetValueAtKeys(self, keys, values):
        """ SetValueAtKeys(self: Dictionary, keys: IList[str], values: IList[object]) -> Dictionary """
        pass

    def ValueAtKey(self, key):
        """ ValueAtKey(self: Dictionary, key: str) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: Dictionary) -> int

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Keys(self: Dictionary) -> IEnumerable[str]

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Values(self: Dictionary) -> IEnumerable[object]

"""



class Get(object):
    # no doc
    @staticmethod
    def ValueAtIndex(*__args):
        """
        ValueAtIndex(list: IList, index: int) -> object
        ValueAtIndex(dictionary: Dictionary, key: str) -> object
        """
        pass

    __all__ = [
        'ValueAtIndex',
    ]


