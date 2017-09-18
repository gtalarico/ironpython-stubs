class Surface(GeometryBase,IDisposable,ISerializable):
 """
 Represents a base class that is common to most RhinoCommon surface types.

    A surface represents an entity that can be all visited by providing

    two independent parameters,usually called (u,v),or sometimes (s,t).
 """
 def ClosestPoint(self,testPoint,u,v):
  """
  ClosestPoint(self: Surface,testPoint: Point3d) -> (bool,float,float)

  

   Input the parameters of the point on the surface that is closest to testPoint.

  

   testPoint: A point to test against.

   Returns: true on success,false on failure.
  """
  pass
 def ClosestSide(self,u,v):
  """
  ClosestSide(self: Surface,u: float,v: float) -> IsoStatus

  

   Gets the side that is closest,in terms of 3D-distance,to a U and V parameter.

  

   u: A u parameter.

   v: A v parameter.

   Returns: A side.
  """
  pass
 def ConstructConstObject(self,*args):
  """
  ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int)

   Assigns a parent object and a subobject index to this.

  

   parentObject: The parent object.

   subobject_index: The subobject index.
  """
  pass
 @staticmethod
 def CreateExtrusion(profile,direction):
  """
  CreateExtrusion(profile: Curve,direction: Vector3d) -> Surface

  

   Constructs a surface by extruding a curve along a vector.

  

   profile: Profile curve to extrude.

   direction: Direction and length of extrusion.

   Returns: A surface on success or null on failure.
  """
  pass
 @staticmethod
 def CreateExtrusionToPoint(profile,apexPoint):
  """
  CreateExtrusionToPoint(profile: Curve,apexPoint: Point3d) -> Surface

  

   Constructs a surface by extruding a curve to a point.

  

   profile: Profile curve to extrude.

   apexPoint: Apex point of extrusion.

   Returns: A Surface on success or null on failure.
  """
  pass
 @staticmethod
 def CreatePeriodicSurface(baseSurface,direction):
  """
  CreatePeriodicSurface(baseSurface: Surface,direction: int) -> Surface

  

   Constructs a periodic surface from a base surface and a direction.

  

   baseSurface: A base surface.

   direction: 0 is first parameter,1 is second parameter.

   Returns: A new surface; or null on error.
  """
  pass
 @staticmethod
 def CreateRollingBallFillet(surfaceA,*__args):
  """
  CreateRollingBallFillet(surfaceA: Surface,uvA: Point2d,surfaceB: Surface,uvB: Point2d,radius: float,tolerance: float) -> Array[Surface]

  

   Constructs a rolling ball fillet between two surfaces.

  

   surfaceA: A first surface.

   uvA: A point in the parameter space of FaceA near where the fillet is expected to hit the surface.

   surfaceB: A second surface.

   uvB: A point in the parameter space of FaceB near where the fillet is expected to hit the surface.

   radius: A radius value.

   tolerance: A tolerance value used for approximating and intersecting offset surfaces.

   Returns: A new array of rolling ball fillet surfaces; this array can be empty on failure.

  CreateRollingBallFillet(surfaceA: Surface,flipA: bool,surfaceB: Surface,flipB: bool,radius: float,tolerance: float) -> Array[Surface]

  

   Constructs a rolling ball fillet between two surfaces.

  

   surfaceA: A first surface.

   flipA: A value that indicates whether A should be used in flipped mode.

   surfaceB: A second surface.

   flipB: A value that indicates whether B should be used in flipped mode.

   radius: A radius value.

   tolerance: A tolerance value.

   Returns: A new array of rolling ball fillet surfaces; this array can be empty on failure.

  CreateRollingBallFillet(surfaceA: Surface,surfaceB: Surface,radius: float,tolerance: float) -> Array[Surface]

  

   Constructs a rolling ball fillet between two surfaces.

  

   surfaceA: A first surface.

   surfaceB: A second surface.

   radius: A radius value.

   tolerance: A tolerance value.

   Returns: A new array of rolling ball fillet surfaces; this array can be empty on failure.
  """
  pass
 def CurvatureAt(self,u,v):
  """
  CurvatureAt(self: Surface,u: float,v: float) -> SurfaceCurvature

  

   Computes the curvature at the given UV coordinate.

  

   u: U parameter for evaluation.

   v: V parameter for evaluation.

   Returns: Surface Curvature data for the point at uv or null on failure.
  """
  pass
 def Degree(self,direction):
  """
  Degree(self: Surface,direction: int) -> int

  

   Returns the maximum algebraic degree of any span

     (or a good estimate if curve spans 

    are not algebraic).

  

  

   direction: 0 gets first parameter's domain,1 gets second parameter's domain.

   Returns: The maximum degree.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: CommonObject,disposing: bool)

   For derived class implementers.

     This method is called with argument true when class 

    user calls Dispose(),while with argument false when

     the Garbage Collector invokes 

    the finalizer,or Finalize() method.You must reclaim all used unmanaged resources in both cases,

    and can use this chance to call Dispose on disposable fields if the argument is true.Also,you 

    must call the base virtual method within your overriding method.

  

  

   disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 

    finalizer.
  """
  pass
 def Domain(self,direction):
  """
  Domain(self: Surface,direction: int) -> Interval

  

   Gets the domain in a direction.

  

   direction: 0 gets first parameter,1 gets second parameter.

   Returns: An interval value.
  """
  pass
 def Evaluate(self,u,v,numberDerivatives,point,derivatives):
  """
  Evaluate(self: Surface,u: float,v: float,numberDerivatives: int) -> (bool,Point3d,Array[Vector3d])

  

   Evaluates a surface mathematically.

  

   u: A U parameter.

   v: A V parameter.

   numberDerivatives: The number of derivatives.

   Returns: true if the operation succeeded; false otherwise.
  """
  pass
 def Extend(self,edge,extensionLength,smooth):
  """
  Extend(self: Surface,edge: IsoStatus,extensionLength: float,smooth: bool) -> Surface

  

   Extends an untrimmed surface along one edge.

  

   edge: Edge to extend.  Must be North,South,East,or West.

   extensionLength: distance to extend.

   smooth: true for smooth (C-infinity) extension. 

     false for a C1- ruled extension.

   Returns: New extended surface on success.
  """
  pass
 def Fit(self,uDegree,vDegree,fitTolerance):
  """
  Fit(self: Surface,uDegree: int,vDegree: int,fitTolerance: float) -> Surface

  

   Fits a new surface through an existing surface.

  

   uDegree: the output surface U degree. Must be bigger than 1.

   vDegree: the output surface V degree. Must be bigger than 1.

   fitTolerance: The fitting tolerance.

   Returns: A surface,or null on error.
  """
  pass
 def FrameAt(self,u,v,frame):
  """
  FrameAt(self: Surface,u: float,v: float) -> (bool,Plane)

  

   Computes the orient plane on a surface given a U and V parameter.

     This is the 

    simple evaluation call with no error handling.

  

  

   u: A first parameter.

   v: A second parameter.

   Returns: true if this operation succeeded; otherwise false.
  """
  pass
 def GetNextDiscontinuity(self,direction,continuityType,t0,t1,t):
  """
  GetNextDiscontinuity(self: Surface,direction: int,continuityType: Continuity,t0: float,t1: float) -> (bool,float)

  

   Searches for a derivative,tangent,or curvature discontinuity.

  

   direction: If 0,then "u" parameter is checked. If 1,then the "v" parameter is checked.

   continuityType: The desired continuity.

   t0: Search begins at t0. If there is a discontinuity at t0,it will be ignored. 

     This 

    makes it possible to repeatedly call GetNextDiscontinuity and step through the discontinuities.

  

   t1: (t0 != t1) If there is a discontinuity at t1 is will be ingored unless c is a locus 

    discontinuity

     type and t1 is at the start or end of the curve.

  

   Returns: Parametric continuity tests c=(C0_continuous,...,G2_continuous):

     TRUE if a 

    parametric discontinuity was found strictly between t0 and t1.

     Note well that all 

    curves are parametrically continuous at the ends of their domains.

     

     

    Locus continuity tests c=(C0_locus_continuous,...,G2_locus_continuous):

     TRUE if 

    a locus discontinuity was found strictly between t0 and t1 or at t1 is the

     at the 

    end of a curve. Note well that all open curves (IsClosed()=false) are locus

     

    discontinuous at the ends of their domains.  All closed curves (IsClosed()=true) are

       

     at least C0_locus_continuous at the ends of their domains.
  """
  pass
 def GetSpanVector(self,direction):
  """
  GetSpanVector(self: Surface,direction: int) -> Array[float]

  

   Gets array of span "knots".

  

   direction: 0 gets first parameter's domain,1 gets second parameter's domain.

   Returns: An array with span vectors; or null on error.
  """
  pass
 def GetSurfaceSize(self,width,height):
  """
  GetSurfaceSize(self: Surface) -> (bool,float,float)

  

   Gets an estimate of the size of the rectangle that would be created

     if the 3d 

    surface where flattened into a rectangle.

  

   Returns: true if successful.
  """
  pass
 def HasNurbsForm(self):
  """
  HasNurbsForm(self: Surface) -> int

  

   Is there a NURBS surface representation of this surface.

   Returns: 0 unable to create NURBS representation with desired accuracy.

     1 success - NURBS 

    parameterization matches the surface's

     2 success - NURBS point locus matches the 

    surface's and the

     domain of the NURBS surface is correct. However,This surface's

   

      parameterization and the NURBS surface parameterization may not

     match.  

    This situation happens when getting NURBS representations

     of surfaces that have a 

    transendental parameterization like spheres,

     cylinders,and cones.
  """
  pass
 def InterpolatedCurveOnSurface(self,points,tolerance):
  """ InterpolatedCurveOnSurface(self: Surface,points: IEnumerable[Point3d],tolerance: float) -> NurbsCurve """
  pass
 def InterpolatedCurveOnSurfaceUV(self,points,tolerance):
  """ InterpolatedCurveOnSurfaceUV(self: Surface,points: IEnumerable[Point2d],tolerance: float) -> NurbsCurve """
  pass
 def IsAtSeam(self,u,v):
  """
  IsAtSeam(self: Surface,u: float,v: float) -> int

  

   Tests if a surface parameter value is at a seam.

  

   u: Surface u parameter to test.

   v: Surface v parameter to test.

   Returns: 0 if not a seam,

     1 if u == Domain(0)[i] and srf(u,v) == srf(Domain(0)[1-i],v)

     

       2 if v == Domain(1)[i] and srf(u,v) == srf(u,Domain(1)[1-i])

     3 if 1 and 

    2 are true.
  """
  pass
 def IsAtSingularity(self,u,v,exact):
  """
  IsAtSingularity(self: Surface,u: float,v: float,exact: bool) -> bool

  

   Tests if a surface parameter value is at a singularity.

  

   u: Surface u parameter to test.

   v: Surface v parameter to test.

   exact: If true,test if (u,v) is exactly at a singularity.

     If false,test if close enough 

    to cause numerical problems.

  

   Returns: true if surface is singular at (s,t)
  """
  pass
 def IsClosed(self,direction):
  """
  IsClosed(self: Surface,direction: int) -> bool

  

   Gets a value indicating if the surface is closed in a direction.

  

   direction: 0=U,1=V.

   Returns: The indicating boolean value.
  """
  pass
 def IsCone(self,tolerance=None):
  """
  IsCone(self: Surface,tolerance: float) -> bool

  

   Determines if the surface is a portion of a cone within a given tolerance.

  

   tolerance: tolerance to use when checking.

   Returns: true if the surface is a portion of a cone.

  IsCone(self: Surface) -> bool

  

   Determines if the surface is a portion of a cone within RhinoMath.ZeroTolerance.

   Returns: true if the surface is a portion of a cone.
  """
  pass
 def IsContinuous(self,continuityType,u,v):
  """
  IsContinuous(self: Surface,continuityType: Continuity,u: float,v: float) -> bool

  

   Tests continuity at a surface parameter value.

  

   continuityType: The continuity type to sample.

   u: Surface u parameter to test.

   v: Surface v parameter to test.

   Returns: true if the surface has at least the specified continuity at the (u,v) parameter.
  """
  pass
 def IsCylinder(self,tolerance=None):
  """
  IsCylinder(self: Surface,tolerance: float) -> bool

  

   Determines if the surface is a portion of a cylinder within a given tolerance.

  

   tolerance: tolerance to use when checking.

   Returns: true if the surface is a portion of a cylinder.

  IsCylinder(self: Surface) -> bool

  

   Determines if the surface is a portion of a cylinder within RhinoMath.ZeroTolerance.

   Returns: true if the surface is a portion of a cylinder.
  """
  pass
 def IsIsoparametric(self,*__args):
  """
  IsIsoparametric(self: Surface,bbox: BoundingBox) -> IsoStatus

  

   Determines if a 2d bounding box is iso-parameteric in the parameter space of this surface.

  

   bbox: Bounding box to test.

   Returns: IsoStatus flag describing the iso-parametric relationship between the surface and the bounding 

    box.

  

  IsIsoparametric(self: Surface,curve: Curve) -> IsoStatus

  

   Determines if a 2d curve is iso-parameteric in the parameter space of this surface.

  

   curve: Curve to test.

   Returns: IsoStatus flag describing the iso-parametric relationship between the surface and the curve.

  IsIsoparametric(self: Surface,curve: Curve,curveDomain: Interval) -> IsoStatus

  

   Determines if a 2D curve is iso-parameteric in the parameter space of this surface.

  

   curve: Curve to test.

   curveDomain: Sub domain of the curve.

   Returns: IsoStatus flag describing the iso-parametric relationship between the surface and the curve.
  """
  pass
 def IsoCurve(self,direction,constantParameter):
  """
  IsoCurve(self: Surface,direction: int,constantParameter: float) -> Curve

  

   Gets isoparametric curve.

  

   direction: 0 first parameter varies and second parameter is constant

     e.g.,point on 

    IsoCurve(0,c) at t is srf(t,c)

     This is a horizontal line from left to right

      

      

     1 first parameter is constant and second parameter varies

     e.g.,

    point on IsoCurve(1,c) at t is srf(c,t

     This is a vertical line from bottom to top.

  

   constantParameter: The parameter that was constant on the original surface.

   Returns: An isoparametric curve or null on error.
  """
  pass
 def IsPeriodic(self,direction):
  """
  IsPeriodic(self: Surface,direction: int) -> bool

  

   Gets a value indicating if thr surface is periodic in a direction (default is false).

  

   direction: 0=U,1=V.

   Returns: The indicating boolean value.
  """
  pass
 def IsPlanar(self,tolerance=None):
  """
  IsPlanar(self: Surface,tolerance: float) -> bool

  

   Tests a surface to see if it is planar to a given tolerance.

  

   tolerance: tolerance to use when checking.

   Returns: true if there is a plane such that the maximum distance from

     the surface to the 

    plane is <= tolerance.

  

  IsPlanar(self: Surface) -> bool

  

   Tests a surface to see if it is planar to zero tolerance.

   Returns: true if the surface is planar (flat) to within RhinoMath.ZeroTolerance units (1e-12).
  """
  pass
 def IsSingular(self,side):
  """
  IsSingular(self: Surface,side: int) -> bool

  

   true if surface side is collapsed to a point.

  

   side: side of parameter space to test

     0=south,1=east,2=north,3=west.

   Returns: True if this specific side of the surface is singular; otherwise,false.
  """
  pass
 def IsSphere(self,tolerance=None):
  """
  IsSphere(self: Surface,tolerance: float) -> bool

  

   Determines if the surface is a portion of a sphere within a given tolerance.

  

   tolerance: tolerance to use when checking.

   Returns: true if the surface is a portion of a sphere.

  IsSphere(self: Surface) -> bool

  

   Determines if the surface is a portion of a sphere within RhinoMath.ZeroTolerance.

   Returns: true if the surface is a portion of a sphere.
  """
  pass
 def IsTorus(self,tolerance=None):
  """
  IsTorus(self: Surface,tolerance: float) -> bool

  

   Determines if the surface is a portion of a torus within a given tolerance.

  

   tolerance: tolerance to use when checking.

   Returns: true if the surface is a portion of a torus.

  IsTorus(self: Surface) -> bool

  

   Determines if the surface is a portion of a torus within RhinoMath.ZeroTolerance.

   Returns: true if the surface is a portion of a torus.
  """
  pass
 def NonConstOperation(self,*args):
  """
  NonConstOperation(self: CommonObject)

   For derived classes implementers.

     Defines the necessary implementation to free the 

    instance from being const.
  """
  pass
 def NormalAt(self,u,v):
  """
  NormalAt(self: Surface,u: float,v: float) -> Vector3d

  

   Computes the surface normal at a point.

     This is the simple evaluation call - it 

    does not support error handling.

  

  

   u: A U parameter.

   v: A V parameter.

   Returns: The normal.
  """
  pass
 def Offset(self,distance,tolerance):
  """
  Offset(self: Surface,distance: float,tolerance: float) -> Surface

  

   Constructs a new surface which is offset from the current surface.

  

   distance: Distance (along surface normal) to offset.

   tolerance: Offset accuracy.

   Returns: The offsetted surface or null on failure.
  """
  pass
 def OnSwitchToNonConst(self,*args):
  """
  OnSwitchToNonConst(self: GeometryBase)

   Is called when a non-const operation occurs.
  """
  pass
 def PointAt(self,u,v):
  """
  PointAt(self: Surface,u: float,v: float) -> Point3d

  

   Evaluates a point at a given parameter.

  

   u: evaluation parameters.

   v: evaluation parameters.

   Returns: Point3d.Unset on failure.
  """
  pass
 def Pullback(self,curve3d,tolerance,curve3dSubdomain=None):
  """
  Pullback(self: Surface,curve3d: Curve,tolerance: float,curve3dSubdomain: Interval) -> Curve

  

   Pulls a 3d curve back to the surface's parameter space.

  

   curve3d: A curve.

   tolerance: the maximum acceptable 3d distance between from surface(curve_2d(t))

     to the locus 

    of points on the surface that are closest to curve_3d.

  

   curve3dSubdomain: A subdomain of the curve to sample.

   Returns: 2d curve.

  Pullback(self: Surface,curve3d: Curve,tolerance: float) -> Curve

  

   Pulls a 3d curve back to the surface's parameter space.

  

   curve3d: The curve to pull.

   tolerance: the maximum acceptable 3d distance between from surface(curve_2d(t))

     to the locus 

    of points on the surface that are closest to curve_3d.

  

   Returns: 2d curve.
  """
  pass
 def Pushup(self,curve2d,tolerance,curve2dSubdomain=None):
  """
  Pushup(self: Surface,curve2d: Curve,tolerance: float) -> Curve

  

   Computes a 3d curve that is the composite of a 2d curve and the surface map.

  

   curve2d: a 2d curve whose image is in the surface's domain.

   tolerance: the maximum acceptable distance from the returned 3d curve to the image of curve_2d on the 

    surface.

  

   Returns: 3d curve.

  Pushup(self: Surface,curve2d: Curve,tolerance: float,curve2dSubdomain: Interval) -> Curve

  

   Computes a 3d curve that is the composite of a 2d curve and the surface map.

  

   curve2d: a 2d curve whose image is in the surface's domain.

   tolerance: the maximum acceptable distance from the returned 3d curve to the image of curve_2d on the 

    surface.

  

   curve2dSubdomain: The curve interval (a sub-domain of the original curve) to use.

   Returns: 3d curve.
  """
  pass
 def Rebuild(self,uDegree,vDegree,uPointCount,vPointCount):
  """
  Rebuild(self: Surface,uDegree: int,vDegree: int,uPointCount: int,vPointCount: int) -> NurbsSurface

  

   Rebuilds an existing surface to a given degree and point count.

  

   uDegree: the output surface u degree.

   vDegree: the output surface u degree.

   uPointCount: The number of points in the output surface u direction. Must be bigger

     than uDegree 

    (maximum value is 1000)

  

   vPointCount: The number of points in the output surface v direction. Must be bigger

     than vDegree 

    (maximum value is 1000)

  

   Returns: new rebuilt surface on success. null on failure.
  """
  pass
 def Reverse(self,direction,inPlace=None):
  """
  Reverse(self: Surface,direction: int,inPlace: bool) -> Surface

  

   Same as Reverse,but if inPlace is set to true this Surface is modified

     instead of 

    a new copy being created.

  

  

   direction: 0 for first parameter's domain,1 for second parameter's domain.

   Returns: If inPlace is False,a new reversed surface on success. If inPlace is

     true,this 

    surface instance is returned on success.

  

  Reverse(self: Surface,direction: int) -> Surface

  

   Reverses parameterization Domain changes from [a,b] to [-b,-a]

  

   direction: 0 for first parameter's domain,1 for second parameter's domain.

   Returns: a new reversed surface on success.
  """
  pass
 def SetDomain(self,direction,domain):
  """
  SetDomain(self: Surface,direction: int,domain: Interval) -> bool

  

   Sets the domain in a direction.

  

   direction: 0 sets first parameter's domain,1 sets second parameter's domain.

   domain: A new domain to be assigned.

   Returns: true if setting succeeded,otherwise false.
  """
  pass
 def ShortPath(self,start,end,tolerance):
  """
  ShortPath(self: Surface,start: Point2d,end: Point2d,tolerance: float) -> Curve

  

   Constructs a geodesic between 2 points,used by ShortPath command in Rhino.

  

   start: start point of curve in parameter space. Points must be distinct in the domain of thie surface.

   end: end point of curve in parameter space. Points must be distinct in the domain of thie surface.

   tolerance: tolerance used in fitting discrete solution.

   Returns: a geodesic curve on the surface on success. null on failure.
  """
  pass
 def SpanCount(self,direction):
  """
  SpanCount(self: Surface,direction: int) -> int

  

   Gets number of smooth nonempty spans in the parameter direction.

  

   direction: 0 gets first parameter's domain,1 gets second parameter's domain.

   Returns: The span count.
  """
  pass
 def Split(self,direction,parameter):
  """
  Split(self: Surface,direction: int,parameter: float) -> Array[Surface]

  

   Splits (divides) the surface into two parts at the specified parameter

  

   direction: 0=The surface is split vertically. The "west" side is returned as the first

     

    surface in the array and the "east" side is returned as the second surface in

     the 

    array.

     1=The surface is split horizontally. The "south" side is returned as the 

    first surface in the array and the "north"

     side is returned as the second surfae in 

    the array

  

   parameter: value of constant parameter in interval returned by Domain(direction)

   Returns: Array of two surfaces on success
  """
  pass
 def ToBrep(self):
  """
  ToBrep(self: Surface) -> Brep

  

   Converts the surface into a Brep.

   Returns: A Brep with a similar shape like this surface or null.
  """
  pass
 def ToNurbsSurface(self,tolerance=None,accuracy=None):
  """
  ToNurbsSurface(self: Surface,tolerance: float) -> (NurbsSurface,int)

  

   Gets a NURBS surface representation of this surface.

  

   tolerance: tolerance to use when creating NURBS representation.

   Returns: NurbsSurface on success,null on failure.

  ToNurbsSurface(self: Surface) -> NurbsSurface

  

   Gets a NURBS surface representation of this surface. Default 

     tolerance of 0.0 is 

    used.

  

   Returns: NurbsSurface on success,null on failure.
  """
  pass
 def Transpose(self,inPlace=None):
  """
  Transpose(self: Surface,inPlace: bool) -> Surface

  

   Transposes surface parameterization (swap U and V)

   Returns: New transposed surface on success,null on failure.

  Transpose(self: Surface) -> Surface

  

   Transposes surface parameterization (swap U and V)

   Returns: New transposed surface on success,null on failure.
  """
  pass
 def Trim(self,u,v):
  """
  Trim(self: Surface,u: Interval,v: Interval) -> Surface

  

   Constructs a sub-surface that covers the specified UV trimming domain.

  

   u: Domain of surface along U direction to include in the subsurface.

   v: Domain of surface along V direction to include in the subsurface.

   Returns: SubSurface on success,null on failure.
  """
  pass
 def TryGetCone(self,cone,tolerance=None):
  """
  TryGetCone(self: Surface,tolerance: float) -> (bool,Cone)

  

   Tests a surface to see if it is a portion of a cone and returns the cone.

  

   tolerance: tolerance to use when checking.

   Returns: true if the surface is a portion of a cone.

  TryGetCone(self: Surface) -> (bool,Cone)

  

   Tests a surface to see if it is a portion of a cone within RhinoMath.ZeroTolerance and return 

    the cone.

  

   Returns: true if the surface is a portion of a cone.
  """
  pass
 def TryGetCylinder(self,cylinder,tolerance=None):
  """
  TryGetCylinder(self: Surface,tolerance: float) -> (bool,Cylinder)

  

   Tests a surface to see if it is a portion of a cylinder and return the cylinder.

  

   tolerance: tolerance to use when checking.

   Returns: true if the surface is a portion of a cylinder.

  TryGetCylinder(self: Surface) -> (bool,Cylinder)

  

   Tests a surface to see if it is a portion of a cylinder within RhinoMath.ZeroTolerance and 

    return the cylinder.

  

   Returns: true if the surface is a portion of a cylinder.
  """
  pass
 def TryGetPlane(self,plane,tolerance=None):
  """
  TryGetPlane(self: Surface,tolerance: float) -> (bool,Plane)

  

   Tests a surface for planarity and return the plane.

  

   tolerance: tolerance to use when checking.

   Returns: true if there is a plane such that the maximum distance from the surface to the plane is <= 

    tolerance.

  

  TryGetPlane(self: Surface) -> (bool,Plane)

  

   Tests a surface for planarity and return the plane.

   Returns: true if there is a plane such that the maximum distance from the surface to the plane is <= 

    RhinoMath.ZeroTolerance.
  """
  pass
 def TryGetSphere(self,sphere,tolerance=None):
  """
  TryGetSphere(self: Surface,tolerance: float) -> (bool,Sphere)

  

   Test a surface to see if it is a portion of a sphere and return the sphere.

  

   tolerance: tolerance to use when checking.

   Returns: true if the surface is a portion of a sphere.

  TryGetSphere(self: Surface) -> (bool,Sphere)

  

   Test a surface to see if it is a portion of a sphere and return the sphere.

   Returns: true if the surface is a portion of a sphere.
  """
  pass
 def TryGetTorus(self,torus,tolerance=None):
  """
  TryGetTorus(self: Surface,tolerance: float) -> (bool,Torus)

  

   Tests a surface to see if it is a portion of a torus and returns the torus.

  

   tolerance: tolerance to use when checking.

   Returns: true if the surface is a portion of a torus.

  TryGetTorus(self: Surface) -> (bool,Torus)

  

   Tests a surface to see if it is a portion of a torus within RhinoMath.ZeroTolerance and returns 

    the torus.

  

   Returns: true if the surface is a portion of a torus.
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
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 IsSolid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a values indicating whether a surface is solid.



Get: IsSolid(self: Surface) -> bool



"""


