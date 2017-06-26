class RebarShapeSegment(object,IDisposable):
 """
 Part of a RebarShapeDefinitionBySegments,representing one segment
    of a shape definition.
 """
 def Dispose(self):
  """ Dispose(self: RebarShapeSegment) """
  pass
 def GetConstraints(self):
  """
  GetConstraints(self: RebarShapeSegment) -> IList[RebarShapeConstraint]
  
   Retrieve the list of constraints associated with this segment.
   Returns: The list of constraints.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RebarShapeSegment,disposing: bool) """
  pass
 def SetConstraints(self,constraints):
  """ SetConstraints(self: RebarShapeSegment,constraints: IList[RebarShapeConstraint]) """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarShapeSegment) -> bool

"""


