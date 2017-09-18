class RepeaterBounds(object,IDisposable):
 """
 Represents bounds of the array of repeating references in 0,1,or 2 dimensions.

    (See Autodesk.Revit.DB.RepeatingReferenceSource).
 """
 def AdjustForCyclicalBounds(self,coordinates):
  """
  AdjustForCyclicalBounds(self: RepeaterBounds,coordinates: RepeaterCoordinates) -> RepeaterCoordinates

  

   Shifts the input coordinates in the cyclical dimensions so that they fall in 

    the [lower bounds,upper bounds] range.

  

  

   coordinates: The coordinates.

   Returns: The adjusted coordinates.
  """
  pass
 def AreCoordinatesInBounds(self,coordinates,treatCyclicalBoundsAsInfinite):
  """
  AreCoordinatesInBounds(self: RepeaterBounds,coordinates: RepeaterCoordinates,treatCyclicalBoundsAsInfinite: bool) -> bool

  

   Determines whether given coordinates are within the bounds.

  

   coordinates: The coordinates.

   treatCyclicalBoundsAsInfinite: True if cyclical directions should be treated as unbounded.

   Returns: True if the coordinates are within the bounds.
  """
  pass
 def Dispose(self):
  """ Dispose(self: RepeaterBounds) """
  pass
 def GetLowerBound(self,dimension):
  """
  GetLowerBound(self: RepeaterBounds,dimension: int) -> int

  

   Returns the smallest index of the array in the given dimension.

  

   dimension: The dimension.

   Returns: The smallest index of the array in the given dimension.
  """
  pass
 def GetUpperBound(self,dimension):
  """
  GetUpperBound(self: RepeaterBounds,dimension: int) -> int

  

   Returns the highest index of the array in the given dimension.

  

   dimension: The dimension.

   Returns: The highest index of the array in the given dimension.
  """
  pass
 def IsCyclical(self,dimension):
  """
  IsCyclical(self: RepeaterBounds,dimension: int) -> bool

  

   True if the array doesn't have finite bounds in the given dimension. Cyclical 

    bounds indicate that the array forms a closed loop in the given dimension.

  

  

   dimension: The dimension.

   Returns: True if the bounds are cyclical in the given dimension.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RepeaterBounds,disposing: bool) """
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
 DimensionCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of dimensions of the bounds (0,1 or 2 for zero,one or two dimensional arrays.)



Get: DimensionCount(self: RepeaterBounds) -> int



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: RepeaterBounds) -> bool



"""


