class SpatialElementGeometryCalculator(object,IDisposable):
 """
 Use this class to calculate the geometry of a spatial element and obtain the relationships between the geometry and

    the element's boundary elements.

 

 SpatialElementGeometryCalculator(aDoc: Document,options: SpatialElementBoundaryOptions)

 SpatialElementGeometryCalculator(aDoc: Document)
 """
 def CalculateSpatialElementGeometry(self,spatialElement):
  """
  CalculateSpatialElementGeometry(self: SpatialElementGeometryCalculator,spatialElement: SpatialElement) -> SpatialElementGeometryResults

  

   Compute the spatial element geometry and returns the boundary face information.

  

   spatialElement: Specifies the spatial element needs to be computed,should be Room or Space.

   Returns: Requested boundary face information.
  """
  pass
 @staticmethod
 def CanCalculateGeometry(spatialElement):
  """
  CanCalculateGeometry(spatialElement: SpatialElement) -> bool

  

   This indicates whether the input spatial element is a valid one.

  

   spatialElement: The spatial element to be checked if its geometry can be calculated.

   Returns: It will return false if the room/space is not enclosed in 2d or has no 

    location,or the height is too small.
  """
  pass
 def Dispose(self):
  """ Dispose(self: SpatialElementGeometryCalculator) """
  pass
 def GetOptions(self):
  """
  GetOptions(self: SpatialElementGeometryCalculator) -> SpatialElementBoundaryOptions

  

   The options that control the calculation.

   Returns: The options.
  """
  pass
 @staticmethod
 def IsRoomOrSpace(spatialElement):
  """
  IsRoomOrSpace(spatialElement: SpatialElement) -> bool

  

   This indicates whether the input spatial element is a room or a space.

  

   spatialElement: The spatial element to be checked if it is a room or a space or not.

   Returns: True if the input spatial element is a room or a space,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: SpatialElementGeometryCalculator,disposing: bool) """
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
 def __new__(self,aDoc,options=None):
  """
  __new__(cls: type,aDoc: Document,options: SpatialElementBoundaryOptions)

  __new__(cls: type,aDoc: Document)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: SpatialElementGeometryCalculator) -> bool



"""


