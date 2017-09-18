class ViewportInfo(object,IDisposable,ISerializable):
 """
 Represents a viewing frustum.

 

 ViewportInfo()

 ViewportInfo(other: ViewportInfo)

 ViewportInfo(rhinoViewport: RhinoViewport)
 """
 def ChangeToParallelProjection(self,symmetricFrustum):
  """
  ChangeToParallelProjection(self: ViewportInfo,symmetricFrustum: bool) -> bool

  

   Use this function to change projections of valid viewports

     from parallel to 

    perspective.  It will make common additional

     adjustments to the frustum and camera 

    location so the resulting

     views are similar.  The camera direction and target point 

    are

     not be changed.

     If the current projection is parallel and 

    symmetricFrustum,

     FrustumIsLeftRightSymmetric() and FrustumIsTopBottomSymmetric()

   

      are all equal,then no changes are made and true is returned.

  

  

   symmetricFrustum: true if you want the resulting frustum to be symmetric.

   Returns: true if the operation succeeded; otherwise,false.
  """
  pass
 def ChangeToPerspectiveProjection(self,targetDistance,symmetricFrustum,lensLength):
  """
  ChangeToPerspectiveProjection(self: ViewportInfo,targetDistance: float,symmetricFrustum: bool,lensLength: float) -> bool

  

   Use this function to change projections of valid viewports

     from parallel to 

    perspective.  It will make common additional

     adjustments to the frustum and camera 

    location so the resulting

     views are similar.  The camera direction and target point 

    are

     not changed.

     If the current projection is perspective and 

    symmetricFrustum,

     IsFrustumIsLeftRightSymmetric,and IsFrustumIsTopBottomSymmetric

  

       are all equal,then no changes are made and true is returned.

  

  

   targetDistance: If RhinoMath.UnsetValue this parameter is ignored.

     Otherwise it must be > 0 and 

    indicates which plane in the current view frustum should be perserved.

  

   symmetricFrustum: true if you want the resulting frustum to be symmetric.

   lensLength: (pass 50.0 when in doubt)

     35 mm lens length to use when changing from parallel

   

      to perspective projections. If the current projection

     is perspective or 

    lens_length is <= 0.0,

     then this parameter is ignored.

  

   Returns: true if the operation succeeded; otherwise,false.
  """
  pass
 def ChangeToSymmetricFrustum(self,isLeftRightSymmetric,isTopBottomSymmetric,targetDistance):
  """
  ChangeToSymmetricFrustum(self: ViewportInfo,isLeftRightSymmetric: bool,isTopBottomSymmetric: bool,targetDistance: float) -> bool

  

   If needed,adjusts the current frustum so it has the 

     specified symmetries and 

    adjust the camera location

     so the target plane remains visible.

  

  

   isLeftRightSymmetric: If true,the frustum will be adjusted so left=-right.

   isTopBottomSymmetric: If true,the frustum will be adjusted so top=-bottom.

   targetDistance: If projection is not perspective or target_distance is RhinoMath.UnsetValue,

     then 

    this parameter is ignored. If the projection is perspective and targetDistance

     is 

    not RhinoMath.UnsetValue,then it must be > 0.0 and it is used to determine

     which 

    plane in the old frustum will appear unchanged in the new frustum.

  

   Returns: Returns true if the viewport has now a frustum with the specified symmetries.
  """
  pass
 def ChangeToTwoPointPerspectiveProjection(self,targetDistance,up,lensLength):
  """
  ChangeToTwoPointPerspectiveProjection(self: ViewportInfo,targetDistance: float,up: Vector3d,lensLength: float) -> bool

  

   Changes projections of valid viewports

     to a two point perspective.  It will make 

    common additional

     adjustments to the frustum and camera location and direction

   

      so the resulting views are similar.

     If the current projection is 

    perspective and

     IsFrustumIsLeftRightSymmetric is true and

     

    IsFrustumIsTopBottomSymmetric is false,then no changes are

     made and true is 

    returned.

  

  

   targetDistance: If RhinoMath.UnsetValue this parameter is ignored.  Otherwise

     it must be > 0 and 

    indicates which plane in the current 

     view frustum should be perserved.

  

   up: The locked up direction. Pass Vector3d.Zero if you want to use the world

     axis 

    direction that is closest to the current up direction.

     Pass CameraY() if you want 

    to preserve the current up direction.

  

   lensLength: (pass 50.0 when in doubt)

     35 mm lens length to use when changing from parallel

   

      to perspective projections. If the current projection

     is perspective or 

    lens_length is <= 0.0,

     then this parameter is ignored.

  

   Returns: true if the operation succeeded; otherwise,false.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: ViewportInfo)

   Actively reclaims unmanaged resources that this instance uses.
  """
  pass
 def DollyCamera(self,dollyVector):
  """
  DollyCamera(self: ViewportInfo,dollyVector: Vector3d) -> bool

  

   DollyCamera() does not update the frustum's clipping planes.

     To update the 

    frustum's clipping planes call DollyFrustum(d)

     with d=dollyVector o cameraFrameZ. 

     To convert screen locations

     into a dolly vector,use GetDollyCameraVector().

    

     Does not update frustum.  To update frustum use DollyFrustum(d) with d=dollyVector o 

    cameraFrameZ.

  

  

   dollyVector: dolly vector in world coordinates.

   Returns: true if the operation succeeded; otherwise,false.
  """
  pass
 def DollyExtents(self,*__args):
  """
  DollyExtents(self: ViewportInfo,cameraCoordinateBoundingBox: BoundingBox,border: float) -> bool

  

   Dolly the camera location and so that the view frustum contains

     all of the document 

    objects that can be seen in view.

     If the projection is perspective,the camera 

    angle is not changed.

  

  

   border: If border > 1.0,then the fustum in enlarged by this factor

     to provide a border 

    around the view.  1.1 works well for

     parallel projections; 0.0 is suggested for 

    perspective projections.

  

   Returns: True if successful.

  DollyExtents(self: ViewportInfo,geometry: IEnumerable[GeometryBase],border: float) -> bool
  """
  pass
 def DollyFrustum(self,dollyDistance):
  """
  DollyFrustum(self: ViewportInfo,dollyDistance: float) -> bool

  

   Moves the frustum clipping planes.

  

   dollyDistance: Distance to move in camera direction.

   Returns: true if the operation succeeded; otherwise,false.
  """
  pass
 def Extents(self,halfViewAngleRadians,*__args):
  """
  Extents(self: ViewportInfo,halfViewAngleRadians: float,sphere: Sphere) -> bool

  

   Extends this viewport view to include a sphere.

     Use Extents() as a quick way to set 

    a viewport to so that bounding

     volume is inside of a viewports frustrum.

      

      The view angle is used to determine the position of the camera.

  

  

   halfViewAngleRadians: 1/2 smallest subtended view angle in radians.

   sphere: A sphere in 3d world coordinates.

   Returns: true if the operation succeeded; otherwise,false.

  Extents(self: ViewportInfo,halfViewAngleRadians: float,bbox: BoundingBox) -> bool

  

   Extends this viewport view to include a bounding box.

     Use Extents() as a quick way 

    to set a viewport to so that bounding

     volume is inside of a viewports frustrum.

     

       The view angle is used to determine the position of the camera.

  

  

   halfViewAngleRadians: 1/2 smallest subtended view angle in radians.

   bbox: A bounding box in 3d world coordinates.

   Returns: true if the operation succeeded; otherwise,false.
  """
  pass
 def FrustumCenterPoint(self,targetDistance):
  """
  FrustumCenterPoint(self: ViewportInfo,targetDistance: float) -> Point3d

  

   Return a point on the central axis of the view frustum.

     This point is a good choice 

    for a general purpose target point.

  

  

   targetDistance: If targetDistance > 0.0,then the distance from the returned

     point to the camera 

    plane will be targetDistance. Note that

     if the frustum is not symmetric,the 

    distance from the

     returned point to the camera location will be larger than

      

      targetDistance.

     If targetDistance == ON_UNSET_VALUE and the frustum

      

      is valid with near > 0.0,then 0.5*(near + far) will be used

     as the 

    targetDistance.

  

   Returns: A point on the frustum's central axis.  If the viewport or input

     is not valid,then 

    ON_3dPoint::UnsetPoint is returned.
  """
  pass
 def GetBoundingBoxDepth(self,bbox,nearDistance,farDistance):
  """
  GetBoundingBoxDepth(self: ViewportInfo,bbox: BoundingBox) -> (bool,float,float)

  

   Gets near and far clipping distances of a bounding box.

     This function ignores the 

    current value of the viewport's 

     near and far settings. If the viewport is a 

    perspective

     projection,the it intersects the semi infinite frustum

     

    volume with the bounding box and returns the near and far

     distances of the 

    intersection.  If the viewport is a parallel

     projection,it instersects the infinte 

    view region with the

     bounding box and returns the near and far distances of the

     

       projection.

  

  

   bbox: The bounding box to sample.

   Returns: true if the bounding box intersects the view frustum and near_dist/far_dist were set. 

     

    false if the bounding box does not intesect the view frustum.
  """
  pass
 def GetCameraAngles(self,halfDiagonalAngleRadians,halfVerticalAngleRadians,halfHorizontalAngleRadians):
  """
  GetCameraAngles(self: ViewportInfo) -> (bool,float,float,float)

  

   Gets the field of view angles.

   Returns: true if the operation succeeded; otherwise,false.
  """
  pass
 def GetCameraFrame(self,location,cameraX,cameraY,cameraZ):
  """
  GetCameraFrame(self: ViewportInfo) -> (bool,Point3d,Vector3d,Vector3d,Vector3d)

  

   Gets location and vectors of this camera.

   Returns: true if current camera orientation is valid; otherwise false.
  """
  pass
 def GetDollyCameraVector(self,*__args):
  """
  GetDollyCameraVector(self: ViewportInfo,screen0: Point,screen1: Point,projectionPlaneDistance: float) -> Vector3d

  

   Gets a world coordinate dolly vector that can be passed to DollyCamera().

  

   screen0: Start point.

   screen1: End point.

   projectionPlaneDistance: Distance of projection plane from camera. When in doubt,use 0.5*(frus_near+frus_far).

   Returns: The world coordinate dolly vector.

  GetDollyCameraVector(self: ViewportInfo,screenX0: int,screenY0: int,screenX1: int,screenY1: int,projectionPlaneDistance: float) -> Vector3d

  

   Gets a world coordinate dolly vector that can be passed to DollyCamera().

  

   screenX0: Screen coords of start point.

   screenY0: Screen coords of start point.

   screenX1: Screen coords of end point.

   screenY1: Screen coords of end point.

   projectionPlaneDistance: Distance of projection plane from camera. When in doubt,use 0.5*(frus_near+frus_far).

   Returns: The world coordinate dolly vector.
  """
  pass
 def GetFarPlaneCorners(self):
  """
  GetFarPlaneCorners(self: ViewportInfo) -> Array[Point3d]

  

   Gets the corners of far clipping plane rectangle.

     4 points are returned in the 

    order of bottom left,bottom right,

     top left,top right.

  

   Returns: Four corner points on success.

     Empty array if viewport is not valid.
  """
  pass
 def GetFrustum(self,left,right,bottom,top,nearDistance,farDistance):
  """
  GetFrustum(self: ViewportInfo) -> (bool,float,float,float,float,float,float)

  

   Gets the view frustum.

   Returns: true if operation succeeded; otherwise,false.
  """
  pass
 def GetFrustumLine(self,*__args):
  """
  GetFrustumLine(self: ViewportInfo,screenPoint: PointF) -> Line

  

   Gets the world coordinate line in the view frustum

     that projects to a point on the 

    screen.

  

  

   screenPoint: screen location

   Returns: 3d world coordinate line segment starting on the near clipping plane and ending on the far 

    clipping plane.

  

  GetFrustumLine(self: ViewportInfo,screenPoint: Point) -> Line

  

   Gets the world coordinate line in the view frustum

     that projects to a point on the 

    screen.

  

  

   screenPoint: screen location

   Returns: 3d world coordinate line segment starting on the near clipping plane and ending on the far 

    clipping plane.

  

  GetFrustumLine(self: ViewportInfo,screenX: float,screenY: float) -> Line

  

   Gets the world coordinate line in the view frustum

     that projects to a point on the 

    screen.

  

  

   screenX: (screenx,screeny)=screen location.

   screenY: (screenx,screeny)=screen location.

   Returns: 3d world coordinate line segment starting on the near clipping plane and ending on the far 

    clipping plane.
  """
  pass
 def GetNearPlaneCorners(self):
  """
  GetNearPlaneCorners(self: ViewportInfo) -> Array[Point3d]

  

   Gets the corners of near clipping plane rectangle.

     4 points are returned in the 

    order of bottom left,bottom right,

     top left,top right.

  

   Returns: Four corner points on success.

     Empty array if viewport is not valid.
  """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: ViewportInfo,info: SerializationInfo,context: StreamingContext)

   Populates a System.Runtime.Serialization.SerializationInfo with the data needed to serialize the 

    target object.

  

  

   info: The System.Runtime.Serialization.SerializationInfo to populate with data.

   context: The destination (see System.Runtime.Serialization.StreamingContext) for this serialization.
  """
  pass
 def GetPointDepth(self,point,distance):
  """
  GetPointDepth(self: ViewportInfo,point: Point3d) -> (bool,float)

  

   Gets the clipping distance of a point. This function ignores the

     current value of 

    the viewport's near and far settings. If

     the viewport is a perspective projection,

    then it intersects

     the semi infinite frustum volume with the bounding box and

    

     returns the near and far distances of the intersection.

     If the viewport is a 

    parallel projection,it instersects the

     infinte view region with the bounding box 

    and returns the

     near and far distances of the projection.

  

  

   point: A point to measure.

   Returns: true if the bounding box intersects the view frustum and

     near_dist/far_dist were 

    set.

     false if the bounding box does not intesect the view frustum.
  """
  pass
 def GetScreenPort(self,near=None,far=None):
  """
  GetScreenPort(self: ViewportInfo) -> Rectangle

  

   Gets the location of viewport in pixels.

     See documentation for 

    Rhino.DocObjects.ViewportInfo.SetScreenPort(System.Int32,System.Int32,System.Int32,System.Int32,S

    ystem.Int32,System.Int32)SetScreenPort.

  

   Returns: The rectangle,or System.Drawing.Rectangle.EmptyEmpty rectangle on error.

  GetScreenPort(self: ViewportInfo) -> (Rectangle,int,int)

  

   Gets the location of viewport in pixels.

     See value meanings in 

    Rhino.DocObjects.ViewportInfo.SetScreenPort(System.Int32,System.Int32,System.Int32,System.Int32,S

    ystem.Int32,System.Int32)SetScreenPort.

  

   Returns: The rectangle,or System.Drawing.Rectangle.EmptyEmpty rectangle on error.
  """
  pass
 def GetSphereDepth(self,sphere,nearDistance,farDistance):
  """
  GetSphereDepth(self: ViewportInfo,sphere: Sphere) -> (bool,float,float)

  

   Gets near and far clipping distances of a bounding sphere.

  

   sphere: The sphere to sample.

   Returns: true if the sphere intersects the view frustum and near_dist/far_dist were set.

     

    false if the sphere does not intesect the view frustum.
  """
  pass
 def GetWorldToScreenScale(self,pointInFrustum):
  """
  GetWorldToScreenScale(self: ViewportInfo,pointInFrustum: Point3d) -> float

  

   Gets the scale factor from point in frustum to screen scale.

  

   pointInFrustum: point in viewing frustum.

   Returns: number of pixels per world unit at the 3d point.
  """
  pass
 def GetXform(self,sourceSystem,destinationSystem):
  """
  GetXform(self: ViewportInfo,sourceSystem: CoordinateSystem,destinationSystem: CoordinateSystem) -> Transform

  

   Computes a transform from a coordinate system to another.

  

   sourceSystem: The coordinate system to map from.

   destinationSystem: The coordinate system to map into.

   Returns: The 4x4 transformation matrix (acts on the left).
  """
  pass
 def SetCameraDirection(self,direction):
  """
  SetCameraDirection(self: ViewportInfo,direction: Vector3d) -> bool

  

   Sets the direction that the camera faces.

  

   direction: A new direction.

   Returns: true if the direction was set; otherwise false.
  """
  pass
 def SetCameraLocation(self,location):
  """
  SetCameraLocation(self: ViewportInfo,location: Point3d) -> bool

  

   Sets the camera location (position) point.

   Returns: true if the operation succeeded; otherwise,false.
  """
  pass
 def SetCameraUp(self,up):
  """
  SetCameraUp(self: ViewportInfo,up: Vector3d) -> bool

  

   Sets the camera up vector.

  

   up: A new direction.

   Returns: true if the direction was set; otherwise false.
  """
  pass
 def SetFrustum(self,left,right,bottom,top,nearDistance,farDistance):
  """
  SetFrustum(self: ViewportInfo,left: float,right: float,bottom: float,top: float,nearDistance: float,farDistance: float) -> bool

  

   Sets the view frustum. If FrustumSymmetryIsLocked() is true

     and left != -right or 

    bottom != -top,then they will be

     adjusted so the resulting frustum is symmetric.

  

  

   left: A new left value.

   right: A new right value.

   bottom: A new bottom value.

   top: A new top value.

   nearDistance: A new near distance value.

   farDistance: A new far distance value.

   Returns: true if operation succeeded; otherwise,false.
  """
  pass
 def SetFrustumNearFar(self,*__args):
  """
  SetFrustumNearFar(self: ViewportInfo,nearDistance: float,farDistance: float) -> bool

  

   Sets the frustum near and far distances using two values.

  

   nearDistance: The new near distance.

   farDistance: The new far distance.

   Returns: true if operation succeeded; otherwise,false.

  SetFrustumNearFar(self: ViewportInfo,nearDistance: float,farDistance: float,minNearDistance: float,minNearOverFar: float,targetDistance: float) -> bool

  

   Sets near and far clipping distance subject to constraints.

  

   nearDistance: (>0) desired near clipping distance.

   farDistance: (>near_dist) desired near clipping distance.

   minNearDistance: If min_near_dist <= 0.0,it is ignored.

     If min_near_dist > 0 and near_dist < 

    min_near_dist,then the frustum's near_dist will be increased to min_near_dist.

  

   minNearOverFar: If min_near_over_far <= 0.0,it is ignored.

     If near_dist < 

    far_dist*min_near_over_far,then

     near_dist is increased and/or far_dist is 

    decreased

     so that near_dist=far_dist*min_near_over_far.

     If near_dist 

    < target_dist < far_dist,then near_dist

     near_dist is increased and far_dist is 

    decreased so that

     projection precision will be good at target_dist.

     

    Otherwise,near_dist is simply set to 

     far_dist*min_near_over_far.

  

   targetDistance: If target_dist <= 0.0,it is ignored.

     If target_dist > 0,it is used as described 

    in the

     description of the min_near_over_far parameter.

  

   Returns: true if operation succeeded; otherwise,false.

  SetFrustumNearFar(self: ViewportInfo,boundingBox: BoundingBox) -> bool

  

   Sets the frustum near and far using a bounding box.

  

   boundingBox: A bounding box to use.

   Returns: true if operation succeeded; otherwise,false.

  SetFrustumNearFar(self: ViewportInfo,center: Point3d,radius: float) -> bool

  

   Sets the frustum near and far using a center point and radius.

  

   center: A center point.

   radius: A radius value.

   Returns: true if operation succeeded; otherwise,false.
  """
  pass
 def SetScreenPort(self,*__args):
  """
  SetScreenPort(self: ViewportInfo,windowRectangle: Rectangle) -> bool

  

   Gets the location of viewport in pixels.

     See value meanings in 

    Rhino.DocObjects.ViewportInfo.SetScreenPort(System.Int32,System.Int32,System.Int32,System.Int32,S

    ystem.Int32,System.Int32)SetScreenPort.

  

  

   windowRectangle: A new rectangle.

   Returns: true if input is valid.

  SetScreenPort(self: ViewportInfo,windowRectangle: Rectangle,near: int,far: int) -> bool

  

   Gets the location of viewport in pixels.

     See value meanings in 

    Rhino.DocObjects.ViewportInfo.SetScreenPort(System.Int32,System.Int32,System.Int32,System.Int32,S

    ystem.Int32,System.Int32)SetScreenPort.

  

  

   windowRectangle: A new rectangle.

   near: The near value.

   far: The far value.

   Returns: true if input is valid.

  SetScreenPort(self: ViewportInfo,left: int,right: int,bottom: int,top: int,near: int,far: int) -> bool

  

   Location of viewport in pixels.

     These are provided so you can set the port you are 

    using

     and get the appropriate transformations to and from

     screen 

    space.

     // For a Windows window

     /   int width=width of window 

    client area in pixels;

     /   int height=height of window client area in pixels;

  

       /   port_left=0;

     /   port_right=width;

     /   

    port_top=0;

     /   port_bottom=height;

     /   port_near=0;

    

     /   port_far=1;

     /   SetScreenPort( port_left,port_right,

     

    /      port_bottom,port_top,

     /      port_near,

    port_far );

  

  

   left: A left value.

   right: A left value. (port_left != port_right)

   bottom: A bottom value.

   top: A top value. (port_top != port_bottom)

   near: A near value.

   far: A far value.

   Returns: true if input is valid.
  """
  pass
 def TargetDistance(self,useFrustumCenterFallback):
  """
  TargetDistance(self: ViewportInfo,useFrustumCenterFallback: bool) -> float

  

   Gets the distance from the target point to the camera plane.

     Note that if the 

    frustum is not symmetric,then this distance

     is shorter than the distance from the 

    target to the camera location.

  

  

   useFrustumCenterFallback: If bUseFrustumCenterFallback is false and the target point is

     not valid,then 

    ON_UNSET_VALUE is returned.

     If bUseFrustumCenterFallback is true and the frustum is 

    valid

     and current target point is not valid or is behind the camera,

     

    then 0.5*(near + far) is returned.

  

   Returns: Shortest signed distance from camera plane to target point.

     If the target point is 

    on the visible side of the camera,

     a positive value is returned.  ON_UNSET_VALUE is 

    returned

     when the input of view is not valid.
  """
  pass
 def UnlockCamera(self):
  """
  UnlockCamera(self: ViewportInfo)

   Unlocks the camera vectors and location.
  """
  pass
 def UnlockFrustumSymmetry(self):
  """
  UnlockFrustumSymmetry(self: ViewportInfo)

   Unlocks frustum horizontal and vertical symmetries.
  """
  pass
 def ZoomToScreenRect(self,*__args):
  """
  ZoomToScreenRect(self: ViewportInfo,windowRectangle: Rectangle) -> bool

  

   Zooms to a screen zone.

     View changing from screen input points. Handy for

     

    using a mouse to manipulate a view.

     ZoomToScreenRect() may change camera and 

    frustum settings.

  

  

   windowRectangle: The new window rectangle in screen space.

   Returns: true if the operation succeeded; otherwise,false.

  ZoomToScreenRect(self: ViewportInfo,left: int,top: int,right: int,bottom: int) -> bool

  

   Zooms to a screen zone.

     View changing from screen input points. Handy for

     

    using a mouse to manipulate a view.

     ZoomToScreenRect() may change camera and 

    frustum settings.

  

  

   left: Screen coord.

   top: Screen coord.

   right: Screen coord.

   bottom: Screen coord.

   Returns: true if the operation succeeded; otherwise,false.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,other: ViewportInfo)

  __new__(cls: type,rhinoViewport: RhinoViewport)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Camera35mmLensLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property assumes the camera is horizontal and crop the

   film rather than the image when the aspect of the frustum

   is not 36/24.  (35mm film is 36mm wide and 24mm high.)

   Setting preserves camera location,

   changes the frustum,but maintains the frustum's aspect.



