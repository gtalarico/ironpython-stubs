class CableTrayConduitBase(MEPCurve,IDisposable):
 """ The CableTrayConduitBase class is implemented as the base class for cable tray or conduit """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def IsValidEndPoints(startPoint,endPoint):
  """
  IsValidEndPoints(startPoint: XYZ,endPoint: XYZ) -> bool
  
   Identifies if two end points are valid.
  
   startPoint: The start point of the location line.
   endPoint: The end point of the location line.
   Returns: True if the two end points are valid,false otherwise.
  """
  pass
 @staticmethod
 def IsValidLevelId(document,levelId):
  """
  IsValidLevelId(document: Document,levelId: ElementId) -> bool
  
   Identifies if a level id is valid.
  
   document: The document.
   levelId: The level id.
   Returns: True if the level id is valid,false otherwise.
  """
  pass
 def IsWithFitting(self):
  """
  IsWithFitting(self: CableTrayConduitBase) -> bool
  
   Return whether its cable tray/conduit type is with fitting
   Returns: return true if its type is with fitting type.
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
 RunId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the run to which this element belongs.

Get: RunId(self: CableTrayConduitBase) -> ElementId

"""


