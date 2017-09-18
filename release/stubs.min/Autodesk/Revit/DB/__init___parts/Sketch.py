class Sketch(SketchBase,IDisposable):
 """ Provides access to the Sketch in Autodesk Revit. """
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
 Profile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the Profile of the Sketch.



Get: Profile(self: Sketch) -> CurveArrArray



"""

 SketchPlane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the Sketch Plane of the Sketch.



Get: SketchPlane(self: Sketch) -> SketchPlane



"""