Get: Camera35mmLensLength(self: ViewportInfo) -> float



Set: Camera35mmLensLength(self: ViewportInfo)=value

"""

 CameraAngle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the 1/2 smallest angle. See Rhino.DocObjects.ViewportInfo.GetCameraAngles(System.Double@,System.Double@,System.Double@) for more information.



Get: CameraAngle(self: ViewportInfo) -> float



Set: CameraAngle(self: ViewportInfo)=value

"""

 CameraDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the direction that the camera faces.



Get: CameraDirection(self: ViewportInfo) -> Vector3d



"""

 CameraLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the camera location (position) point.



Get: CameraLocation(self: ViewportInfo) -> Point3d



"""

 CameraUp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the camera up vector.



Get: CameraUp(self: ViewportInfo) -> Vector3d



"""

 CameraX=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the unit "to the right" vector.



Get: CameraX(self: ViewportInfo) -> Vector3d



"""

 CameraY=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the unit "up" vector.



Get: CameraY(self: ViewportInfo) -> Vector3d



"""

 CameraZ=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the unit vector in -CameraDirection.



Get: CameraZ(self: ViewportInfo) -> Vector3d



"""

 FrustumAspect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Setting FrustumAspect changes the larger of the frustum's width/height

   so that the resulting value of width/height matches the requested

   aspect.  The camera angle is not changed.  If you change the shape

   of the view port with a call SetScreenPort(),then you generally 

   want to call SetFrustumAspect() with the value returned by 

   GetScreenPortAspect().



