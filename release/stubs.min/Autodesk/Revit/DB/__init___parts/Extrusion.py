class Extrusion(GenericForm,IDisposable):
 """ A extrusion solid or void form. """
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
 EndOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The offset of the end of the extrusion relative to the sketch plane.



Get: EndOffset(self: Extrusion) -> float



Set: EndOffset(self: Extrusion)=value

"""

 Sketch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the Sketch of the Extrusion.



Get: Sketch(self: Extrusion) -> Sketch



"""

 StartOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The offset of the start of the extrusion relative to the sketch plane.



Get: StartOffset(self: Extrusion) -> float



Set: StartOffset(self: Extrusion)=value

"""


