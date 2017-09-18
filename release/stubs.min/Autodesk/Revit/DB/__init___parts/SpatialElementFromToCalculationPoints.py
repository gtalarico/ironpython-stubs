class SpatialElementFromToCalculationPoints(SpatialElementCalculationLocation,IDisposable):
 """
 SpatialElementFromToCalculationPoints is used to specify the search points for a family instance which connects

    two rooms or spaces,such as a door or window. The points determine which room or space is considered the "from"

    and which is considered the "to".
 """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def Flip(self):
  """
  Flip(self: SpatialElementFromToCalculationPoints)

   flip the direction of the "from" and "to" points
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def IsAcceptableFromPosition(self,fromPosition):
  """
  IsAcceptableFromPosition(self: SpatialElementFromToCalculationPoints,fromPosition: XYZ) -> bool

  

   Checks whether a given "from" position is valid.

   Returns: True if the input is an acceptable "from" position and False otherwise.
  """
  pass
 def IsAcceptableToPosition(self,toPosition):
  """
  IsAcceptableToPosition(self: SpatialElementFromToCalculationPoints,toPosition: XYZ) -> bool

  

   Checks whether a given "to" position is valid.

   Returns: True if the input is an acceptable "to" position and False otherwise.
  """
  pass
 def MakeFromPositionAcceptable(self,newFromLocation):
  """
  MakeFromPositionAcceptable(self: SpatialElementFromToCalculationPoints,newFromLocation: XYZ) -> XYZ

  

   This function takes a potential "from" point and converts it to be a similar 

    point on the opposite side of the family's host from

     the "to" point if 

    necessary.

  

  

   newFromLocation: The desired "from" location

   Returns: The valid "from" location.
  """
  pass
 def MakeToPositionAcceptable(self,newToLocation):
  """
  MakeToPositionAcceptable(self: SpatialElementFromToCalculationPoints,newToLocation: XYZ) -> XYZ

  

   This function takes a potential "to" point and converts it to be a similar 

    point on the opposite side of the family's host from

     the "from" point if 

    necessary.

  

  

   newToLocation: The desired "to" location

   Returns: The valid "to" location.
  """
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
 FromPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The "from" position of spatial element connecting calculation point.



Get: FromPosition(self: SpatialElementFromToCalculationPoints) -> XYZ



Set: FromPosition(self: SpatialElementFromToCalculationPoints)=value

"""

 ToPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The "to" position of spatial element connecting calculation point.



Get: ToPosition(self: SpatialElementFromToCalculationPoints) -> XYZ



Set: ToPosition(self: SpatialElementFromToCalculationPoints)=value

"""