Get: FrustumAspect(self: ViewportInfo) -> float



Set: FrustumAspect(self: ViewportInfo)=value

"""

 FrustumBottom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the frustum bottom value. This is -top if the frustum has a horizontal symmetry axis.

   This number is usually negative.



Get: FrustumBottom(self: ViewportInfo) -> float



"""

 FrustumBottomPlane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the frustum bottom plane that separates visibile from off-screen.



Get: FrustumBottomPlane(self: ViewportInfo) -> Plane



"""

 FrustumCenter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the frustum center point.



Get: FrustumCenter(self: ViewportInfo) -> Point3d



"""

 FrustumFar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the frustum far-cutting value.



Get: FrustumFar(self: ViewportInfo) -> float



"""

 FrustumFarPlane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets far clipping plane if camera and frustum

   are valid.  The plane's frame is the same as the camera's

   frame.  The origin is located at the intersection of the

   camera direction ray and the far clipping plane. The plane's

   normal points into the frustum towards the camera location.



Get: FrustumFarPlane(self: ViewportInfo) -> Plane



"""

 FrustumHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the frustum height. This is Rhino.DocObjects.ViewportInfo.FrustumTop - Rhino.DocObjects.ViewportInfo.FrustumBottom.



Get: FrustumHeight(self: ViewportInfo) -> float



