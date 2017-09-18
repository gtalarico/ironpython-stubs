class RebarShapeConstraintSegmentLength(RebarShapeConstraint,IDisposable):
 """
 A constraint that controls the length of a segment.
 
 RebarShapeConstraintSegmentLength(paramId: ElementId,refType0: RebarShapeSegmentEndReferenceType,refType1: RebarShapeSegmentEndReferenceType)
 """
 def Dispose(self):
  """ Dispose(self: RebarShapeConstraint,A_0: bool) """
  pass
 def GetSegmentEndReferenceType(self,index):
  """
  GetSegmentEndReferenceType(self: RebarShapeConstraintSegmentLength,index: int) -> RebarShapeSegmentEndReferenceType
  
   Choice of two possibilities for the start and end references of the length 
    constraint.
  
  
   index: Which reference on the constraint. Either 0 or 1.
  """
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
 def __new__(self,paramId,refType0,refType1):
  """ __new__(cls: type,paramId: ElementId,refType0: RebarShapeSegmentEndReferenceType,refType1: RebarShapeSegmentEndReferenceType) """
  pass
