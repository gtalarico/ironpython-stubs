# encoding: utf-8
# module Wms.RemotingObjects.ErpLocking calls itself ErpLocking
# from Wms.RemotingObjects,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ErpLock:
 """ ErpLock() """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 CurrentState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CurrentState(self: ErpLock) -> ErpLockState

Set: CurrentState(self: ErpLock)=value
"""

 CurrentStateAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CurrentStateAsString(self: ErpLock) -> str

"""

 EntityKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EntityKey(self: ErpLock) -> str

Set: EntityKey(self: ErpLock)=value
"""

 EntityType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EntityType(self: ErpLock) -> ErpLockEntityType

Set: EntityType(self: ErpLock)=value
"""

 EntityTypeAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EntityTypeAsString(self: ErpLock) -> str

"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: ErpLock) -> int

Set: Id(self: ErpLock)=value
"""

 MigrateToState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MigrateToState(self: ErpLock) -> ErpLockState

Set: MigrateToState(self: ErpLock)=value
"""

 MigrateToStateAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MigrateToStateAsString(self: ErpLock) -> str

"""



class ErpLockEntityType:
 """ enum ErpLockEntityType,values: PurchaseOrder (1),SalesOrder (0) """
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
 PurchaseOrder=None
 SalesOrder=None
 value__=None


class ErpLockState:
 """ enum ErpLockState,values: Locked (1),Unkown (0),Unlocked (2) """
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
 Locked=None
 Unkown=None
 Unlocked=None
 value__=None


