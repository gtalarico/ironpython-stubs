class FillGrid(object,IDisposable):
 """
 Represents a grid line in a fill pattern.
 
 FillGrid(angle: float,spacing: float)
 FillGrid()
 FillGrid(other: FillGrid)
 """
 def CalculateLengthPerArea(self):
  """
  CalculateLengthPerArea(self: FillGrid) -> float
  
   Calculates length of the pattern per unit area.
   Returns: The length per area.
  """
  pass
 def CalculateLinesPerLength(self):
  """
  CalculateLinesPerLength(self: FillGrid) -> float
  
   Calculates the number of solid lines of the pattern per unit length.
   Returns: The solid lines per length.
  """
  pass
 def CalculateStrokesPerArea(self):
  """
  CalculateStrokesPerArea(self: FillGrid) -> float
  
   Calculates the number of the segments of the pattern per unit area.
   Returns: The strokes per area.
  """
  pass
 def Dispose(self):
  """ Dispose(self: FillGrid) """
  pass
 def GetHatchingDirection(self):
  """
  GetHatchingDirection(self: FillGrid) -> UV
  
   Provides the hatching propagation. Hatching is inverted.
   Returns: The direction of hatching.
  """
  pass
 def GetPointLineZone(self,point,nearestPoint=None):
  """
  GetPointLineZone(self: FillGrid,point: UV) -> int
  
   Gets the index of fill grid line closest to the input 2d point.
  
   point: Input point.
   Returns: The index of fill grid line.
  GetPointLineZone(self: FillGrid,point: UV) -> (int,UV)
  
   Gets the index of fill grid line and the point on the grid line nearest to the 
    input point.
  
  
   point: Input point.
   Returns: The index of fill grid line.
  """
  pass
 def GetSegmentDirection(self):
  """
  GetSegmentDirection(self: FillGrid) -> UV
  
   Provides the segment direction.
   Returns: The direction of segment.
  """
  pass
 def GetSegments(self):
  """
  GetSegments(self: FillGrid) -> IList[float]
  
   Gets the segments of the fill grid.
   Returns: The segments.
  """
  pass
 def IsEqual(self,other):
  """
  IsEqual(self: FillGrid,other: FillGrid) -> bool
  
   Check if two fill grids are equal.
  
   other: The fill grid to be compared.
   Returns: True if the two fill grids are equal,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FillGrid,disposing: bool) """
  pass
 def SetSegments(self,segArr):
  """ SetSegments(self: FillGrid,segArr: IList[float]) """
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
 def __new__(self,*__args):
  """
  __new__(cls: type,angle: float,spacing: float)
  __new__(cls: type)
  __new__(cls: type,other: FillGrid)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Angle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets and sets the angle of the fill grid.

Get: Angle(self: FillGrid) -> float

Set: Angle(self: FillGrid)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FillGrid) -> bool

"""

 Offset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets and sets the offset of the fill grid.

Get: Offset(self: FillGrid) -> float

Set: Offset(self: FillGrid)=value
"""

 Origin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets and sets the origin of the fill grid.

Get: Origin(self: FillGrid) -> UV

Set: Origin(self: FillGrid)=value
"""

 Shift=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets and sets the shift of the fill grid.

Get: Shift(self: FillGrid) -> float

Set: Shift(self: FillGrid)=value
"""


