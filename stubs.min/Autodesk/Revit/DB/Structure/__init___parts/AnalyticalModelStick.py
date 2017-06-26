class AnalyticalModelStick(AnalyticalModel,IDisposable):
 """
 An element that represents a stick in the structural analytical model.
    Could be one of beam,brace or column type.
 """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def GetAlignmentMethod(self,selector):
  """
  GetAlignmentMethod(self: AnalyticalModelStick,selector: AnalyticalElementSelector) -> AnalyticalAlignmentMethod
  
   Gets the alignment method for a given selector.
  
   selector: End of the analytical model.
   Returns: The alignment method at a given end.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetLocalCoordinateSystem(self,*__args):
  """
  GetLocalCoordinateSystem(self: AnalyticalModelStick,point: XYZ) -> Transform
  
   Gets the local coordinate system (LCS) reflects analytical model orientation at 
    the specified point.
  
  
   point: The point on the analytical model stick element.
   Returns: Transformation matrix.
     x - longitudinal axis,y - transversal,section - 
    horizontal,strong axis,z - transversal,section - vertical,weak axis,origin 
    - base point of LCS.
  
  GetLocalCoordinateSystem(self: AnalyticalModelStick,parameter: float) -> Transform
  
   Gets the local coordinate system (LCS) reflects analytical model orientation at 
    the specified parameter value along a curve.
  
  
   parameter: The parameter value along a curve that should be in the range [0,1],where 0 
    represents start and 1 represents end of the element.
  
   Returns: Transformation matrix.
     x - longitudinal axis,y - transversal,section - 
    horizontal,strong axis,z - transversal,section - vertical,weak axis,origin 
    - base point of LCS.
  """
  pass
 def GetMemberForces(self):
  """
  GetMemberForces(self: AnalyticalModelStick) -> IList[MemberForces]
  
   Gets the member forces associated with this element.
   Returns: Returns a collection of Member Forces associated with this element. Empty 
    collection will be returned if element doesn't have any Member Forces.
     To 
    find out with which end member forces are associated use 
    Autodesk::Revit::DB::Structure::MemberForces::Position
     property to obtain a 
    position of Member Forces on element.
  """
  pass
 def GetProjectionPlaneY(self,selector):
  """
  GetProjectionPlaneY(self: AnalyticalModelStick,selector: AnalyticalElementSelector) -> ElementId
  
   Retrieves analytical model projection information for Y direction.
  
   selector: End of the analytical model.
   Returns: Plane on to which analytical model is projected,or invalidElementId if
     not 
    projected to a Plane.
  """
  pass
 def GetProjectionPlaneZ(self,selector):
  """
  GetProjectionPlaneZ(self: AnalyticalModelStick,selector: AnalyticalElementSelector) -> ElementId
  
   Retrieves analytical model projection information for Z direction.
  
   selector: End of the analytical model.
   Returns: Plane on to which analytical model is projected,or invalidElementId if
     not 
    projected to a Plane.
  """
  pass
 def GetProjectionY(self,selector):
  """
  GetProjectionY(self: AnalyticalModelStick,selector: AnalyticalElementSelector) -> StickElementProjectionY
  
   Retrieves analytical model projection information for Y direction.
  
   selector: End of the analytical model.
   Returns: Indicates if the projection is a preset value,or refers to a Plane.
  """
  pass
 def GetProjectionZ(self,selector):
  """
  GetProjectionZ(self: AnalyticalModelStick,selector: AnalyticalElementSelector) -> StickElementProjectionZ
  
   Retrieves analytical model projection information for Z direction.
  
   selector: End of the analytical model.
   Returns: Indicates if the projection is a preset value,or refers to a Plane.
  """
  pass
 def GetReleases(self,start,fx,fy,fz,mx,my,mz):
  """
  GetReleases(self: AnalyticalModelStick,start: bool) -> (bool,bool,bool,bool,bool,bool)
  
   Gets the releases of element.
  
   start: The position on analytical model stick element. True for start,false for end.
  """
  pass
 def GetReleaseType(self,start):
  """
  GetReleaseType(self: AnalyticalModelStick,start: bool) -> ReleaseType
  
   Gets the release type.
  
   start: The position on analytical model stick element. True for start,false for end.
   Returns: The type of release.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RemoveAllMemberForces(self):
  """
  RemoveAllMemberForces(self: AnalyticalModelStick) -> bool
  
   Removes all member forces associated with element.
   Returns: True if any member forces were removed,false otherwise.
  """
  pass
 def RemoveMemberForces(self,start):
  """
  RemoveMemberForces(self: AnalyticalModelStick,start: bool) -> bool
  
   Removes member forces defined for given position.
  
   start: Member Forces position on analytical model stick element. True for start,false 
    for end.
  
   Returns: True if member forces for provided position were removed,false otherwise.
  """
  pass
 def SetAlignmentMethod(self,selector,method):
  """
  SetAlignmentMethod(self: AnalyticalModelStick,selector: AnalyticalElementSelector,method: AnalyticalAlignmentMethod)
   Sets the alignment method for a given selector.
  
   selector: End of the analytical model.
   method: The alignment method at a given end.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetMemberForces(self,*__args):
  """
  SetMemberForces(self: AnalyticalModelStick,start: bool,force: XYZ,moment: XYZ)
   Adds Member Forces to element.
  
   start: Member Forces position on analytical model stick element. True for start,false 
    for end.
  
   force: The translational forces at specified position of the element.
     The x value 
    of XYZ object represents force along x-axis of the analytical model coordinate 
    system,y along y-axis,z along z-axis respectively.
  
   moment: The rotational forces at specified position of the element.
     The x value of 
    XYZ object represents moment about x-axis of the analytical model coordinate 
    system,y about y-axis,z about z-axis respectively.
  
  SetMemberForces(self: AnalyticalModelStick,memberForces: MemberForces)
   Sets Member Forces to element.
  
   memberForces: End to which member forces will be added is defined by setting 
    Autodesk::Revit::DB::Structure::MemberForces::Position
     property in provided 
    Member Forces object.
  """
  pass
 def SetProjection(self,selector,*__args):
  """
  SetProjection(self: AnalyticalModelStick,selector: AnalyticalElementSelector,planeIdY: ElementId,projectionZ: StickElementProjectionZ)
   Sets the analytical model projection to a preset value.
  
   selector: End of the analytical model.
   planeIdY: Plane on to which analytical model may be projected in Y direction.
     Plane 
    identifies a Level,a Grid,or a Ref Plane.
  
   projectionZ: Preset value for Analytical Model Stick projection Z.
  SetProjection(self: AnalyticalModelStick,selector: AnalyticalElementSelector,projectionY: StickElementProjectionY,projectionZ: StickElementProjectionZ)
   Sets the analytical model projection to a preset value.
  
   selector: End of the analytical model.
   projectionY: Preset value for Analytical Model Stick projection Y.
   projectionZ: Preset value for Analytical Model Stick projection Z.
  SetProjection(self: AnalyticalModelStick,selector: AnalyticalElementSelector,planeIdY: ElementId,planeIdZ: ElementId)
   Sets the analytical model projection to a preset value.
  
   selector: End of the analytical model.
   planeIdY: Plane on to which analytical model may be projected in Y direction.
     Plane 
    identifies a Level,a Grid,or a Ref Plane.
  
   planeIdZ: Plane on to which analytical model may be projected in Z direction.
     Plane 
    identifies a Level,a Grid,or a Ref Plane.
  
  SetProjection(self: AnalyticalModelStick,selector: AnalyticalElementSelector,projectionY: StickElementProjectionY,planeIdZ: ElementId)
   Sets the analytical model projection to a preset value.
  
   selector: End of the analytical model.
   projectionY: Preset value for Analytical Model Stick projection Y.
   planeIdZ: Plane on to which analytical model may be projected in Z direction.
     Plane 
    identifies a Level,a Grid,or a Ref Plane.
  """
  pass
 def SetReleases(self,start,fx,fy,fz,mx,my,mz):
  """
  SetReleases(self: AnalyticalModelStick,start: bool,fx: bool,fy: bool,fz: bool,mx: bool,my: bool,mz: bool)
   Sets the releases of element.
  
   start: The position on analytical model stick element. True for start,false for end.
  """
  pass
 def SetReleaseType(self,start,releaseType):
  """
  SetReleaseType(self: AnalyticalModelStick,start: bool,releaseType: ReleaseType)
   Sets the release type.
  
   start: The position on analytical model stick element. True for start,false for end.
   releaseType: The type of release.
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