"""

 FrustumLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the frustum left value. This is -right if the frustum has a vertical symmetry axis.

   This number is usually negative.



Get: FrustumLeft(self: ViewportInfo) -> float



"""

 FrustumLeftPlane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the frustum left plane that separates visibile from off-screen.



Get: FrustumLeftPlane(self: ViewportInfo) -> Plane



"""

 FrustumMaximumDiameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the frustum maximum diameter,or the maximum between Rhino.DocObjects.ViewportInfo.FrustumWidth and Rhino.DocObjects.ViewportInfo.FrustumHeight.



Get: FrustumMaximumDiameter(self: ViewportInfo) -> float



"""

 FrustumMinimumDiameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the frustum minimum diameter,or the minimum between Rhino.DocObjects.ViewportInfo.FrustumWidth and Rhino.DocObjects.ViewportInfo.FrustumHeight.



Get: FrustumMinimumDiameter(self: ViewportInfo) -> float



"""

 FrustumNear=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the frustum near-cutting value.



Get: FrustumNear(self: ViewportInfo) -> float



"""

 FrustumNearPlane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets near clipping plane if camera and frustum

   are valid.  The plane's frame is the same as the camera's

   frame.  The origin is located at the intersection of the

   camera direction ray and the near clipping plane. The plane's

   normal points out of the frustum towards the camera

   location.



