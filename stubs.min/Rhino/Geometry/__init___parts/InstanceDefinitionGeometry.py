class InstanceDefinitionGeometry(GeometryBase,IDisposable,ISerializable):
 """ InstanceDefinitionGeometry() """
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 def Dispose(self):
  """ Dispose(self: CommonObject,disposing: bool) """
  pass
 def GetObjectIds(self):
  """ GetObjectIds(self: InstanceDefinitionGeometry) -> Array[Guid] """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: CommonObject) """
  pass
 def OnSwitchToNonConst(self,*args):
  """ OnSwitchToNonConst(self: GeometryBase) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Description(self: InstanceDefinitionGeometry) -> str

Set: Description(self: InstanceDefinitionGeometry)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: InstanceDefinitionGeometry) -> Guid

Set: Id(self: InstanceDefinitionGeometry)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: InstanceDefinitionGeometry) -> str

Set: Name(self: InstanceDefinitionGeometry)=value
"""


