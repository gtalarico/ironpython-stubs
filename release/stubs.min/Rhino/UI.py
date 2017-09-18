# encoding: utf-8
# module Rhino.UI calls itself UI
# from Rhino3dmIO,Version=5.1.30000.14,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DistanceDisplayMode(Enum,IComparable,IFormattable,IConvertible):
 """ enum DistanceDisplayMode,values: Decimal (0),FeetInches (2),Fractional (1) """
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
 Decimal=None
 FeetInches=None
 Fractional=None
 value__=None


class LOC(object):
 # no doc
 @staticmethod
 def COMMANDNAME(english):
  """ COMMANDNAME(english: str) -> str """
  pass
 @staticmethod
 def CON(english,assemblyFromObject=None):
  """
  CON(english: str,assemblyFromObject: object) -> LocalizeStringPair
  CON(english: str) -> LocalizeStringPair
  """
  pass
 @staticmethod
 def COV(engilsh,assemblyFromObject=None):
  """
  COV(engilsh: str,assemblyFromObject: object) -> LocalizeStringPair
  COV(engilsh: str) -> LocalizeStringPair
  """
  pass
 @staticmethod
 def STR(english,assemblyOrObject=None):
  """
  STR(english: str,assemblyOrObject: object) -> str
  STR(english: str) -> str
  """
  pass
 __all__=[
  'COMMANDNAME',
  'CON',
  'COV',
  'STR',
 ]


class Localization(object):
 # no doc
 @staticmethod
 def GetAssemblyFromObject(assemblyOrObject):
  """ GetAssemblyFromObject(assemblyOrObject: object) -> Assembly """
  pass
 @staticmethod
 def LocalizeCommandName(english,assemblyOrObject=None):
  """
  LocalizeCommandName(english: str,assemblyOrObject: object) -> str
  LocalizeCommandName(english: str) -> str
  """
  pass
 @staticmethod
 def LocalizeCommandOptionName(english,*__args):
  """
  LocalizeCommandOptionName(english: str,assemblyOrObject: object,contextId: int) -> LocalizeStringPair
  LocalizeCommandOptionName(english: str,contextId: int) -> LocalizeStringPair
  """
  pass
 @staticmethod
 def LocalizeCommandOptionValue(english,*__args):
  """
  LocalizeCommandOptionValue(english: str,assemblyOrObject: object,contextId: int) -> LocalizeStringPair
  LocalizeCommandOptionValue(english: str,contextId: int) -> LocalizeStringPair
  """
  pass
 @staticmethod
 def LocalizeDialogItem(assemblyOrObject,key,english):
  """ LocalizeDialogItem(assemblyOrObject: object,key: str,english: str) -> str """
  pass
 @staticmethod
 def LocalizeString(english,*__args):
  """
  LocalizeString(english: str,assemblyOrObject: object,contextId: int) -> str
  LocalizeString(english: str,contextId: int) -> str
  """
  pass
 @staticmethod
 def SetLanguageId(id):
  """ SetLanguageId(id: int) -> bool """
  pass
 __all__=[
  'GetAssemblyFromObject',
  'LocalizeCommandName',
  'LocalizeCommandOptionName',
  'LocalizeCommandOptionValue',
  'LocalizeDialogItem',
  'LocalizeString',
  'SetLanguageId',
 ]


class LocalizeStringPair(object):
 """ LocalizeStringPair(english: str,local: str) """
 @staticmethod
 def __new__(self,english,local):
  """ __new__(cls: type,english: str,local: str) """
  pass
 English=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: English(self: LocalizeStringPair) -> str

"""

 Local=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Local(self: LocalizeStringPair) -> str

"""



