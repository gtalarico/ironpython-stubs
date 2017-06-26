class MEPCurve(HostObject,IDisposable):
 """ A curve object for duct or pipe blend elements. """
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
 ConnectorManager=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The connector manager of this MEP curve.

Get: ConnectorManager(self: MEPCurve) -> ConnectorManager

"""

 Diameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The diameter of the MEP curve.

Get: Diameter(self: MEPCurve) -> float

"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The height of the MEP curve.

Get: Height(self: MEPCurve) -> float

"""

 LevelOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The offset of the MEP curve.

Get: LevelOffset(self: MEPCurve) -> float

Set: LevelOffset(self: MEPCurve)=value
"""

 MEPSystem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The system of the MEP curve.

Get: MEPSystem(self: MEPCurve) -> MEPSystem

"""

 ReferenceLevel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The reference level of the MEP curve.

Get: ReferenceLevel(self: MEPCurve) -> Level

Set: ReferenceLevel(self: MEPCurve)=value
"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The width of the MEP curve.

Get: Width(self: MEPCurve) -> float

"""


