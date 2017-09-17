class Dimension(Element,IDisposable):
 """ An object that represents a dimension within the Revit project. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def IsTextPositionAdjustable(self):
  """
  IsTextPositionAdjustable(self: Dimension) -> bool
  
   Indicates if this dimension is supported to set/get TextPosition/LeaderPosition.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def ResetTextPosition(self):
  """
  ResetTextPosition(self: Dimension)
   Resets the text position of the dimension to the initial position determined by 
    its type and parameters.
  """
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
 Above=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The text shown above the segment's value.

Get: Above(self: Dimension) -> str

Set: Above(self: Dimension)=value
"""

 AreSegmentsEqual=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if all segments are forced to be equal.

Get: AreSegmentsEqual(self: Dimension) -> bool

Set: AreSegmentsEqual(self: Dimension)=value
"""

 Below=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The text shown below the segment's value.

Get: Below(self: Dimension) -> str

Set: Below(self: Dimension)=value
"""

 Curve=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A curve that represents the dimension line.

Get: Curve(self: Dimension) -> Curve

"""

 DimensionShape=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The shape of this dimension.

Get: DimensionShape(self: Dimension) -> DimensionShape

"""

 DimensionType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The dimension style of this dimension.

Get: DimensionType(self: Dimension) -> DimensionType

Set: DimensionType(self: Dimension)=value
"""

 FamilyLabel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The family parameter label of the dimension.

Get: FamilyLabel(self: Dimension) -> FamilyParameter

Set: FamilyLabel(self: Dimension)=value
"""

 IsLocked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if this dimension is locked.

Get: IsLocked(self: Dimension) -> bool

Set: IsLocked(self: Dimension)=value
"""

 LeaderEndPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The position of the dimension's leader end point.

Get: LeaderEndPosition(self: Dimension) -> XYZ

Set: LeaderEndPosition(self: Dimension)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves or changes the name associated with the Dimension.

Get: Name(self: Dimension) -> str

Set: Name(self: Dimension)=value
"""

 NumberOfSegments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of segments for the dimension.

Get: NumberOfSegments(self: Dimension) -> int

"""

 Origin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The dimension origin.

Get: Origin(self: Dimension) -> XYZ

"""

 Prefix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The text shown before the segment's value.

Get: Prefix(self: Dimension) -> str

Set: Prefix(self: Dimension)=value
"""

 References=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns an array of geometric references to which the dimension is attached.

Get: References(self: Dimension) -> ReferenceArray

"""

 Segments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The segments in the dimension.

Get: Segments(self: Dimension) -> DimensionSegmentArray

"""

 Suffix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The text shown after the segment's value.

Get: Suffix(self: Dimension) -> str

Set: Suffix(self: Dimension)=value
"""

 TextPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The position of the dimension text's drag point.

Get: TextPosition(self: Dimension) -> XYZ

Set: TextPosition(self: Dimension)=value
"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The value of the dimension.

Get: Value(self: Dimension) -> Nullable[float]

"""

 ValueOverride=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The text that replaces the segment's value.

Get: ValueOverride(self: Dimension) -> str

Set: ValueOverride(self: Dimension)=value
"""

 ValueString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The dimension value as a user visible string.

Get: ValueString(self: Dimension) -> str

"""

 View=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Supplies the view that contains the dimension if the dimension is view specific.

Get: View(self: Dimension) -> View

"""


