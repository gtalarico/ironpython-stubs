class LoadBase(Element,IDisposable):
 """ The LoadBase object is the base class for all load objects within the Autodesk Revit API. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def IsOrientToPermitted(self,orientTo):
  """
  IsOrientToPermitted(self: LoadBase,orientTo: LoadOrientTo) -> bool
  
   Indicates if the provided orientation is permitted for this load.
  
   orientTo: Load orientation to check.
   Returns: True if provided orientation type is permitted for this load,false if not.
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
 HostElement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The host element for the load.

Get: HostElement(self: LoadBase) -> AnalyticalModel

"""

 HostElementId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The host element ID for the load.

Get: HostElementId(self: LoadBase) -> ElementId

"""

 IsHosted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the Load is hosted or non-hosted.

Get: IsHosted(self: LoadBase) -> bool

"""

 IsReaction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The load is reaction option.

Get: IsReaction(self: LoadBase) -> bool

Set: IsReaction(self: LoadBase)=value
"""

 LoadCase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The load case for the load.

Get: LoadCase(self: LoadBase) -> LoadCase

"""

 LoadCaseId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The load case ID for the load.

Get: LoadCaseId(self: LoadBase) -> ElementId

Set: LoadCaseId(self: LoadBase)=value
"""

 LoadCaseName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the load case to which this load belongs.

Get: LoadCaseName(self: LoadBase) -> str

"""

 LoadCategoryName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the category to which this load belongs.

Get: LoadCategoryName(self: LoadBase) -> str

"""

 LoadNatureName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A string representing the nature of the load.

Get: LoadNatureName(self: LoadBase) -> str

"""

 OrientTo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The load orientation option.

Get: OrientTo(self: LoadBase) -> LoadOrientTo

Set: OrientTo(self: LoadBase)=value
"""

 WorkPlaneId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Id of the work plane which may determine the orientation of the load.

Get: WorkPlaneId(self: LoadBase) -> ElementId

"""


