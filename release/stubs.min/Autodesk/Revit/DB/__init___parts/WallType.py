class WallType(HostObjAttributes,IDisposable):
 """ Represents a specific type of wall,such as 'Generic -8" '. """
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
 Function=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The wall function.



Get: Function(self: WallType) -> WallFunction



Set: Function(self: WallType)=value

"""

 Kind=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The nature of the wall.



Get: Kind(self: WallType) -> WallKind



"""

 ThermalProperties=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The calculated and settable thermal properties of the WallType



Get: ThermalProperties(self: WallType) -> ThermalProperties



"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The overall thickness of this type of wall.



Get: Width(self: WallType) -> float



"""


