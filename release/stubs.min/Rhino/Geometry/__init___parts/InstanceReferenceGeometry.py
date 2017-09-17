class InstanceReferenceGeometry(GeometryBase,IDisposable,ISerializable):
 """ InstanceReferenceGeometry(instanceDefinitionId: Guid,transform: Transform) """
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 def Dispose(self):
  """ Dispose(self: CommonObject,disposing: bool) """
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
 @staticmethod
 def __new__(self,instanceDefinitionId,transform):
  """ __new__(cls: type,instanceDefinitionId: Guid,transform: Transform) """
  pass
 ParentIdefId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ParentIdefId(self: InstanceReferenceGeometry) -> Guid

"""

 Xform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Xform(self: InstanceReferenceGeometry) -> Transform

"""


