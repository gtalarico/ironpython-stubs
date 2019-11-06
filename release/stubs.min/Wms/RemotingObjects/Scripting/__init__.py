# encoding: utf-8
# module Wms.RemotingObjects.Scripting calls itself Scripting
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from System.Collections.Generic import *
from ..__init__ import *

# no functions
# classes

class GetScriptArgs(object):
 """ GetScriptArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return GetScriptArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Active=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Active(self: GetScriptArgs) -> Nullable[bool]

Set: Active(self: GetScriptArgs)=value
"""

 Filter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Filter(self: GetScriptArgs) -> str

Set: Filter(self: GetScriptArgs)=value
"""

 Hook=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Hook(self: GetScriptArgs) -> str

Set: Hook(self: GetScriptArgs)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: GetScriptArgs) -> int

Set: Id(self: GetScriptArgs)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Name(self: GetScriptArgs) -> str

Set: Name(self: GetScriptArgs)=value
"""

 ZoneId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ZoneId(self: GetScriptArgs) -> int

Set: ZoneId(self: GetScriptArgs)=value
"""



class PythonError(object):
 """
 PythonError(message: str,span: SourceSpan,errorCode: int,severity: ErrorSeverity)
 PythonError()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PythonError()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,message=None,span=None,errorCode=None,severity=None):
  """
  __new__(cls: type,message: str,span: SourceSpan,errorCode: int,severity: ErrorSeverity)
  __new__(cls: type)
  """
  pass
 ErrorCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ErrorCode(self: PythonError) -> int

Set: ErrorCode(self: PythonError)=value
"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Message(self: PythonError) -> str

Set: Message(self: PythonError)=value
"""

 Severity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Severity(self: PythonError) -> ErrorSeverity

Set: Severity(self: PythonError)=value
"""

 Span=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Span(self: PythonError) -> SourceSpan

Set: Span(self: PythonError)=value
"""


 ErrorSeverity=None


class ScriptSnippet(object):
 """ ScriptSnippet() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ScriptSnippet()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Description(self: ScriptSnippet) -> str

Set: Description(self: ScriptSnippet)=value
"""

 Script=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Script(self: ScriptSnippet) -> str

Set: Script(self: ScriptSnippet)=value
"""



class SourceLocation(object):
 """
 SourceLocation()
 SourceLocation(index: int,line: int,column: int)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return SourceLocation()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def Compare(left,right):
  """ Compare(left: SourceLocation,right: SourceLocation) -> int """
  pass
 def Equals(self,obj):
  """ Equals(self: SourceLocation,obj: object) -> bool """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: SourceLocation) -> int """
  pass
 def ToString(self):
  """ ToString(self: SourceLocation) -> str """
  pass
 def __cmp__(self,*args):
  """ x.__cmp__(y) <==> cmp(x,y) """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 @staticmethod
 def __new__(self,index=None,line=None,column=None):
  """
  __new__(cls: type)
  __new__(cls: type,index: int,line: int,column: int)
  """
  pass
 def __ne__(self,*args):
  pass
 Column=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Column(self: SourceLocation) -> int

"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Index(self: SourceLocation) -> int

"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsValid(self: SourceLocation) -> bool

"""

 Line=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Line(self: SourceLocation) -> int

"""


 Invalid=None
 MinValue=None
 None_ =None


class SourceSpan(object):
 """
 SourceSpan()
 SourceSpan(start: SourceLocation,end: SourceLocation)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return SourceSpan()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Equals(self,obj):
  """ Equals(self: SourceSpan,obj: object) -> bool """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: SourceSpan) -> int """
  pass
 def ToString(self):
  """ ToString(self: SourceSpan) -> str """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,start=None,end=None):
  """
  __new__(cls: type)
  __new__(cls: type,start: SourceLocation,end: SourceLocation)
  """
  pass
 def __ne__(self,*args):
  pass
 End=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: End(self: SourceSpan) -> SourceLocation

"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsValid(self: SourceSpan) -> bool

"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Length(self: SourceSpan) -> int

"""

 Start=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Start(self: SourceSpan) -> SourceLocation

"""


 Invalid=None
 None_ =None


class ZoneScript(DbObject):
 """ ZoneScript() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ZoneScript()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Clone(self):
  """ Clone(self: ZoneScript) -> object """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 Active=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Active(self: ZoneScript) -> bool

Set: Active(self: ZoneScript)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Description(self: ZoneScript) -> str

Set: Description(self: ZoneScript)=value
"""

 HasScript=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: HasScript(self: ZoneScript) -> bool

"""

 Hook=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Hook(self: ZoneScript) -> str

Set: Hook(self: ZoneScript)=value
"""

 HookSourceVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: HookSourceVersion(self: ZoneScript) -> int

Set: HookSourceVersion(self: ZoneScript)=value
"""

 HookVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: HookVersion(self: ZoneScript) -> int

Set: HookVersion(self: ZoneScript)=value
"""

 HookVersionDifference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: HookVersionDifference(self: ZoneScript) -> bool

Set: HookVersionDifference(self: ZoneScript)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: ZoneScript) -> int

Set: Id(self: ZoneScript)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Name(self: ZoneScript) -> str

Set: Name(self: ZoneScript)=value
"""

 ScriptToExecute=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ScriptToExecute(self: ZoneScript) -> str

Set: ScriptToExecute(self: ZoneScript)=value
"""

 TreeOrder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: TreeOrder(self: ZoneScript) -> int

Set: TreeOrder(self: ZoneScript)=value
"""

 TreePath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: TreePath(self: ZoneScript) -> str

Set: TreePath(self: ZoneScript)=value
"""

 ZoneId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ZoneId(self: ZoneScript) -> int

Set: ZoneId(self: ZoneScript)=value
"""



class ZoneScripts(FindableList):
 """ ZoneScripts() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ZoneScripts()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def FromIEnumerable(list):
  """ FromIEnumerable(list: IEnumerable[ZoneScript]) -> ZoneScripts """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 DisplayMember='Name'
 ValueMember='Id'


# variables with complex values

