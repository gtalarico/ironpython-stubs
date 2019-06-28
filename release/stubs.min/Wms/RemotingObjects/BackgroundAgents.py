# encoding: utf-8
# module Wms.RemotingObjects.BackgroundAgents calls itself BackgroundAgents
# from Wms.RemotingObjects,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BackgroundAgent:
 """ BackgroundAgent() """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 BackgroundAgentPk=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BackgroundAgentPk(self: BackgroundAgent) -> int

Set: BackgroundAgentPk(self: BackgroundAgent)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: BackgroundAgent) -> str

Set: Id(self: BackgroundAgent)=value
"""

 IsActive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsActive(self: BackgroundAgent) -> bool

"""

 IsAuthorized=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsAuthorized(self: BackgroundAgent) -> bool

Set: IsAuthorized(self: BackgroundAgent)=value
"""

 LastSeen=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LastSeen(self: BackgroundAgent) -> DateTime

Set: LastSeen(self: BackgroundAgent)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: BackgroundAgent) -> str

Set: Name(self: BackgroundAgent)=value
"""

 OS=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OS(self: BackgroundAgent) -> str

Set: OS(self: BackgroundAgent)=value
"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Type(self: BackgroundAgent) -> BackgroundAgentType

Set: Type(self: BackgroundAgent)=value
"""



class BackgroundAgents:
 """ BackgroundAgents() """
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

class BackgroundAgentStatus:
 """ BackgroundAgentStatus() """
 ActiveAgents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ActiveAgents(self: BackgroundAgentStatus) -> int

Set: ActiveAgents(self: BackgroundAgentStatus)=value
"""

 InactiveAgents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: InactiveAgents(self: BackgroundAgentStatus) -> int

Set: InactiveAgents(self: BackgroundAgentStatus)=value
"""



class BackgroundAgentType:
 """ enum BackgroundAgentType,values: PrintAgent (1),Unknown (0) """
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
 PrintAgent=None
 Unknown=None
 value__=None


class PingMessage:
 """ PingMessage() """
 AgentType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AgentType(self: PingMessage) -> BackgroundAgentType

Set: AgentType(self: PingMessage)=value
"""

 CreatedAt=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedAt(self: PingMessage) -> DateTime

Set: CreatedAt(self: PingMessage)=value
"""

 ListenerId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ListenerId(self: PingMessage) -> str

Set: ListenerId(self: PingMessage)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: PingMessage) -> str

Set: Name(self: PingMessage)=value
"""

 OS=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OS(self: PingMessage) -> str

Set: OS(self: PingMessage)=value
"""



