# encoding: utf-8
# module Wms.RemotingImplementation.Generation.Ranges calls itself Ranges
# from Wms.RemotingImplementation,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BaseRange:
 """ BaseRange(numberGeneration: INumberGeneration) """
 def AddGenerationArgs(self,*args):
  """ AddGenerationArgs[T](self: BaseRange,dfObject: DataFlowObject[T],numberRange: NumberRange,numbersToGenerate: int) """
  pass
 def AddGenerator(self,*args):
  """ AddGenerator[T](self: BaseRange,dfObject: DataFlowObject[T],numberRange: NumberRange,numbersToGenerate: int) """
  pass
 def CreateGenerator(self,*args):
  """ CreateGenerator(self: BaseRange) -> IGenerator """
  pass
 def PostGenerateCheck(self,*args):
  """ PostGenerateCheck[T](self: BaseRange,dfObject: DataFlowObject[T],numberRange: NumberRange,numbersToGenerate: int) -> bool """
  pass
 def PreGenerateCheck(self,*args):
  """ PreGenerateCheck[T](self: BaseRange,dfObject: DataFlowObject[T],numberRange: NumberRange,numbersToGenerate: int) """
  pass
 def RegisterUsedNumbers(self,*args):
  """ RegisterUsedNumbers[T](self: BaseRange,dfObject: DataFlowObject[T]) """
  pass
 def ReserveNumbers(self,dfObject):
  """ ReserveNumbers[T](self: BaseRange,dfObject: DataFlowObject[T]) -> DataFlowObject[T] """
  pass
 def ResetRange(self,dfObject,manualReset):
  """ ResetRange(self: BaseRange,dfObject: DataFlowObject[NumberRange],manualReset: bool) -> DataFlowObject[NumberRange] """
  pass
 def UpdateRange(self,range,currentNumber):
  """ UpdateRange(self: BaseRange,range: NumberRange,currentNumber: int) """
  pass
 def Validate(self,*args):
  """ Validate[T](self: BaseRange,dfObject: DataFlowObject[T]) -> DataFlowObject[T] """
  pass
 @staticmethod
 def __new__(self,numberGeneration):
  """ __new__(cls: type,numberGeneration: INumberGeneration) """
  pass
 EndOfRangeKey='WarningEndOfRange'
 _numberGeneration=None


class NumberRangeFactory:
 # no doc
 @staticmethod
 def GetRange(rangeType):
  """ GetRange(rangeType: NumberRangeType) -> BaseRange """
  pass
 __all__=[
  'GetRange',
 ]


class SSCCRange:
 """ SSCCRange(numberGeneration: INumberGeneration) """
 def ResetRange(self,dfObject,manualReset):
  """ ResetRange(self: SSCCRange,dfObject: DataFlowObject[NumberRange],manualReset: bool) -> DataFlowObject[NumberRange] """
  pass
 @staticmethod
 def __new__(self,numberGeneration):
  """ __new__(cls: type,numberGeneration: INumberGeneration) """
  pass
 KeyUpdateExtensionDigit='UpdateExtensionDigit'
 _numberGeneration=None


