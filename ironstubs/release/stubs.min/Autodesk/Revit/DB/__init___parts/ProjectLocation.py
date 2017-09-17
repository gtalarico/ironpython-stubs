class ProjectLocation(Instance,IDisposable):
 """ An object that represents a named location in a project. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def Duplicate(self,name):
  """
  Duplicate(self: ProjectLocation,name: str) -> ProjectLocation
  
   Generate a copy of this project location with the specified name.
  
   name: The name to be assigned to the duplicated project location.
   Returns: If successful a duplicate of this project location object with the specified 
    name.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
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
 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the project location.

Get: Name(self: ProjectLocation) -> str

Set: Name(self: ProjectLocation)=value
"""

 SiteLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The site location to which this project location refers.

Get: SiteLocation(self: ProjectLocation) -> SiteLocation

"""


