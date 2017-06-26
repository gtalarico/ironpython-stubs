class CurveByPoints(CurveElement,IDisposable):
 """ A curve interpolating two or more points. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetPoints(self):
  """
  GetPoints(self: CurveByPoints) -> ReferencePointArray
  
   Get the sequence of points interpolated by this curve.
  """
  pass
 def GetVisibility(self):
  """
  GetVisibility(self: CurveByPoints) -> FamilyElementVisibility
  
   Gets the visibility.
   Returns: A copy of visibility settings for the curve.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetPoints(self,points):
  """
  SetPoints(self: CurveByPoints,points: ReferencePointArray)
   Change the sequence of points interpolated by this curve.
  
   points: An array of 2 or more ReferencePoints.
  """
  pass
 def SetVisibility(self,visibility):
  """
  SetVisibility(self: CurveByPoints,visibility: FamilyElementVisibility)
   Sets the visibility.
  """
  pass
 @staticmethod
 def SortPoints(arr):
  """
  SortPoints(arr: ReferencePointArray) -> bool
  
   Order a set of ReferencePoints in the same way Revit does
  when creating a 
    curve from points.
  
  
   arr: An array of ReferencePoints. The array is reordered
  if sortPoints returns 
    true,and is unchanged if
  sortPoints returns false.
  
   Returns: False if the least-squares method is unable to find a solution;
  true otherwise.
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
 IsReferenceLine=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsReferenceLine(self: CurveByPoints) -> bool

Set: IsReferenceLine(self: CurveByPoints)=value
"""

 ReferenceType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates the type of reference.

Get: ReferenceType(self: CurveByPoints) -> ReferenceType

Set: ReferenceType(self: CurveByPoints)=value
"""

 SketchPlane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Override the SketchPlane property of CurveElement.

Get: SketchPlane(self: CurveByPoints) -> SketchPlane

Set: SketchPlane(self: CurveByPoints)=value
"""

 Subcategory=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The subcategory,or graphics style,of the CurveByPoints.

Get: Subcategory(self: CurveByPoints) -> GraphicsStyle

Set: Subcategory(self: CurveByPoints)=value
"""

 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether the point is visible when the family is loaded
into a project.

Get: Visible(self: CurveByPoints) -> bool

Set: Visible(self: CurveByPoints)=value
"""


