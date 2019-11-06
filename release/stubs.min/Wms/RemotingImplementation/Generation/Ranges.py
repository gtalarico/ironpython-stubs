# encoding: utf-8
# module Wms.RemotingImplementation.Generation.Ranges calls itself Ranges
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class BaseRange(object):
 """ BaseRange(numberGeneration: INumberGeneration) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return BaseRange()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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


class NumberRangeFactory(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return NumberRangeFactory()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def GetRange(rangeType):
  """ GetRange(rangeType: NumberRangeType) -> BaseRange """
  pass
 __all__=[
  'GetRange',
 ]


class SSCCRange(BaseRange):
 """ SSCCRange(numberGeneration: INumberGeneration) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return SSCCRange()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def ResetRange(self,dfObject,manualReset):
  """ ResetRange(self: SSCCRange,dfObject: DataFlowObject[NumberRange],manualReset: bool) -> DataFlowObject[NumberRange] """
  pass
 @staticmethod
 def __new__(self,numberGeneration):
  """ __new__(cls: type,numberGeneration: INumberGeneration) """
  pass
 KeyUpdateExtensionDigit='UpdateExtensionDigit'
 _numberGeneration=None


