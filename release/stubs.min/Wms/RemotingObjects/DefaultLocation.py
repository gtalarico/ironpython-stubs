# encoding: utf-8
# module Wms.RemotingObjects.DefaultLocation calls itself DefaultLocation
# from Wms.RemotingObjects,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ChangeDefaultLocation:
 """ enum ChangeDefaultLocation,values: Always (0),Ask (2),Never (1) """
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
 Always=None
 Ask=None
 Never=None
 value__=None


class UpdateItemDefaultLocationArgs:
 """ UpdateItemDefaultLocationArgs() """
 IsDirectTransfer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDirectTransfer(self: UpdateItemDefaultLocationArgs) -> bool

Set: IsDirectTransfer(self: UpdateItemDefaultLocationArgs)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemCode(self: UpdateItemDefaultLocationArgs) -> str

Set: ItemCode(self: UpdateItemDefaultLocationArgs)=value
"""

 NewLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NewLocation(self: UpdateItemDefaultLocationArgs) -> str

Set: NewLocation(self: UpdateItemDefaultLocationArgs)=value
"""

 OldLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OldLocation(self: UpdateItemDefaultLocationArgs) -> str

Set: OldLocation(self: UpdateItemDefaultLocationArgs)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseCode(self: UpdateItemDefaultLocationArgs) -> str

Set: WarehouseCode(self: UpdateItemDefaultLocationArgs)=value
"""



class WarehouseItemLocation:
 """
 WarehouseItemLocation()
 WarehouseItemLocation(warehouseCode: str,warehouseDescription: str,warehouseLocationCode: str)
 """
 @staticmethod
 def __new__(self,warehouseCode=None,warehouseDescription=None,warehouseLocationCode=None):
  """
  __new__(cls: type)
  __new__(cls: type,warehouseCode: str,warehouseDescription: str,warehouseLocationCode: str)
  """
  pass
 LocationCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LocationCode(self: WarehouseItemLocation) -> str

Set: LocationCode(self: WarehouseItemLocation)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseCode(self: WarehouseItemLocation) -> str

Set: WarehouseCode(self: WarehouseItemLocation)=value
"""

 WarehouseDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseDescription(self: WarehouseItemLocation) -> str

Set: WarehouseDescription(self: WarehouseItemLocation)=value
"""



