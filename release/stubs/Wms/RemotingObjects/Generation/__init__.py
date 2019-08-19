# encoding: utf-8
# module Wms.RemotingObjects.Generation calls itself Generation
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AddUsedNumberArgs():
    """
    AddUsedNumberArgs()
    AddUsedNumberArgs(number: str, type: NumberRangeType)
    """
    @staticmethod # known case of __new__
    def __new__(self, number=None, type=None):
        """
        __new__(cls: type)
        __new__(cls: type, number: str, type: NumberRangeType)
        """
        pass

    Numbers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Numbers(self: AddUsedNumberArgs) -> List[str]

Set: Numbers(self: AddUsedNumberArgs) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: AddUsedNumberArgs) -> NumberRangeType

Set: Type(self: AddUsedNumberArgs) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return AddUsedNumberArgs()

class UsedNumberArgs():
    """ UsedNumberArgs() """
    CheckAfterDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckAfterDate(self: UsedNumberArgs) -> Nullable[DateTime]

Set: CheckAfterDate(self: UsedNumberArgs) = value
"""

    ExclusionList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExclusionList(self: UsedNumberArgs) -> List[object]

Set: ExclusionList(self: UsedNumberArgs) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: UsedNumberArgs) -> str

Set: Number(self: UsedNumberArgs) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: UsedNumberArgs) -> NumberRangeType

Set: Type(self: UsedNumberArgs) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return UsedNumberArgs()

# variables with complex values

