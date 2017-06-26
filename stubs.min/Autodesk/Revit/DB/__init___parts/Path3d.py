class Path3d(SketchBase,IDisposable):
 """ Provides access to the Generic 3D path object in Autodesk Revit. """
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
 AllCurveLoops=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get all the Curve Loops of Path3d.

Get: AllCurveLoops(self: Path3d) -> CurveArrArray

"""

 NumCurveLoops=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the Number of Curve Loops of Path3d.

Get: NumCurveLoops(self: Path3d) -> int

"""


