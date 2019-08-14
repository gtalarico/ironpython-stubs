# encoding: utf-8
# module Wms.RemotingImplementation.Helpers calls itself Helpers
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DataFlowObjectHelper():
    # no doc
    Instance = DataFlowObjectHelper
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def AreAllQuestionAnsweredPositive(dfObject):
        """ AreAllQuestionAnsweredPositive[T](dfObject: DataFlowObject[T]) -> DataFlowObject[T] """
        pass

    @staticmethod
    def IsQuestionAnswered(dfObject, key, answer):
        """ IsQuestionAnswered[T](dfObject: DataFlowObject[T], key: str) -> (bool, AnswerOptionsEnum) """
        pass

    @staticmethod
    def IsQuestionAnsweredPositive(dfObject, key, answer):
        """ IsQuestionAnsweredPositive[T](dfObject: DataFlowObject[T], key: str) -> (bool, AnswerOptionsEnum) """
        pass

    @staticmethod
    def LogDataFlowResult(dfObject):
        """ LogDataFlowResult[T](dfObject: DataFlowObject[T]) """
        pass

    __all__ = [
        'AreAllQuestionAnsweredPositive',
        'IsQuestionAnswered',
        'IsQuestionAnsweredPositive',
        'LogDataFlowResult',
    ]


class DecimalExtensions():
    # no doc
    Instance = DecimalExtensions
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def FormatDecimal(value):
        """ FormatDecimal(value: Decimal) -> str """
        pass

    __all__ = [
        'FormatDecimal',
    ]


class GlobalizationHelper():
    # no doc
    Instance = GlobalizationHelper
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def ClearResourceCache():
        """ ClearResourceCache() """
        pass

    @staticmethod
    def GetCultureName(culture):
        """ GetCultureName(culture: str) -> str """
        pass

    @staticmethod
    def GetResources(resourceSet, culture):
        """ GetResources(resourceSet: str, culture: str) -> Translation """
        pass

    @staticmethod
    def SetGlobalizationSettings():
        """ SetGlobalizationSettings() """
        pass

    __all__ = [
        'ClearResourceCache',
        'GetCultureName',
        'GetResources',
        'SetGlobalizationSettings',
    ]


class LabelHelper():
    # no doc
    Instance = LabelHelper
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def GetPlaceholders(label, systemFieldsRegEx):
        """ GetPlaceholders(label: PrintLabel, systemFieldsRegEx: str) -> List[str] """
        pass

    @staticmethod
    def RenderLabel(label, *__args):
        """
        RenderLabel(label: PrintLabel, data: DataRow, systemFieldsRegEx: str) -> str
        RenderLabel(label: PrintLabel, headerData: DataRow, itemData: DataTable, systemFieldsRegEx: str) -> List[str]
        """
        pass

    __all__ = [
        'GetPlaceholders',
        'RenderLabel',
    ]


class OrderMatchesCustomerValidator():
    """ OrderMatchesCustomerValidator() """
    Instance = OrderMatchesCustomerValidator
    """hardcoded/returns an instance of the class"""
    def OrderMatchesCustomer(self, order, customer):
        """ OrderMatchesCustomer(self: OrderMatchesCustomerValidator, order: OutboundOrder, customer: Customer) -> bool """
        pass

    CheckCustomerContact = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckCustomerContact(self: OrderMatchesCustomerValidator) -> bool

Set: CheckCustomerContact(self: OrderMatchesCustomerValidator) = value
"""

    OrderMatchesCustomerDelegate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderMatchesCustomerDelegate(self: OrderMatchesCustomerValidator) -> OnOrderMatchesCustomerDelegate

Set: OrderMatchesCustomerDelegate(self: OrderMatchesCustomerValidator) = value
"""


    OnOrderMatchesCustomerDelegate = None


class SettingsHelper:
    """ SettingsHelper(settingsObject: object) """
    Instance = SettingsHelper
    """hardcoded/returns an instance of the class"""
    def Dispose(self):
        """ Dispose(self: SettingsHelper) """
        pass

    def Load(self, onlyUserAndMachineSettings=None):
        """ Load(self: SettingsHelper)Load(self: SettingsHelper, onlyUserAndMachineSettings: bool) """
        pass

    def LoadMemberValue(self, *__args):
        """ LoadMemberValue(self: SettingsHelper, member: MemberInfo)LoadMemberValue(self: SettingsHelper, memberName: str) """
        pass

    def SaveAll(self, onlyUserAndMachineSettings=None):
        """ SaveAll(self: SettingsHelper)SaveAll(self: SettingsHelper, onlyUserAndMachineSettings: bool) """
        pass

    def SaveMemberValue(self, *__args):
        """ SaveMemberValue(self: SettingsHelper, member: MemberInfo)SaveMemberValue(self: SettingsHelper, memberName: str, value: object) """
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
    def __new__(self, settingsObject):
        """ __new__(cls: type, settingsObject: object) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class StringHelpers():
    # no doc
    Instance = StringHelpers
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def CreateMessageFromCollection(message, collection):
        """ CreateMessageFromCollection(message: str, collection: IEnumerable[str]) -> str """
        pass

    @staticmethod
    def EncodeAsCode128SetA(input):
        """ EncodeAsCode128SetA(input: str) -> str """
        pass

    @staticmethod
    def NormalizeForAscii(input):
        """ NormalizeForAscii(input: str) -> str """
        pass

    @staticmethod
    def RemoveNonAsciiCharacters(input, replaceWith=None):
        """
        RemoveNonAsciiCharacters(input: str, replaceWith: str) -> str
        RemoveNonAsciiCharacters(input: str) -> str
        """
        pass

    __all__ = [
        'CreateMessageFromCollection',
        'EncodeAsCode128SetA',
        'NormalizeForAscii',
        'RemoveNonAsciiCharacters',
    ]