Get: FrustumNearPlane(self: ViewportInfo) -> Plane



"""

 FrustumRight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the frustum right value. This is -left if the frustum has a vertical symmetry axis.

   This number is usually positive.



Get: FrustumRight(self: ViewportInfo) -> float



"""

 FrustumRightPlane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the frustum right plane that separates visibile from off-screen.



Get: FrustumRightPlane(self: ViewportInfo) -> Plane



"""

 FrustumTop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the frustum top value. This is -bottom if the frustum has a horizontal symmetry axis.

   This number is usually positive.



Get: FrustumTop(self: ViewportInfo) -> float



"""

 FrustumTopPlane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the frustum top plane that separates visibile from off-screen.



Get: FrustumTopPlane(self: ViewportInfo) -> Plane



"""

 FrustumWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the frustum width. This is Rhino.DocObjects.ViewportInfo.FrustumRight - Rhino.DocObjects.ViewportInfo.FrustumLeft.



Get: FrustumWidth(self: ViewportInfo) -> float



"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Sets the viewport's id to the value used to 

   uniquely identify this viewport.

   There is no approved way to change the viewport 

   id once it is set in order to maintain consistency

   across multiple viewports and those routines that 

   manage them.



Get: Id(self: ViewportInfo) -> Guid



"""

 IsCameraDirectionLocked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the direction that the camera faces is unmodifiable.



