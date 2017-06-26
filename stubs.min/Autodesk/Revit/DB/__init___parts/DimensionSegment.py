class DimensionSegment(APIObject,IDisposable):
 """ A segment of a dimension within the Autodesk Revit project. """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def IsTextPositionAdjustable(self):
  """
  IsTextPositionAdjustable(self: DimensionSegment) -> bool
  
   Indicates if this dimension is supported to set/get TextPosition/LeaderPosition.
   Returns: True if this dimension is supported to set/get TextPosition/LeaderPosition,
    false otherwise.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
  pass
 def ResetTextPosition(self):
  """
  ResetTextPosition(self: DimensionSegment)
   Resets the text position of the segment to the initial position determined by 
    its type and parameters.
  """
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
 Above=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The text shown above the segment's value.

Get: Above(self: DimensionSegment) -> str

Set: Above(self: DimensionSegment)=value
"""

 Below=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The text shown below the segment's value.

Get: Below(self: DimensionSegment) -> str

Set: Below(self: DimensionSegment)=value
"""

 IsLocked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if this segment is locked.

Get: IsLocked(self: DimensionSegment) -> bool

Set: IsLocked(self: DimensionSegment)=value
"""

 LeaderEndPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The position of the dimension leader end point.

Get: LeaderEndPosition(self: DimensionSegment) -> XYZ

Set: LeaderEndPosition(self: DimensionSegment)=value
"""

 Origin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The segment origin.

Get: Origin(self: DimensionSegment) -> XYZ

"""

 Prefix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The text shown before the segment's value.

Get: Prefix(self: DimensionSegment) -> str

Set: Prefix(self: DimensionSegment)=value
"""

 Suffix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The text shown after the segment's value.

Get: Suffix(self: DimensionSegment) -> str

Set: Suffix(self: DimensionSegment)=value
"""

 TextPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The position of the dimension text's drag point.

Get: TextPosition(self: DimensionSegment) -> XYZ

Set: TextPosition(self: DimensionSegment)=value
"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The length of the segment.

Get: Value(self: DimensionSegment) -> Nullable[float]

"""

 ValueOverride=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The text that replaces the segment's value.

Get: ValueOverride(self: DimensionSegment) -> str

Set: ValueOverride(self: DimensionSegment)=value
"""

 ValueString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The displayed value shown for the dimension segment.

Get: ValueString(self: DimensionSegment) -> str

"""


