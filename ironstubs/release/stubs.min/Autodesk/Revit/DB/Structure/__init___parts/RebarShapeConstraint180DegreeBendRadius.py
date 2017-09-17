class RebarShapeConstraint180DegreeBendRadius(RebarShapeConstraint,IDisposable):
 """
 A constraint which can be applied to a RebarShapeSegment,and causes the segment
    to be replaced with a 180-degree arc. The associated parameter drives
    the radius of the arc.
 
 RebarShapeConstraint180DegreeBendRadius(paramId: ElementId,refType: RebarShapeArcReferenceType)
 """
 def Dispose(self):
  """ Dispose(self: RebarShapeConstraint,A_0: bool) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RebarShapeConstraint,disposing: bool) """
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
 def __new__(self,paramId,refType):
  """ __new__(cls: type,paramId: ElementId,refType: RebarShapeArcReferenceType) """
  pass
 ArcReferenceType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A choice of rule for measuring the radius.

Get: ArcReferenceType(self: RebarShapeConstraint180DegreeBendRadius) -> RebarShapeArcReferenceType

"""


