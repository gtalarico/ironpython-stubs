class ReferencePoint(Element,IDisposable):
 """ A reference point in an Autodesk Revit family. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetCoordinatePlaneReferenceXY(self):
  """
  GetCoordinatePlaneReferenceXY(self: ReferencePoint) -> Reference
  
   A reference for the XY plane of the coordinate
  system.
  """
  pass
 def GetCoordinatePlaneReferenceXZ(self):
  """
  GetCoordinatePlaneReferenceXZ(self: ReferencePoint) -> Reference
  
   A reference for the XZ plane of the coordinate
  system.
  """
  pass
 def GetCoordinatePlaneReferenceYZ(self):
  """
  GetCoordinatePlaneReferenceYZ(self: ReferencePoint) -> Reference
  
   A reference for the YZ plane of the coordinate
  system.
  """
  pass
 def GetCoordinateSystem(self):
  """
  GetCoordinateSystem(self: ReferencePoint) -> Transform
  
   The position and orientation of the ReferencePoint.
  """
  pass
 def GetHubId(self):
  """
  GetHubId(self: ReferencePoint) -> ElementId
  
   Id of associated Hub.
  """
  pass
 def GetInterpolatingCurves(self):
  """
  GetInterpolatingCurves(self: ReferencePoint) -> CurveByPointsArray
  
   The set of CurveByPoints elements that interpolate
  a ReferencePoint.
  """
  pass
 def GetPointElementReference(self):
  """
  GetPointElementReference(self: ReferencePoint) -> PointElementReference
  
   Retrieve a copy of the rule that computes the
  location of the ReferencePoint 
    relative to other elements in
  the document.
  
   Returns: A PointElementReference object,or ll if the
  ReferencePoint does not have a 
    reference.
  """
  pass
 def GetVisibility(self):
  """
  GetVisibility(self: ReferencePoint) -> FamilyElementVisibility
  
   Gets the visibility for the point.
   Returns: A copy of visibility settings for the
  ReferencePoint.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def SetCoordinateSystem(self,coordinateSystem):
  """
  SetCoordinateSystem(self: ReferencePoint,coordinateSystem: Transform)
   The position and orientation of the ReferencePoint.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetPointElementReference(self,pointElementReference):
  """
  SetPointElementReference(self: ReferencePoint,pointElementReference: PointElementReference)
   Change the rule for computing the 
  location of the ReferencePoint relative to 
    other elements in
  the document.
  
  
   pointElementReference: An object specifying
  a rule for the location and orientation of a 
    ReferencePoint.
  (Note: The ReferencePoint object does not store the
  
    pointElementReference object after this call.)
  """
  pass
 def SetVisibility(self,visibility):
  """
  SetVisibility(self: ReferencePoint,visibility: FamilyElementVisibility)
   Sets the visibility for the point.
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
 CoordinatePlaneVisibility=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Visibility settings for the coordinate reference planes.

Get: CoordinatePlaneVisibility(self: ReferencePoint) -> CoordinatePlaneVisibility

Set: CoordinatePlaneVisibility(self: ReferencePoint)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: ReferencePoint) -> str

Set: Name(self: ReferencePoint)=value
"""

 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The position of the ReferencePoint.

Get: Position(self: ReferencePoint) -> XYZ

Set: Position(self: ReferencePoint)=value
"""

 ShowNormalReferencePlaneOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether all three coordinate planes are shown,or only the
normal (XY) plane.

Get: ShowNormalReferencePlaneOnly(self: ReferencePoint) -> bool

Set: ShowNormalReferencePlaneOnly(self: ReferencePoint)=value
"""

 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether the point is visible when the family is loaded
into a project.

Get: Visible(self: ReferencePoint) -> bool

Set: Visible(self: ReferencePoint)=value
"""


