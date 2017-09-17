class BrepLoop(GeometryBase,IDisposable,ISerializable):
 # no doc
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
 def To2dCurve(self):
  """ To2dCurve(self: BrepLoop) -> Curve """
  pass
 def To3dCurve(self):
  """ To3dCurve(self: BrepLoop) -> Curve """
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
 Brep=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Brep(self: BrepLoop) -> Brep

"""

 Face=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Face(self: BrepLoop) -> BrepFace

"""

 LoopIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LoopIndex(self: BrepLoop) -> int

"""

 LoopType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LoopType(self: BrepLoop) -> BrepLoopType

"""

 Trims=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Trims(self: BrepLoop) -> BrepTrimList

"""


