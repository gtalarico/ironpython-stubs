# encoding: utf-8
# module Wms.RemotingObjects.MetaData calls itself MetaData
# from Wms.RemotingObjects, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class EnumHelper:
    """ EnumHelper() """
    @staticmethod
    def ParseOrDefault(input, defaultValue, ignoreCase):
        """ ParseOrDefault[T](input: str, defaultValue: T, ignoreCase: bool) -> T """
        pass

    @staticmethod
    def TryParse(input, defaultValue, result, ignoreCase):
        """ TryParse[T](input: str, defaultValue: T, ignoreCase: bool) -> (bool, T) """
        pass


class EnumStringHelper:
    """ EnumStringHelper(enumType: Type) """
    def GetListValues(self):
        """ GetListValues(self: EnumStringHelper) -> IList """
        pass

    def GetStringValue(self, *__args):
        """
        GetStringValue(self: EnumStringHelper, valueName: str) -> str
        GetStringValue(value: Enum) -> str
        """
        pass

    def GetStringValues(self):
        """ GetStringValues(self: EnumStringHelper) -> List[str] """
        pass

    def IsStringDefined(self, *__args):
        """
        IsStringDefined(self: EnumStringHelper, stringValue: str) -> bool
        IsStringDefined(self: EnumStringHelper, stringValue: str, ignoreCase: bool) -> bool
        IsStringDefined(enumType: Type, stringValue: str) -> bool
        IsStringDefined(enumType: Type, stringValue: str, ignoreCase: bool) -> bool
        """
        pass

    @staticmethod
    def Parse(type, stringValue, ignoreCase=None):
        """
        Parse(type: Type, stringValue: str) -> object
        Parse(type: Type, stringValue: str, ignoreCase: bool) -> object
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, enumType):
        """ __new__(cls: type, enumType: Type) """
        pass

    EnumType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnumType(self: EnumStringHelper) -> Type

"""



class EnumStringValueAttribute:
    """ EnumStringValueAttribute(value: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value):
        """ __new__(cls: type, value: str) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: EnumStringValueAttribute) -> str

"""



