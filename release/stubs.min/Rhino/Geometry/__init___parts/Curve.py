class Curve(GeometryBase,IDisposable,ISerializable):
 """
 Represents a base class that is common to most RhinoCommon curve types.

    A curve represents an entity that can be all visited by providing

    a single parameter,usually called t.
 """
 def ChangeClosedCurveSeam(self,t):
  """
  ChangeClosedCurveSeam(self: Curve,t: float) -> bool

  

   If this curve is closed,then modify it so that the start/end point is at curve parameter t.

  

   t: Curve parameter of new start/end point. The returned curves domain will start at t.

   Returns: true on success,false on failure.
  """
  pass
 def ChangeDimension(self,desiredDimension):
  """
  ChangeDimension(self: Curve,desiredDimension: int) -> bool

  

   Changes the dimension of a curve.

  

   desiredDimension: The desired dimension.

   Returns: true if the curve's dimension was already desiredDimension

     or if the curve's 

    dimension was successfully changed to desiredDimension;

     otherwise false.
  """
  pass
 def ClosedCurveOrientation(self,*__args):
  """
  ClosedCurveOrientation(self: Curve,xform: Transform) -> CurveOrientation

  

   Determines the orientation (counterclockwise or clockwise) of a closed planar curve.

       

     Only works with simple (no self intersections) closed planar curves.

  

  

   xform: Transformation to map the curve to the xy plane. If the curve is parallel

     to the xy 

    plane,you may pass Identity matrix.

  

   Returns: The orientation of this curve in the world xy-plane.

  ClosedCurveOrientation(self: Curve,plane: Plane) -> CurveOrientation

  

   Determines the orientation (counterclockwise or clockwise) of a closed planar curve in a given 

    plane.

     Only works with simple (no self intersections) closed planar curves.

  

  

   plane: The plane in which to solve the orientation.

   Returns: The orientation of this curve in the given plane.

  ClosedCurveOrientation(self: Curve,upDirection: Vector3d) -> CurveOrientation

  

   Determines the orientation (counterclockwise or clockwise) of a closed planar curve in a given 

    plane.

     Only works with simple (no self intersections) closed planar curves.

  

  

   upDirection: A vector that is considered "up".

   Returns: The orientation of this curve with respect to a defined up direction.
  """
  pass
 def ClosestPoint(self,testPoint,t,maximumDistance=None):
  """
  ClosestPoint(self: Curve,testPoint: Point3d,maximumDistance: float) -> (bool,float)

  

   Finds the parameter of the point on a curve that is closest to testPoint.

     If the 

    maximumDistance parameter is > 0,then only points whose distance

     to the given 

    point is <= maximumDistance will be returned.  Using a 

     positive value of 

    maximumDistance can substantially speed up the search.

  

  

   testPoint: Point to project.

   maximumDistance: The maximum allowed distance.

     Past this distance,the search is given up and false 

    is returned.Use 0 to turn off this parameter.

  

   Returns: true on success,false on failure.

  ClosestPoint(self: Curve,testPoint: Point3d) -> (bool,float)

  

   Finds parameter of the point on a curve that is closest to testPoint.

     If the 

    maximumDistance parameter is > 0,then only points whose distance

     to the given 

    point is <= maximumDistance will be returned.  Using a 

     positive value of 

    maximumDistance can substantially speed up the search.

  

  

   testPoint: Point to search from.

   Returns: true on success,false on failure.
  """
  pass
 def ClosestPoints(self,*__args):
  """
  ClosestPoints(self: Curve,otherCurve: Curve) -> (bool,Point3d,Point3d)

  

   Gets closest points between this and another curves.

  

   otherCurve: The other curve.

   Returns: true on success; false on error.

  ClosestPoints(self: Curve,geometry: IEnumerable[GeometryBase]) -> (bool,Point3d,Point3d,int)

  ClosestPoints(self: Curve,geometry: IEnumerable[GeometryBase],maximumDistance: float) -> (bool,Point3d,Point3d,int)
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
 def Contains(self,testPoint,plane=None,tolerance=None):
  """
  Contains(self: Curve,testPoint: Point3d,plane: Plane,tolerance: float) -> PointContainment

  

   Computes the relationship between a point and a closed curve region. 

     This curve 

    must be closed or the return value will be Unset.

  

  

   testPoint: Point to test.

   plane: Plane in in which to compare point and region.

   tolerance: Tolerance to use during comparison.

   Returns: Relationship between point and curve region.

  Contains(self: Curve,testPoint: Point3d,plane: Plane) -> PointContainment

  

   Computes the relationship between a point and a closed curve region. 

     This curve 

    must be closed or the return value will be Unset.

  

  

   testPoint: Point to test.

   plane: Plane in in which to compare point and region.

   Returns: Relationship between point and curve region.

  Contains(self: Curve,testPoint: Point3d) -> PointContainment

  

   Computes the relationship between a point and a closed curve region. 

     This curve 

    must be closed or the return value will be Unset.

     Both curve and point are 

    projected to the World XY plane.

  

  

   testPoint: Point to test.

   Returns: Relationship between point and curve region.
  """
  pass
 @staticmethod
 def CreateBlendCurve(*__args):
  """
  CreateBlendCurve(curve0: Curve,t0: float,reverse0: bool,continuity0: BlendContinuity,curve1: Curve,t1: float,reverse1: bool,continuity1: BlendContinuity) -> Curve

  

   Makes a curve blend between 2 curves at the parameters specified

     with the 

    directions and continuities specified

  

  

   curve0: First curve to blend from

   t0: Parameter on first curve for blend endpoint

   reverse0: If false,the blend will go in the natural direction of the curve.

     If true,the 

    blend will go in the opposite direction to the curve

  

   continuity0: continuity for the blend at the start

   curve1: Second curve to blend from

   t1: Parameter on second curve for blend endpoint

   reverse1: If false,the blend will go in the natural direction of the curve.

     If true,the 

    blend will go in the opposite direction to the curve

  

   continuity1: continuity for the blend at the end

   Returns: the blend curve on success. null on failure

  CreateBlendCurve(curveA: Curve,curveB: Curve,continuity: BlendContinuity,bulgeA: float,bulgeB: float) -> Curve

  

   Create a Blend curve between two existing curves.

  

   curveA: Curve to blend from (blending will occur at curve end point).

   curveB: Curve to blend to (blending will occur at curve start point).

   continuity: Continuity of blend.

   bulgeA: Bulge factor at curveA end of blend. Values near 1.0 work best.

   bulgeB: Bulge factor at curveB end of blend. Values near 1.0 work best.

   Returns: A curve representing the blend between A and B or null on failure.

  CreateBlendCurve(curveA: Curve,curveB: Curve,continuity: BlendContinuity) -> Curve

  

   Create a Blend curve between two existing curves.

  

   curveA: Curve to blend from (blending will occur at curve end point).

   curveB: Curve to blend to (blending will occur at curve start point).

   continuity: Continuity of blend.

   Returns: A curve representing the blend between A and B or null on failure.
  """
  pass
 @staticmethod
 def CreateBooleanDifference(curveA,*__args):
  """
  CreateBooleanDifference(curveA: Curve,subtractors: IEnumerable[Curve]) -> Array[Curve]

  CreateBooleanDifference(curveA: Curve,curveB: Curve) -> Array[Curve]

  

   Calculates the boolean difference between two closed,planar curves. 

     Note,curves 

    must be co-planar.

  

  

   curveA: The first closed,planar curve.

   curveB: The second closed,planar curve.

   Returns: Result curves on success,empty array if no difference could be calculated.
  """
  pass
 @staticmethod
 def CreateBooleanIntersection(curveA,curveB):
  """
  CreateBooleanIntersection(curveA: Curve,curveB: Curve) -> Array[Curve]

  

   Calculates the boolean intersection of two closed,planar curves. 

     Note,curves 

    must be co-planar.

  

  

   curveA: The first closed,planar curve.

   curveB: The second closed,planar curve.

   Returns: Result curves on success,empty array if no intersection could be calculated.
  """
  pass
 @staticmethod
 def CreateBooleanUnion(curves):
  """ CreateBooleanUnion(curves: IEnumerable[Curve]) -> Array[Curve] """
  pass
 @staticmethod
 def CreateControlPointCurve(points,degree=None):
  """
  CreateControlPointCurve(points: IEnumerable[Point3d]) -> Curve

  CreateControlPointCurve(points: IEnumerable[Point3d],degree: int) -> Curve
  """
  pass
 @staticmethod
 def CreateFillet(curve0,curve1,radius,t0Base,t1Base):
  """
  CreateFillet(curve0: Curve,curve1: Curve,radius: float,t0Base: float,t1Base: float) -> Arc

  

   Computes the fillet arc for a curve filleting operation.

  

   curve0: First curve to fillet.

   curve1: Second curve to fillet.

   radius: Fillet radius.

   t0Base: Parameter on curve0 where the fillet ought to start (approximately).

   t1Base: Parameter on curve1 where the fillet ought to end (approximately).

   Returns: The fillet arc on success,or Arc.Unset on failure.
  """
  pass
 @staticmethod
 def CreateFilletCurves(curve0,point0,curve1,point1,radius,join,trim,arcExtension,tolerance,angleTolerance):
  """
  CreateFilletCurves(curve0: Curve,point0: Point3d,curve1: Curve,point1: Point3d,radius: float,join: bool,trim: bool,arcExtension: bool,tolerance: float,angleTolerance: float) -> Array[Curve]

  

   Creates a tangent arc between two curves and trims or extends the curves to the arc.

  

   curve0: The first curve to fillet.

   point0: A point on the first curve that is near the end where the fillet will

     be created.

   curve1: The second curve to fillet.

   point1: A point on the second curve that is near the end where the fillet will

     be created.

   radius: The radius of the fillet.

   join: Join the output curves.

   trim: Trim copies of the input curves to the output fillet curve.

   arcExtension: Applies when arcs are filleted but need to be extended to meet the

     fillet curve or 

    chamfer line. If true,then the arc is extended

     maintaining its validity. If false,

    then the arc is extended with a

     line segment,which is joined to the arc converting 

    it to a polycurve.

  

   tolerance: The tolerance,generally the document's absolute tolerance.

   Returns: The results of the fillet operation. The number of output curves depends

     on the 

    input curves and the values of the parameters that were used

     during the fillet 

    operation. In most cases,the output array will contain

     either one or three curves,

    although two curves can be returned if the

     radius is zero and join=false.

      

      For example,if both join and trim=true,then the output curve

     will be a 

    polycurve containing the fillet curve joined with trimmed copies

     of the input 

    curves. If join=false and trim=true,then three curves,

     the fillet curve and 

    trimmed copies of the input curves,will be returned.

     If both join and trim=

    false,then just the fillet curve is returned.
  """
  pass
 @staticmethod
 def CreateInterpolatedCurve(points,degree,knots=None,startTangent=None,endTangent=None):
  """
  CreateInterpolatedCurve(points: IEnumerable[Point3d],degree: int,knots: CurveKnotStyle,startTangent: Vector3d,endTangent: Vector3d) -> Curve

  CreateInterpolatedCurve(points: IEnumerable[Point3d],degree: int,knots: CurveKnotStyle) -> Curve

  CreateInterpolatedCurve(points: IEnumerable[Point3d],degree: int) -> Curve
  """
  pass
 @staticmethod
 def CreateMeanCurve(curveA,curveB,angleToleranceRadians=None):
  """
  CreateMeanCurve(curveA: Curve,curveB: Curve) -> Curve

  

   Constructs a mean,or average,curve from two curves.

  

   curveA: A first curve.

   curveB: A second curve.

   Returns: The average curve,or null on error.

  CreateMeanCurve(curveA: Curve,curveB: Curve,angleToleranceRadians: float) -> Curve

  

   Constructs a mean,or average,curve from two curves.

  

   curveA: A first curve.

   curveB: A second curve.

   angleToleranceRadians: The angle tolerance,in radians,used to match kinks between curves.

     If you are 

    unsure how to set this parameter,then either use the

     document's angle tolerance 

    RhinoDoc.AngleToleranceRadians,

     or the default value (RhinoMath.UnsetValue)

  

   Returns: The average curve,or null on error.
  """
  pass
 @staticmethod
 def CreateTweenCurves(curve0,curve1,numCurves):
  """
  CreateTweenCurves(curve0: Curve,curve1: Curve,numCurves: int) -> Array[Curve]

  

   Creates curves between two open or closed input curves. Uses the control points of the curves 

    for finding tween curves.

     That means the first control point of first curve is 

    matched to first control point of the second curve and so on.

     There is no matching 

    of curves direction. Caller must match input curves direction before calling the function.

  

  

   curve0: The first,or starting,curve.

   curve1: The second,or ending,curve.

   numCurves: Number of tween curves to create.

   Returns: An array of joint curves. This array can be empty.
  """
  pass
 @staticmethod
 def CreateTweenCurvesWithMatching(curve0,curve1,numCurves):
  """
  CreateTweenCurvesWithMatching(curve0: Curve,curve1: Curve,numCurves: int) -> Array[Curve]

  

   Creates curves between two open or closed input curves. Make the structure of input curves 

    compatible if needed.

     Refits the input curves to have the same structure. The 

    resulting curves are usually more complex than input unless

     input curves are 

    compatible and no refit is needed. There is no matching of curves direction.

     Caller 

    must match input curves direction before calling the function.

  

  

   curve0: The first,or starting,curve.

   curve1: The second,or ending,curve.

   numCurves: Number of tween curves to create.

   Returns: An array of joint curves. This array can be empty.
  """
  pass
 @staticmethod
 def CreateTweenCurvesWithSampling(curve0,curve1,numCurves,numSamples):
  """
  CreateTweenCurvesWithSampling(curve0: Curve,curve1: Curve,numCurves: int,numSamples: int) -> Array[Curve]

  

   Creates curves between two open or closed input curves. Use sample points method to make curves 

    compatible.

     This is how the algorithm workd: Divides the two curves into an equal 

    number of points,finds the midpoint between the 

     corresponding points on the 

    curves and interpolates the tween curve through those points. There is no matching of curves

     

       direction. Caller must match input curves direction before calling the function.

  

  

   curve0: The first,or starting,curve.

   curve1: The second,or ending,curve.

   numCurves: Number of tween curves to create.

   numSamples: Number of sample points along input curves.

   Returns: >An array of joint curves. This array can be empty.
  """
  pass
 def CurvatureAt(self,t):
  """
  CurvatureAt(self: Curve,t: float) -> Vector3d

  

   Evaluate the curvature vector at a curve parameter.

  

   t: Evaluation parameter.

   Returns: Curvature vector of the curve at the parameter t.
  """
  pass
 def DerivativeAt(self,t,derivativeCount,side=None):
  """
  DerivativeAt(self: Curve,t: float,derivativeCount: int,side: CurveEvaluationSide) -> Array[Vector3d]

  

   Evaluate the derivatives at the specified curve parameter.

  

   t: Curve parameter to evaluate.

   derivativeCount: Number of derivatives to evaluate,must be at least 0.

   side: Side of parameter to evaluate. If the parameter is at a kink,

     it makes a big 

    difference whether the evaluation is from below or above.

  

   Returns: An array of vectors that represents all the derivatives starting at zero.

  DerivativeAt(self: Curve,t: float,derivativeCount: int) -> Array[Vector3d]

  

   Evaluate the derivatives at the specified curve parameter.

  

   t: Curve parameter to evaluate.

   derivativeCount: Number of derivatives to evaluate,must be at least 0.

   Returns: An array of vectors that represents all the derivatives starting at zero.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Curve,disposing: bool)

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
 def DivideAsContour(self,contourStart,contourEnd,interval):
  """
  DivideAsContour(self: Curve,contourStart: Point3d,contourEnd: Point3d,interval: float) -> Array[Point3d]

  

   Divides this curve at fixed steps along a defined contour line.

  

   contourStart: The start of the contouring line.

   contourEnd: The end of the contouring line.

   interval: A distance to measure on the contouring axis.

   Returns: An array of points; or null on error.
  """
  pass
 def DivideByCount(self,segmentCount,includeEnds,points=None):
  """
  DivideByCount(self: Curve,segmentCount: int,includeEnds: bool) -> (Array[float],Array[Point3d])

  

   Divide the curve into a number of equal-length segments.

  

   segmentCount: Segment count. Note that the number of division points may differ from the segment count.

   includeEnds: If true,then the points at the start and end of the curve are included.

   Returns: Array containing division curve parameters on success,null on failure.

  DivideByCount(self: Curve,segmentCount: int,includeEnds: bool) -> Array[float]

  

   Divide the curve into a number of equal-length segments.

  

   segmentCount: Segment count. Note that the number of division points may differ from the segment count.

   includeEnds: If true,then the points at the start and end of the curve are included.

   Returns: List of curve parameters at the division points on success,null on failure.
  """
  pass
 def DivideByLength(self,segmentLength,includeStart,points=None):
  """
  DivideByLength(self: Curve,segmentLength: float,includeStart: bool) -> (Array[float],Array[Point3d])

  

   Divide the curve into specific length segments.

  

   segmentLength: The length of each and every segment (except potentially the last one).

   includeStart: If true,then the point at the start of the curve is included.

   Returns: Array containing division curve parameters if successful,null on failure.

  DivideByLength(self: Curve,segmentLength: float,includeStart: bool) -> Array[float]

  

   Divide the curve into specific length segments.

  

   segmentLength: The length of each and every segment (except potentially the last one).

   includeStart: If true,then the points at the start of the curve is included.

   Returns: Array containing division curve parameters if successful,null on failure.
  """
  pass
 def DivideEquidistant(self,distance):
  """
  DivideEquidistant(self: Curve,distance: float) -> Array[Point3d]

  

   Calculates 3d points on a curve where the linear distance between the points is equal.

  

   distance: The distance betwen division points.

   Returns: An array of equidistant points,or null on error.
  """
  pass
 @staticmethod
 def DoDirectionsMatch(curveA,curveB):
  """
  DoDirectionsMatch(curveA: Curve,curveB: Curve) -> bool

  

   Determines whether two curves travel more or less in the same direction.

  

   curveA: First curve to test.

   curveB: Second curve to test.

   Returns: true if both curves more or less point in the same direction,

     false if they point 

    in the opposite directions.
  """
  pass
 def Duplicate(self):
  """
  Duplicate(self: Curve) -> GeometryBase

  

   Constructs an exact duplicate of this Curve.
  """
  pass
 def DuplicateCurve(self):
  """
  DuplicateCurve(self: Curve) -> Curve

  

   Constructs an exact duplicate of this curve.

   Returns: An exact copy of this curve.
  """
  pass
 def DuplicateSegments(self):
  """
  DuplicateSegments(self: Curve) -> Array[Curve]

  

   Polylines will be exploded into line segments. ExplodeCurves will

     return the curves 

    in topological order.

  

   Returns: An array of all the segments that make up this curve.
  """
  pass
 def Extend(self,*__args):
  """
  Extend(self: Curve,side: CurveEnd,style: CurveExtensionStyle,geometry: IEnumerable[GeometryBase]) -> Curve

  Extend(self: Curve,side: CurveEnd,style: CurveExtensionStyle,endPoint: Point3d) -> Curve

  

   Extends a curve to a point.

  

   side: The end of the curve to extend.

   style: The style or type of extension to use.

   endPoint: A new end point.

   Returns: New extended curve result on success,null on failure.

  Extend(self: Curve,side: CurveEnd,length: float,style: CurveExtensionStyle) -> Curve

  

   Extends a curve by a specific length.

  

   side: Curve end to extend.

   length: Length to add to the curve end.

   style: Extension style.

   Returns: A curve with extended ends or null on failure.

  Extend(self: Curve,t0: float,t1: float) -> Curve

  

   Where possible,analytically extends curve to include the given domain. 

     This will 

    not work on closed curves. The original curve will be identical to the 

     restriction 

    of the resulting curve to the original curve domain.

  

  

   t0: Start of extension domain,if the start is not inside the 

     Domain of this curve,an 

    attempt will be made to extend the curve.

  

   t1: End of extension domain,if the end is not inside the 

     Domain of this curve,an 

    attempt will be made to extend the curve.

  

   Returns: Extended curve on success,null on failure.

  Extend(self: Curve,domain: Interval) -> Curve

  

   Where possible,analytically extends curve to include the given domain. 

     This will 

    not work on closed curves. The original curve will be identical to the 

     restriction 

    of the resulting curve to the original curve domain.

  

  

   domain: Extension domain.

   Returns: Extended curve on success,null on failure.
  """
  pass
 def ExtendByArc(self,side,geometry):
  """ ExtendByArc(self: Curve,side: CurveEnd,geometry: IEnumerable[GeometryBase]) -> Curve """
  pass
 def ExtendByLine(self,side,geometry):
  """ ExtendByLine(self: Curve,side: CurveEnd,geometry: IEnumerable[GeometryBase]) -> Curve """
  pass
 def ExtendOnSurface(self,side,*__args):
  """
  ExtendOnSurface(self: Curve,side: CurveEnd,face: BrepFace) -> Curve

  

   Extends a curve on a surface.

  

   side: The end of the curve to extend.

   face: BrepFace that contains the curve.

   Returns: New extended curve result on success,null on failure.

  ExtendOnSurface(self: Curve,side: CurveEnd,surface: Surface) -> Curve

  

   Extends a curve on a surface.

  

   side: The end of the curve to extend.

   surface: Surface that contains the curve.

   Returns: New extended curve result on success,null on failure.
  """
  pass
 def Fair(self,distanceTolerance,angleTolerance,clampStart,clampEnd,iterations):
  """
  Fair(self: Curve,distanceTolerance: float,angleTolerance: float,clampStart: int,clampEnd: int,iterations: int) -> Curve

  

   Fairs a curve object. Fair works best on degree 3 (cubic) curves. Attempts to 

     

    remove large curvature variations while limiting the geometry changes to be no 

     

    more than the specified tolerance.

  

  

   distanceTolerance: Maximum allowed distance the faired curve is allowed to deviate from the input.

   angleTolerance: (in radians) kinks with angles <= angleTolerance are smoothed out 0.05 is a good default.

   clampStart: The number of (control vertices-1) to preserve at start. 

     0=preserve start point1 

   =preserve start point and 1st derivative2=preserve start point,1st and 2nd derivative

  

   clampEnd: Same as clampStart.

   iterations: The number of iteratoins to use in adjusting the curve.

   Returns: Returns new faired Curve on success,null on failure.
  """
  pass
 def Fit(self,degree,fitTolerance,angleTolerance):
  """
  Fit(self: Curve,degree: int,fitTolerance: float,angleTolerance: float) -> Curve

  

   Fits a new curve through an existing curve.

  

   degree: The degree of the returned Curve. Must be bigger than 1.

   fitTolerance: The fitting tolerance. If fitTolerance is RhinoMath.UnsetValue or <=0.0,

     the 

    document absolute tolerance is used.

  

   angleTolerance: The kink smoothing tolerance in radians.

     If angleTolerance is 0.0,all kinks are 

    smoothedIf angleTolerance is >0.0,kinks smaller than angleTolerance are smoothedIf 

    angleTolerance is RhinoMath.UnsetValue or <0.0,the document angle tolerance is used for the 

    kink smoothing

  

   Returns: Returns a new fitted Curve if successful,null on failure.
  """
  pass
 def FrameAt(self,t,plane):
  """
  FrameAt(self: Curve,t: float) -> (bool,Plane)

  

   Returns a 3d frame at a parameter.

  

   t: Evaluation parameter.

   Returns: true on success,false on failure.
  """
  pass
 def GetCurveParameterFromNurbsFormParameter(self,nurbsParameter,curveParameter):
  """
  GetCurveParameterFromNurbsFormParameter(self: Curve,nurbsParameter: float) -> (bool,float)

  

   Convert a NURBS curve parameter to a curve parameter.

  

   nurbsParameter: Nurbs form parameter.

   Returns: true on success,false on failure.
  """
  pass
 @staticmethod
 def GetDistancesBetweenCurves(curveA,curveB,tolerance,maxDistance,maxDistanceParameterA,maxDistanceParameterB,minDistance,minDistanceParameterA,minDistanceParameterB):
  """
  GetDistancesBetweenCurves(curveA: Curve,curveB: Curve,tolerance: float) -> (bool,float,float,float,float,float,float)

  

   Computes the distances between two arbitrary curves that overlap.

  

   curveA: A curve.

   curveB: Another curve.

   tolerance: A tolerance value.

   Returns: true if the operation succeeded; otherwise false.
  """
  pass
 @staticmethod
 def GetFilletPoints(curve0,curve1,radius,t0Base,t1Base,t0,t1,filletPlane):
  """
  GetFilletPoints(curve0: Curve,curve1: Curve,radius: float,t0Base: float,t1Base: float) -> (bool,float,float,Plane)

  

   Finds points at which to cut a pair of curves so that a fillet of given radius can be inserted.

  

   curve0: First curve to fillet.

   curve1: Second curve to fillet.

   radius: Fillet radius.

   t0Base: Parameter value for base point on curve0.

   t1Base: Parameter value for base point on curve1.

   Returns: true on success,false on failure.
  """
  pass
 def GetLength(self,*__args):
  """
  GetLength(self: Curve,subdomain: Interval) -> float

  

   Get the length of a sub-section of the curve with a fractional tolerance of 1e-8.

  

   subdomain: The calculation is performed on the specified sub-domain of the curve (must be non-decreasing).

   Returns: The length of the sub-curve on success,or zero on failure.

  GetLength(self: Curve,fractionalTolerance: float,subdomain: Interval) -> float

  

   Get the length of a sub-section of the curve.

  

   fractionalTolerance: Desired fractional precision. 

     fabs(("exact" length from start to t) - 

    arc_length)/arc_length <= fractionalTolerance.

  

   subdomain: The calculation is performed on the specified sub-domain of the curve (must be non-decreasing).

   Returns: The length of the sub-curve on success,or zero on failure.

  GetLength(self: Curve) -> float

  

   Gets the length of the curve with a fractional tolerance of 1.0e-8.

   Returns: The length of the curve on success,or zero on failure.

  GetLength(self: Curve,fractionalTolerance: float) -> float

  

   Get the length of the curve.

  

   fractionalTolerance: Desired fractional precision. 

     fabs(("exact" length from start to t) - 

    arc_length)/arc_length <= fractionalTolerance.

  

   Returns: The length of the curve on success,or zero on failure.
  """
  pass
 def GetNextDiscontinuity(self,continuityType,t0,t1,t):
  """
  GetNextDiscontinuity(self: Curve,continuityType: Continuity,t0: float,t1: float) -> (bool,float)

  

   Searches for a derivative,tangent,or curvature discontinuity.

  

   continuityType: Type of continuity to search for.

   t0: Search begins at t0. If there is a discontinuity at t0,it will be ignored. This makes it

     

       possible to repeatedly call GetNextDiscontinuity() and step through the discontinuities.

  

   t1: (t0 != t1)  If there is a discontinuity at t1 it will be ignored unless continuityType is

     

       a locus discontinuity type and t1 is at the start or end of the curve.

  

   Returns: Parametric continuity tests c=(C0_continuous,...,G2_continuous):

      true if a 

    parametric discontinuity was found strictly between t0 and t1. Note well that

      all 

    curves are parametrically continuous at the ends of their domains.

     

     

    Locus continuity tests c=(C0_locus_continuous,...,G2_locus_continuous):

      true if 

    a locus discontinuity was found strictly between t0 and t1 or at t1 is the at the end

      

    of a curve. Note well that all open curves (IsClosed()=false) are locus discontinuous at the

  

        ends of their domains.  All closed curves (IsClosed()=true) are at least 

    C0_locus_continuous at 

      the ends of their domains.
  """
  pass
 def GetNurbsFormParameterFromCurveParameter(self,curveParameter,nurbsParameter):
  """
  GetNurbsFormParameterFromCurveParameter(self: Curve,curveParameter: float) -> (bool,float)

  

   Convert a curve parameter to a NURBS curve parameter.

  

   curveParameter: Curve parameter.

   Returns: true on success,false on failure.
  """
  pass
 def GetPerpendicularFrames(self,parameters):
  """ GetPerpendicularFrames(self: Curve,parameters: IEnumerable[float]) -> Array[Plane] """
  pass
 def HasNurbsForm(self):
  """
  HasNurbsForm(self: Curve) -> int

  

   Does a NURBS curve representation of this curve exist?

   Returns: 0   unable to create NURBS representation with desired accuracy.

     1   success - 

    NURBS parameterization matches the curve's to the desired accuracy

     2   success - 

    NURBS point locus matches the curve's and the domain of the NURBS

          

    curve is correct. However,This curve's parameterization and the

          

    NURBS curve parameterization may not match. This situation happens

          

    when getting NURBS representations of curves that have a

          

    transendental parameterization like circles.
  """
  pass
 def IsArc(self,tolerance=None):
  """
  IsArc(self: Curve,tolerance: float) -> bool

  

   Test a curve to see if it can be represented by an arc or circle within the given tolerance.

  

   tolerance: Tolerance to use when checking.

   Returns: true if the curve can be represented by an arc or a circle within tolerance.

  IsArc(self: Curve) -> bool

  

   Test a curve to see if it can be represented by an arc or circle within RhinoMath.ZeroTolerance.

   Returns: true if the curve can be represented by an arc or a circle within tolerance.
  """
  pass
 def IsCircle(self,tolerance=None):
  """
  IsCircle(self: Curve,tolerance: float) -> bool

  

   Test a curve to see if it can be represented by a circle within the given tolerance.

  

   tolerance: Tolerance to use when checking.

   Returns: true if the curve can be represented by a circle to within tolerance.

  IsCircle(self: Curve) -> bool

  

   Test a curve to see if it can be represented by a circle within RhinoMath.ZeroTolerance.

   Returns: true if the Curve can be represented by a circle within tolerance.
  """
  pass
 def IsClosable(self,tolerance,minimumAbsoluteSize=None,minimumRelativeSize=None):
  """
  IsClosable(self: Curve,tolerance: float) -> bool

  

   Decide if it makes sense to close off this curve by moving the endpoint 

     to the 

    start based on start-end gap size and length of curve as 

     approximated by chord 

    defined by 6 points.

  

  

   tolerance: Maximum allowable distance between start and end. 

     If start - end gap is greater 

    than tolerance,this function will return false.

  

   Returns: true if start and end points are close enough based on above conditions.

  IsClosable(self: Curve,tolerance: float,minimumAbsoluteSize: float,minimumRelativeSize: float) -> bool

  

   Decide if it makes sense to close off this curve by moving the endpoint

     to the 

    start based on start-end gap size and length of curve as

     approximated by chord 

    defined by 6 points.

  

  

   tolerance: Maximum allowable distance between start and end. 

     If start - end gap is greater 

    than tolerance,this function will return false.

  

   minimumAbsoluteSize: If greater than 0.0 and none of the interior sampled points are at

     least 

    minimumAbsoluteSize from start,this function will return false.

  

   minimumRelativeSize: If greater than 1.0 and chord length is less than 

     minimumRelativeSize*gap,this 

    function will return false.

  

   Returns: true if start and end points are close enough based on above conditions.
  """
  pass
 def IsContinuous(self,continuityType,t):
  """
  IsContinuous(self: Curve,continuityType: Continuity,t: float) -> bool

  

   Test continuity at a curve parameter value.

  

   continuityType: Type of continuity to test for.

   t: Parameter to test.

   Returns: true if the curve has at least the c type continuity at the parameter t.
  """
  pass
 def IsEllipse(self,tolerance=None):
  """
  IsEllipse(self: Curve,tolerance: float) -> bool

  

   Test a curve to see if it can be represented by an ellipse within a given tolerance.

  

   tolerance: Tolerance to use for checking.

   Returns: true if the Curve can be represented by an ellipse within tolerance.

  IsEllipse(self: Curve) -> bool

  

   Test a curve to see if it can be represented by an ellipse within RhinoMath.ZeroTolerance.

   Returns: true if the Curve can be represented by an ellipse within tolerance.
  """
  pass
 def IsInPlane(self,testPlane,tolerance=None):
  """
  IsInPlane(self: Curve,testPlane: Plane,tolerance: float) -> bool

  

   Test a curve to see if it lies in a specific plane.

  

   testPlane: Plane to test for.

   tolerance: Tolerance to use when checking.

   Returns: true if the maximum distance from the curve to the testPlane is <= tolerance.

  IsInPlane(self: Curve,testPlane: Plane) -> bool

  

   Test a curve to see if it lies in a specific plane.

  

   testPlane: Plane to test for.

   Returns: true if the maximum distance from the curve to the testPlane is <= RhinoMath.ZeroTolerance.
  """
  pass
 def IsLinear(self,tolerance=None):
  """
  IsLinear(self: Curve,tolerance: float) -> bool

  

   Test a curve to see if it is linear to within the custom tolerance.

  

   tolerance: Tolerance to use when checking linearity.

   Returns: true if the ends of the curve are farther than tolerance apart

     and the maximum 

    distance from any point on the curve to

     the line segment connecting the curve ends 

    is <= tolerance.

  

  IsLinear(self: Curve) -> bool

  

   Test a curve to see if it is linear to within RhinoMath.ZeroTolerance units (1e-12).

   Returns: true if the curve is linear.
  """
  pass
 def IsPlanar(self,tolerance=None):
  """
  IsPlanar(self: Curve,tolerance: float) -> bool

  

   Test a curve for planarity.

  

   tolerance: Tolerance to use when checking.

   Returns: true if there is a plane such that the maximum distance from the curve to the plane is <= 

    tolerance.

  

  IsPlanar(self: Curve) -> bool

  

   Test a curve for planarity.

   Returns: true if the curve is planar (flat) to within RhinoMath.ZeroTolerance units (1e-12).
  """
  pass
 def IsPolyline(self):
  """
  IsPolyline(self: Curve) -> bool

  

   Several types of Curve can have the form of a polyline

     including a degree 1 

    NurbsCurve,a PolylineCurve,

     and a PolyCurve all of whose segments are some form of


    
     polyline. IsPolyline tests a curve to see if it can be

     represented as 

    a polyline.

  

   Returns: true if this curve can be represented as a polyline; otherwise,false.
  """
  pass
 def IsShort(self,tolerance,subdomain=None):
  """
  IsShort(self: Curve,tolerance: float,subdomain: Interval) -> bool

  

   Used to quickly find short curves.

  

   tolerance: Length threshold value for "shortness".

   subdomain: The test is performed on the interval that is the intersection of subdomain with Domain()

   Returns: true if the length of the curve is <= tolerance.

  IsShort(self: Curve,tolerance: float) -> bool

  

   Used to quickly find short curves.

  

   tolerance: Length threshold value for "shortness".

   Returns: true if the length of the curve is <= tolerance.
  """
  pass
 @staticmethod
 def JoinCurves(inputCurves,joinTolerance=None,preserveDirection=None):
  """
  JoinCurves(inputCurves: IEnumerable[Curve],joinTolerance: float,preserveDirection: bool) -> Array[Curve]

  JoinCurves(inputCurves: IEnumerable[Curve],joinTolerance: float) -> Array[Curve]

  JoinCurves(inputCurves: IEnumerable[Curve]) -> Array[Curve]
  """
  pass
 def LengthParameter(self,segmentLength,t,*__args):
  """
  LengthParameter(self: Curve,segmentLength: float,subdomain: Interval) -> (bool,float)

  

   Gets the parameter along the curve which coincides with a given length along the curve. 

      

      A fractional tolerance of 1e-8 is used in this version of the function.

  

  

   segmentLength: Length of segment to measure. Must be less than or equal to the length of the subdomain.

   subdomain: The calculation is performed on the specified sub-domain of the curve rather than the whole 

    curve.

  

   Returns: true on success,false on failure.

  LengthParameter(self: Curve,segmentLength: float,fractionalTolerance: float,subdomain: Interval) -> (bool,float)

  

   Gets the parameter along the curve which coincides with a given length along the curve.

  

   segmentLength: Length of segment to measure. Must be less than or equal to the length of the subdomain.

   fractionalTolerance: Desired fractional precision. 

     fabs(("exact" length from start to t) - 

    arc_length)/arc_length <= fractionalTolerance.

  

   subdomain: The calculation is performed on the specified sub-domain of the curve rather than the whole 

    curve.

  

   Returns: true on success,false on failure.

  LengthParameter(self: Curve,segmentLength: float) -> (bool,float)

  

   Gets the parameter along the curve which coincides with a given length along the curve. 

      

      A fractional tolerance of 1e-8 is used in this version of the function.

  

  

   segmentLength: Length of segment to measure. Must be less than or equal to the length of the curve.

   Returns: true on success,false on failure.

  LengthParameter(self: Curve,segmentLength: float,fractionalTolerance: float) -> (bool,float)

  

   Gets the parameter along the curve which coincides with a given length along the curve.

  

   segmentLength: Length of segment to measure. Must be less than or equal to the length of the curve.

   fractionalTolerance: Desired fractional precision.

     fabs(("exact" length from start to t) - 

    arc_length)/arc_length <= fractionalTolerance.

  

   Returns: true on success,false on failure.
  """
  pass
 def MakeClosed(self,tolerance):
  """
  MakeClosed(self: Curve,tolerance: float) -> bool

  

   If IsClosed,just return true. Otherwise,decide if curve can be closed as 

     

    follows: Linear curves polylinear curves with 2 segments,Nurbs with 3 or less 

     

    control points cannot be made closed. Also,if tolerance > 0 and the gap between 

     

    start and end is larger than tolerance,curve cannot be made closed. 

     Adjust the 

    curve's endpoint to match its start point.

  

  

   tolerance: If nonzero,and the gap is more than tolerance,curve cannot be made closed.

   Returns: true on success,false on failure.
  """
  pass
 @staticmethod
 def MakeEndsMeet(curveA,adjustStartCurveA,curveB,adjustStartCurveB):
  """
  MakeEndsMeet(curveA: Curve,adjustStartCurveA: bool,curveB: Curve,adjustStartCurveB: bool) -> bool

  

   Makes adjustments to the ends of one or both input curves so that they meet at a point.

  

   curveA: 1st curve to adjust.

   adjustStartCurveA: Which end of the 1st curve to adjust: true is start,false is end.

   curveB: 2nd curve to adjust.

   adjustStartCurveB: which end of the 2nd curve to adjust true==start,false==end.

   Returns: true on success.
  """
  pass
 def NonConstOperation(self,*args):
  """
  NonConstOperation(self: Curve)

   For derived classes implementers.

     Defines the necessary implementation to free the 

    instance from being const.
  """
  pass
 def NormalizedLengthParameter(self,s,t,*__args):
  """
  NormalizedLengthParameter(self: Curve,s: float,subdomain: Interval) -> (bool,float)

  

   Input the parameter of the point on the curve that is a prescribed arc length from the start of 

    the curve. 

     A fractional tolerance of 1e-8 is used in this version of the function.

  

  

   s: Normalized arc length parameter. 

     E.g.,0=start of curve,1/2=midpoint of 

    curve,1=end of curve.

  

   subdomain: The calculation is performed on the specified sub-domain of the curve.

   Returns: true on success,false on failure.

  NormalizedLengthParameter(self: Curve,s: float,fractionalTolerance: float,subdomain: Interval) -> (bool,float)

  

   Input the parameter of the point on the curve that is a prescribed arc length from the start of 

    the curve.

  

  

   s: Normalized arc length parameter. 

     E.g.,0=start of curve,1/2=midpoint of 

    curve,1=end of curve.

  

   fractionalTolerance: Desired fractional precision. 

     fabs(("exact" length from start to t) - 

    arc_length)/arc_length <= fractionalTolerance.

  

   subdomain: The calculation is performed on the specified sub-domain of the curve.

   Returns: true on success,false on failure.

  NormalizedLengthParameter(self: Curve,s: float) -> (bool,float)

  

   Input the parameter of the point on the curve that is a prescribed arc length from the start of 

    the curve. 

     A fractional tolerance of 1e-8 is used in this version of the function.

  

  

   s: Normalized arc length parameter. 

     E.g.,0=start of curve,1/2=midpoint of 

    curve,1=end of curve.

  

   Returns: true on success,false on failure.

  NormalizedLengthParameter(self: Curve,s: float,fractionalTolerance: float) -> (bool,float)

  

   Input the parameter of the point on the curve that is a prescribed arc length from the start of 

    the curve.

  

  

   s: Normalized arc length parameter. 

     E.g.,0=start of curve,1/2=midpoint of 

    curve,1=end of curve.

  

   fractionalTolerance: Desired fractional precision. 

     fabs(("exact" length from start to t) - 

    arc_length)/arc_length <= fractionalTolerance.

  

   Returns: true on success,false on failure.
  """
  pass
 def NormalizedLengthParameters(self,s,absoluteTolerance,*__args):
  """
  NormalizedLengthParameters(self: Curve,s: Array[float],absoluteTolerance: float,subdomain: Interval) -> Array[float]

  

   Input the parameter of the point on the curve that is a prescribed arc length from the start of 

    the curve. 

     A fractional tolerance of 1e-8 is used in this version of the function.

  

  

   s: Array of normalized arc length parameters. 

     E.g.,0=start of curve,1/2=

    midpoint of curve,1=end of curve.

  

   absoluteTolerance: If absoluteTolerance > 0,then the difference between (s[i+1]-s[i])*curve_length 

     

    and the length of the curve segment from t[i] to t[i+1] will be <= absoluteTolerance.

  

   subdomain: The calculation is performed on the specified sub-domain of the curve. 

     A 0.0 s 

    value corresponds to subdomain->Min() and a 1.0 s value corresponds to subdomain->Max().

  

   Returns: If successful,array of curve parameters such that the length of the curve from its start to 

    t[i] is s[i]*curve_length. 

     Null on failure.

  

  NormalizedLengthParameters(self: Curve,s: Array[float],absoluteTolerance: float,fractionalTolerance: float,subdomain: Interval) -> Array[float]

  

   Input the parameter of the point on the curve that is a prescribed arc length from the start of 

    the curve.

  

  

   s: Array of normalized arc length parameters. 

     E.g.,0=start of curve,1/2=

    midpoint of curve,1=end of curve.

  

   absoluteTolerance: If absoluteTolerance > 0,then the difference between (s[i+1]-s[i])*curve_length 

     

    and the length of the curve segment from t[i] to t[i+1] will be <= absoluteTolerance.

  

   fractionalTolerance: Desired fractional precision for each segment. 

     fabs("true" length - actual 

    length)/(actual length) <= fractionalTolerance.

  

   subdomain: The calculation is performed on the specified sub-domain of the curve. 

     A 0.0 s 

    value corresponds to subdomain->Min() and a 1.0 s value corresponds to subdomain->Max().

  

   Returns: If successful,array of curve parameters such that the length of the curve from its start to 

    t[i] is s[i]*curve_length. 

     Null on failure.

  

  NormalizedLengthParameters(self: Curve,s: Array[float],absoluteTolerance: float) -> Array[float]

  

   Input the parameter of the point on the curve that is a prescribed arc length from the start of 

    the curve. 

     A fractional tolerance of 1e-8 is used in this version of the function.

  

  

   s: Array of normalized arc length parameters. 

     E.g.,0=start of curve,1/2=

    midpoint of curve,1=end of curve.

  

   absoluteTolerance: If absoluteTolerance > 0,then the difference between (s[i+1]-s[i])*curve_length 

     

    and the length of the curve segment from t[i] to t[i+1] will be <= absoluteTolerance.

  

   Returns: If successful,array of curve parameters such that the length of the curve from its start to 

    t[i] is s[i]*curve_length. 

     Null on failure.

  

  NormalizedLengthParameters(self: Curve,s: Array[float],absoluteTolerance: float,fractionalTolerance: float) -> Array[float]

  

   Input the parameter of the point on the curve that is a prescribed arc length from the start of 

    the curve.

  

  

   s: Array of normalized arc length parameters. 

     E.g.,0=start of curve,1/2=

    midpoint of curve,1=end of curve.

  

   absoluteTolerance: If absoluteTolerance > 0,then the difference between (s[i+1]-s[i])*curve_length 

     

    and the length of the curve segment from t[i] to t[i+1] will be <= absoluteTolerance.

  

   fractionalTolerance: Desired fractional precision for each segment. 

     fabs("true" length - actual 

    length)/(actual length) <= fractionalTolerance.

  

   Returns: If successful,array of curve parameters such that the length of the curve from its start to 

    t[i] is s[i]*curve_length. 

     Null on failure.
  """
  pass
 def Offset(self,*__args):
  """
  Offset(self: Curve,directionPoint: Point3d,normal: Vector3d,distance: float,tolerance: float,cornerStyle: CurveOffsetCornerStyle) -> Array[Curve]

  

   Offsets this curve. If you have a nice offset,then there will be one entry in 

     the 

    array. If the original curve had kinks or the offset curve had self 

     intersections,

    you will get multiple segments in the offset_curves[] array.

  

  

   directionPoint: A point that indicates the direction of the offset.

   normal: The normal to the offset plane.

   distance: The positive or negative distance to offset.

   tolerance: The offset or fitting tolerance.

   cornerStyle: Corner style for offset kinks.

   Returns: Offset curves on success,null on failure.

  Offset(self: Curve,plane: Plane,distance: float,tolerance: float,cornerStyle: CurveOffsetCornerStyle) -> Array[Curve]

  

   Offsets this curve. If you have a nice offset,then there will be one entry in 

     the 

    array. If the original curve had kinks or the offset curve had self 

     intersections,

    you will get multiple segments in the offset_curves[] array.

  

  

   plane: Offset solution plane.

   distance: The positive or negative distance to offset.

   tolerance: The offset or fitting tolerance.

   cornerStyle: Corner style for offset kinks.

   Returns: Offset curves on success,null on failure.
  """
  pass
 def OffsetNormalToSurface(self,surface,height):
  """
  OffsetNormalToSurface(self: Curve,surface: Surface,height: float) -> Curve

  

   Finds a curve by offsetting an existing curve normal to a surface.

     The caller is 

    responsible for ensuring that the curve lies on the input surface.

  

  

   surface: Surface from which normals are calculated.

   height: offset distance (distance from surface to result curve)

   Returns: Offset curve at distance height from the surface.  The offset curve is

     interpolated 

    through a small number of points so if the surface is irregular

     or complicated,the 

    result will not be a very accurate offset.
  """
  pass
 def OffsetOnSurface(self,*__args):
  """
  OffsetOnSurface(self: Curve,surface: Surface,distance: float,fittingTolerance: float) -> Array[Curve]

  

   Offset a curve on a surface. This curve must lie on the surface.

  

   surface: A surface on which to offset.

   distance: A distance to offset (+)left,(-)right.

   fittingTolerance: A fitting tolerance.

   Returns: Offset curves on success,or null on failure.

  OffsetOnSurface(self: Curve,surface: Surface,throughPoint: Point2d,fittingTolerance: float) -> Array[Curve]

  

   Offset a curve on a surface. This curve must lie on the surface.

     This overload 

    allows to specify a surface point at which the offset will pass.

  

  

   surface: A surface on which to offset.

   throughPoint: 2d point on the brep face to offset through.

   fittingTolerance: A fitting tolerance.

   Returns: Offset curves on success,or null on failure.

  OffsetOnSurface(self: Curve,surface: Surface,curveParameters: Array[float],offsetDistances: Array[float],fittingTolerance: float) -> Array[Curve]

  

   Offset this curve on a surface. This curve must lie on the surface.

     This overload 

    allows to specify different offsets for different curve parameters.

  

  

   surface: A surface on which to offset.

   curveParameters: Curve parameters corresponding to the offset distances.

   offsetDistances: Distances to offset (+)left,(-)right.

   fittingTolerance: A fitting tolerance.

   Returns: Offset curves on success,or null on failure.

  OffsetOnSurface(self: Curve,face: BrepFace,distance: float,fittingTolerance: float) -> Array[Curve]

  

   Offset this curve on a brep face surface. This curve must lie on the surface.

  

   face: The brep face on which to offset.

   distance: A distance to offset (+)left,(-)right.

   fittingTolerance: A fitting tolerance.

   Returns: Offset curves on success,or null on failure.

  OffsetOnSurface(self: Curve,face: BrepFace,throughPoint: Point2d,fittingTolerance: float) -> Array[Curve]

  

   Offset a curve on a brep face surface. This curve must lie on the surface.

     This 

    overload allows to specify a surface point at which the offset will pass.

  

  

   face: The brep face on which to offset.

   throughPoint: 2d point on the brep face to offset through.

   fittingTolerance: A fitting tolerance.

   Returns: Offset curves on success,or null on failure.

  OffsetOnSurface(self: Curve,face: BrepFace,curveParameters: Array[float],offsetDistances: Array[float],fittingTolerance: float) -> Array[Curve]

  

   Offset a curve on a brep face surface. This curve must lie on the surface.

     This 

    overload allows to specify different offsets for different curve parameters.

  

  

   face: The brep face on which to offset.

   curveParameters: Curve parameters corresponding to the offset distances.

   offsetDistances: distances to offset (+)left,(-)right.

   fittingTolerance: A fitting tolerance.

   Returns: Offset curves on success,or null on failure.
  """
  pass
 def OnSwitchToNonConst(self,*args):
  """
  OnSwitchToNonConst(self: GeometryBase)

   Is called when a non-const operation occurs.
  """
  pass
 def PerpendicularFrameAt(self,t,plane):
  """
  PerpendicularFrameAt(self: Curve,t: float) -> (bool,Plane)

  

   Return a 3d frame at a parameter. This is slightly different than FrameAt in

     that 

    the frame is computed in a way so there is minimal rotation from one

     frame to the 

    next.

  

  

   t: Evaluation parameter.

   Returns: true on success,false on failure.
  """
  pass
 @staticmethod
 def PlanarClosedCurveRelationship(curveA,curveB,testPlane,tolerance):
  """
  PlanarClosedCurveRelationship(curveA: Curve,curveB: Curve,testPlane: Plane,tolerance: float) -> RegionContainment

  

   Determines whether two coplanar simple closed curves are disjoint or intersect;

     

    otherwise,if the regions have a containment relationship,discovers

     which curve 

    encloses the other.

  

  

   curveA: A first curve.

   curveB: A second curve.

   testPlane: A plane.

   tolerance: A tolerance value.

   Returns: A value indicating the relationship between the first and the second curve.
  """
  pass
 @staticmethod
 def PlanarCurveCollision(curveA,curveB,testPlane,tolerance):
  """
  PlanarCurveCollision(curveA: Curve,curveB: Curve,testPlane: Plane,tolerance: float) -> bool

  

   Determines if two coplanar curves collide (intersect).

  

   curveA: A curve.

   curveB: Another curve.

   testPlane: A valid plane containing the curves.

   tolerance: A tolerance value for intersection.

   Returns: true if the curves intersect,otherwise false
  """
  pass
 def PointAt(self,t):
  """
  PointAt(self: Curve,t: float) -> Point3d

  

   Evaluates point at a curve parameter.

  

   t: Evaluation parameter.

   Returns: Point (location of curve at the parameter t).
  """
  pass
 def PointAtLength(self,length):
  """
  PointAtLength(self: Curve,length: float) -> Point3d

  

   Gets a point at a certain length along the curve. The length must be 

     non-negative 

    and less than or equal to the length of the curve. 

     Lengths will not be wrapped 

    when the curve is closed or periodic.

  

  

   length: Length along the curve between the start point and the returned point.

   Returns: Point on the curve at the specified length from the start point or Poin3d.Unset on failure.
  """
  pass
 def PointAtNormalizedLength(self,length):
  """
  PointAtNormalizedLength(self: Curve,length: float) -> Point3d

  

   Gets a point at a certain normalized length along the curve. The length must be 

     

    between or including 0.0 and 1.0,where 0.0 equals the start of the curve and 

     1.0 

    equals the end of the curve.

  

  

   length: Normalized length along the curve between the start point and the returned point.

   Returns: Point on the curve at the specified normalized length from the start point or Poin3d.Unset on 

    failure.
  """
  pass
 @staticmethod
 def ProjectToBrep(*__args):
  """
  ProjectToBrep(curves: IEnumerable[Curve],breps: IEnumerable[Brep],direction: Vector3d,tolerance: float) -> Array[Curve]

  ProjectToBrep(curves: IEnumerable[Curve],breps: IEnumerable[Brep],direction: Vector3d,tolerance: float) -> (Array[Curve],Array[int],Array[int])

  ProjectToBrep(curve: Curve,breps: IEnumerable[Brep],direction: Vector3d,tolerance: float) -> (Array[Curve],Array[int])

  ProjectToBrep(curve: Curve,brep: Brep,direction: Vector3d,tolerance: float) -> Array[Curve]

  

   Projects a Curve onto a Brep along a given direction.

  

   curve: Curve to project.

   brep: Brep to project onto.

   direction: Direction of projection.

   tolerance: Tolerance to use for projection.

   Returns: An array of projected curves or empty array if the projection set is empty.

  ProjectToBrep(curve: Curve,breps: IEnumerable[Brep],direction: Vector3d,tolerance: float) -> Array[Curve]
  """
  pass
 @staticmethod
 def ProjectToMesh(*__args):
  """
  ProjectToMesh(curves: IEnumerable[Curve],meshes: IEnumerable[Mesh],direction: Vector3d,tolerance: float) -> Array[Curve]

  ProjectToMesh(curve: Curve,meshes: IEnumerable[Mesh],direction: Vector3d,tolerance: float) -> Array[Curve]

  ProjectToMesh(curve: Curve,mesh: Mesh,direction: Vector3d,tolerance: float) -> Array[Curve]

  

   Projects a curve to a mesh using a direction and tolerance.

  

   curve: A curve.

   mesh: A mesh.

   direction: A direction vector.

   tolerance: A tolerance value.

   Returns: A curve array.
  """
  pass
 @staticmethod
 def ProjectToPlane(curve,plane):
  """
  ProjectToPlane(curve: Curve,plane: Plane) -> Curve

  

   Constructs a curve by projecting an existing curve to a plane.

  

   curve: A curve.

   plane: A plane.

   Returns: The projected curve on success; null on failure.
  """
  pass
 def PullToBrepFace(self,*__args):
  """
  PullToBrepFace(curve: Curve,face: BrepFace,tolerance: float) -> Array[Curve]

  

   Pull a curve to a BrepFace using closest point projection.

  

   curve: Curve to pull.

   face: Brepface that pulls.

   tolerance: Tolerance to use for pulling.

   Returns: An array of pulled curves,or an empty array on failure.

  PullToBrepFace(self: Curve,face: BrepFace,tolerance: float) -> Array[Curve]

  

   Pulls this curve to a brep face and returns the result of that operation.

  

   face: A brep face.

   tolerance: A tolerance value.

   Returns: An array containing the resulting curves after pulling. This array could be empty.
  """
  pass
 def PullToMesh(self,mesh,tolerance):
  """
  PullToMesh(self: Curve,mesh: Mesh,tolerance: float) -> PolylineCurve

  

   Makes a polyline approximation of the curve and gets the closest point on the mesh for each 

    point on the curve. 

     Then it "connects the points" so that you have a polyline on 

    the mesh.

  

  

   mesh: Mesh to project onto.

   tolerance: Input tolerance (RhinoDoc.ModelAbsoluteTolerance is a good default)

   Returns: A polyline curve on success,null on failure.
  """
  pass
 def Rebuild(self,pointCount,degree,preserveTangents):
  """
  Rebuild(self: Curve,pointCount: int,degree: int,preserveTangents: bool) -> NurbsCurve

  

   Rebuild a curve with a specific point count.

  

   pointCount: Number of control points in the rebuild curve.

   degree: Degree of curve. Valid values are between and including 1 and 11.

   preserveTangents: If true,the end tangents of the input curve will be preserved.

   Returns: A Nurbs curve on success or null on failure.
  """
  pass
 def RemoveShortSegments(self,tolerance):
  """
  RemoveShortSegments(self: Curve,tolerance: float) -> bool

  

   Looks for segments that are shorter than tolerance that can be removed. 

     Does not 

    change the domain,but it will change the relative parameterization.

  

  

   tolerance: Tolerance which defines "short" segments.

   Returns: true if removable short segments were found. 

     false if no removable short segments 

    were found.
  """
  pass
 def Reverse(self):
  """
  Reverse(self: Curve) -> bool

  

   Reverses the direction of the curve.

   Returns: true on success,false on failure.
  """
  pass
 def SetEndPoint(self,point):
  """
  SetEndPoint(self: Curve,point: Point3d) -> bool

  

   Forces the curve to end at a specified point. 

     Not all curve types support this 

    operation.

  

  

   point: New end point of curve.

   Returns: true on success,false on failure.
  """
  pass
 def SetStartPoint(self,point):
  """
  SetStartPoint(self: Curve,point: Point3d) -> bool

  

   Forces the curve to start at a specified point. 

     Not all curve types support this 

    operation.

  

  

   point: New start point of curve.

   Returns: true on success,false on failure.
  """
  pass
 def Simplify(self,options,distanceTolerance,angleToleranceRadians):
  """
  Simplify(self: Curve,options: CurveSimplifyOptions,distanceTolerance: float,angleToleranceRadians: float) -> Curve

  

   Returns a geometrically equivalent PolyCurve.

     The PolyCurve has the following 

    properties

     1. All the PolyCurve segments are LineCurve,PolylineCurve,ArcCurve,or 

    NurbsCurve.

     

     2. The Nurbs Curves segments do not have fully multiple 

    interior knots.

     

     3. Rational Nurbs curves do not have constant 

    weights.

     

     4. Any segment for which IsLinear() or IsArc() is true is a 

    Line,

        Polyline segment,or an Arc.

     

     5. Adjacent 

    Colinear or Cocircular segments are combined.

     

     6. Segments that meet 

    with G1-continuity have there ends tuned up so

        that they meet with G1-continuity 

    to within machine precision.

  

  

   options: Simplification options.

   distanceTolerance: A distance tolerance for the simplification.

   angleToleranceRadians: An angle tolerance for the simplification.

   Returns: New simplified curve on success,null on failure.
  """
  pass
 def SimplifyEnd(self,end,options,distanceTolerance,angleToleranceRadians):
  """
  SimplifyEnd(self: Curve,end: CurveEnd,options: CurveSimplifyOptions,distanceTolerance: float,angleToleranceRadians: float) -> Curve

  

   Same as SimplifyCurve,but simplifies only the last two segments at "side" end.

  

   end: If CurveEnd.Start the function simplifies the last two start 

     side segments,

    otherwise if CurveEnd.End the last two end side segments are simplified.

  

   options: Simplification options.

   distanceTolerance: A distance tolerance for the simplification.

   angleToleranceRadians: An angle tolerance for the simplification.

   Returns: New simplified curve on success,null on failure.
  """
  pass
 def SpanDomain(self,spanIndex):
  """
  SpanDomain(self: Curve,spanIndex: int) -> Interval

  

   Get the domain of the curve span with the given index. 

     Use the SpanCount property 

    to test how many spans there are.

  

  

   spanIndex: Index of span.

   Returns: Interval of the span with the given index.
  """
  pass
 def Split(self,*__args):
  """
  Split(self: Curve,cutter: Brep,tolerance: float) -> Array[Curve]

  

   Splits a curve into pieces using a polysurface.

  

   cutter: A cutting surface or polysurface.

   tolerance: A tolerance for computing intersections.

   Returns: An array of curves. This array can be empty.

  Split(self: Curve,cutter: Surface,tolerance: float) -> Array[Curve]

  

   Splits a curve into pieces using a surface.

  

   cutter: A cutting surface or polysurface.

   tolerance: A tolerance for computing intersections.

   Returns: An array of curves. This array can be empty.

  Split(self: Curve,t: float) -> Array[Curve]

  

   Splits (divides) the curve at the specified parameter. 

     The parameter must be in 

    the interior of the curve's domain.

  

  

   t: Parameter to split the curve at in the interval returned by Domain().

   Returns: Two curves on success,null on failure.

  Split(self: Curve,t: IEnumerable[float]) -> Array[Curve]
  """
  pass
 def TangentAt(self,t):
  """
  TangentAt(self: Curve,t: float) -> Vector3d

  

   Evaluates the unit tangent vector at a curve parameter.

  

   t: Evaluation parameter.

   Returns: Unit tangent vector of the curve at the parameter t.
  """
  pass
 def ToNurbsCurve(self,subdomain=None):
  """
  ToNurbsCurve(self: Curve) -> NurbsCurve

  

   Constructs a NURBS curve representation of this curve.

   Returns: NURBS representation of the curve on success,null on failure.

  ToNurbsCurve(self: Curve,subdomain: Interval) -> NurbsCurve

  

   Constructs a NURBS curve representation of this curve.

  

   subdomain: The NURBS representation for this portion of the curve is returned.

   Returns: NURBS representation of the curve on success,null on failure.
  """
  pass
 def ToPolyline(self,mainSegmentCount,subSegmentCount,maxAngleRadians,maxChordLengthRatio,maxAspectRatio,tolerance,minEdgeLength,maxEdgeLength,keepStartPoint,curveDomain=None):
  """
  ToPolyline(self: Curve,mainSegmentCount: int,subSegmentCount: int,maxAngleRadians: float,maxChordLengthRatio: float,maxAspectRatio: float,tolerance: float,minEdgeLength: float,maxEdgeLength: float,keepStartPoint: bool,curveDomain: Interval) -> PolylineCurve

  

   Gets a polyline approximation of a curve.

  

   mainSegmentCount: If mainSegmentCount <= 0,then both subSegmentCount and mainSegmentCount are ignored. 

     

    If mainSegmentCount > 0,then subSegmentCount must be >= 1. In this 

     case the 

    nurb will be broken into mainSegmentCount equally spaced 

     chords. If needed,each 

    of these chords can be split into as many 

     subSegmentCount sub-parts if the 

    subdivision is necessary for the 

     mesh to meet the other meshing constraints. In 

    particular,if 

     subSegmentCount=0,then the curve is broken into mainSegmentCount 

    

     pieces and no further testing is performed.

  

   subSegmentCount: An amount of subsegments.

   maxAngleRadians: ( 0 to pi ) Maximum angle (in radians) between unit tangents at 

     adjacent vertices.

   maxChordLengthRatio: Maximum permitted value of 

     (distance chord midpoint to curve) / (length of chord).

   maxAspectRatio: If maxAspectRatio < 1.0,the parameter is ignored. 

     If 1 <= maxAspectRatio < 

    sqrt(2),it is treated as if maxAspectRatio=sqrt(2). 

     This parameter controls the 

    maximum permitted value of 

     (length of longest chord) / (length of shortest chord).

  

   tolerance: If tolerance=0,the parameter is ignored. 

     This parameter controls the maximum 

    permitted value of the 

     distance from the curve to the polyline.

  

   minEdgeLength: The minimum permitted edge length.

   maxEdgeLength: If maxEdgeLength=0,the parameter 

     is ignored. This parameter controls the 

    maximum permitted edge length.

  

   keepStartPoint: If true the starting point of the curve 

     is added to the polyline. If false the 

    starting point of the curve is 

     not added to the polyline.

  

   curveDomain: This subdomain of the NURBS curve is approximated.

   Returns: PolylineCurve on success,null on error.

  ToPolyline(self: Curve,mainSegmentCount: int,subSegmentCount: int,maxAngleRadians: float,maxChordLengthRatio: float,maxAspectRatio: float,tolerance: float,minEdgeLength: float,maxEdgeLength: float,keepStartPoint: bool) -> PolylineCurve

  

   Gets a polyline approximation of a curve.

  

   mainSegmentCount: If mainSegmentCount <= 0,then both subSegmentCount and mainSegmentCount are ignored. 

     

    If mainSegmentCount > 0,then subSegmentCount must be >= 1. In this 

     case the 

    nurb will be broken into mainSegmentCount equally spaced 

     chords. If needed,each 

    of these chords can be split into as many 

     subSegmentCount sub-parts if the 

    subdivision is necessary for the 

     mesh to meet the other meshing constraints. In 

    particular,if 

     subSegmentCount=0,then the curve is broken into mainSegmentCount 

    

     pieces and no further testing is performed.

  

   subSegmentCount: An amount of subsegments.

   maxAngleRadians: ( 0 to pi ) Maximum angle (in radians) between unit tangents at 

     adjacent vertices.

   maxChordLengthRatio: Maximum permitted value of 

     (distance chord midpoint to curve) / (length of chord).

   maxAspectRatio: If maxAspectRatio < 1.0,the parameter is ignored. 

     If 1 <= maxAspectRatio < 

    sqrt(2),it is treated as if maxAspectRatio=sqrt(2). 

     This parameter controls the 

    maximum permitted value of 

     (length of longest chord) / (length of shortest chord).

  

   tolerance: If tolerance=0,the parameter is ignored. 

     This parameter controls the maximum 

    permitted value of the 

     distance from the curve to the polyline.

  

   minEdgeLength: The minimum permitted edge length.

   maxEdgeLength: If maxEdgeLength=0,the parameter 

     is ignored. This parameter controls the 

    maximum permitted edge length.

  

   keepStartPoint: If true the starting point of the curve 

     is added to the polyline. If false the 

    starting point of the curve is 

     not added to the polyline.

  

   Returns: PolylineCurve on success,null on error.
  """
  pass
 def Trim(self,*__args):
  """
  Trim(self: Curve,side: CurveEnd,length: float) -> Curve

  

   Shortens a curve by a given length

   Returns: Trimmed curve if successful,null on failure.

  Trim(self: Curve,domain: Interval) -> Curve

  

   Removes portions of the curve outside the specified interval.

  

   domain: Trimming interval. Portions of the curve before curve(domain[0])

     and after 

    curve(domain[1]) are removed.

  

   Returns: Trimmed curve if successful,null on failure.

  Trim(self: Curve,t0: float,t1: float) -> Curve

  

   Removes portions of the curve outside the specified interval.

  

   t0: Start of the trimming interval. Portions of the curve before curve(t0) are removed.

   t1: End of the trimming interval. Portions of the curve after curve(t1) are removed.

   Returns: Trimmed portion of this curve is successfull,null on failure.
  """
  pass
 def TryGetArc(self,*__args):
  """
  TryGetArc(self: Curve,plane: Plane) -> (bool,Arc)

  

   Try to convert this curve into an Arc using RhinoMath.ZeroTolerance.

  

   plane: Plane in which the comparison is performed.

   Returns: true if the curve could be converted into an arc within the given plane.

  TryGetArc(self: Curve,plane: Plane,tolerance: float) -> (bool,Arc)

  

   Try to convert this curve into an Arc using a custom tolerance.

  

   plane: Plane in which the comparison is performed.

   tolerance: Tolerance to use when checking.

   Returns: true if the curve could be converted into an arc within the given plane.

  TryGetArc(self: Curve) -> (bool,Arc)

  

   Try to convert this curve into an Arc using RhinoMath.ZeroTolerance.

   Returns: true if the curve could be converted into an arc.

  TryGetArc(self: Curve,tolerance: float) -> (bool,Arc)

  

   Try to convert this curve into an Arc using a custom tolerance.

  

   tolerance: Tolerance to use when checking.

   Returns: true if the curve could be converted into an arc.
  """
  pass
 def TryGetCircle(self,circle,tolerance=None):
  """
  TryGetCircle(self: Curve,tolerance: float) -> (bool,Circle)

  

   Try to convert this curve into a Circle using a custom tolerance.

  

   tolerance: Tolerance to use when checking.

   Returns: true if the curve could be converted into a Circle within tolerance.

  TryGetCircle(self: Curve) -> (bool,Circle)

  

   Try to convert this curve into a circle using RhinoMath.ZeroTolerance.

   Returns: true if the curve could be converted into a Circle.
  """
  pass
 def TryGetEllipse(self,*__args):
  """
  TryGetEllipse(self: Curve,plane: Plane) -> (bool,Ellipse)

  

   Try to convert this curve into an Ellipse within RhinoMath.ZeroTolerance.

  

   plane: Plane in which the comparison is performed.

   Returns: true if the curve could be converted into an Ellipse within the given plane.

  TryGetEllipse(self: Curve,plane: Plane,tolerance: float) -> (bool,Ellipse)

  

   Try to convert this curve into an Ellipse using a custom tolerance.

  

   plane: Plane in which the comparison is performed.

   tolerance: Tolerance to use when checking.

   Returns: true if the curve could be converted into an Ellipse within the given plane.

  TryGetEllipse(self: Curve) -> (bool,Ellipse)

  

   Try to convert this curve into an Ellipse within RhinoMath.ZeroTolerance.

   Returns: true if the curve could be converted into an Ellipse.

  TryGetEllipse(self: Curve,tolerance: float) -> (bool,Ellipse)

  

   Try to convert this curve into an Ellipse using a custom tolerance.

  

   tolerance: Tolerance to use when checking.

   Returns: true if the curve could be converted into an Ellipse.
  """
  pass
 def TryGetPlane(self,plane,tolerance=None):
  """
  TryGetPlane(self: Curve,tolerance: float) -> (bool,Plane)

  

   Test a curve for planarity and return the plane.

  

   tolerance: Tolerance to use when checking.

   Returns: true if there is a plane such that the maximum distance from the curve to the plane is <= 

    tolerance.

  

  TryGetPlane(self: Curve) -> (bool,Plane)

  

   Test a curve for planarity and return the plane.

   Returns: true if there is a plane such that the maximum distance from the curve to the plane is <= 

    RhinoMath.ZeroTolerance.
  """
  pass
 def TryGetPolyline(self,polyline,parameters=None):
  """
  TryGetPolyline(self: Curve) -> (bool,Polyline,Array[float])

  

   Several types of Curve can have the form of a polyline 

     including a degree 1 

    NurbsCurve,a PolylineCurve,

     and a PolyCurve all of whose segments are some form 

    of 

     polyline. IsPolyline tests a curve to see if it can be 

     

    represented as a polyline.

  

   Returns: true if this curve can be represented as a polyline; otherwise,false.

  TryGetPolyline(self: Curve) -> (bool,Polyline)

  

   Several types of Curve can have the form of a polyline 

     including a degree 1 

    NurbsCurve,a PolylineCurve,

     and a PolyCurve all of whose segments are some form 

    of 

     polyline. IsPolyline tests a curve to see if it can be 

     

    represented as a polyline.

  

   Returns: true if this curve can be represented as a polyline; otherwise,false.
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
 Degree=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the maximum algebraic degree of any span

   or a good estimate if curve spans are not algebraic.



Get: Degree(self: Curve) -> int



"""

 Dimension=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the dimension of the object.

   The dimension is typically three. For parameter space trimming

   curves the dimension is two. In rare cases the dimension can

   be one or greater than three.



Get: Dimension(self: Curve) -> int



"""

 Domain=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the domain of the curve.



Get: Domain(self: Curve) -> Interval



Set: Domain(self: Curve)=value

"""

 IsClosed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not this curve is a closed curve.



Get: IsClosed(self: Curve) -> bool



"""

 IsPeriodic=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not this curve is considered to be Periodic.



Get: IsPeriodic(self: Curve) -> bool



"""

 PointAtEnd=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Evaluates point at the end of the curve.



Get: PointAtEnd(self: Curve) -> Point3d



"""

 PointAtStart=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Evaluates point at the start of the curve.



Get: PointAtStart(self: Curve) -> Point3d



"""

 SpanCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of non-empty smooth (c-infinity) spans in the curve.



Get: SpanCount(self: Curve) -> int



"""

 TangentAtEnd=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Evaluate unit tangent vector at the end of the curve.



Get: TangentAtEnd(self: Curve) -> Vector3d



"""

 TangentAtStart=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Evaluates the unit tangent vector at the start of the curve.



Get: TangentAtStart(self: Curve) -> Vector3d



"""


