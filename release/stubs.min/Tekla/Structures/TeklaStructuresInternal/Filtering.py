# encoding: utf-8
# module Tekla.Structures.TeklaStructuresInternal.Filtering calls itself Filtering
# from Tekla.Structures,Version=2017.0.0.0,Culture=neutral,PublicKeyToken=2f04dbe497b71114
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BinaryFilterExpressionToken(object):
 """ BinaryFilterExpressionToken(FilterString: str,BinaryFilterOperatorType: BinaryFilterOperatorType,IsCollection: bool,Enabled: bool) """
 @staticmethod
 def __new__(self,FilterString,BinaryFilterOperatorType,IsCollection,Enabled):
  """ __new__(cls: type,FilterString: str,BinaryFilterOperatorType: BinaryFilterOperatorType,IsCollection: bool,Enabled: bool) """
  pass
 BinaryFilterOperatorType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BinaryFilterOperatorType(self: BinaryFilterExpressionToken) -> BinaryFilterOperatorType

Set: BinaryFilterOperatorType(self: BinaryFilterExpressionToken)=value
"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Enabled(self: BinaryFilterExpressionToken) -> bool

Set: Enabled(self: BinaryFilterExpressionToken)=value
"""

 FilterString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FilterString(self: BinaryFilterExpressionToken) -> str

Set: FilterString(self: BinaryFilterExpressionToken)=value
"""

 IsCollection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsCollection(self: BinaryFilterExpressionToken) -> bool

