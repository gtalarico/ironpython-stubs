class EnergyAnalysisSpace(Element,IDisposable):
 """ Analytical space. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def GetAnalyticalSurfaces(self):
  """
  GetAnalyticalSurfaces(self: EnergyAnalysisSpace) -> IList[EnergyAnalysisSurface]
  
   Provides a way to access the collection of
     analytical surfaces for a space.
    
     Geometry data defining an analytical space volume.
     Through an 
    analytical surface you can connect a
     source element with each polygon in a 
    space.
     The analytical surfaces defines an enclosed volume
     bounded by 
    the center plane of walls
     and the top plane of roofs and floors.
  
   Returns: the collection of analytical surfaces for a space.
  """
  pass
 def GetBoundary(self):
  """
  GetBoundary(self: EnergyAnalysisSpace) -> IList[Polyloop]
  
   Gets the collection of polygons that form the 2D boundary.
     This method 
    returns a collection of polyloops (planar
     polygons) that defines an 
    enclosed area measured by
     interior bounding surfaces.
  
   Returns: The collection of polygons that form the 2D boundary.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetClosedShell(self):
  """
  GetClosedShell(self: EnergyAnalysisSpace) -> IList[Polyloop]
  
   Gets the collection of polygons that form a closed shell.
     This method 
    returns a collection of polyloops (planar
     polygons) that defines an 
    enclosed volume measured by
     interior bounding surfaces.
  
   Returns: the collection of polygons that form a closed shell.
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
 AnalyticalVolume=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The volume for this space.

Get: AnalyticalVolume(self: EnergyAnalysisSpace) -> float

"""

 Area=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The area for this space.

Get: Area(self: EnergyAnalysisSpace) -> float

"""

 CADObjectUniqueId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The unique id of the originating CAD object (model element) associated with this space.

Get: CADObjectUniqueId(self: EnergyAnalysisSpace) -> str

"""

 ComposedName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The composed name for this space.

Get: ComposedName(self: EnergyAnalysisSpace) -> str

"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The description.

Get: Description(self: EnergyAnalysisSpace) -> str

"""

 InnerVolume=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The analytical volume for this space.

Get: InnerVolume(self: EnergyAnalysisSpace) -> float

"""

 SpaceName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name.

Get: SpaceName(self: EnergyAnalysisSpace) -> str

"""