Get: IsCameraDirectionLocked(self: ViewportInfo) -> bool



Set: IsCameraDirectionLocked(self: ViewportInfo)=value

"""

 IsCameraLocationLocked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the camera location is unmodifiable.



Get: IsCameraLocationLocked(self: ViewportInfo) -> bool



Set: IsCameraLocationLocked(self: ViewportInfo)=value

"""

 IsCameraUpLocked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the camera up vector is unmodifiable.



Get: IsCameraUpLocked(self: ViewportInfo) -> bool



Set: IsCameraUpLocked(self: ViewportInfo)=value

"""

 IsFrustumLeftRightSymmetric=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the camera frustum has a vertical symmetry axis.



Get: IsFrustumLeftRightSymmetric(self: ViewportInfo) -> bool



Set: IsFrustumLeftRightSymmetric(self: ViewportInfo)=value

"""

 IsFrustumTopBottomSymmetric=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the camera frustum has a horizontal symmetry axis.



Get: IsFrustumTopBottomSymmetric(self: ViewportInfo) -> bool



Set: IsFrustumTopBottomSymmetric(self: ViewportInfo)=value

"""

 IsParallelProjection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or set whether this projection is parallel.



Get: IsParallelProjection(self: ViewportInfo) -> bool



Set: IsParallelProjection(self: ViewportInfo)=value

"""

 IsPerspectiveProjection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or set whether this projection is perspective.



