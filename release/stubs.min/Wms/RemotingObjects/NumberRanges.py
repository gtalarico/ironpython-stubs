# encoding: utf-8
# module Wms.RemotingObjects.NumberRanges calls itself NumberRanges
# from Wms.RemotingObjects,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class GenerateArgs:
 """
 GenerateArgs()
 GenerateArgs(numberRange: NumberRange)
 """
 @staticmethod
 def __new__(self,numberRange=None):
  """
  __new__(cls: type)
  __new__(cls: type,numberRange: NumberRange)
  """
  pass
 Arguments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Arguments(self: GenerateArgs) -> Array[object]

Set: Arguments(self: GenerateArgs)=value
"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Length(self: GenerateArgs) -> int

Set: Length(self: GenerateArgs)=value
"""

 Prefix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Prefix(self: GenerateArgs) -> str

Set: Prefix(self: GenerateArgs)=value
"""

 StartingNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: StartingNumber(self: GenerateArgs) -> int

Set: StartingNumber(self: GenerateArgs)=value
"""

 Suffix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Suffix(self: GenerateArgs) -> str

Set: Suffix(self: GenerateArgs)=value
"""



class GenerateNumbersBaseArgs:
 """
 GenerateNumbersBaseArgs()
 GenerateNumbersBaseArgs(id: int,type: NumberRangeType)
 GenerateNumbersBaseArgs(id: int,type: NumberRangeType,numbersToGenerate: int)
 """
 def AddGenerationArgs(self,args,numbersToGenerate):
  """ AddGenerationArgs(self: GenerateNumbersBaseArgs,args: GenerateArgs,numbersToGenerate: int) """
  pass
 def AddGenerator(self,generator,args,numbersToGenerate):
  """ AddGenerator(self: GenerateNumbersBaseArgs,generator: IGenerator,args: GenerateArgs,numbersToGenerate: int) """
  pass
 def Generate(self):
  """ Generate(self: GenerateNumbersBaseArgs) -> IEnumerable[IGeneratedBarcode] """
  pass
 def GenerateOne(self):
  """ GenerateOne(self: GenerateNumbersBaseArgs) -> IGeneratedBarcode """
  pass
 @staticmethod
 def __new__(self,id=None,type=None,numbersToGenerate=None):
  """
  __new__(cls: type)
  __new__(cls: type,id: int,type: NumberRangeType)
  __new__(cls: type,id: int,type: NumberRangeType,numbersToGenerate: int)
  """
  pass
 AdditionalArguments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AdditionalArguments(self: GenerateNumbersBaseArgs) -> SerializableDictionary[str,object]

"""

 Ascending=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Ascending(self: GenerateNumbersBaseArgs) -> bool

Set: Ascending(self: GenerateNumbersBaseArgs)=value
"""

 HasGenerator=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasGenerator(self: GenerateNumbersBaseArgs) -> bool

"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: GenerateNumbersBaseArgs) -> int

Set: Id(self: GenerateNumbersBaseArgs)=value
"""

 NumbersToGenerate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NumbersToGenerate(self: GenerateNumbersBaseArgs) -> int

Set: NumbersToGenerate(self: GenerateNumbersBaseArgs)=value
"""

 RegisterNumbersAsUsed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: RegisterNumbersAsUsed(self: GenerateNumbersBaseArgs) -> bool

Set: RegisterNumbersAsUsed(self: GenerateNumbersBaseArgs)=value
"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Type(self: GenerateNumbersBaseArgs) -> NumberRangeType

Set: Type(self: GenerateNumbersBaseArgs)=value
"""



class GenerateBarcodeLabelArgs:
 """
 GenerateBarcodeLabelArgs()
 GenerateBarcodeLabelArgs(id: int,type: NumberRangeType)
 GenerateBarcodeLabelArgs(id: int,type: NumberRangeType,numbersToGenerate: int)
 """
 @staticmethod
 def __new__(self,id=None,type=None,numbersToGenerate=None):
  """
  __new__(cls: type)
  __new__(cls: type,id: int,type: NumberRangeType)
  __new__(cls: type,id: int,type: NumberRangeType,numbersToGenerate: int)
  """
  pass
 LabelName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LabelName(self: GenerateBarcodeLabelArgs) -> str

Set: LabelName(self: GenerateBarcodeLabelArgs)=value
"""

 Printer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Printer(self: GenerateBarcodeLabelArgs) -> str

Set: Printer(self: GenerateBarcodeLabelArgs)=value
"""

 PrintingOptions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PrintingOptions(self: GenerateBarcodeLabelArgs) -> PrintingOptions

Set: PrintingOptions(self: GenerateBarcodeLabelArgs)=value
"""



class GetNumberRangeArgs:
 """ GetNumberRangeArgs() """
 Filter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Filter(self: GetNumberRangeArgs) -> str

Set: Filter(self: GetNumberRangeArgs)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: GetNumberRangeArgs) -> int

Set: Id(self: GetNumberRangeArgs)=value
"""

 IsTypeSet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsTypeSet(self: GetNumberRangeArgs) -> bool

Set: IsTypeSet(self: GetNumberRangeArgs)=value
"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Type(self: GetNumberRangeArgs) -> NumberRangeType

Set: Type(self: GetNumberRangeArgs)=value
"""


 Default=None


class NumberRange:
 """ NumberRange() """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 Current=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Current(self: NumberRange) -> int

Set: Current(self: NumberRange)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Description(self: NumberRange) -> str

Set: Description(self: NumberRange)=value
"""

 From=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: From(self: NumberRange) -> int

Set: From(self: NumberRange)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: NumberRange) -> int

Set: Id(self: NumberRange)=value
"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Length(self: NumberRange) -> int

Set: Length(self: NumberRange)=value
"""

 Prefix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Prefix(self: NumberRange) -> str

Set: Prefix(self: NumberRange)=value
"""

 RangeType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: RangeType(self: NumberRange) -> NumberRangeType

Set: RangeType(self: NumberRange)=value
"""

 ResetBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ResetBy(self: NumberRange) -> str

Set: ResetBy(self: NumberRange)=value
"""

 ResetOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ResetOn(self: NumberRange) -> DateTime

Set: ResetOn(self: NumberRange)=value
"""

 Suffix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Suffix(self: NumberRange) -> str

Set: Suffix(self: NumberRange)=value
"""

 To=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: To(self: NumberRange) -> int

Set: To(self: NumberRange)=value
"""



class NumberRangeType:
 """ enum NumberRangeType,values: PickBatch (2),Regular (0),SSCC (1) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 PickBatch=None
 Regular=None
 SSCC=None
 value__=None


