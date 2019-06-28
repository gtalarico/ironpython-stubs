# encoding: utf-8
# module Wms.RemotingObjects.Connection calls itself Connection
# from Wms.RemotingObjects,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ConnectionEntries:
 """ ConnectionEntries() """
 def AddUnique(self,entry):
  """ AddUnique(self: ConnectionEntries,entry: ConnectionEntry) """
  pass
 def AddUniqueRange(self,entries):
  """ AddUniqueRange(self: ConnectionEntries,entries: IEnumerable[ConnectionEntry]) """
  pass
 def LoadFromRegistry(self):
  """ LoadFromRegistry(self: ConnectionEntries) """
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
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass

class ConnectionEntry:
 """
 ConnectionEntry(host: str,port: int,name: str,description: str,pinned: bool)
 ConnectionEntry(host: str,port: int,name: str,description: str,pinned: bool,lastLoggedInUser: int)
 """
 def UpdateRegistry(self):
  """ UpdateRegistry(self: ConnectionEntry) """
  pass
 @staticmethod
 def __new__(self,host,port,name,description,pinned,lastLoggedInUser=None):
  """
  __new__(cls: type,host: str,port: int,name: str,description: str,pinned: bool)
  __new__(cls: type,host: str,port: int,name: str,description: str,pinned: bool,lastLoggedInUser: int)
  """
  pass
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Description(self: ConnectionEntry) -> str

Set: Description(self: ConnectionEntry)=value
"""

 FullHostAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FullHostAddress(self: ConnectionEntry) -> str

"""

 Host=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Host(self: ConnectionEntry) -> str

Set: Host(self: ConnectionEntry)=value
"""

 LastLoggedInUser=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LastLoggedInUser(self: ConnectionEntry) -> int

Set: LastLoggedInUser(self: ConnectionEntry)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: ConnectionEntry) -> str

Set: Name(self: ConnectionEntry)=value
"""

 Pinned=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Pinned(self: ConnectionEntry) -> bool

Set: Pinned(self: ConnectionEntry)=value
"""

 Port=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Port(self: ConnectionEntry) -> int

Set: Port(self: ConnectionEntry)=value
"""