Get: IsPerspectiveProjection(self: ViewportInfo) -> bool



Set: IsPerspectiveProjection(self: ViewportInfo)=value

"""

 IsTwoPointPerspectiveProjection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this projection is a two-point perspective.



Get: IsTwoPointPerspectiveProjection(self: ViewportInfo) -> bool



"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this complete object is valid.



Get: IsValid(self: ViewportInfo) -> bool



"""

 IsValidCamera=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the camera is valid.



Get: IsValidCamera(self: ViewportInfo) -> bool



"""

 IsValidFrustum=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the frustum is valid.



Get: IsValidFrustum(self: ViewportInfo) -> bool



"""

 ScreenPortAspect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the sceen aspect ratio.

   This is width / height.



Get: ScreenPortAspect(self: ViewportInfo) -> float



"""

 TargetPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The current value of the target point.  This point does not play

   a role in the view projection calculations.  It can be used as a 

   fixed point when changing the camera so the visible regions of the

   before and after frustums both contain the region of interest.

   The default constructor sets this point on ON_3dPoint::UnsetPoint.

   You must explicitly call one SetTargetPoint() functions to set

   the target point.



Get: TargetPoint(self: ViewportInfo) -> Point3d



Set: TargetPoint(self: ViewportInfo)=value

"""

 ViewScale=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Applies scaling factors to parallel projection clipping coordinates

   by setting the m_clip_mod transformation. 

   If you want to compress the view projection across the viewing

   plane,then set x=0.5,y=1.0,and z=1.0.



Get: ViewScale(self: ViewportInfo) -> SizeF



Set: ViewScale(self: ViewportInfo)=value

"""



# variables with complex values

