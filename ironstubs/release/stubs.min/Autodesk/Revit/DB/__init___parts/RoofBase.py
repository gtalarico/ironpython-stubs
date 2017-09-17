class RoofBase(HostObject,IDisposable):
 """ Represents all kinds of Roofs. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
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
 EaveCuts=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieve or set the EaveCutterType.

Get: EaveCuts(self: RoofBase) -> EaveCutterType

Set: EaveCuts(self: RoofBase)=value
"""

 FasciaDepth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieve or set the FasciaDepth.

Get: FasciaDepth(self: RoofBase) -> float

Set: FasciaDepth(self: RoofBase)=value
"""

 RoofType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieve or set the Type.

Get: RoofType(self: RoofBase) -> RoofType

Set: RoofType(self: RoofBase)=value
"""

 SlabShapeEditor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the SlabShapeEditor used for slab shape editing.

Get: SlabShapeEditor(self: RoofBase) -> SlabShapeEditor

"""


