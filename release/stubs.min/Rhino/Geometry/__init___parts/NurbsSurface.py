class NurbsSurface(Surface,IDisposable,ISerializable,IEpsilonComparable[NurbsSurface]):
 """
 Represents a Non Uniform Rational B-Splines (NURBS) surface.

 

 NurbsSurface(other: NurbsSurface)
 """
 def ConstructConstObject(self,*args):
  """
  ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int)

   Assigns a parent object and a subobject index to this.

  

   parentObject: The parent object.

   subobject_index: The subobject index.
  """
  pass
 def CopyFrom(self,other):
  """
  CopyFrom(self: NurbsSurface,other: NurbsSurface)

   Copies this NURBS surface from another NURBS surface.

  

   other: The other NURBS surface to use as source.
  """
  pass
 @staticmethod
 def Create(dimension,isRational,order0,order1,controlPointCount0,controlPointCount1):
  """
  Create(dimension: int,isRational: bool,order0: int,order1: int,controlPointCount0: int,controlPointCount1: int) -> NurbsSurface

  

   Constructs a new NURBS surface with internal uninitialized arrays.

  

   dimension: The number of dimensions.>= 1. This value is usually 3.

   isRational: true to make a rational NURBS.

   order0: The order in U direction.>= 2.

   order1: The order in V direction.>= 2.

   controlPointCount0: Control point count in U direction.>= order0.

   controlPointCount1: Control point count in V direction.>= order1.

   Returns: A new NURBS surface,or null on error.
  """
  pass
 @staticmethod
 def CreateFromCone(cone):
  """
  CreateFromCone(cone: Cone) -> NurbsSurface

  

   Constructs a new NURBS surfaces from cone data.

  

   cone: A cone value.

   Returns: A new NURBS surface,or null on error.
  """
  pass
 @staticmethod
 def CreateFromCorners(corner1,corner2,corner3,corner4=None,tolerance=None):
  """
  CreateFromCorners(corner1: Point3d,corner2: Point3d,corner3: Point3d) -> NurbsSurface

  

   Makes a surface from 3 corner points.

  

   corner1: The first corner.

   corner2: The second corner.

   corner3: The third corner.

   Returns: The resulting surface or null on error.

  CreateFromCorners(corner1: Point3d,corner2: Point3d,corner3: Point3d,corner4: Point3d,tolerance: float) -> NurbsSurface

  

   Makes a surface from 4 corner points.

  

   corner1: The first corner.

   corner2: The second corner.

   corner3: The third corner.

   corner4: The fourth corner.

   tolerance: Minimum edge length without collapsing to a singularity.

   Returns: The resulting surface or null on error.

  CreateFromCorners(corner1: Point3d,corner2: Point3d,corner3: Point3d,corner4: Point3d) -> NurbsSurface

  

   Makes a surface from 4 corner points.

     This is the same as calling 

    Rhino.Geometry.NurbsSurface.CreateFromCorners(Rhino.Geometry.Point3d,Rhino.Geometry.Point3d,Rhino

    .Geometry.Point3d,Rhino.Geometry.Point3d,System.Double) with tolerance 0.

  

  

   corner1: The first corner.

   corner2: The second corner.

   corner3: The third corner.

   corner4: The fourth corner.

   Returns: the resulting surface or null on error.
  """
  pass
 @staticmethod
 def CreateFromCylinder(cylinder):
  """
  CreateFromCylinder(cylinder: Cylinder) -> NurbsSurface

  

   Constructs a new NURBS surfaces from cylinder data.

  

   cylinder: A cylinder value.

   Returns: A new NURBS surface,or null on error.
  """
  pass
 @staticmethod
 def CreateFromPoints(points,uCount,vCount,uDegree,vDegree):
  """ CreateFromPoints(points: IEnumerable[Point3d],uCount: int,vCount: int,uDegree: int,vDegree: int) -> NurbsSurface """
  pass
 @staticmethod
 def CreateFromSphere(sphere):
  """
  CreateFromSphere(sphere: Sphere) -> NurbsSurface

  

   Constructs a new NURBS surfaces from sphere data.

  

   sphere: A sphere value.

   Returns: A new NURBS surface,or null on error.
  """
  pass
 @staticmethod
 def CreateFromTorus(torus):
  """
  CreateFromTorus(torus: Torus) -> NurbsSurface

  

   Constructs a new NURBS surfaces from torus data.

  

   torus: A torus value.

   Returns: A new NURBS surface,or null on error.
  """
  pass
 @staticmethod
 def CreateNetworkSurface(*__args):
  """
  CreateNetworkSurface(curves: IEnumerable[Curve],continuity: int,edgeTolerance: float,interiorTolerance: float,angleTolerance: float) -> (NurbsSurface,int)

  CreateNetworkSurface(uCurves: IEnumerable[Curve],uContinuityStart: int,uContinuityEnd: int,vCurves: IEnumerable[Curve],vContinuityStart: int,vContinuityEnd: int,edgeTolerance: float,interiorTolerance: float,angleTolerance: float) -> (NurbsSurface,int)
  """
  pass
 @staticmethod
 def CreateRailRevolvedSurface(profile,rail,axis,scaleHeight):
  """
  CreateRailRevolvedSurface(profile: Curve,rail: Curve,axis: Line,scaleHeight: bool) -> NurbsSurface

  

   Constructs a railed Surface-of-Revolution.

  

   profile: Profile curve for revolution.

   rail: Rail curve for revolution.

   axis: Axis of revolution.

   scaleHeight: If true,surface will be locally scaled.

   Returns: A NurbsSurface or null on failure.
  """
  pass
 @staticmethod
 def CreateRuledSurface(curveA,curveB):
  """
  CreateRuledSurface(curveA: Curve,curveB: Curve) -> NurbsSurface

  

   Constructs a ruled surface between two curves. Curves must share the same knot-vector.

  

   curveA: First curve.

   curveB: Second curve.

   Returns: A ruled surface on success or null on failure.
  """
  pass
 @staticmethod
 def CreateThroughPoints(points,uCount,vCount,uDegree,vDegree,uClosed,vClosed):
  """ CreateThroughPoints(points: IEnumerable[Point3d],uCount: int,vCount: int,uDegree: int,vDegree: int,uClosed: bool,vClosed: bool) -> NurbsSurface """
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
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: NurbsSurface,other: NurbsSurface,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def IncreaseDegreeU(self,desiredDegree):
  """
  IncreaseDegreeU(self: NurbsSurface,desiredDegree: int) -> bool

  

   Increase the degree of this surface in U direction.

  

   desiredDegree: The desired degree. 

     Degrees should be number between and including 1 and 11.

   Returns: true on success,false on failure.
  """
  pass
 def IncreaseDegreeV(self,desiredDegree):
  """
  IncreaseDegreeV(self: NurbsSurface,desiredDegree: int) -> bool

  

   Increase the degree of this surface in V direction.

  

   desiredDegree: The desired degree. 

     Degrees should be number between and including 1 and 11.

   Returns: true on success,false on failure.
  """
  pass
 def MakeNonRational(self):
  """
  MakeNonRational(self: NurbsSurface) -> bool

  

   Makes this surface non-rational.

   Returns: true if the operation succeeded; otherwise,false.
  """
  pass
 def MakeRational(self):
  """
  MakeRational(self: NurbsSurface) -> bool

  

   Makes this surface rational.

   Returns: true if the operation succeeded; otherwise,false.
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
 def OnSwitchToNonConst(self,*args):
  """
  OnSwitchToNonConst(self: GeometryBase)

   Is called when a non-const operation occurs.
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
 def __new__(self,other):
  """
  __new__(cls: type,other: NurbsSurface)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 IsRational=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not the nurbs surface is rational.



Get: IsRational(self: NurbsSurface) -> bool



"""

 KnotsU=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The U direction knot vector.



Get: KnotsU(self: NurbsSurface) -> NurbsSurfaceKnotList



"""

 KnotsV=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The V direction knot vector.



Get: KnotsV(self: NurbsSurface) -> NurbsSurfaceKnotList



"""

 OrderU=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the order in the U direction.



Get: OrderU(self: NurbsSurface) -> int



"""

 OrderV=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the order in the V direction.



Get: OrderV(self: NurbsSurface) -> int



"""

 Points=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of surface control points that form this surface.



Get: Points(self: NurbsSurface) -> NurbsSurfacePointList



"""


