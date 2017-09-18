class Revolution(GenericForm,IDisposable):
 """ A revolution solid or void form. """
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
 Axis=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the Axis of the Revolution.



Get: Axis(self: Revolution) -> ModelLine



"""

 EndAngle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The end angle of the revolution relative to the sketch plane.



Get: EndAngle(self: Revolution) -> float



Set: EndAngle(self: Revolution)=value

"""

 Sketch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the Sketch of the Revolution.



Get: Sketch(self: Revolution) -> Sketch



"""

 StartAngle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The start angle of the revolution relative to the sketch plane.



Get: StartAngle(self: Revolution) -> float



Set: StartAngle(self: Revolution)=value

"""


