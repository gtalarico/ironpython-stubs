class PointCloudInstance(Instance,IDisposable):
 """ Represents a single instance of a point cloud in the Revit document. """
 def ContainsScan(self,scanName):
  """
  ContainsScan(self: PointCloudInstance,scanName: str) -> bool
  
   Identifies whether the instance contains a scan.
  
   scanName: Name of the scan.
  """
  pass
 @staticmethod
 def Create(document,typeId,transform):
  """
  Create(document: Document,typeId: ElementId,transform: Transform) -> PointCloudInstance
  
   Creates a new instance of a point cloud based on an input point cloud type and 
    transformation.
  
  
   document: The document in which the new instance is created
   typeId: The element id of the PointCloudType.
   transform: The transform that defines the placement of the instance in the Revit document 
    coordinate system.
  
   Returns: The newly created point cloud instance.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetPoints(self,filter,averageDistance,numPoints):
  """
  GetPoints(self: PointCloudInstance,filter: PointCloudFilter,averageDistance: float,numPoints: int) -> PointCollection
  
   Extracts a collection of points based on a filter.
  
   filter: The filter to control which points are extracted. The filter should be passed 
    in the coordinates
     of the Revit model.
  
   averageDistance: Desired average distance between "adjacent" cloud points (Revit units of 
    length).
     The smaller the averageDistance the larger number of points will 
    be returned up to the numPoints limit.
     Specifying this parameter makes 
    actual number of points returned for a given filter independent of the
     
    density of coverage produced by the scanner.
  
   numPoints: The maximum number of points requested.
   Returns: A collection object containing points that pass the filter,but no more than 
    the maximum number requested.
  """
  pass
 def GetRegions(self):
  """
  GetRegions(self: PointCloudInstance) -> IList[str]
  
   Returns array of region names.
   Returns: Resulting array of region names.
  """
  pass
 def GetScanOrigin(self,scanName):
  """
  GetScanOrigin(self: PointCloudInstance,scanName: str) -> XYZ
  
   Returns the origin point of a scan in model coordinates.
  
   scanName: Name of the scan.
   Returns: Resulting origin point of the scan.
  """
  pass
 def GetScans(self):
  """
  GetScans(self: PointCloudInstance) -> IList[str]
  
   Returns array of scan names.
   Returns: Resulting array of scan names.
  """
  pass
 def GetSelectionFilter(self):
  """
  GetSelectionFilter(self: PointCloudInstance) -> PointCloudFilter
  
   Returns the currently active selection filter for this point cloud.
   Returns: Currently active selection filter or ll if none is active.
  """
  pass
 def HasColor(self):
  """
  HasColor(self: PointCloudInstance) -> bool
  
   Returns true if at least one scan of the element have color,false otherwise.
   Returns: True if at least one scan of the element have color,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetSelectionFilter(self,pFilter):
  """
  SetSelectionFilter(self: PointCloudInstance,pFilter: PointCloudFilter)
   Sets active selection filter by cloning of the one passed to it.
  
   pFilter: The filter object to be made active.  If ll is supplied,the
     active filter 
    is removed.
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
 FilterAction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The action taken based on the results of the selection filter applied to this point cloud.

Get: FilterAction(self: PointCloudInstance) -> SelectionFilterAction

Set: FilterAction(self: PointCloudInstance)=value
"""

 SupportsOverrides=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies whether the instance can have graphic overrides.

Get: SupportsOverrides(self: PointCloudInstance) -> bool

"""


