# encoding: utf-8
# module Wms.RemotingImplementation.Generation.Ranges calls itself Ranges
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BaseRange():
    """ BaseRange(numberGeneration: INumberGeneration) """
    Instance = BaseRange
    """hardcoded/returns an instance of the class"""
    def AddGenerationArgs(self, *args): #cannot find CLR method
        """ AddGenerationArgs[T](self: BaseRange, dfObject: DataFlowObject[T], numberRange: NumberRange, numbersToGenerate: int) """
        pass

    def AddGenerator(self, *args): #cannot find CLR method
        """ AddGenerator[T](self: BaseRange, dfObject: DataFlowObject[T], numberRange: NumberRange, numbersToGenerate: int) """
        pass

    def CreateGenerator(self, *args): #cannot find CLR method
        """ CreateGenerator(self: BaseRange) -> IGenerator """
        pass

    def PostGenerateCheck(self, *args): #cannot find CLR method
        """ PostGenerateCheck[T](self: BaseRange, dfObject: DataFlowObject[T], numberRange: NumberRange, numbersToGenerate: int) -> bool """
        pass

    def PreGenerateCheck(self, *args): #cannot find CLR method
        """ PreGenerateCheck[T](self: BaseRange, dfObject: DataFlowObject[T], numberRange: NumberRange, numbersToGenerate: int) """
        pass

    def RegisterUsedNumbers(self, *args): #cannot find CLR method
        """ RegisterUsedNumbers[T](self: BaseRange, dfObject: DataFlowObject[T]) """
        pass

    def ReserveNumbers(self, dfObject):
        """ ReserveNumbers[T](self: BaseRange, dfObject: DataFlowObject[T]) -> DataFlowObject[T] """
        pass

    def ResetRange(self, dfObject, manualReset):
        """ ResetRange(self: BaseRange, dfObject: DataFlowObject[NumberRange], manualReset: bool) -> DataFlowObject[NumberRange] """
        pass

    def UpdateRange(self, range, currentNumber):
        """ UpdateRange(self: BaseRange, range: NumberRange, currentNumber: int) """
        pass

    def Validate(self, *args): #cannot find CLR method
        """ Validate[T](self: BaseRange, dfObject: DataFlowObject[T]) -> DataFlowObject[T] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, numberGeneration):
        """ __new__(cls: type, numberGeneration: INumberGeneration) """
        pass

    EndOfRangeKey = 'WarningEndOfRange'
    _numberGeneration = None


class NumberRangeFactory():
    # no doc
    Instance = NumberRangeFactory
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def GetRange(rangeType):
        """ GetRange(rangeType: NumberRangeType) -> BaseRange """
        pass

    __all__ = [
        'GetRange',
    ]


class SSCCRange(BaseRange):
    """ SSCCRange(numberGeneration: INumberGeneration) """
    Instance = SSCCRange
    """hardcoded/returns an instance of the class"""
    def ResetRange(self, dfObject, manualReset):
        """ ResetRange(self: SSCCRange, dfObject: DataFlowObject[NumberRange], manualReset: bool) -> DataFlowObject[NumberRange] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, numberGeneration):
        """ __new__(cls: type, numberGeneration: INumberGeneration) """
        pass

    KeyUpdateExtensionDigit = 'UpdateExtensionDigit'
    _numberGeneration = None


