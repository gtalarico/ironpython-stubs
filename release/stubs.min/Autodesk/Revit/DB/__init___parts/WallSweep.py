class WallSweep(HostObject,IDisposable):
 """ Represents a wall sweep or reveal. """
 @staticmethod
 def Create(wall,wallSweepType,wallSweepInfo):
  """
  Create(wall: Wall,wallSweepType: ElementId,wallSweepInfo: WallSweepInfo) -> WallSweep

  

   Creates a new wall sweep or reveal.

  

   wall: The wall upon which to create the new sweep or reveal.

   wallSweepType: The wall sweep or reveal type.

   wallSweepInfo: The information that describes the new wall sweep or reveal.

   Returns: The new wall sweep.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetHostIds(self):
  """
  GetHostIds(self: WallSweep) -> IList[ElementId]

  

   Gets a list of all host walls on which the sweep resides.

   Returns: The list of wall ids.
  """
  pass
 def GetWallSweepInfo(self):
  """
  GetWallSweepInfo(self: WallSweep) -> WallSweepInfo

  

   Gets the information of the wall sweep or reveal.

   Returns: The information that describes the wall sweep or reveal.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 @staticmethod
 def WallAllowsWallSweep(wall):
  """
  WallAllowsWallSweep(wall: Wall) -> bool

  

   Validates that the wall is of a type that may be a host for a wall sweep or 

    reveal.

  

  

   wall: The wall.

   Returns: True if the wall may host a wall sweep,false otherwise.
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
