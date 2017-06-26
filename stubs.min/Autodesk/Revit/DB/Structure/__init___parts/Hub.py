class Hub(Element,IDisposable):
 """ Represents a connection between two or more Autodesk Revit Elements. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetHubConnectorManager(self):
  """
  GetHubConnectorManager(self: Hub) -> ConnectorManager
  
   Retrieves the ConnectorManager of the Hub.
   Returns: The ConnectorManager.
  """
  pass
 def GetOrigin(self):
  """
  GetOrigin(self: Hub) -> XYZ
  
   Retrieves position of a Hub if such position is a 3D point.
   Returns: The origin.
  """
  pass
 def HasOrigin(self):
  """
  HasOrigin(self: Hub) -> bool
  
   Provides information if Hub has a specific location at point in 3D space.
   Returns: True if the Hub has a specific location at point in 3D space.
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