Set: IsCollection(self: BinaryFilterExpressionToken)=value
"""



class FilterExpressionGenerator(object):
 # no doc
 def Generate(self,FilterExpression,FilterExpressionFileType=None,FullFileName=None):
  """
  Generate(self: FilterExpressionGenerator,FilterExpression: FilterExpression,FilterExpressionFileType: FilterExpressionFileType,FullFileName: str) -> str
  Generate(self: FilterExpressionGenerator,FilterExpression: FilterExpression) -> str
  """
  pass
 def GenerateBinaryFilterExpression(self,*args):
  """ GenerateBinaryFilterExpression(self: FilterExpressionGenerator,BinaryFilterExpression: BinaryFilterExpression,TextWriter: TextWriter) """
  pass
 def GenerateBinaryFilterExpressionCollection(self,*args):
  """ GenerateBinaryFilterExpressionCollection(self: FilterExpressionGenerator,BinaryFilterExpressionCollection: BinaryFilterExpressionCollection,TextWriter: TextWriter) """
  pass
 def GenerateBinaryFilterItemOperatorType(self,*args):
  """ GenerateBinaryFilterItemOperatorType(self: FilterExpressionGenerator,BinaryFilterItemOperatorType: BinaryFilterOperatorType,TextWriter: TextWriter) """
  pass
 def GenerateExpression(self,*args):
  """ GenerateExpression(self: FilterExpressionGenerator,Expression: Expression,TextWriter: TextWriter) """
  pass
 def GenerateFilterExpression(self,*args):
  """ GenerateFilterExpression(self: FilterExpressionGenerator,FilterExpression: DataFilterExpression,TextWriter: TextWriter) """
  pass
 def GenerateOperatorType(self,*args):
  """ GenerateOperatorType(self: FilterExpressionGenerator,OperatorType: OperatorType,TextWriter: TextWriter) """
  pass
 def GetFilterExpressionFileExtension(self,*args):
  """ GetFilterExpressionFileExtension(self: FilterExpressionGenerator,FilterExpressionFileType: FilterExpressionFileType) -> str """
  pass
 def GetFilterExpressionsCount(self,*args):
  """ GetFilterExpressionsCount(Expression: Expression,Count: int) -> int """
  pass

class FilterExpressionGeneratorFactory(object):
 # no doc
 @staticmethod
 def CreateGenerator(FilterExpressionGeneratoryType=None):
  """
  CreateGenerator(FilterExpressionGeneratoryType: FilterExpressionGeneratorType) -> FilterExpressionGenerator
  CreateGenerator() -> FilterExpressionGenerator
  """
  pass
 __all__=[
  'CreateGenerator',
 ]


class FilterExpressionGeneratorType(Enum):
 """ enum FilterExpressionGeneratorType,values: C (2),TEKLA (0),XML (1) """
 C=None
 TEKLA=None
 value__=None
 XML=None


class FilterExpressionParser(object):
 # no doc
 def FindDataFilterExpression(self,*args):
  """ FindDataFilterExpression[T](InputString: str) -> T """
  pass
 def GetBinaryFilterExpressionElements(self,*args):
  """ GetBinaryFilterExpressionElements(self: FilterExpressionParser,BinaryFilterExpressionString: str) -> Array[str] """
  pass
 def Parse(self,FullFileName,Provider):
  """ Parse(self: FilterExpressionParser,FullFileName: str,Provider: IFormatProvider) -> FilterExpression """
  pass
 def ParseBinaryFilterExpression(self,*args):
  """ ParseBinaryFilterExpression(self: FilterExpressionParser,BinaryFilterExpressionString: str,Provider: IFormatProvider) -> FilterExpression """
  pass
 def ParseBooleanConstantFilterExpression(self,*args):
  """ ParseBooleanConstantFilterExpression(self: FilterExpressionParser,BooleanConstantString: str) -> BooleanConstantFilterExpression """
  pass
 def ParseBooleanOperatorType(self,*args):
  """ ParseBooleanOperatorType(self: FilterExpressionParser,BooleanOperatorTypeString: str) -> BooleanOperatorType """
  pass
 def ParseDateTimeConstantFilterExpression(self,*args):
  """ ParseDateTimeConstantFilterExpression(self: FilterExpressionParser,DateTimeConstantString: str,Provider: IFormatProvider) -> DateTimeConstantFilterExpression """
  pass
 def ParseDateTimeOperatorType(self,*args):
  """ ParseDateTimeOperatorType(self: FilterExpressionParser,DateTimeOperatorString: str) -> DateTimeOperatorType """
  pass
 def ParseExpressionString(self,FilterString,Provider):
  """ ParseExpressionString(self: FilterExpressionParser,FilterString: str,Provider: IFormatProvider) -> FilterExpression """
  pass
 def ParseLeftOperand(self,*args):
  """ ParseLeftOperand(self: FilterExpressionParser,BinaryFilterExpressionString: str) -> object """
  pass
 def ParseNumericConstantFilterExpression(self,*args):
  """ ParseNumericConstantFilterExpression(self: FilterExpressionParser,NumericConstantString: str,Provider: IFormatProvider) -> NumericConstantFilterExpression """
  pass
 def ParseNumericOperatorType(self,*args):
  """ ParseNumericOperatorType(self: FilterExpressionParser,NumericOperatorString: str) -> NumericOperatorType """
  pass
 def ParseString(self,*args):
  """ ParseString(self: FilterExpressionParser,FilterString: str,Provider: IFormatProvider) -> FilterExpression """
  pass
 def ParseStringConstantFilterExpression(self,*args):
  """ ParseStringConstantFilterExpression(self: FilterExpressionParser,StringConstantString: str) -> StringConstantFilterExpression """
  pass
 def ParseStringOperatorType(self,*args):
  """ ParseStringOperatorType(self: FilterExpressionParser,StringOperatorTypeString: str) -> StringOperatorType """
  pass
 def Tokenizer(self,*args):
  """ Tokenizer(self: FilterExpressionParser,FilterString: str) -> List[BinaryFilterExpressionToken] """
  pass

class FilterExpressionParserFactory(object):
 # no doc
 @staticmethod
 def CreateParser(FilterExpressionParserType=None):
  """
  CreateParser(FilterExpressionParserType: FilterExpressionParserType) -> FilterExpressionParser
  CreateParser() -> FilterExpressionParser
  """
  pass
 __all__=[
  'CreateParser',
 ]


class FilterExpressionParserType(Enum):
 """ enum FilterExpressionParserType,values: C (1),TEKLA (0) """
 C=None
 TEKLA=None
 value__=None


