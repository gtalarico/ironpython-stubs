class Level(DatumPlane,IDisposable):
 """ Represents a Level line within Autodesk Revit. """
 @staticmethod
 def Create(document,elevation):
  """
  Create(document: Document,elevation: float) -> Level

  

   Creates a new instance of level based on an input elevation.

  

   document: The document in which the new instance is created

   elevation: The elevation of the level to be created.

   Returns: The newly created level instance.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetPlaneReference(self):
  """
  GetPlaneReference(self: Level) -> Reference

  

   Returns a reference to this element as a plane.
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
 Elevation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves or changes the elevation above or below the ground level.



Get: Elevation(self: Level) -> float



Set: Elevation(self: Level)=value

"""

 ProjectElevation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves the elevation relative to project origin,no matter

   what values of the Elevation Base parameter is set.



Get: ProjectElevation(self: Level) -> float



"""


