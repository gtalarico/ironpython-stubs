class Sweep(GenericForm,IDisposable):
 """ A sweep solid or void form. """
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
 IsTrajectorySegmentationEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The trajectory segmentation option for the sweep.

Get: IsTrajectorySegmentationEnabled(self: Sweep) -> bool

Set: IsTrajectorySegmentationEnabled(self: Sweep)=value
"""

 MaxSegmentAngle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The maximum segment angle of the sweep in radians.

Get: MaxSegmentAngle(self: Sweep) -> float

Set: MaxSegmentAngle(self: Sweep)=value
"""

 Path3d=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The selected curves used for the sweep path.

Get: Path3d(self: Sweep) -> Path3d

"""

 PathSketch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The sketched path for the sweep.

Get: PathSketch(self: Sweep) -> Sketch

"""

 ProfileSketch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The profile sketch of the sweep.

Get: ProfileSketch(self: Sweep) -> Sketch

"""

 ProfileSymbol=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The family symbol profile details for the sweep.

Get: ProfileSymbol(self: Sweep) -> FamilySymbolProfile

"""


