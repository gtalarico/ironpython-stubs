class RebarShapeConstraintAngleFromFixedDir(RebarShapeConstraint,IDisposable):
 """
 A constraint which can be applied to a RebarShapeSegment and drives the angle

    of the segment relative to a fixed direction in UV-space.

 

 RebarShapeConstraintAngleFromFixedDir(paramId: ElementId,sign: int,direction: UV)
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
 def __new__(self,paramId,sign,direction):
  """ __new__(cls: type,paramId: ElementId,sign: int,direction: UV) """
  pass
 Direction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A fixed direction in UV-space. The parameter will drive

   the segment's angle relative to this direction.



Get: Direction(self: RebarShapeConstraintAngleFromFixedDir) -> UV



Set: Direction(self: RebarShapeConstraintAngleFromFixedDir)=value

"""

 Sign=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When the sign is 1,the Direction is rotated clockwise by the angle's value.

   When -1,the Direction is rotated counter-clockwise.



Get: Sign(self: RebarShapeConstraintAngleFromFixedDir) -> int



Set: Sign(self: RebarShapeConstraintAngleFromFixedDir)=value

"""


