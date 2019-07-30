# encoding: utf-8
# module System.Linq.Dynamic calls itself Dynamic
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important

# no functions
# classes

class DynamicClass(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DynamicClass()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def ToString(self):
  """ ToString(self: DynamicClass) -> str """
  pass

class DynamicExpression(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DynamicExpression()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def CreateClass(properties):
  """
  CreateClass(*properties: Array[DynamicProperty]) -> Type
  CreateClass(properties: IEnumerable[DynamicProperty]) -> Type
  """
  pass
 @staticmethod
 def Parse(resultType,expression,values):
  """ Parse(resultType: Type,expression: str,*values: Array[object]) -> Expression """
  pass
 @staticmethod
 def ParseLambda(*__args):
  """
  ParseLambda(itType: Type,resultType: Type,expression: str,*values: Array[object]) -> LambdaExpression
  ParseLambda(parameters: Array[ParameterExpression],resultType: Type,expression: str,*values: Array[object]) -> LambdaExpression
  ParseLambda[(T,S)](expression: str,*values: Array[object]) -> Expression[Func[T,S]]
  """
  pass
 __all__=[
  'CreateClass',
  'Parse',
  'ParseLambda',
 ]


class DynamicProperty(object):
 """ DynamicProperty(name: str,type: Type) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DynamicProperty()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,name,type):
  """ __new__(cls: type,name: str,type: Type) """
  pass
 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: DynamicProperty) -> str

"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Type(self: DynamicProperty) -> Type

"""



class DynamicQueryable(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DynamicQueryable()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def Any(source):
  """ Any(source: IQueryable) -> bool """
  pass
 @staticmethod
 def Count(source):
  """ Count(source: IQueryable) -> int """
  pass
 @staticmethod
 def GroupBy(source,keySelector,elementSelector,values):
  """ GroupBy(source: IQueryable,keySelector: str,elementSelector: str,*values: Array[object]) -> IQueryable """
  pass
 @staticmethod
 def OrderBy(source,ordering,values):
  """
  OrderBy[T](source: IQueryable[T],ordering: str,*values: Array[object]) -> IQueryable[T]
  OrderBy(source: IQueryable,ordering: str,*values: Array[object]) -> IQueryable
  """
  pass
 @staticmethod
 def Select(source,selector,values):
  """ Select(source: IQueryable,selector: str,*values: Array[object]) -> IQueryable """
  pass
 @staticmethod
 def Skip(source,count):
  """ Skip(source: IQueryable,count: int) -> IQueryable """
  pass
 @staticmethod
 def Take(source,count):
  """ Take(source: IQueryable,count: int) -> IQueryable """
  pass
 @staticmethod
 def Where(source,predicate,values):
  """
  Where[T](source: IQueryable[T],predicate: str,*values: Array[object]) -> IQueryable[T]
  Where(source: IQueryable,predicate: str,*values: Array[object]) -> IQueryable
  """
  pass
 __all__=[
  'Any',
  'Count',
  'GroupBy',
  'OrderBy',
  'Select',
  'Skip',
  'Take',
  'Where',
 ]


class ParseException(Exception):
 """ ParseException(message: str,position: int) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ParseException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def ToString(self):
  """ ToString(self: ParseException) -> str """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message,position):
  """ __new__(cls: type,message: str,position: int) """
  pass
 def __str__(self,*args):
  pass
 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Position(self: ParseException) -> int

"""


 SerializeObjectState=None


