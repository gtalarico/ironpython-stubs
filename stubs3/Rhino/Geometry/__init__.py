# encoding: utf-8
# module Rhino.Geometry calls itself Geometry
# from Rhino3dmIO, Version=5.1.30000.14, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class GeometryBase(CommonObject):
    # no doc
    def ComponentIndex(self):
        """ ComponentIndex(self: GeometryBase) -> ComponentIndex """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GeometryBase) -> GeometryBase """
        pass

    def DuplicateShallow(self):
        """ DuplicateShallow(self: GeometryBase) -> GeometryBase """
        pass

    def GetBoundingBox(self, *__args):
        """
        GetBoundingBox(self: GeometryBase, plane: Plane) -> BoundingBox
        GetBoundingBox(self: GeometryBase, plane: Plane) -> (BoundingBox, Box)
        GetBoundingBox(self: GeometryBase, accurate: bool) -> BoundingBox
        GetBoundingBox(self: GeometryBase, xform: Transform) -> BoundingBox
        """
        pass

    def GetUserString(self, key):
        """ GetUserString(self: GeometryBase, key: str) -> str """
        pass

    def GetUserStrings(self):
        """ GetUserStrings(self: GeometryBase) -> NameValueCollection """
        pass

    def MakeDeformable(self):
        """ MakeDeformable(self: GeometryBase) -> bool """
        pass

    def MemoryEstimate(self):
        """ MemoryEstimate(self: GeometryBase) -> UInt32 """
        pass

    def Rotate(self, angleRadians, rotationAxis, rotationCenter):
        """ Rotate(self: GeometryBase, angleRadians: float, rotationAxis: Vector3d, rotationCenter: Point3d) -> bool """
        pass

    def Scale(self, scaleFactor):
        """ Scale(self: GeometryBase, scaleFactor: float) -> bool """
        pass

    def SetUserString(self, key, value):
        """ SetUserString(self: GeometryBase, key: str, value: str) -> bool """
        pass

    def Transform(self, xform):
        """ Transform(self: GeometryBase, xform: Transform) -> bool """
        pass

    def Translate(self, *__args):
        """
        Translate(self: GeometryBase, x: float, y: float, z: float) -> bool
        Translate(self: GeometryBase, translationVector: Vector3d) -> bool
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    HasBrepForm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasBrepForm(self: GeometryBase) -> bool

"""

    IsDeformable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDeformable(self: GeometryBase) -> bool

"""

    IsDocumentControlled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDocumentControlled(self: GeometryBase) -> bool

"""

    ObjectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectType(self: GeometryBase) -> ObjectType

"""

    UserStringCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserStringCount(self: GeometryBase) -> int

"""



class AnnotationBase(GeometryBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: AnnotationBase) -> int

Set: Index(self: AnnotationBase) = value
"""

    NumericValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumericValue(self: AnnotationBase) -> float

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: AnnotationBase) -> Plane

Set: Plane(self: AnnotationBase) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: AnnotationBase) -> str

Set: Text(self: AnnotationBase) = value
"""

    TextFormula = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextFormula(self: AnnotationBase) -> str

Set: TextFormula(self: AnnotationBase) = value
"""

    TextHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextHeight(self: AnnotationBase) -> float

Set: TextHeight(self: AnnotationBase) = value
"""



class AngularDimension(AnnotationBase):
    """ AngularDimension(arc: Arc, offset: float) """
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, arc, offset):
        """
        __new__(cls: type, arc: Arc, offset: float)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class Arc(object):
    """
    Arc(circle: Circle, angleRadians: float)
    Arc(circle: Circle, angleIntervalRadians: Interval)
    Arc(plane: Plane, radius: float, angleRadians: float)
    Arc(center: Point3d, radius: float, angleRadians: float)
    Arc(plane: Plane, center: Point3d, radius: float, angleRadians: float)
    Arc(startPoint: Point3d, pointOnInterior: Point3d, endPoint: Point3d)
    Arc(pointA: Point3d, tangentA: Vector3d, pointB: Point3d)
    """
    def BoundingBox(self):
        """ BoundingBox(self: Arc) -> BoundingBox """
        pass

    def ClosestParameter(self, testPoint):
        """ ClosestParameter(self: Arc, testPoint: Point3d) -> float """
        pass

    def ClosestPoint(self, testPoint):
        """ ClosestPoint(self: Arc, testPoint: Point3d) -> Point3d """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Arc, other: Arc, epsilon: float) -> bool """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Arc, other: Arc) -> bool
        Equals(self: Arc, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Arc) -> int """
        pass

    def PointAt(self, t):
        """ PointAt(self: Arc, t: float) -> Point3d """
        pass

    def Reverse(self):
        """ Reverse(self: Arc) """
        pass

    def TangentAt(self, t):
        """ TangentAt(self: Arc, t: float) -> Vector3d """
        pass

    def ToNurbsCurve(self):
        """ ToNurbsCurve(self: Arc) -> NurbsCurve """
        pass

    def Transform(self, xform):
        """ Transform(self: Arc, xform: Transform) -> bool """
        pass

    def Trim(self, domain):
        """ Trim(self: Arc, domain: Interval) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Arc]() -> Arc
        
        __new__(cls: type, circle: Circle, angleRadians: float)
        __new__(cls: type, circle: Circle, angleIntervalRadians: Interval)
        __new__(cls: type, plane: Plane, radius: float, angleRadians: float)
        __new__(cls: type, center: Point3d, radius: float, angleRadians: float)
        __new__(cls: type, plane: Plane, center: Point3d, radius: float, angleRadians: float)
        __new__(cls: type, startPoint: Point3d, pointOnInterior: Point3d, endPoint: Point3d)
        __new__(cls: type, pointA: Point3d, tangentA: Vector3d, pointB: Point3d)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle(self: Arc) -> float

Set: Angle(self: Arc) = value
"""

    AngleDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleDegrees(self: Arc) -> float

Set: AngleDegrees(self: Arc) = value
"""

    AngleDomain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleDomain(self: Arc) -> Interval

Set: AngleDomain(self: Arc) = value
"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Center(self: Arc) -> Point3d

Set: Center(self: Arc) = value
"""

    Circumference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Circumference(self: Arc) -> float

"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: Arc) -> float

Set: Diameter(self: Arc) = value
"""

    EndAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndAngle(self: Arc) -> float

Set: EndAngle(self: Arc) = value
"""

    EndAngleDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndAngleDegrees(self: Arc) -> float

Set: EndAngleDegrees(self: Arc) = value
"""

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: Arc) -> Point3d

"""

    IsCircle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCircle(self: Arc) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Arc) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Arc) -> float

"""

    MidPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MidPoint(self: Arc) -> Point3d

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: Arc) -> Plane

Set: Plane(self: Arc) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: Arc) -> float

Set: Radius(self: Arc) = value
"""

    StartAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartAngle(self: Arc) -> float

Set: StartAngle(self: Arc) = value
"""

    StartAngleDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartAngleDegrees(self: Arc) -> float

Set: StartAngleDegrees(self: Arc) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: Arc) -> Point3d

"""



class Curve(GeometryBase):
    # no doc
    def ChangeClosedCurveSeam(self, t):
        """ ChangeClosedCurveSeam(self: Curve, t: float) -> bool """
        pass

    def ChangeDimension(self, desiredDimension):
        """ ChangeDimension(self: Curve, desiredDimension: int) -> bool """
        pass

    def ClosedCurveOrientation(self, *__args):
        """
        ClosedCurveOrientation(self: Curve, xform: Transform) -> CurveOrientation
        ClosedCurveOrientation(self: Curve, plane: Plane) -> CurveOrientation
        ClosedCurveOrientation(self: Curve, upDirection: Vector3d) -> CurveOrientation
        """
        pass

    @staticmethod
    def CreateControlPointCurve(points, degree=None):
        """
        CreateControlPointCurve(points: IEnumerable[Point3d]) -> Curve
        CreateControlPointCurve(points: IEnumerable[Point3d], degree: int) -> Curve
        """
        pass

    def CurvatureAt(self, t):
        """ CurvatureAt(self: Curve, t: float) -> Vector3d """
        pass

    def DerivativeAt(self, t, derivativeCount, side=None):
        """
        DerivativeAt(self: Curve, t: float, derivativeCount: int, side: CurveEvaluationSide) -> Array[Vector3d]
        DerivativeAt(self: Curve, t: float, derivativeCount: int) -> Array[Vector3d]
        """
        pass

    def Dispose(self):
        """ Dispose(self: Curve, disposing: bool) """
        pass

    def Duplicate(self):
        """ Duplicate(self: Curve) -> GeometryBase """
        pass

    def DuplicateCurve(self):
        """ DuplicateCurve(self: Curve) -> Curve """
        pass

    def FrameAt(self, t, plane):
        """ FrameAt(self: Curve, t: float) -> (bool, Plane) """
        pass

    def GetCurveParameterFromNurbsFormParameter(self, nurbsParameter, curveParameter):
        """ GetCurveParameterFromNurbsFormParameter(self: Curve, nurbsParameter: float) -> (bool, float) """
        pass

    def GetNextDiscontinuity(self, continuityType, t0, t1, t):
        """ GetNextDiscontinuity(self: Curve, continuityType: Continuity, t0: float, t1: float) -> (bool, float) """
        pass

    def GetNurbsFormParameterFromCurveParameter(self, curveParameter, nurbsParameter):
        """ GetNurbsFormParameterFromCurveParameter(self: Curve, curveParameter: float) -> (bool, float) """
        pass

    def HasNurbsForm(self):
        """ HasNurbsForm(self: Curve) -> int """
        pass

    def IsArc(self, tolerance=None):
        """
        IsArc(self: Curve, tolerance: float) -> bool
        IsArc(self: Curve) -> bool
        """
        pass

    def IsCircle(self, tolerance=None):
        """
        IsCircle(self: Curve, tolerance: float) -> bool
        IsCircle(self: Curve) -> bool
        """
        pass

    def IsClosable(self, tolerance, minimumAbsoluteSize=None, minimumRelativeSize=None):
        """
        IsClosable(self: Curve, tolerance: float, minimumAbsoluteSize: float, minimumRelativeSize: float) -> bool
        IsClosable(self: Curve, tolerance: float) -> bool
        """
        pass

    def IsContinuous(self, continuityType, t):
        """ IsContinuous(self: Curve, continuityType: Continuity, t: float) -> bool """
        pass

    def IsEllipse(self, tolerance=None):
        """
        IsEllipse(self: Curve, tolerance: float) -> bool
        IsEllipse(self: Curve) -> bool
        """
        pass

    def IsInPlane(self, testPlane, tolerance=None):
        """
        IsInPlane(self: Curve, testPlane: Plane, tolerance: float) -> bool
        IsInPlane(self: Curve, testPlane: Plane) -> bool
        """
        pass

    def IsLinear(self, tolerance=None):
        """
        IsLinear(self: Curve, tolerance: float) -> bool
        IsLinear(self: Curve) -> bool
        """
        pass

    def IsPlanar(self, tolerance=None):
        """
        IsPlanar(self: Curve, tolerance: float) -> bool
        IsPlanar(self: Curve) -> bool
        """
        pass

    def IsPolyline(self):
        """ IsPolyline(self: Curve) -> bool """
        pass

    def PointAt(self, t):
        """ PointAt(self: Curve, t: float) -> Point3d """
        pass

    def Reverse(self):
        """ Reverse(self: Curve) -> bool """
        pass

    def SetEndPoint(self, point):
        """ SetEndPoint(self: Curve, point: Point3d) -> bool """
        pass

    def SetStartPoint(self, point):
        """ SetStartPoint(self: Curve, point: Point3d) -> bool """
        pass

    def SpanDomain(self, spanIndex):
        """ SpanDomain(self: Curve, spanIndex: int) -> Interval """
        pass

    def Split(self, t):
        """
        Split(self: Curve, t: IEnumerable[float]) -> Array[Curve]
        Split(self: Curve, t: float) -> Array[Curve]
        """
        pass

    def TangentAt(self, t):
        """ TangentAt(self: Curve, t: float) -> Vector3d """
        pass

    def ToNurbsCurve(self, subdomain=None):
        """
        ToNurbsCurve(self: Curve, subdomain: Interval) -> NurbsCurve
        ToNurbsCurve(self: Curve) -> NurbsCurve
        """
        pass

    def Trim(self, *__args):
        """
        Trim(self: Curve, domain: Interval) -> Curve
        Trim(self: Curve, t0: float, t1: float) -> Curve
        """
        pass

    def TryGetArc(self, *__args):
        """
        TryGetArc(self: Curve, plane: Plane) -> (bool, Arc)
        TryGetArc(self: Curve, plane: Plane, tolerance: float) -> (bool, Arc)
        TryGetArc(self: Curve) -> (bool, Arc)
        TryGetArc(self: Curve, tolerance: float) -> (bool, Arc)
        """
        pass

    def TryGetCircle(self, circle, tolerance=None):
        """
        TryGetCircle(self: Curve, tolerance: float) -> (bool, Circle)
        TryGetCircle(self: Curve) -> (bool, Circle)
        """
        pass

    def TryGetEllipse(self, *__args):
        """
        TryGetEllipse(self: Curve, plane: Plane) -> (bool, Ellipse)
        TryGetEllipse(self: Curve, plane: Plane, tolerance: float) -> (bool, Ellipse)
        TryGetEllipse(self: Curve) -> (bool, Ellipse)
        TryGetEllipse(self: Curve, tolerance: float) -> (bool, Ellipse)
        """
        pass

    def TryGetPlane(self, plane, tolerance=None):
        """
        TryGetPlane(self: Curve, tolerance: float) -> (bool, Plane)
        TryGetPlane(self: Curve) -> (bool, Plane)
        """
        pass

    def TryGetPolyline(self, polyline, parameters=None):
        """
        TryGetPolyline(self: Curve) -> (bool, Polyline, Array[float])
        TryGetPolyline(self: Curve) -> (bool, Polyline)
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    Degree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Degree(self: Curve) -> int

"""

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: Curve) -> int

"""

    Domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Domain(self: Curve) -> Interval

Set: Domain(self: Curve) = value
"""

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsClosed(self: Curve) -> bool

"""

    IsPeriodic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPeriodic(self: Curve) -> bool

"""

    PointAtEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointAtEnd(self: Curve) -> Point3d

"""

    PointAtStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointAtStart(self: Curve) -> Point3d

"""

    SpanCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpanCount(self: Curve) -> int

"""

    TangentAtEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TangentAtEnd(self: Curve) -> Vector3d

"""

    TangentAtStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TangentAtStart(self: Curve) -> Vector3d

"""



class ArcCurve(Curve):
    """
    ArcCurve()
    ArcCurve(other: ArcCurve)
    ArcCurve(arc: Arc)
    ArcCurve(arc: Arc, t0: float, t1: float)
    ArcCurve(circle: Circle)
    ArcCurve(circle: Circle, t0: float, t1: float)
    """
    def Dispose(self):
        """ Dispose(self: Curve, disposing: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, other: ArcCurve)
        __new__(cls: type, arc: Arc)
        __new__(cls: type, arc: Arc, t0: float, t1: float)
        __new__(cls: type, circle: Circle)
        __new__(cls: type, circle: Circle, t0: float, t1: float)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    AngleDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleDegrees(self: ArcCurve) -> float

"""

    AngleRadians = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleRadians(self: ArcCurve) -> float

"""

    Arc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arc(self: ArcCurve) -> Arc

"""

    IsCompleteCircle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCompleteCircle(self: ArcCurve) -> bool

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: ArcCurve) -> float

"""



class BezierCurve(object):
    """
    BezierCurve(controlPoints: IEnumerable[Point2d])
    BezierCurve(controlPoints: IEnumerable[Point3d])
    BezierCurve(controlPoints: IEnumerable[Point4d])
    """
    def ChangeDimension(self, desiredDimension):
        """ ChangeDimension(self: BezierCurve, desiredDimension: int) -> bool """
        pass

    @staticmethod
    def CreateLoftedBezier(points):
        """
        CreateLoftedBezier(points: IEnumerable[Point2d]) -> BezierCurve
        CreateLoftedBezier(points: IEnumerable[Point3d]) -> BezierCurve
        """
        pass

    def CurvatureAt(self, t):
        """ CurvatureAt(self: BezierCurve, t: float) -> Vector3d """
        pass

    def Dispose(self):
        """ Dispose(self: BezierCurve) """
        pass

    def GetBoundingBox(self, accurate):
        """ GetBoundingBox(self: BezierCurve, accurate: bool) -> BoundingBox """
        pass

    def GetControlVertex2d(self, index):
        """ GetControlVertex2d(self: BezierCurve, index: int) -> Point2d """
        pass

    def GetControlVertex3d(self, index):
        """ GetControlVertex3d(self: BezierCurve, index: int) -> Point3d """
        pass

    def GetControlVertex4d(self, index):
        """ GetControlVertex4d(self: BezierCurve, index: int) -> Point4d """
        pass

    def IncreaseDegree(self, desiredDegree):
        """ IncreaseDegree(self: BezierCurve, desiredDegree: int) -> bool """
        pass

    def MakeNonRational(self):
        """ MakeNonRational(self: BezierCurve) -> bool """
        pass

    def MakeRational(self):
        """ MakeRational(self: BezierCurve) -> bool """
        pass

    def PointAt(self, t):
        """ PointAt(self: BezierCurve, t: float) -> Point3d """
        pass

    def TangentAt(self, t):
        """ TangentAt(self: BezierCurve, t: float) -> Vector3d """
        pass

    def ToNurbsCurve(self):
        """ ToNurbsCurve(self: BezierCurve) -> NurbsCurve """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, controlPoints):
        """
        __new__(cls: type, controlPoints: IEnumerable[Point2d])
        __new__(cls: type, controlPoints: IEnumerable[Point3d])
        __new__(cls: type, controlPoints: IEnumerable[Point4d])
        """
        pass

    ControlVertexCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ControlVertexCount(self: BezierCurve) -> int

"""

    IsRational = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRational(self: BezierCurve) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: BezierCurve) -> bool

"""



class BlendContinuity(Enum):
    """ enum BlendContinuity, values: Curvature (2), Position (0), Tangency (1) """
    Curvature = None
    Position = None
    Tangency = None
    value__ = None


class BoundingBox(object):
    """
    BoundingBox(min: Point3d, max: Point3d)
    BoundingBox(minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float)
    BoundingBox(points: IEnumerable[Point3d])
    """
    def ClosestPoint(self, point, includeInterior=None):
        """
        ClosestPoint(self: BoundingBox, point: Point3d, includeInterior: bool) -> Point3d
        ClosestPoint(self: BoundingBox, point: Point3d) -> Point3d
        """
        pass

    def Contains(self, *__args):
        """
        Contains(self: BoundingBox, box: BoundingBox) -> bool
        Contains(self: BoundingBox, box: BoundingBox, strict: bool) -> bool
        Contains(self: BoundingBox, point: Point3d) -> bool
        Contains(self: BoundingBox, point: Point3d, strict: bool) -> bool
        """
        pass

    def Corner(self, minX, minY, minZ):
        """ Corner(self: BoundingBox, minX: bool, minY: bool, minZ: bool) -> Point3d """
        pass

    def FurthestPoint(self, point):
        """ FurthestPoint(self: BoundingBox, point: Point3d) -> Point3d """
        pass

    def GetCorners(self):
        """ GetCorners(self: BoundingBox) -> Array[Point3d] """
        pass

    def GetEdges(self):
        """ GetEdges(self: BoundingBox) -> Array[Line] """
        pass

    def Inflate(self, *__args):
        """ Inflate(self: BoundingBox, xAmount: float, yAmount: float, zAmount: float)Inflate(self: BoundingBox, amount: float) """
        pass

    @staticmethod
    def Intersection(a, b):
        """ Intersection(a: BoundingBox, b: BoundingBox) -> BoundingBox """
        pass

    def IsDegenerate(self, tolerance):
        """ IsDegenerate(self: BoundingBox, tolerance: float) -> int """
        pass

    def MakeValid(self):
        """ MakeValid(self: BoundingBox) -> bool """
        pass

    def PointAt(self, tx, ty, tz):
        """ PointAt(self: BoundingBox, tx: float, ty: float, tz: float) -> Point3d """
        pass

    def ToBrep(self):
        """ ToBrep(self: BoundingBox) -> Brep """
        pass

    def ToString(self):
        """ ToString(self: BoundingBox) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: BoundingBox, xform: Transform) -> bool """
        pass

    def Union(self, *__args):
        """
        Union(a: BoundingBox, b: BoundingBox) -> BoundingBox
        Union(box: BoundingBox, point: Point3d) -> BoundingBox
        Union(self: BoundingBox, other: BoundingBox)Union(self: BoundingBox, point: Point3d)
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[BoundingBox]() -> BoundingBox
        
        __new__(cls: type, min: Point3d, max: Point3d)
        __new__(cls: type, minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float)
        __new__(cls: type, points: IEnumerable[Point3d])
        """
        pass

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Center(self: BoundingBox) -> Point3d

"""

    Diagonal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diagonal(self: BoundingBox) -> Vector3d

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: BoundingBox) -> bool

"""

    Max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Max(self: BoundingBox) -> Point3d

Set: Max(self: BoundingBox) = value
"""

    Min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Min(self: BoundingBox) -> Point3d

Set: Min(self: BoundingBox) = value
"""


    Empty = None
    Unset = None


class Box(object):
    """
    Box(bbox: BoundingBox)
    Box(basePlane: Plane, xSize: Interval, ySize: Interval, zSize: Interval)
    Box(basePlane: Plane, points: IEnumerable[Point3d])
    Box(basePlane: Plane, geometry: GeometryBase)
    Box(basePlane: Plane, boundingbox: BoundingBox)
    """
    def ClosestPoint(self, point):
        """ ClosestPoint(self: Box, point: Point3d) -> Point3d """
        pass

    def Contains(self, *__args):
        """
        Contains(self: Box, box: BoundingBox, strict: bool) -> bool
        Contains(self: Box, box: Box) -> bool
        Contains(self: Box, box: Box, strict: bool) -> bool
        Contains(self: Box, point: Point3d) -> bool
        Contains(self: Box, point: Point3d, strict: bool) -> bool
        Contains(self: Box, box: BoundingBox) -> bool
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Box, other: Box, epsilon: float) -> bool """
        pass

    def FurthestPoint(self, point):
        """ FurthestPoint(self: Box, point: Point3d) -> Point3d """
        pass

    def GetCorners(self):
        """ GetCorners(self: Box) -> Array[Point3d] """
        pass

    def Inflate(self, *__args):
        """ Inflate(self: Box, xAmount: float, yAmount: float, zAmount: float)Inflate(self: Box, amount: float) """
        pass

    def MakeValid(self):
        """ MakeValid(self: Box) -> bool """
        pass

    def PointAt(self, x, y, z):
        """ PointAt(self: Box, x: float, y: float, z: float) -> Point3d """
        pass

    def RepositionBasePlane(self, origin):
        """ RepositionBasePlane(self: Box, origin: Point3d) """
        pass

    def ToBrep(self):
        """ ToBrep(self: Box) -> Brep """
        pass

    def Transform(self, xform):
        """ Transform(self: Box, xform: Transform) -> bool """
        pass

    def Union(self, point):
        """ Union(self: Box, point: Point3d) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Box]() -> Box
        
        __new__(cls: type, bbox: BoundingBox)
        __new__(cls: type, basePlane: Plane, xSize: Interval, ySize: Interval, zSize: Interval)
        __new__(cls: type, basePlane: Plane, points: IEnumerable[Point3d])
        __new__(cls: type, basePlane: Plane, geometry: GeometryBase)
        __new__(cls: type, basePlane: Plane, boundingbox: BoundingBox)
        """
        pass

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Area(self: Box) -> float

"""

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: Box) -> BoundingBox

"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Center(self: Box) -> Point3d

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Box) -> bool

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: Box) -> Plane

Set: Plane(self: Box) = value
"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Volume(self: Box) -> float

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Box) -> Interval

Set: X(self: Box) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Box) -> Interval

Set: Y(self: Box) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: Box) -> Interval

Set: Z(self: Box) = value
"""


    Empty = None
    Unset = None


class Brep(GeometryBase):
    """ Brep() """
    def AddEdgeCurve(self, curve):
        """ AddEdgeCurve(self: Brep, curve: Curve) -> int """
        pass

    def AddSurface(self, surface):
        """ AddSurface(self: Brep, surface: Surface) -> int """
        pass

    def AddTrimCurve(self, curve):
        """ AddTrimCurve(self: Brep, curve: Curve) -> int """
        pass

    def Append(self, other):
        """ Append(self: Brep, other: Brep) """
        pass

    def Compact(self):
        """ Compact(self: Brep) """
        pass

    @staticmethod
    def CreateFromBox(*__args):
        """
        CreateFromBox(corners: IEnumerable[Point3d]) -> Brep
        CreateFromBox(box: Box) -> Brep
        CreateFromBox(box: BoundingBox) -> Brep
        """
        pass

    @staticmethod
    def CreateFromCone(cone, capBottom):
        """ CreateFromCone(cone: Cone, capBottom: bool) -> Brep """
        pass

    @staticmethod
    def CreateFromCylinder(cylinder, capBottom, capTop):
        """ CreateFromCylinder(cylinder: Cylinder, capBottom: bool, capTop: bool) -> Brep """
        pass

    @staticmethod
    def CreateFromMesh(mesh, trimmedTriangles):
        """ CreateFromMesh(mesh: Mesh, trimmedTriangles: bool) -> Brep """
        pass

    @staticmethod
    def CreateFromRevSurface(surface, capStart, capEnd):
        """ CreateFromRevSurface(surface: RevSurface, capStart: bool, capEnd: bool) -> Brep """
        pass

    @staticmethod
    def CreateFromSphere(sphere):
        """ CreateFromSphere(sphere: Sphere) -> Brep """
        pass

    @staticmethod
    def CreateFromSurface(surface):
        """ CreateFromSurface(surface: Surface) -> Brep """
        pass

    @staticmethod
    def CreatePlanarBreps(*__args):
        """
        CreatePlanarBreps(inputLoop: Curve) -> Array[Brep]
        CreatePlanarBreps(inputLoops: IEnumerable[Curve]) -> Array[Brep]
        """
        pass

    def CullUnused2dCurves(self):
        """ CullUnused2dCurves(self: Brep) -> bool """
        pass

    def CullUnused3dCurves(self):
        """ CullUnused3dCurves(self: Brep) -> bool """
        pass

    def CullUnusedEdges(self):
        """ CullUnusedEdges(self: Brep) -> bool """
        pass

    def CullUnusedFaces(self):
        """ CullUnusedFaces(self: Brep) -> bool """
        pass

    def CullUnusedLoops(self):
        """ CullUnusedLoops(self: Brep) -> bool """
        pass

    def CullUnusedSurfaces(self):
        """ CullUnusedSurfaces(self: Brep) -> bool """
        pass

    def CullUnusedTrims(self):
        """ CullUnusedTrims(self: Brep) -> bool """
        pass

    def CullUnusedVertices(self):
        """ CullUnusedVertices(self: Brep) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def Duplicate(self):
        """ Duplicate(self: Brep) -> GeometryBase """
        pass

    def DuplicateBrep(self):
        """ DuplicateBrep(self: Brep) -> Brep """
        pass

    def DuplicateEdgeCurves(self, nakedOnly=None):
        """
        DuplicateEdgeCurves(self: Brep, nakedOnly: bool) -> Array[Curve]
        DuplicateEdgeCurves(self: Brep) -> Array[Curve]
        """
        pass

    def DuplicateNakedEdgeCurves(self, outer, inner):
        """ DuplicateNakedEdgeCurves(self: Brep, outer: bool, inner: bool) -> Array[Curve] """
        pass

    def DuplicateSubBrep(self, faceIndices):
        """ DuplicateSubBrep(self: Brep, faceIndices: IEnumerable[int]) -> Brep """
        pass

    def DuplicateVertices(self):
        """ DuplicateVertices(self: Brep) -> Array[Point3d] """
        pass

    def Flip(self):
        """ Flip(self: Brep) """
        pass

    def IsDuplicate(self, other, tolerance):
        """ IsDuplicate(self: Brep, other: Brep, tolerance: float) -> bool """
        pass

    def IsValidGeometry(self, log):
        """ IsValidGeometry(self: Brep) -> (bool, str) """
        pass

    def IsValidTolerancesAndFlags(self, log):
        """ IsValidTolerancesAndFlags(self: Brep) -> (bool, str) """
        pass

    def IsValidTopology(self, log):
        """ IsValidTopology(self: Brep) -> (bool, str) """
        pass

    def SetTrimIsoFlags(self):
        """ SetTrimIsoFlags(self: Brep) """
        pass

    def SetVertices(self):
        """ SetVertices(self: Brep) """
        pass

    def Standardize(self):
        """ Standardize(self: Brep) """
        pass

    @staticmethod
    def TryConvertBrep(geometry):
        """ TryConvertBrep(geometry: GeometryBase) -> Brep """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    Curves2D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Curves2D(self: Brep) -> BrepCurveList

"""

    Curves3D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Curves3D(self: Brep) -> BrepCurveList

"""

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edges(self: Brep) -> BrepEdgeList

"""

    Faces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Faces(self: Brep) -> BrepFaceList

"""

    IsManifold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsManifold(self: Brep) -> bool

"""

    IsSolid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSolid(self: Brep) -> bool

"""

    IsSurface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSurface(self: Brep) -> bool

"""

    Loops = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loops(self: Brep) -> BrepLoopList

"""

    SolidOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SolidOrientation(self: Brep) -> BrepSolidOrientation

"""

    Surfaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Surfaces(self: Brep) -> BrepSurfaceList

"""

    Trims = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Trims(self: Brep) -> BrepTrimList

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: Brep) -> BrepVertexList

"""



class CurveProxy(Curve):
    # no doc
    def Dispose(self):
        """ Dispose(self: Curve, disposing: bool) """
        pass

    ProxyCurveIsReversed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProxyCurveIsReversed(self: CurveProxy) -> bool

"""



class BrepEdge(CurveProxy):
    # no doc
    def AdjacentFaces(self):
        """ AdjacentFaces(self: BrepEdge) -> Array[int] """
        pass

    def Dispose(self):
        """ Dispose(self: Curve, disposing: bool) """
        pass

    def SetEdgeCurve(self, curve3dIndex, subDomain=None):
        """
        SetEdgeCurve(self: BrepEdge, curve3dIndex: int, subDomain: Interval) -> bool
        SetEdgeCurve(self: BrepEdge, curve3dIndex: int) -> bool
        """
        pass

    Brep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Brep(self: BrepEdge) -> Brep

"""

    EdgeIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeIndex(self: BrepEdge) -> int

"""

    EndVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndVertex(self: BrepEdge) -> BrepVertex

"""

    StartVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartVertex(self: BrepEdge) -> BrepVertex

"""

    Tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tolerance(self: BrepEdge) -> float

Set: Tolerance(self: BrepEdge) = value
"""

    TrimCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TrimCount(self: BrepEdge) -> int

"""

    Valence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Valence(self: BrepEdge) -> EdgeAdjacency

"""



class Surface(GeometryBase):
    # no doc
    def CurvatureAt(self, u, v):
        """ CurvatureAt(self: Surface, u: float, v: float) -> SurfaceCurvature """
        pass

    def Degree(self, direction):
        """ Degree(self: Surface, direction: int) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def Domain(self, direction):
        """ Domain(self: Surface, direction: int) -> Interval """
        pass

    def Evaluate(self, u, v, numberDerivatives, point, derivatives):
        """ Evaluate(self: Surface, u: float, v: float, numberDerivatives: int) -> (bool, Point3d, Array[Vector3d]) """
        pass

    def FrameAt(self, u, v, frame):
        """ FrameAt(self: Surface, u: float, v: float) -> (bool, Plane) """
        pass

    def GetNextDiscontinuity(self, direction, continuityType, t0, t1, t):
        """ GetNextDiscontinuity(self: Surface, direction: int, continuityType: Continuity, t0: float, t1: float) -> (bool, float) """
        pass

    def GetSpanVector(self, direction):
        """ GetSpanVector(self: Surface, direction: int) -> Array[float] """
        pass

    def HasNurbsForm(self):
        """ HasNurbsForm(self: Surface) -> int """
        pass

    def IsAtSeam(self, u, v):
        """ IsAtSeam(self: Surface, u: float, v: float) -> int """
        pass

    def IsAtSingularity(self, u, v, exact):
        """ IsAtSingularity(self: Surface, u: float, v: float, exact: bool) -> bool """
        pass

    def IsClosed(self, direction):
        """ IsClosed(self: Surface, direction: int) -> bool """
        pass

    def IsCone(self, tolerance=None):
        """
        IsCone(self: Surface, tolerance: float) -> bool
        IsCone(self: Surface) -> bool
        """
        pass

    def IsContinuous(self, continuityType, u, v):
        """ IsContinuous(self: Surface, continuityType: Continuity, u: float, v: float) -> bool """
        pass

    def IsCylinder(self, tolerance=None):
        """
        IsCylinder(self: Surface, tolerance: float) -> bool
        IsCylinder(self: Surface) -> bool
        """
        pass

    def IsIsoparametric(self, *__args):
        """
        IsIsoparametric(self: Surface, bbox: BoundingBox) -> IsoStatus
        IsIsoparametric(self: Surface, curve: Curve) -> IsoStatus
        IsIsoparametric(self: Surface, curve: Curve, curveDomain: Interval) -> IsoStatus
        """
        pass

    def IsoCurve(self, direction, constantParameter):
        """ IsoCurve(self: Surface, direction: int, constantParameter: float) -> Curve """
        pass

    def IsPeriodic(self, direction):
        """ IsPeriodic(self: Surface, direction: int) -> bool """
        pass

    def IsPlanar(self, tolerance=None):
        """
        IsPlanar(self: Surface, tolerance: float) -> bool
        IsPlanar(self: Surface) -> bool
        """
        pass

    def IsSingular(self, side):
        """ IsSingular(self: Surface, side: int) -> bool """
        pass

    def IsSphere(self, tolerance=None):
        """
        IsSphere(self: Surface, tolerance: float) -> bool
        IsSphere(self: Surface) -> bool
        """
        pass

    def IsTorus(self, tolerance=None):
        """
        IsTorus(self: Surface, tolerance: float) -> bool
        IsTorus(self: Surface) -> bool
        """
        pass

    def NormalAt(self, u, v):
        """ NormalAt(self: Surface, u: float, v: float) -> Vector3d """
        pass

    def PointAt(self, u, v):
        """ PointAt(self: Surface, u: float, v: float) -> Point3d """
        pass

    def Reverse(self, direction, inPlace=None):
        """
        Reverse(self: Surface, direction: int, inPlace: bool) -> Surface
        Reverse(self: Surface, direction: int) -> Surface
        """
        pass

    def SetDomain(self, direction, domain):
        """ SetDomain(self: Surface, direction: int, domain: Interval) -> bool """
        pass

    def SpanCount(self, direction):
        """ SpanCount(self: Surface, direction: int) -> int """
        pass

    def Split(self, direction, parameter):
        """ Split(self: Surface, direction: int, parameter: float) -> Array[Surface] """
        pass

    def ToBrep(self):
        """ ToBrep(self: Surface) -> Brep """
        pass

    def ToNurbsSurface(self, tolerance=None, accuracy=None):
        """
        ToNurbsSurface(self: Surface, tolerance: float) -> (NurbsSurface, int)
        ToNurbsSurface(self: Surface) -> NurbsSurface
        """
        pass

    def Transpose(self, inPlace=None):
        """
        Transpose(self: Surface, inPlace: bool) -> Surface
        Transpose(self: Surface) -> Surface
        """
        pass

    def Trim(self, u, v):
        """ Trim(self: Surface, u: Interval, v: Interval) -> Surface """
        pass

    def TryGetCone(self, cone, tolerance=None):
        """
        TryGetCone(self: Surface, tolerance: float) -> (bool, Cone)
        TryGetCone(self: Surface) -> (bool, Cone)
        """
        pass

    def TryGetCylinder(self, cylinder, tolerance=None):
        """
        TryGetCylinder(self: Surface, tolerance: float) -> (bool, Cylinder)
        TryGetCylinder(self: Surface) -> (bool, Cylinder)
        """
        pass

    def TryGetPlane(self, plane, tolerance=None):
        """
        TryGetPlane(self: Surface, tolerance: float) -> (bool, Plane)
        TryGetPlane(self: Surface) -> (bool, Plane)
        """
        pass

    def TryGetSphere(self, sphere, tolerance=None):
        """
        TryGetSphere(self: Surface, tolerance: float) -> (bool, Sphere)
        TryGetSphere(self: Surface) -> (bool, Sphere)
        """
        pass

    def TryGetTorus(self, torus, tolerance=None):
        """
        TryGetTorus(self: Surface, tolerance: float) -> (bool, Torus)
        TryGetTorus(self: Surface) -> (bool, Torus)
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    IsSolid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSolid(self: Surface) -> bool

"""



class SurfaceProxy(Surface):
    # no doc
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass


class BrepFace(SurfaceProxy):
    # no doc
    def AdjacentEdges(self):
        """ AdjacentEdges(self: BrepFace) -> Array[int] """
        pass

    def AdjacentFaces(self):
        """ AdjacentFaces(self: BrepFace) -> Array[int] """
        pass

    def CreateExtrusion(self, pathCurve, cap):
        """ CreateExtrusion(self: BrepFace, pathCurve: Curve, cap: bool) -> Brep """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def DuplicateFace(self, duplicateMeshes):
        """ DuplicateFace(self: BrepFace, duplicateMeshes: bool) -> Brep """
        pass

    def DuplicateSurface(self):
        """ DuplicateSurface(self: BrepFace) -> Surface """
        pass

    def GetMesh(self, meshType):
        """ GetMesh(self: BrepFace, meshType: MeshType) -> Mesh """
        pass

    def SetDomain(self, direction, domain):
        """ SetDomain(self: BrepFace, direction: int, domain: Interval) -> bool """
        pass

    def SetMesh(self, meshType, mesh):
        """ SetMesh(self: BrepFace, meshType: MeshType, mesh: Mesh) -> bool """
        pass

    def UnderlyingSurface(self):
        """ UnderlyingSurface(self: BrepFace) -> Surface """
        pass

    FaceIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FaceIndex(self: BrepFace) -> int

"""

    IsSurface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSurface(self: BrepFace) -> bool

"""

    Loops = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loops(self: BrepFace) -> BrepLoopList

"""

    OrientationIsReversed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrientationIsReversed(self: BrepFace) -> bool

Set: OrientationIsReversed(self: BrepFace) = value
"""

    OuterLoop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OuterLoop(self: BrepFace) -> BrepLoop

"""

    SurfaceIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceIndex(self: BrepFace) -> int

"""



class BrepLoop(GeometryBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def To2dCurve(self):
        """ To2dCurve(self: BrepLoop) -> Curve """
        pass

    def To3dCurve(self):
        """ To3dCurve(self: BrepLoop) -> Curve """
        pass

    Brep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Brep(self: BrepLoop) -> Brep

"""

    Face = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Face(self: BrepLoop) -> BrepFace

"""

    LoopIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoopIndex(self: BrepLoop) -> int

"""

    LoopType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoopType(self: BrepLoop) -> BrepLoopType

"""

    Trims = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Trims(self: BrepLoop) -> BrepTrimList

"""



class BrepLoopType(Enum):
    """ enum BrepLoopType, values: CurveOnSurface (4), Inner (2), Outer (1), PointOnSurface (5), Slit (3), Unknown (0) """
    CurveOnSurface = None
    Inner = None
    Outer = None
    PointOnSurface = None
    Slit = None
    Unknown = None
    value__ = None


class BrepSolidOrientation(Enum):
    """ enum BrepSolidOrientation, values: Inward (-1), None (0), Outward (1), Unknown (2) """
    Inward = None
    None = None
    Outward = None
    Unknown = None
    value__ = None


class BrepTrim(CurveProxy):
    # no doc
    def Dispose(self):
        """ Dispose(self: Curve, disposing: bool) """
        pass

    def GetTolerances(self, toleranceU, toleranceV):
        """ GetTolerances(self: BrepTrim) -> (float, float) """
        pass

    def SetTolerances(self, toleranceU, toleranceV):
        """ SetTolerances(self: BrepTrim, toleranceU: float, toleranceV: float) """
        pass

    def SetTrimCurve(self, curve2dIndex, subDomain=None):
        """
        SetTrimCurve(self: BrepTrim, curve2dIndex: int, subDomain: Interval) -> bool
        SetTrimCurve(self: BrepTrim, curve2dIndex: int) -> bool
        """
        pass

    Brep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Brep(self: BrepTrim) -> Brep

"""

    Edge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edge(self: BrepTrim) -> BrepEdge

"""

    Face = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Face(self: BrepTrim) -> BrepFace

"""

    IsoStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsoStatus(self: BrepTrim) -> IsoStatus

Set: IsoStatus(self: BrepTrim) = value
"""

    Loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loop(self: BrepTrim) -> BrepLoop

"""

    TrimIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TrimIndex(self: BrepTrim) -> int

"""

    TrimType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TrimType(self: BrepTrim) -> BrepTrimType

Set: TrimType(self: BrepTrim) = value
"""



class BrepTrimType(Enum):
    """ enum BrepTrimType, values: Boundary (1), CurveOnSurface (5), Mated (2), PointOnSurface (6), Seam (3), Singular (4), Slit (7), Unknown (0) """
    Boundary = None
    CurveOnSurface = None
    Mated = None
    PointOnSurface = None
    Seam = None
    Singular = None
    Slit = None
    Unknown = None
    value__ = None


class Point(GeometryBase):
    """ Point(location: Point3d) """
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, location):
        """
        __new__(cls: type, location: Point3d)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: Point) -> Point3d

Set: Location(self: Point) = value
"""



class BrepVertex(Point):
    # no doc
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    Brep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Brep(self: BrepVertex) -> Brep

"""

    VertexIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VertexIndex(self: BrepVertex) -> int

"""



class Circle(object):
    """
    Circle(radius: float)
    Circle(plane: Plane, radius: float)
    Circle(center: Point3d, radius: float)
    Circle(arc: Arc)
    Circle(point1: Point3d, point2: Point3d, point3: Point3d)
    Circle(plane: Plane, center: Point3d, radius: float)
    Circle(startPoint: Point3d, tangentAtP: Vector3d, pointOnCircle: Point3d)
    """
    def ClosestParameter(self, testPoint, t):
        """ ClosestParameter(self: Circle, testPoint: Point3d) -> (bool, float) """
        pass

    def ClosestPoint(self, testPoint):
        """ ClosestPoint(self: Circle, testPoint: Point3d) -> Point3d """
        pass

    def DerivativeAt(self, derivative, t):
        """ DerivativeAt(self: Circle, derivative: int, t: float) -> Vector3d """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Circle, other: Circle, epsilon: float) -> bool """
        pass

    def IsInPlane(self, plane, tolerance):
        """ IsInPlane(self: Circle, plane: Plane, tolerance: float) -> bool """
        pass

    def PointAt(self, t):
        """ PointAt(self: Circle, t: float) -> Point3d """
        pass

    def Reverse(self):
        """ Reverse(self: Circle) """
        pass

    def Rotate(self, *__args):
        """
        Rotate(self: Circle, angle: float, axis: Vector3d) -> bool
        Rotate(self: Circle, angle: float, axis: Vector3d, point: Point3d) -> bool
        Rotate(self: Circle, sinAngle: float, cosAngle: float, axis: Vector3d) -> bool
        Rotate(self: Circle, sinAngle: float, cosAngle: float, axis: Vector3d, point: Point3d) -> bool
        """
        pass

    def TangentAt(self, t):
        """ TangentAt(self: Circle, t: float) -> Vector3d """
        pass

    def ToNurbsCurve(self):
        """ ToNurbsCurve(self: Circle) -> NurbsCurve """
        pass

    def Transform(self, xform):
        """ Transform(self: Circle, xform: Transform) -> bool """
        pass

    def Translate(self, delta):
        """ Translate(self: Circle, delta: Vector3d) -> bool """
        pass

    @staticmethod
    def TryFitCircleTT(c1, c2, t1, t2):
        """ TryFitCircleTT(c1: Curve, c2: Curve, t1: float, t2: float) -> Circle """
        pass

    @staticmethod
    def TryFitCircleTTT(c1, c2, c3, t1, t2, t3):
        """ TryFitCircleTTT(c1: Curve, c2: Curve, c3: Curve, t1: float, t2: float, t3: float) -> Circle """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Circle]() -> Circle
        
        __new__(cls: type, radius: float)
        __new__(cls: type, plane: Plane, radius: float)
        __new__(cls: type, center: Point3d, radius: float)
        __new__(cls: type, arc: Arc)
        __new__(cls: type, point1: Point3d, point2: Point3d, point3: Point3d)
        __new__(cls: type, plane: Plane, center: Point3d, radius: float)
        __new__(cls: type, startPoint: Point3d, tangentAtP: Vector3d, pointOnCircle: Point3d)
        """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: Circle) -> BoundingBox

"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Center(self: Circle) -> Point3d

Set: Center(self: Circle) = value
"""

    Circumference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Circumference(self: Circle) -> float

Set: Circumference(self: Circle) = value
"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: Circle) -> float

Set: Diameter(self: Circle) = value
"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Circle) -> bool

"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Normal(self: Circle) -> Vector3d

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: Circle) -> Plane

Set: Plane(self: Circle) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: Circle) -> float

Set: Radius(self: Circle) = value
"""


    Unset = None


class PlaneSurface(Surface):
    """ PlaneSurface(plane: Plane, xExtents: Interval, yExtents: Interval) """
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, plane, xExtents, yExtents):
        """
        __new__(cls: type, plane: Plane, xExtents: Interval, yExtents: Interval)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class ClippingPlaneSurface(PlaneSurface):
    # no doc
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def ViewportIds(self):
        """ ViewportIds(self: ClippingPlaneSurface) -> Array[Guid] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: ClippingPlaneSurface) -> Plane

Set: Plane(self: ClippingPlaneSurface) = value
"""



class ComponentIndex(object):
    """ ComponentIndex(type: ComponentIndexType, index: int) """
    @staticmethod # known case of __new__
    def __new__(self, type, index):
        """
        __new__[ComponentIndex]() -> ComponentIndex
        
        __new__(cls: type, type: ComponentIndexType, index: int)
        """
        pass

    ComponentIndexType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentIndexType(self: ComponentIndex) -> ComponentIndexType

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: ComponentIndex) -> int

"""


    Unset = None


class ComponentIndexType(Enum):
    """ enum ComponentIndexType, values: BrepEdge (2), BrepFace (3), BrepLoop (5), BrepTrim (4), BrepVertex (1), DimAngularPoint (102), DimLinearPoint (100), DimOrdinatePoint (103), DimRadialPoint (101), DimTextPoint (104), GroupMember (51), InstanceDefinitionPart (21), InvalidType (0), MeshFace (14), MeshTopologyEdge (13), MeshTopologyVertex (12), MeshVertex (11), NoType (268435455), PointCloudPoint (41), PolycurveSegment (31) """
    BrepEdge = None
    BrepFace = None
    BrepLoop = None
    BrepTrim = None
    BrepVertex = None
    DimAngularPoint = None
    DimLinearPoint = None
    DimOrdinatePoint = None
    DimRadialPoint = None
    DimTextPoint = None
    GroupMember = None
    InstanceDefinitionPart = None
    InvalidType = None
    MeshFace = None
    MeshTopologyEdge = None
    MeshTopologyVertex = None
    MeshVertex = None
    NoType = None
    PointCloudPoint = None
    PolycurveSegment = None
    value__ = None


class Cone(object):
    """ Cone(plane: Plane, height: float, radius: float) """
    def AngleInDegrees(self):
        """ AngleInDegrees(self: Cone) -> float """
        pass

    def AngleInRadians(self):
        """ AngleInRadians(self: Cone) -> float """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Cone, other: Cone, epsilon: float) -> bool """
        pass

    def ToBrep(self, capBottom):
        """ ToBrep(self: Cone, capBottom: bool) -> Brep """
        pass

    def ToNurbsSurface(self):
        """ ToNurbsSurface(self: Cone) -> NurbsSurface """
        pass

    def ToRevSurface(self):
        """ ToRevSurface(self: Cone) -> RevSurface """
        pass

    @staticmethod # known case of __new__
    def __new__(self, plane, height, radius):
        """
        __new__[Cone]() -> Cone
        
        __new__(cls: type, plane: Plane, height: float, radius: float)
        """
        pass

    ApexPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApexPoint(self: Cone) -> Point3d

"""

    Axis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Axis(self: Cone) -> Vector3d

"""

    BasePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BasePoint(self: Cone) -> Point3d

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: Cone) -> float

Set: Height(self: Cone) = value
"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Cone) -> bool

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: Cone) -> Plane

Set: Plane(self: Cone) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: Cone) -> float

Set: Radius(self: Cone) = value
"""


    Unset = None


class Continuity(Enum):
    """ enum Continuity, values: C0_continuous (1), C0_locus_continuous (6), C1_continuous (2), C1_locus_continuous (7), C2_continuous (3), C2_locus_continuous (8), Cinfinity_continuous (11), G1_continuous (4), G1_locus_continuous (9), G2_continuous (5), G2_locus_continuous (10), None (0) """
    C0_continuous = None
    C0_locus_continuous = None
    C1_continuous = None
    C1_locus_continuous = None
    C2_continuous = None
    C2_locus_continuous = None
    Cinfinity_continuous = None
    G1_continuous = None
    G1_locus_continuous = None
    G2_continuous = None
    G2_locus_continuous = None
    None = None
    value__ = None


class ControlPoint(object):
    """
    ControlPoint(x: float, y: float, z: float)
    ControlPoint(x: float, y: float, z: float, weight: float)
    ControlPoint(pt: Point3d)
    ControlPoint(pt: Point3d, weight: float)
    ControlPoint(pt: Point4d)
    """
    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: ControlPoint, other: ControlPoint, epsilon: float) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[ControlPoint]() -> ControlPoint
        
        __new__(cls: type, x: float, y: float, z: float)
        __new__(cls: type, x: float, y: float, z: float, weight: float)
        __new__(cls: type, pt: Point3d)
        __new__(cls: type, pt: Point3d, weight: float)
        __new__(cls: type, pt: Point4d)
        """
        pass

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: ControlPoint) -> Point3d

Set: Location(self: ControlPoint) = value
"""

    Weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weight(self: ControlPoint) -> float

Set: Weight(self: ControlPoint) = value
"""


    Unset = None


class CurveEnd(Enum):
    """ enum (flags) CurveEnd, values: Both (3), End (2), None (0), Start (1) """
    Both = None
    End = None
    None = None
    Start = None
    value__ = None


class CurveEvaluationSide(Enum):
    """ enum CurveEvaluationSide, values: Above (1), Below (-1), Default (0) """
    Above = None
    Below = None
    Default = None
    value__ = None


class CurveExtensionStyle(Enum):
    """ enum CurveExtensionStyle, values: Arc (1), Line (0), Smooth (2) """
    Arc = None
    Line = None
    Smooth = None
    value__ = None


class CurveKnotStyle(Enum):
    """ enum CurveKnotStyle, values: Chord (1), ChordPeriodic (4), ChordSquareRoot (2), ChordSquareRootPeriodic (5), Uniform (0), UniformPeriodic (3) """
    Chord = None
    ChordPeriodic = None
    ChordSquareRoot = None
    ChordSquareRootPeriodic = None
    Uniform = None
    UniformPeriodic = None
    value__ = None


class CurveOffsetCornerStyle(Enum):
    """ enum CurveOffsetCornerStyle, values: Chamfer (4), None (0), Round (2), Sharp (1), Smooth (3) """
    Chamfer = None
    None = None
    Round = None
    Sharp = None
    Smooth = None
    value__ = None


class CurveOrientation(Enum):
    """ enum CurveOrientation, values: Clockwise (-1), CounterClockwise (1), Undefined (0) """
    Clockwise = None
    CounterClockwise = None
    Undefined = None
    value__ = None


class CurveSimplifyOptions(Enum):
    """ enum (flags) CurveSimplifyOptions, values: AdjustG1 (16), All (63), Merge (32), None (0), RebuildArcs (4), RebuildLines (2), RebuildRationals (8), SplitAtFullyMultipleKnots (1) """
    AdjustG1 = None
    All = None
    Merge = None
    None = None
    RebuildArcs = None
    RebuildLines = None
    RebuildRationals = None
    SplitAtFullyMultipleKnots = None
    value__ = None


class Cylinder(object):
    """
    Cylinder(baseCircle: Circle)
    Cylinder(baseCircle: Circle, height: float)
    """
    def CircleAt(self, linearParameter):
        """ CircleAt(self: Cylinder, linearParameter: float) -> Circle """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Cylinder, other: Cylinder, epsilon: float) -> bool """
        pass

    def LineAt(self, angularParameter):
        """ LineAt(self: Cylinder, angularParameter: float) -> Line """
        pass

    def ToBrep(self, capBottom, capTop):
        """ ToBrep(self: Cylinder, capBottom: bool, capTop: bool) -> Brep """
        pass

    def ToNurbsSurface(self):
        """ ToNurbsSurface(self: Cylinder) -> NurbsSurface """
        pass

    def ToRevSurface(self):
        """ ToRevSurface(self: Cylinder) -> RevSurface """
        pass

    @staticmethod # known case of __new__
    def __new__(self, baseCircle, height=None):
        """
        __new__[Cylinder]() -> Cylinder
        
        __new__(cls: type, baseCircle: Circle)
        __new__(cls: type, baseCircle: Circle, height: float)
        """
        pass

    Axis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Axis(self: Cylinder) -> Vector3d

"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Center(self: Cylinder) -> Point3d

"""

    Height1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height1(self: Cylinder) -> float

Set: Height1(self: Cylinder) = value
"""

    Height2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height2(self: Cylinder) -> float

Set: Height2(self: Cylinder) = value
"""

    IsFinite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFinite(self: Cylinder) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Cylinder) -> bool

"""

    TotalHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalHeight(self: Cylinder) -> float

"""


    Unset = None


class DetailView(GeometryBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def SetScale(self, modelLength, modelUnits, pageLength, pageUnits):
        """ SetScale(self: DetailView, modelLength: float, modelUnits: UnitSystem, pageLength: float, pageUnits: UnitSystem) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    IsParallelProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsParallelProjection(self: DetailView) -> bool

Set: IsParallelProjection(self: DetailView) = value
"""

    IsPerspectiveProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPerspectiveProjection(self: DetailView) -> bool

Set: IsPerspectiveProjection(self: DetailView) = value
"""

    IsProjectionLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsProjectionLocked(self: DetailView) -> bool

Set: IsProjectionLocked(self: DetailView) = value
"""

    PageToModelRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PageToModelRatio(self: DetailView) -> float

"""



class EdgeAdjacency(Enum):
    """ enum EdgeAdjacency, values: Interior (2), Naked (1), None (0), NonManifold (3) """
    Interior = None
    Naked = None
    None = None
    NonManifold = None
    value__ = None


class Ellipse(object):
    """
    Ellipse(plane: Plane, radius1: float, radius2: float)
    Ellipse(center: Point3d, second: Point3d, third: Point3d)
    """
    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Ellipse, other: Ellipse, epsilon: float) -> bool """
        pass

    def ToNurbsCurve(self):
        """ ToNurbsCurve(self: Ellipse) -> NurbsCurve """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Ellipse]() -> Ellipse
        
        __new__(cls: type, plane: Plane, radius1: float, radius2: float)
        __new__(cls: type, center: Point3d, second: Point3d, third: Point3d)
        """
        pass

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: Ellipse) -> Plane

Set: Plane(self: Ellipse) = value
"""

    Radius1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius1(self: Ellipse) -> float

Set: Radius1(self: Ellipse) = value
"""

    Radius2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius2(self: Ellipse) -> float

Set: Radius2(self: Ellipse) = value
"""



class ExtrudeCornerType(Enum):
    """ enum ExtrudeCornerType, values: Chamfer (4), None (0), Round (2), Sharp (1), Smooth (3) """
    Chamfer = None
    None = None
    Round = None
    Sharp = None
    Smooth = None
    value__ = None


class Extrusion(Surface):
    """ Extrusion() """
    def AddInnerProfile(self, innerProfile):
        """ AddInnerProfile(self: Extrusion, innerProfile: Curve) -> bool """
        pass

    @staticmethod
    def Create(planarCurve, height, cap):
        """ Create(planarCurve: Curve, height: float, cap: bool) -> Extrusion """
        pass

    @staticmethod
    def CreateCylinderExtrusion(cylinder, capBottom, capTop):
        """ CreateCylinderExtrusion(cylinder: Cylinder, capBottom: bool, capTop: bool) -> Extrusion """
        pass

    @staticmethod
    def CreatePipeExtrusion(cylinder, otherRadius, capTop, capBottom):
        """ CreatePipeExtrusion(cylinder: Cylinder, otherRadius: float, capTop: bool, capBottom: bool) -> Extrusion """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def GetMesh(self, meshType):
        """ GetMesh(self: Extrusion, meshType: MeshType) -> Mesh """
        pass

    def GetPathPlane(self, s):
        """ GetPathPlane(self: Extrusion, s: float) -> Plane """
        pass

    def GetProfilePlane(self, s):
        """ GetProfilePlane(self: Extrusion, s: float) -> Plane """
        pass

    def GetProfileTransformation(self, s):
        """ GetProfileTransformation(self: Extrusion, s: float) -> Transform """
        pass

    def PathLineCurve(self):
        """ PathLineCurve(self: Extrusion) -> LineCurve """
        pass

    def Profile3d(self, *__args):
        """
        Profile3d(self: Extrusion, ci: ComponentIndex) -> Curve
        Profile3d(self: Extrusion, profileIndex: int, s: float) -> Curve
        """
        pass

    def ProfileIndex(self, profileParameter):
        """ ProfileIndex(self: Extrusion, profileParameter: float) -> int """
        pass

    def SetOuterProfile(self, outerProfile, cap):
        """ SetOuterProfile(self: Extrusion, outerProfile: Curve, cap: bool) -> bool """
        pass

    def SetPathAndUp(self, a, b, up):
        """ SetPathAndUp(self: Extrusion, a: Point3d, b: Point3d, up: Vector3d) -> bool """
        pass

    def ToBrep(self, splitKinkyFaces=None):
        """ ToBrep(self: Extrusion, splitKinkyFaces: bool) -> Brep """
        pass

    def WallEdge(self, ci):
        """ WallEdge(self: Extrusion, ci: ComponentIndex) -> Curve """
        pass

    def WallSurface(self, ci):
        """ WallSurface(self: Extrusion, ci: ComponentIndex) -> Surface """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type)
        """
        pass

    CapCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CapCount(self: Extrusion) -> int

"""

    IsCappedAtBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCappedAtBottom(self: Extrusion) -> bool

"""

    IsCappedAtTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCappedAtTop(self: Extrusion) -> bool

"""

    IsMiteredAtEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMiteredAtEnd(self: Extrusion) -> bool

"""

    IsMiteredAtStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMiteredAtStart(self: Extrusion) -> bool

"""

    IsSolid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSolid(self: Extrusion) -> bool

"""

    MiterPlaneNormalAtEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MiterPlaneNormalAtEnd(self: Extrusion) -> Vector3d

Set: MiterPlaneNormalAtEnd(self: Extrusion) = value
"""

    MiterPlaneNormalAtStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MiterPlaneNormalAtStart(self: Extrusion) -> Vector3d

Set: MiterPlaneNormalAtStart(self: Extrusion) = value
"""

    PathEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PathEnd(self: Extrusion) -> Point3d

"""

    PathStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PathStart(self: Extrusion) -> Point3d

"""

    PathTangent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PathTangent(self: Extrusion) -> Vector3d

"""

    ProfileCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileCount(self: Extrusion) -> int

"""



class Hatch(GeometryBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def Get3dCurves(self, outer):
        """ Get3dCurves(self: Hatch, outer: bool) -> Array[Curve] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    PatternIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatternIndex(self: Hatch) -> int

Set: PatternIndex(self: Hatch) = value
"""

    PatternRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatternRotation(self: Hatch) -> float

Set: PatternRotation(self: Hatch) = value
"""

    PatternScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatternScale(self: Hatch) -> float

Set: PatternScale(self: Hatch) = value
"""



class InstanceDefinitionGeometry(GeometryBase):
    """ InstanceDefinitionGeometry() """
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def GetObjectIds(self):
        """ GetObjectIds(self: InstanceDefinitionGeometry) -> Array[Guid] """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: InstanceDefinitionGeometry) -> str

Set: Description(self: InstanceDefinitionGeometry) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: InstanceDefinitionGeometry) -> Guid

Set: Id(self: InstanceDefinitionGeometry) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: InstanceDefinitionGeometry) -> str

Set: Name(self: InstanceDefinitionGeometry) = value
"""



class InstanceReferenceGeometry(GeometryBase):
    """ InstanceReferenceGeometry(instanceDefinitionId: Guid, transform: Transform) """
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, instanceDefinitionId, transform):
        """ __new__(cls: type, instanceDefinitionId: Guid, transform: Transform) """
        pass

    ParentIdefId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentIdefId(self: InstanceReferenceGeometry) -> Guid

"""

    Xform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Xform(self: InstanceReferenceGeometry) -> Transform

"""



class Interpolator(RhinoList[float]):
    """
    Interpolator()
    Interpolator(initialCapacity: int)
    Interpolator(list: RhinoList[float])
    Interpolator(collection: IEnumerable[float])
    Interpolator(amount: int, defaultValue: float)
    """
    def InterpolateCatmullRom(self, t):
        """ InterpolateCatmullRom(self: Interpolator, t: float) -> float """
        pass

    def InterpolateCosine(self, t):
        """ InterpolateCosine(self: Interpolator, t: float) -> float """
        pass

    def InterpolateCubic(self, t):
        """ InterpolateCubic(self: Interpolator, t: float) -> float """
        pass

    def InterpolateLinear(self, t):
        """ InterpolateLinear(self: Interpolator, t: float) -> float """
        pass

    def InterpolateNearestNeighbour(self, t):
        """ InterpolateNearestNeighbour(self: Interpolator, t: float) -> float """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, initialCapacity: int)
        __new__(cls: type, list: RhinoList[float])
        __new__(cls: type, collection: IEnumerable[float])
        __new__(cls: type, amount: int, defaultValue: float)
        """
        pass

    Cyclical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cyclical(self: Interpolator) -> bool

Set: Cyclical(self: Interpolator) = value
"""



class Interval(object):
    """
    Interval(t0: float, t1: float)
    Interval(other: Interval)
    """
    def CompareTo(self, other):
        """ CompareTo(self: Interval, other: Interval) -> int """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Interval, other: Interval, epsilon: float) -> bool """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Interval, other: Interval) -> bool
        Equals(self: Interval, obj: object) -> bool
        """
        pass

    @staticmethod
    def FromIntersection(a, b):
        """ FromIntersection(a: Interval, b: Interval) -> Interval """
        pass

    @staticmethod
    def FromUnion(a, b):
        """ FromUnion(a: Interval, b: Interval) -> Interval """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Interval) -> int """
        pass

    def Grow(self, value):
        """ Grow(self: Interval, value: float) """
        pass

    def IncludesInterval(self, interval, strict=None):
        """
        IncludesInterval(self: Interval, interval: Interval, strict: bool) -> bool
        IncludesInterval(self: Interval, interval: Interval) -> bool
        """
        pass

    def IncludesParameter(self, t, strict=None):
        """
        IncludesParameter(self: Interval, t: float, strict: bool) -> bool
        IncludesParameter(self: Interval, t: float) -> bool
        """
        pass

    def MakeIncreasing(self):
        """ MakeIncreasing(self: Interval) """
        pass

    def NormalizedIntervalAt(self, intervalParameter):
        """ NormalizedIntervalAt(self: Interval, intervalParameter: Interval) -> Interval """
        pass

    def NormalizedParameterAt(self, intervalParameter):
        """ NormalizedParameterAt(self: Interval, intervalParameter: float) -> float """
        pass

    def ParameterAt(self, normalizedParameter):
        """ ParameterAt(self: Interval, normalizedParameter: float) -> float """
        pass

    def ParameterIntervalAt(self, normalizedInterval):
        """ ParameterIntervalAt(self: Interval, normalizedInterval: Interval) -> Interval """
        pass

    def Reverse(self):
        """ Reverse(self: Interval) """
        pass

    def Swap(self):
        """ Swap(self: Interval) """
        pass

    def ToString(self):
        """ ToString(self: Interval) -> str """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Interval]() -> Interval
        
        __new__(cls: type, t0: float, t1: float)
        __new__(cls: type, other: Interval)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(number: float, interval: Interval) -> Interval """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(number: float, interval: Interval) -> Interval """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    IsDecreasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDecreasing(self: Interval) -> bool

"""

    IsIncreasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsIncreasing(self: Interval) -> bool

"""

    IsSingleton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSingleton(self: Interval) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Interval) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Interval) -> float

"""

    Max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Max(self: Interval) -> float

"""

    Mid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mid(self: Interval) -> float

"""

    Min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Min(self: Interval) -> float

"""

    T0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: T0(self: Interval) -> float

Set: T0(self: Interval) = value
"""

    T1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: T1(self: Interval) -> float

Set: T1(self: Interval) = value
"""


    Unset = None


class IsoStatus(Enum):
    """ enum IsoStatus, values: East (5), None (0), North (6), South (4), West (3), X (1), Y (2) """
    East = None
    None = None
    North = None
    South = None
    value__ = None
    West = None
    X = None
    Y = None


class Leader(AnnotationBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class Light(GeometryBase):
    """ Light() """
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def GetAttenuation(self, d):
        """ GetAttenuation(self: Light, d: float) -> float """
        pass

    def GetSpotLightRadii(self, innerRadius, outerRadius):
        """ GetSpotLightRadii(self: Light) -> (bool, float, float) """
        pass

    def SetAttenuation(self, a0, a1, a2):
        """ SetAttenuation(self: Light, a0: float, a1: float, a2: float) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    Ambient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ambient(self: Light) -> Color

Set: Ambient(self: Light) = value
"""

    AttenuationVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttenuationVector(self: Light) -> Vector3d

Set: AttenuationVector(self: Light) = value
"""

    CoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoordinateSystem(self: Light) -> CoordinateSystem

"""

    Diffuse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diffuse(self: Light) -> Color

Set: Diffuse(self: Light) = value
"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: Light) -> Vector3d

Set: Direction(self: Light) = value
"""

    HotSpot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HotSpot(self: Light) -> float

Set: HotSpot(self: Light) = value
"""

    Intensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Intensity(self: Light) -> float

Set: Intensity(self: Light) = value
"""

    IsDirectionalLight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDirectionalLight(self: Light) -> bool

"""

    IsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabled(self: Light) -> bool

Set: IsEnabled(self: Light) = value
"""

    IsLinearLight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLinearLight(self: Light) -> bool

"""

    IsPointLight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPointLight(self: Light) -> bool

"""

    IsRectangularLight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRectangularLight(self: Light) -> bool

"""

    IsSpotLight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSpotLight(self: Light) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Light) -> Vector3d

Set: Length(self: Light) = value
"""

    LightStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LightStyle(self: Light) -> LightStyle

Set: LightStyle(self: Light) = value
"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: Light) -> Point3d

Set: Location(self: Light) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Light) -> str

Set: Name(self: Light) = value
"""

    PerpendicularDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PerpendicularDirection(self: Light) -> Vector3d

"""

    PowerCandela = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PowerCandela(self: Light) -> float

Set: PowerCandela(self: Light) = value
"""

    PowerLumens = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PowerLumens(self: Light) -> float

Set: PowerLumens(self: Light) = value
"""

    PowerWatts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PowerWatts(self: Light) -> float

Set: PowerWatts(self: Light) = value
"""

    Specular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Specular(self: Light) -> Color

Set: Specular(self: Light) = value
"""

    SpotAngleRadians = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpotAngleRadians(self: Light) -> float

Set: SpotAngleRadians(self: Light) = value
"""

    SpotExponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpotExponent(self: Light) -> float

Set: SpotExponent(self: Light) = value
"""

    SpotLightShadowIntensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpotLightShadowIntensity(self: Light) -> float

Set: SpotLightShadowIntensity(self: Light) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: Light) -> Vector3d

Set: Width(self: Light) = value
"""



class LightStyle(Enum):
    """ enum LightStyle, values: Ambient (10), CameraDirectional (4), CameraPoint (5), CameraSpot (6), None (0), WorldDirectional (7), WorldLinear (11), WorldPoint (8), WorldRectangular (12), WorldSpot (9) """
    Ambient = None
    CameraDirectional = None
    CameraPoint = None
    CameraSpot = None
    None = None
    value__ = None
    WorldDirectional = None
    WorldLinear = None
    WorldPoint = None
    WorldRectangular = None
    WorldSpot = None


class Line(object):
    """
    Line(from: Point3d, to: Point3d)
    Line(start: Point3d, span: Vector3d)
    Line(start: Point3d, direction: Vector3d, length: float)
    Line(x0: float, y0: float, z0: float, x1: float, y1: float, z1: float)
    """
    def ClosestParameter(self, testPoint):
        """ ClosestParameter(self: Line, testPoint: Point3d) -> float """
        pass

    def ClosestPoint(self, testPoint, limitToFiniteSegment):
        """ ClosestPoint(self: Line, testPoint: Point3d, limitToFiniteSegment: bool) -> Point3d """
        pass

    def DistanceTo(self, testPoint, limitToFiniteSegment):
        """ DistanceTo(self: Line, testPoint: Point3d, limitToFiniteSegment: bool) -> float """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Line, other: Line, epsilon: float) -> bool """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Line, other: Line) -> bool
        Equals(self: Line, obj: object) -> bool
        """
        pass

    def Extend(self, startLength, endLength):
        """ Extend(self: Line, startLength: float, endLength: float) -> bool """
        pass

    def ExtendThroughBox(self, box, additionalLength=None):
        """
        ExtendThroughBox(self: Line, box: Box) -> bool
        ExtendThroughBox(self: Line, box: Box, additionalLength: float) -> bool
        ExtendThroughBox(self: Line, box: BoundingBox) -> bool
        ExtendThroughBox(self: Line, box: BoundingBox, additionalLength: float) -> bool
        """
        pass

    def Flip(self):
        """ Flip(self: Line) """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Line) -> int """
        pass

    def MaximumDistanceTo(self, *__args):
        """
        MaximumDistanceTo(self: Line, testLine: Line) -> float
        MaximumDistanceTo(self: Line, testPoint: Point3d) -> float
        """
        pass

    def MinimumDistanceTo(self, *__args):
        """
        MinimumDistanceTo(self: Line, testLine: Line) -> float
        MinimumDistanceTo(self: Line, testPoint: Point3d) -> float
        """
        pass

    def PointAt(self, t):
        """ PointAt(self: Line, t: float) -> Point3d """
        pass

    def ToNurbsCurve(self):
        """ ToNurbsCurve(self: Line) -> NurbsCurve """
        pass

    def ToString(self):
        """ ToString(self: Line) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: Line, xform: Transform) -> bool """
        pass

    def TryGetPlane(self, plane):
        """ TryGetPlane(self: Line) -> (bool, Plane) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Line]() -> Line
        
        __new__(cls: type, from: Point3d, to: Point3d)
        __new__(cls: type, start: Point3d, span: Vector3d)
        __new__(cls: type, start: Point3d, direction: Vector3d, length: float)
        __new__(cls: type, x0: float, y0: float, z0: float, x1: float, y1: float, z1: float)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: Line) -> BoundingBox

"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: Line) -> Vector3d

"""

    From = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: From(self: Line) -> Point3d

Set: From(self: Line) = value
"""

    FromX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromX(self: Line) -> float

Set: FromX(self: Line) = value
"""

    FromY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromY(self: Line) -> float

Set: FromY(self: Line) = value
"""

    FromZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromZ(self: Line) -> float

Set: FromZ(self: Line) = value
"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Line) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Line) -> float

Set: Length(self: Line) = value
"""

    To = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: To(self: Line) -> Point3d

Set: To(self: Line) = value
"""

    ToX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToX(self: Line) -> float

Set: ToX(self: Line) = value
"""

    ToY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToY(self: Line) -> float

Set: ToY(self: Line) = value
"""

    ToZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToZ(self: Line) -> float

Set: ToZ(self: Line) = value
"""

    UnitTangent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitTangent(self: Line) -> Vector3d

"""


    Unset = None


class LinearDimension(AnnotationBase):
    """
    LinearDimension()
    LinearDimension(dimensionPlane: Plane, extensionLine1End: Point2d, extensionLine2End: Point2d, pointOnDimensionLine: Point2d)
    """
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def SetLocations(self, extensionLine1End, extensionLine2End, pointOnDimensionLine):
        """ SetLocations(self: LinearDimension, extensionLine1End: Point2d, extensionLine2End: Point2d, pointOnDimensionLine: Point2d) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, dimensionPlane=None, extensionLine1End=None, extensionLine2End=None, pointOnDimensionLine=None):
        """
        __new__(cls: type)
        __new__(cls: type, dimensionPlane: Plane, extensionLine1End: Point2d, extensionLine2End: Point2d, pointOnDimensionLine: Point2d)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    Aligned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Aligned(self: LinearDimension) -> bool

Set: Aligned(self: LinearDimension) = value
"""

    Arrowhead1End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arrowhead1End(self: LinearDimension) -> Point2d

"""

    Arrowhead2End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arrowhead2End(self: LinearDimension) -> Point2d

"""

    DimensionStyleIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionStyleIndex(self: LinearDimension) -> int

Set: DimensionStyleIndex(self: LinearDimension) = value
"""

    DistanceBetweenArrowTips = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistanceBetweenArrowTips(self: LinearDimension) -> float

"""

    ExtensionLine1End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionLine1End(self: LinearDimension) -> Point2d

"""

    ExtensionLine2End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionLine2End(self: LinearDimension) -> Point2d

"""

    TextPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextPosition(self: LinearDimension) -> Point2d

Set: TextPosition(self: LinearDimension) = value
"""



class LineCurve(Curve):
    """
    LineCurve()
    LineCurve(other: LineCurve)
    LineCurve(from: Point2d, to: Point2d)
    LineCurve(from: Point3d, to: Point3d)
    LineCurve(line: Line)
    LineCurve(line: Line, t0: float, t1: float)
    """
    def Dispose(self):
        """ Dispose(self: Curve, disposing: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, other: LineCurve)
        __new__(cls: type, from: Point2d, to: Point2d)
        __new__(cls: type, from: Point3d, to: Point3d)
        __new__(cls: type, line: Line)
        __new__(cls: type, line: Line, t0: float, t1: float)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    Line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Line(self: LineCurve) -> Line

Set: Line(self: LineCurve) = value
"""



class LoftType(Enum):
    """ enum LoftType, values: Developable (4), Loose (1), Normal (0), Straight (3), Tight (2), Uniform (5) """
    Developable = None
    Loose = None
    Normal = None
    Straight = None
    Tight = None
    Uniform = None
    value__ = None


class Matrix(object):
    """
    Matrix(rowCount: int, columnCount: int)
    Matrix(xform: Transform)
    """
    def BackSolve(self, zeroTolerance, b):
        """ BackSolve(self: Matrix, zeroTolerance: float, b: Array[float]) -> Array[float] """
        pass

    def BackSolvePoints(self, zeroTolerance, b):
        """ BackSolvePoints(self: Matrix, zeroTolerance: float, b: Array[Point3d]) -> Array[Point3d] """
        pass

    def Dispose(self):
        """ Dispose(self: Matrix) """
        pass

    def Duplicate(self):
        """ Duplicate(self: Matrix) -> Matrix """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Matrix) -> int """
        pass

    def Invert(self, zeroTolerance):
        """ Invert(self: Matrix, zeroTolerance: float) -> bool """
        pass

    def RowReduce(self, zeroTolerance, *__args):
        """
        RowReduce(self: Matrix, zeroTolerance: float, b: Array[Point3d]) -> (int, float)
        RowReduce(self: Matrix, zeroTolerance: float, b: Array[float]) -> (int, float)
        RowReduce(self: Matrix, zeroTolerance: float) -> (int, float, float)
        """
        pass

    def Scale(self, s):
        """ Scale(self: Matrix, s: float) """
        pass

    def SetDiagonal(self, d):
        """ SetDiagonal(self: Matrix, d: float) """
        pass

    def SwapColumns(self, columnA, columnB):
        """ SwapColumns(self: Matrix, columnA: int, columnB: int) -> bool """
        pass

    def SwapRows(self, rowA, rowB):
        """ SwapRows(self: Matrix, rowA: int, rowB: int) -> bool """
        pass

    def Transpose(self):
        """ Transpose(self: Matrix) -> bool """
        pass

    def Zero(self):
        """ Zero(self: Matrix) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, rowCount: int, columnCount: int)
        __new__(cls: type, xform: Transform)
        """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(a: Matrix, b: Matrix) -> Matrix """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(a: Matrix, b: Matrix) -> Matrix """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    ColumnCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColumnCount(self: Matrix) -> int

"""

    IsColumnOrthogonal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsColumnOrthogonal(self: Matrix) -> bool

"""

    IsColumnOrthoNormal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsColumnOrthoNormal(self: Matrix) -> bool

"""

    IsRowOrthogonal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRowOrthogonal(self: Matrix) -> bool

"""

    IsRowOrthoNormal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRowOrthoNormal(self: Matrix) -> bool

"""

    IsSquare = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSquare(self: Matrix) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Matrix) -> bool

"""

    RowCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RowCount(self: Matrix) -> int

"""



class Mesh(GeometryBase):
    """ Mesh() """
    def Append(self, other):
        """ Append(self: Mesh, other: Mesh) """
        pass

    def ClearTextureData(self):
        """ ClearTextureData(self: Mesh) """
        pass

    def Compact(self):
        """ Compact(self: Mesh) -> bool """
        pass

    def CopyFrom(self, other):
        """ CopyFrom(self: Mesh, other: Mesh) """
        pass

    def CreatePartitions(self, maximumVertexCount, maximumTriangleCount):
        """ CreatePartitions(self: Mesh, maximumVertexCount: int, maximumTriangleCount: int) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def Duplicate(self):
        """ Duplicate(self: Mesh) -> GeometryBase """
        pass

    def DuplicateMesh(self):
        """ DuplicateMesh(self: Mesh) -> Mesh """
        pass

    def EvaluateMeshGeometry(self, surface):
        """ EvaluateMeshGeometry(self: Mesh, surface: Surface) -> bool """
        pass

    def Flip(self, vertexNormals, faceNormals, faceOrientation):
        """ Flip(self: Mesh, vertexNormals: bool, faceNormals: bool, faceOrientation: bool) """
        pass

    def GetCachedTextureCoordinates(self, textureMappingId):
        """ GetCachedTextureCoordinates(self: Mesh, textureMappingId: Guid) -> CachedTextureCoordinates """
        pass

    def GetNakedEdgePointStatus(self):
        """ GetNakedEdgePointStatus(self: Mesh) -> Array[bool] """
        pass

    def GetPartition(self, which):
        """ GetPartition(self: Mesh, which: int) -> MeshPart """
        pass

    def IsManifold(self, topologicalTest, isOriented, hasBoundary):
        """ IsManifold(self: Mesh, topologicalTest: bool) -> (bool, bool, bool) """
        pass

    def IsPointInside(self, point, tolerance, strictlyIn):
        """ IsPointInside(self: Mesh, point: Point3d, tolerance: float, strictlyIn: bool) -> bool """
        pass

    def SetCachedTextureCoordinates(self, tm, xf):
        """ SetCachedTextureCoordinates(self: Mesh, tm: TextureMapping, xf: Transform) -> Transform """
        pass

    def SolidOrientation(self):
        """ SolidOrientation(self: Mesh) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    DisjointMeshCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisjointMeshCount(self: Mesh) -> int

"""

    FaceNormals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FaceNormals(self: Mesh) -> MeshFaceNormalList

"""

    Faces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Faces(self: Mesh) -> MeshFaceList

"""

    HasCachedTextureCoordinates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasCachedTextureCoordinates(self: Mesh) -> bool

"""

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsClosed(self: Mesh) -> bool

"""

    Normals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Normals(self: Mesh) -> MeshVertexNormalList

"""

    PartitionCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartitionCount(self: Mesh) -> int

"""

    TextureCoordinates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextureCoordinates(self: Mesh) -> MeshTextureCoordinateList

"""

    TopologyEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TopologyEdges(self: Mesh) -> MeshTopologyEdgeList

"""

    TopologyVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TopologyVertices(self: Mesh) -> MeshTopologyVertexList

"""

    VertexColors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VertexColors(self: Mesh) -> MeshVertexColorList

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: Mesh) -> MeshVertexList

"""



class MeshFace(object):
    """
    MeshFace(a: int, b: int, c: int)
    MeshFace(a: int, b: int, c: int, d: int)
    """
    def Flip(self):
        """ Flip(self: MeshFace) -> MeshFace """
        pass

    def IsValid(self, vertexCount=None):
        """
        IsValid(self: MeshFace, vertexCount: int) -> bool
        IsValid(self: MeshFace) -> bool
        """
        pass

    def Set(self, a, b, c, d=None):
        """ Set(self: MeshFace, a: int, b: int, c: int, d: int)Set(self: MeshFace, a: int, b: int, c: int) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, a, b, c, d=None):
        """
        __new__[MeshFace]() -> MeshFace
        
        __new__(cls: type, a: int, b: int, c: int)
        __new__(cls: type, a: int, b: int, c: int, d: int)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    A = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: A(self: MeshFace) -> int

Set: A(self: MeshFace) = value
"""

    B = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: B(self: MeshFace) -> int

Set: B(self: MeshFace) = value
"""

    C = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: C(self: MeshFace) -> int

Set: C(self: MeshFace) = value
"""

    D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: D(self: MeshFace) -> int

Set: D(self: MeshFace) = value
"""

    IsQuad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsQuad(self: MeshFace) -> bool

"""

    IsTriangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTriangle(self: MeshFace) -> bool

"""


    Unset = None


class MeshingParameters(object):
    """ MeshingParameters() """
    def Dispose(self):
        """ Dispose(self: MeshingParameters) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    ComputeCurvature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComputeCurvature(self: MeshingParameters) -> bool

Set: ComputeCurvature(self: MeshingParameters) = value
"""

    GridAmplification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridAmplification(self: MeshingParameters) -> float

Set: GridAmplification(self: MeshingParameters) = value
"""

    GridAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridAngle(self: MeshingParameters) -> float

Set: GridAngle(self: MeshingParameters) = value
"""

    GridAspectRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridAspectRatio(self: MeshingParameters) -> float

Set: GridAspectRatio(self: MeshingParameters) = value
"""

    GridMaxCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridMaxCount(self: MeshingParameters) -> int

Set: GridMaxCount(self: MeshingParameters) = value
"""

    GridMinCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridMinCount(self: MeshingParameters) -> int

Set: GridMinCount(self: MeshingParameters) = value
"""

    JaggedSeams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JaggedSeams(self: MeshingParameters) -> bool

Set: JaggedSeams(self: MeshingParameters) = value
"""

    MaximumEdgeLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumEdgeLength(self: MeshingParameters) -> float

Set: MaximumEdgeLength(self: MeshingParameters) = value
"""

    MinimumEdgeLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumEdgeLength(self: MeshingParameters) -> float

Set: MinimumEdgeLength(self: MeshingParameters) = value
"""

    MinimumTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumTolerance(self: MeshingParameters) -> float

Set: MinimumTolerance(self: MeshingParameters) = value
"""

    RefineAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RefineAngle(self: MeshingParameters) -> float

Set: RefineAngle(self: MeshingParameters) = value
"""

    RefineGrid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RefineGrid(self: MeshingParameters) -> bool

Set: RefineGrid(self: MeshingParameters) = value
"""

    RelativeTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelativeTolerance(self: MeshingParameters) -> float

Set: RelativeTolerance(self: MeshingParameters) = value
"""

    SimplePlanes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SimplePlanes(self: MeshingParameters) -> bool

Set: SimplePlanes(self: MeshingParameters) = value
"""

    Tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tolerance(self: MeshingParameters) -> float

Set: Tolerance(self: MeshingParameters) = value
"""



class MeshingParameterStyle(Enum):
    """ enum MeshingParameterStyle, values: Custom (9), Fast (1), None (0), PerObject (10), Quality (2) """
    Custom = None
    Fast = None
    None = None
    PerObject = None
    Quality = None
    value__ = None


class MeshPart(object):
    # no doc
    EndFaceIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndFaceIndex(self: MeshPart) -> int

"""

    EndVertexIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndVertexIndex(self: MeshPart) -> int

"""

    StartFaceIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartFaceIndex(self: MeshPart) -> int

"""

    StartVertexIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartVertexIndex(self: MeshPart) -> int

"""

    TriangleCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TriangleCount(self: MeshPart) -> int

"""

    VertexCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VertexCount(self: MeshPart) -> int

"""



class MeshPoint(object):
    # no doc
    ComponentIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentIndex(self: MeshPoint) -> ComponentIndex

"""

    EdgeIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeIndex(self: MeshPoint) -> int

"""

    EdgeParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeParameter(self: MeshPoint) -> float

"""

    FaceIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FaceIndex(self: MeshPoint) -> int

"""

    Mesh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mesh(self: MeshPoint) -> Mesh

"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: MeshPoint) -> Point3d

"""

    T = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: T(self: MeshPoint) -> Array[float]

"""

    Triangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Triangle(self: MeshPoint) -> Char

"""



class MeshType(Enum):
    """ enum MeshType, values: Analysis (2), Any (4), Default (0), Preview (3), Render (1) """
    Analysis = None
    Any = None
    Default = None
    Preview = None
    Render = None
    value__ = None


class MorphControl(GeometryBase):
    """ MorphControl(originCurve: NurbsCurve, targetCurve: NurbsCurve) """
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, originCurve, targetCurve):
        """
        __new__(cls: type, originCurve: NurbsCurve, targetCurve: NurbsCurve)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    PreserveStructure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreserveStructure(self: MorphControl) -> bool

Set: PreserveStructure(self: MorphControl) = value
"""

    QuickPreview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuickPreview(self: MorphControl) -> bool

Set: QuickPreview(self: MorphControl) = value
"""

    SpaceMorphTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpaceMorphTolerance(self: MorphControl) -> float

Set: SpaceMorphTolerance(self: MorphControl) = value
"""



class NurbsCurve(Curve):
    """
    NurbsCurve(other: NurbsCurve)
    NurbsCurve(degree: int, pointCount: int)
    NurbsCurve(dimension: int, rational: bool, order: int, pointCount: int)
    """
    @staticmethod
    def Create(periodic, degree, points):
        """ Create(periodic: bool, degree: int, points: IEnumerable[Point3d]) -> NurbsCurve """
        pass

    @staticmethod
    def CreateFromArc(arc):
        """ CreateFromArc(arc: Arc) -> NurbsCurve """
        pass

    @staticmethod
    def CreateFromCircle(circle):
        """ CreateFromCircle(circle: Circle) -> NurbsCurve """
        pass

    @staticmethod
    def CreateFromEllipse(ellipse):
        """ CreateFromEllipse(ellipse: Ellipse) -> NurbsCurve """
        pass

    @staticmethod
    def CreateFromLine(line):
        """ CreateFromLine(line: Line) -> NurbsCurve """
        pass

    def Dispose(self):
        """ Dispose(self: Curve, disposing: bool) """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: NurbsCurve, other: NurbsCurve, epsilon: float) -> bool """
        pass

    def GrevilleParameter(self, index):
        """ GrevilleParameter(self: NurbsCurve, index: int) -> float """
        pass

    def GrevilleParameters(self):
        """ GrevilleParameters(self: NurbsCurve) -> Array[float] """
        pass

    def GrevillePoint(self, index):
        """ GrevillePoint(self: NurbsCurve, index: int) -> Point3d """
        pass

    def GrevillePoints(self):
        """ GrevillePoints(self: NurbsCurve) -> Point3dList """
        pass

    def IncreaseDegree(self, desiredDegree):
        """ IncreaseDegree(self: NurbsCurve, desiredDegree: int) -> bool """
        pass

    @staticmethod
    def IsDuplicate(curveA, curveB, ignoreParameterization, tolerance):
        """ IsDuplicate(curveA: NurbsCurve, curveB: NurbsCurve, ignoreParameterization: bool, tolerance: float) -> bool """
        pass

    def MakePiecewiseBezier(self, setEndWeightsToOne):
        """ MakePiecewiseBezier(self: NurbsCurve, setEndWeightsToOne: bool) -> bool """
        pass

    def Reparameterize(self, c):
        """ Reparameterize(self: NurbsCurve, c: float) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, other: NurbsCurve)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, degree: int, pointCount: int)
        __new__(cls: type, dimension: int, rational: bool, order: int, pointCount: int)
        """
        pass

    HasBezierSpans = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasBezierSpans(self: NurbsCurve) -> bool

"""

    IsRational = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRational(self: NurbsCurve) -> bool

"""

    Knots = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Knots(self: NurbsCurve) -> NurbsCurveKnotList

"""

    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Order(self: NurbsCurve) -> int

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: NurbsCurve) -> NurbsCurvePointList

"""



class NurbsSurface(Surface):
    """ NurbsSurface(other: NurbsSurface) """
    def CopyFrom(self, other):
        """ CopyFrom(self: NurbsSurface, other: NurbsSurface) """
        pass

    @staticmethod
    def Create(dimension, isRational, order0, order1, controlPointCount0, controlPointCount1):
        """ Create(dimension: int, isRational: bool, order0: int, order1: int, controlPointCount0: int, controlPointCount1: int) -> NurbsSurface """
        pass

    @staticmethod
    def CreateFromCone(cone):
        """ CreateFromCone(cone: Cone) -> NurbsSurface """
        pass

    @staticmethod
    def CreateFromCylinder(cylinder):
        """ CreateFromCylinder(cylinder: Cylinder) -> NurbsSurface """
        pass

    @staticmethod
    def CreateFromSphere(sphere):
        """ CreateFromSphere(sphere: Sphere) -> NurbsSurface """
        pass

    @staticmethod
    def CreateFromTorus(torus):
        """ CreateFromTorus(torus: Torus) -> NurbsSurface """
        pass

    @staticmethod
    def CreateRuledSurface(curveA, curveB):
        """ CreateRuledSurface(curveA: Curve, curveB: Curve) -> NurbsSurface """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: NurbsSurface, other: NurbsSurface, epsilon: float) -> bool """
        pass

    def IncreaseDegreeU(self, desiredDegree):
        """ IncreaseDegreeU(self: NurbsSurface, desiredDegree: int) -> bool """
        pass

    def IncreaseDegreeV(self, desiredDegree):
        """ IncreaseDegreeV(self: NurbsSurface, desiredDegree: int) -> bool """
        pass

    def MakeNonRational(self):
        """ MakeNonRational(self: NurbsSurface) -> bool """
        pass

    def MakeRational(self):
        """ MakeRational(self: NurbsSurface) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, other):
        """
        __new__(cls: type, other: NurbsSurface)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    IsRational = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRational(self: NurbsSurface) -> bool

"""

    KnotsU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KnotsU(self: NurbsSurface) -> NurbsSurfaceKnotList

"""

    KnotsV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KnotsV(self: NurbsSurface) -> NurbsSurfaceKnotList

"""

    OrderU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderU(self: NurbsSurface) -> int

"""

    OrderV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderV(self: NurbsSurface) -> int

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: NurbsSurface) -> NurbsSurfacePointList

"""



class OrdinateDimension(AnnotationBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class PipeCapMode(Enum):
    """ enum PipeCapMode, values: Flat (1), None (0), Round (2) """
    Flat = None
    None = None
    Round = None
    value__ = None


class Plane(object):
    """
    Plane(other: Plane)
    Plane(origin: Point3d, normal: Vector3d)
    Plane(origin: Point3d, xDirection: Vector3d, yDirection: Vector3d)
    Plane(origin: Point3d, xPoint: Point3d, yPoint: Point3d)
    Plane(a: float, b: float, c: float, d: float)
    """
    def ClosestParameter(self, testPoint, s, t):
        """ ClosestParameter(self: Plane, testPoint: Point3d) -> (bool, float, float) """
        pass

    def ClosestPoint(self, testPoint):
        """ ClosestPoint(self: Plane, testPoint: Point3d) -> Point3d """
        pass

    def DistanceTo(self, testPoint):
        """ DistanceTo(self: Plane, testPoint: Point3d) -> float """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Plane, other: Plane, epsilon: float) -> bool """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Plane, plane: Plane) -> bool
        Equals(self: Plane, obj: object) -> bool
        """
        pass

    def ExtendThroughBox(self, box, s, t):
        """
        ExtendThroughBox(self: Plane, box: Box) -> (bool, Interval, Interval)
        ExtendThroughBox(self: Plane, box: BoundingBox) -> (bool, Interval, Interval)
        """
        pass

    def Flip(self):
        """ Flip(self: Plane) """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Plane) -> int """
        pass

    def GetPlaneEquation(self):
        """ GetPlaneEquation(self: Plane) -> Array[float] """
        pass

    def PointAt(self, u, v, w=None):
        """
        PointAt(self: Plane, u: float, v: float, w: float) -> Point3d
        PointAt(self: Plane, u: float, v: float) -> Point3d
        """
        pass

    def RemapToPlaneSpace(self, ptSample, ptPlane):
        """ RemapToPlaneSpace(self: Plane, ptSample: Point3d) -> (bool, Point3d) """
        pass

    def Rotate(self, *__args):
        """
        Rotate(self: Plane, angle: float, axis: Vector3d, centerOfRotation: Point3d) -> bool
        Rotate(self: Plane, sinAngle: float, cosAngle: float, axis: Vector3d, centerOfRotation: Point3d) -> bool
        Rotate(self: Plane, sinAngle: float, cosAngle: float, axis: Vector3d) -> bool
        Rotate(self: Plane, angle: float, axis: Vector3d) -> bool
        """
        pass

    def ToString(self):
        """ ToString(self: Plane) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: Plane, xform: Transform) -> bool """
        pass

    def Translate(self, delta):
        """ Translate(self: Plane, delta: Vector3d) -> bool """
        pass

    def ValueAt(self, p):
        """ ValueAt(self: Plane, p: Point3d) -> float """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Plane]() -> Plane
        
        __new__(cls: type, other: Plane)
        __new__(cls: type, origin: Point3d, normal: Vector3d)
        __new__(cls: type, origin: Point3d, xDirection: Vector3d, yDirection: Vector3d)
        __new__(cls: type, origin: Point3d, xPoint: Point3d, yPoint: Point3d)
        __new__(cls: type, a: float, b: float, c: float, d: float)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Plane) -> bool

"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Normal(self: Plane) -> Vector3d

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Origin(self: Plane) -> Point3d

Set: Origin(self: Plane) = value
"""

    OriginX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginX(self: Plane) -> float

Set: OriginX(self: Plane) = value
"""

    OriginY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginY(self: Plane) -> float

Set: OriginY(self: Plane) = value
"""

    OriginZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginZ(self: Plane) -> float

Set: OriginZ(self: Plane) = value
"""

    XAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XAxis(self: Plane) -> Vector3d

Set: XAxis(self: Plane) = value
"""

    YAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YAxis(self: Plane) -> Vector3d

Set: YAxis(self: Plane) = value
"""

    ZAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZAxis(self: Plane) -> Vector3d

Set: ZAxis(self: Plane) = value
"""


    Unset = None
    WorldXY = None
    WorldYZ = None
    WorldZX = None


class PlaneFitResult(Enum):
    """ enum PlaneFitResult, values: Failure (-1), Inconclusive (1), Success (0) """
    Failure = None
    Inconclusive = None
    Success = None
    value__ = None


class Point2d(object):
    """
    Point2d(x: float, y: float)
    Point2d(vector: Vector2d)
    Point2d(point: Point2d)
    Point2d(point: Point3d)
    """
    @staticmethod
    def Add(*__args):
        """
        Add(point1: Point2d, point2: Point2d) -> Point2d
        Add(vector: Vector2d, point: Point2d) -> Point2d
        Add(point: Point2d, vector: Vector2d) -> Point2d
        """
        pass

    def CompareTo(self, other):
        """ CompareTo(self: Point2d, other: Point2d) -> int """
        pass

    def DistanceTo(self, other):
        """ DistanceTo(self: Point2d, other: Point2d) -> float """
        pass

    @staticmethod
    def Divide(point, t):
        """ Divide(point: Point2d, t: float) -> Point2d """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Point2d, other: Point2d, epsilon: float) -> bool """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Point2d, point: Point2d) -> bool
        Equals(self: Point2d, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Point2d) -> int """
        pass

    @staticmethod
    def Multiply(*__args):
        """
        Multiply(t: float, point: Point2d) -> Point2d
        Multiply(point: Point2d, t: float) -> Point2d
        """
        pass

    @staticmethod
    def Subtract(*__args):
        """
        Subtract(point1: Point2d, point2: Point2d) -> Vector2d
        Subtract(point: Point2d, vector: Vector2d) -> Point2d
        """
        pass

    def ToString(self):
        """ ToString(self: Point2d) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: Point2d, xform: Transform) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Point2d]() -> Point2d
        
        __new__(cls: type, x: float, y: float)
        __new__(cls: type, vector: Vector2d)
        __new__(cls: type, point: Point2d)
        __new__(cls: type, point: Point3d)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(point1: Point2d, point2: Point2d) -> Point2d
        __radd__(vector: Vector2d, point: Point2d) -> Point2d
        """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(t: float, point: Point2d) -> Point2d """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(point1: Point2d, point2: Point2d) -> Vector2d """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Point2d) -> bool

"""

    MaximumCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumCoordinate(self: Point2d) -> float

"""

    MinimumCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumCoordinate(self: Point2d) -> float

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Point2d) -> float

Set: X(self: Point2d) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Point2d) -> float

Set: Y(self: Point2d) = value
"""


    Origin = None
    Unset = None


class Point2f(object):
    """
    Point2f(x: Single, y: Single)
    Point2f(x: float, y: float)
    """
    def CompareTo(self, other):
        """ CompareTo(self: Point2f, other: Point2f) -> int """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Point2f, other: Point2f, epsilon: Single) -> bool """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Point2f, point: Point2f) -> bool
        Equals(self: Point2f, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Point2f) -> int """
        pass

    def ToString(self):
        """ ToString(self: Point2f) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    @staticmethod # known case of __new__
    def __new__(self, x, y):
        """
        __new__[Point2f]() -> Point2f
        
        __new__(cls: type, x: Single, y: Single)
        __new__(cls: type, x: float, y: float)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Point2f) -> bool

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Point2f) -> Single

Set: X(self: Point2f) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Point2f) -> Single

Set: Y(self: Point2f) = value
"""


    Unset = None


class Point3d(object):
    """
    Point3d(x: float, y: float, z: float)
    Point3d(vector: Vector3d)
    Point3d(point: Point3f)
    Point3d(point: Point3d)
    Point3d(point: Point4d)
    """
    @staticmethod
    def Add(*__args):
        """
        Add(point: Point3d, vector: Vector3f) -> Point3d
        Add(vector: Vector3d, point: Point3d) -> Point3d
        Add(point1: Point3d, point2: Point3d) -> Point3d
        Add(point: Point3d, vector: Vector3d) -> Point3d
        """
        pass

    def CompareTo(self, other):
        """ CompareTo(self: Point3d, other: Point3d) -> int """
        pass

    @staticmethod
    def CullDuplicates(points, tolerance):
        """ CullDuplicates(points: IEnumerable[Point3d], tolerance: float) -> Array[Point3d] """
        pass

    def DistanceTo(self, other):
        """ DistanceTo(self: Point3d, other: Point3d) -> float """
        pass

    @staticmethod
    def Divide(point, t):
        """ Divide(point: Point3d, t: float) -> Point3d """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Point3d, other: Point3d, epsilon: float) -> bool """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Point3d, point: Point3d) -> bool
        Equals(self: Point3d, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Point3d) -> int """
        pass

    def Interpolate(self, pA, pB, t):
        """ Interpolate(self: Point3d, pA: Point3d, pB: Point3d, t: float) """
        pass

    @staticmethod
    def Multiply(*__args):
        """
        Multiply(t: float, point: Point3d) -> Point3d
        Multiply(point: Point3d, t: float) -> Point3d
        """
        pass

    @staticmethod
    def Subtract(*__args):
        """
        Subtract(point1: Point3d, point2: Point3d) -> Vector3d
        Subtract(point: Point3d, vector: Vector3d) -> Point3d
        """
        pass

    def ToString(self):
        """ ToString(self: Point3d) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: Point3d, xform: Transform) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Point3d]() -> Point3d
        
        __new__(cls: type, x: float, y: float, z: float)
        __new__(cls: type, vector: Vector3d)
        __new__(cls: type, point: Point3f)
        __new__(cls: type, point: Point3d)
        __new__(cls: type, point: Point4d)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(vector: Vector3d, point: Point3d) -> Point3d
        __radd__(point1: Point3d, point2: Point3d) -> Point3d
        """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(t: float, point: Point3d) -> Point3d """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(point1: Point3d, point2: Point3d) -> Vector3d """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Point3d) -> bool

"""

    MaximumCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumCoordinate(self: Point3d) -> float

"""

    MinimumCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumCoordinate(self: Point3d) -> float

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Point3d) -> float

Set: X(self: Point3d) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Point3d) -> float

Set: Y(self: Point3d) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: Point3d) -> float

Set: Z(self: Point3d) = value
"""


    Origin = None
    Unset = None


class Point3dGrid(GeometryBase):
    """
    Point3dGrid()
    Point3dGrid(rows: int, columns: int)
    """
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, rows=None, columns=None):
        """
        __new__(cls: type)
        __new__(cls: type, rows: int, columns: int)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class Point3f(object):
    """ Point3f(x: Single, y: Single, z: Single) """
    def CompareTo(self, other):
        """ CompareTo(self: Point3f, other: Point3f) -> int """
        pass

    def DistanceTo(self, other):
        """ DistanceTo(self: Point3f, other: Point3f) -> float """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Point3f, other: Point3f, epsilon: Single) -> bool """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Point3f, point: Point3f) -> bool
        Equals(self: Point3f, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Point3f) -> int """
        pass

    @staticmethod
    def Subtract(point1, point2):
        """ Subtract(point1: Point3f, point2: Point3f) -> Vector3f """
        pass

    def ToString(self):
        """ ToString(self: Point3f) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: Point3f, xform: Transform) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    @staticmethod # known case of __new__
    def __new__(self, x, y, z):
        """
        __new__[Point3f]() -> Point3f
        
        __new__(cls: type, x: Single, y: Single, z: Single)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(point1: Point3f, point2: Point3f) -> Vector3f """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Point3f) -> bool

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Point3f) -> Single

Set: X(self: Point3f) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Point3f) -> Single

Set: Y(self: Point3f) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: Point3f) -> Single

Set: Z(self: Point3f) = value
"""


    Origin = None
    Unset = None


class Point4d(object):
    """
    Point4d(x: float, y: float, z: float, w: float)
    Point4d(point: Point3d)
    """
    @staticmethod
    def Add(point1, point2):
        """ Add(point1: Point4d, point2: Point4d) -> Point4d """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Point4d, other: Point4d, epsilon: float) -> bool """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Point4d, point: Point4d) -> bool
        Equals(self: Point4d, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Point4d) -> int """
        pass

    @staticmethod
    def Multiply(point, d):
        """ Multiply(point: Point4d, d: float) -> Point4d """
        pass

    @staticmethod
    def Subtract(point1, point2):
        """ Subtract(point1: Point4d, point2: Point4d) -> Point4d """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Point4d]() -> Point4d
        
        __new__(cls: type, x: float, y: float, z: float, w: float)
        __new__(cls: type, point: Point3d)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(point1: Point4d, point2: Point4d) -> Point4d """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(point1: Point4d, point2: Point4d) -> float """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(point1: Point4d, point2: Point4d) -> Point4d """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    W = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: W(self: Point4d) -> float

Set: W(self: Point4d) = value
"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Point4d) -> float

Set: X(self: Point4d) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Point4d) -> float

Set: Y(self: Point4d) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: Point4d) -> float

Set: Z(self: Point4d) = value
"""


    Unset = None


class PointCloud(GeometryBase):
    """
    PointCloud()
    PointCloud(other: PointCloud)
    PointCloud(points: IEnumerable[Point3d])
    """
    def Add(self, point, *__args):
        """ Add(self: PointCloud, point: Point3d, color: Color)Add(self: PointCloud, point: Point3d, normal: Vector3d, color: Color)Add(self: PointCloud, point: Point3d)Add(self: PointCloud, point: Point3d, normal: Vector3d) """
        pass

    def AddRange(self, points):
        """ AddRange(self: PointCloud, points: IEnumerable[Point3d]) """
        pass

    def AppendNew(self):
        """ AppendNew(self: PointCloud) -> PointCloudItem """
        pass

    def ClearColors(self):
        """ ClearColors(self: PointCloud) """
        pass

    def ClearHiddenFlags(self):
        """ ClearHiddenFlags(self: PointCloud) """
        pass

    def ClearNormals(self):
        """ ClearNormals(self: PointCloud) """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def GetColors(self):
        """ GetColors(self: PointCloud) -> Array[Color] """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: PointCloud) -> IEnumerator[PointCloudItem] """
        pass

    def GetNormals(self):
        """ GetNormals(self: PointCloud) -> Array[Vector3d] """
        pass

    def GetPoints(self):
        """ GetPoints(self: PointCloud) -> Array[Point3d] """
        pass

    def Insert(self, index, point, *__args):
        """ Insert(self: PointCloud, index: int, point: Point3d, color: Color)Insert(self: PointCloud, index: int, point: Point3d, normal: Vector3d, color: Color)Insert(self: PointCloud, index: int, point: Point3d)Insert(self: PointCloud, index: int, point: Point3d, normal: Vector3d) """
        pass

    def InsertNew(self, index):
        """ InsertNew(self: PointCloud, index: int) -> PointCloudItem """
        pass

    def InsertRange(self, index, points):
        """ InsertRange(self: PointCloud, index: int, points: IEnumerable[Point3d]) """
        pass

    def Merge(self, other):
        """ Merge(self: PointCloud, other: PointCloud) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: PointCloud, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PointCloudItem](enumerable: IEnumerable[PointCloudItem], value: PointCloudItem) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, other: PointCloud)
        __new__(cls: type, points: IEnumerable[Point3d])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    ContainsColors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContainsColors(self: PointCloud) -> bool

"""

    ContainsHiddenFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContainsHiddenFlags(self: PointCloud) -> bool

"""

    ContainsNormals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContainsNormals(self: PointCloud) -> bool

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: PointCloud) -> int

"""

    HiddenPointCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HiddenPointCount(self: PointCloud) -> int

"""



class PointCloudItem(object):
    # no doc
    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: PointCloudItem) -> Color

Set: Color(self: PointCloudItem) = value
"""

    Hidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hidden(self: PointCloudItem) -> bool

Set: Hidden(self: PointCloudItem) = value
"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: PointCloudItem) -> int

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: PointCloudItem) -> Point3d

Set: Location(self: PointCloudItem) = value
"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Normal(self: PointCloudItem) -> Vector3d

Set: Normal(self: PointCloudItem) = value
"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: PointCloudItem) -> float

Set: X(self: PointCloudItem) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: PointCloudItem) -> float

Set: Y(self: PointCloudItem) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: PointCloudItem) -> float

Set: Z(self: PointCloudItem) = value
"""



class PointContainment(Enum):
    """ enum PointContainment, values: Coincident (3), Inside (1), Outside (2), Unset (0) """
    Coincident = None
    Inside = None
    Outside = None
    Unset = None
    value__ = None


class PointFaceRelation(Enum):
    """ enum PointFaceRelation, values: Boundary (2), Exterior (0), Interior (1) """
    Boundary = None
    Exterior = None
    Interior = None
    value__ = None


class PolyCurve(Curve):
    """ PolyCurve() """
    def Append(self, *__args):
        """
        Append(self: PolyCurve, curve: Curve) -> bool
        Append(self: PolyCurve, arc: Arc) -> bool
        Append(self: PolyCurve, line: Line) -> bool
        """
        pass

    def Dispose(self):
        """ Dispose(self: Curve, disposing: bool) """
        pass

    def Duplicate(self):
        """ Duplicate(self: PolyCurve) -> GeometryBase """
        pass

    def DuplicatePolyCurve(self):
        """ DuplicatePolyCurve(self: PolyCurve) -> PolyCurve """
        pass

    def Explode(self):
        """ Explode(self: PolyCurve) -> Array[Curve] """
        pass

    def PolyCurveParameter(self, segmentIndex, segmentCurveParameter):
        """ PolyCurveParameter(self: PolyCurve, segmentIndex: int, segmentCurveParameter: float) -> float """
        pass

    def RemoveNesting(self):
        """ RemoveNesting(self: PolyCurve) -> bool """
        pass

    def SegmentCurve(self, index):
        """ SegmentCurve(self: PolyCurve, index: int) -> Curve """
        pass

    def SegmentCurveParameter(self, polycurveParameter):
        """ SegmentCurveParameter(self: PolyCurve, polycurveParameter: float) -> float """
        pass

    def SegmentDomain(self, segmentIndex):
        """ SegmentDomain(self: PolyCurve, segmentIndex: int) -> Interval """
        pass

    def SegmentIndex(self, polycurveParameter):
        """ SegmentIndex(self: PolyCurve, polycurveParameter: float) -> int """
        pass

    def SegmentIndexes(self, subdomain, segmentIndex0, segmentIndex1):
        """ SegmentIndexes(self: PolyCurve, subdomain: Interval) -> (int, int, int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type)
        """
        pass

    HasGap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasGap(self: PolyCurve) -> bool

"""

    IsNested = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNested(self: PolyCurve) -> bool

"""

    SegmentCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentCount(self: PolyCurve) -> int

"""



class Polyline(Point3dList):
    """
    Polyline()
    Polyline(initialCapacity: int)
    Polyline(collection: IEnumerable[Point3d])
    """
    def BreakAtAngles(self, angle):
        """ BreakAtAngles(self: Polyline, angle: float) -> Array[Polyline] """
        pass

    def CenterPoint(self):
        """ CenterPoint(self: Polyline) -> Point3d """
        pass

    def ClosestParameter(self, testPoint):
        """ ClosestParameter(self: Polyline, testPoint: Point3d) -> float """
        pass

    def ClosestPoint(self, testPoint):
        """ ClosestPoint(self: Polyline, testPoint: Point3d) -> Point3d """
        pass

    def CollapseShortSegments(self, tolerance):
        """ CollapseShortSegments(self: Polyline, tolerance: float) -> int """
        pass

    def DeleteShortSegments(self, tolerance):
        """ DeleteShortSegments(self: Polyline, tolerance: float) -> int """
        pass

    def GetSegments(self):
        """ GetSegments(self: Polyline) -> Array[Line] """
        pass

    def IsClosedWithinTolerance(self, tolerance):
        """ IsClosedWithinTolerance(self: Polyline, tolerance: float) -> bool """
        pass

    def PointAt(self, t):
        """ PointAt(self: Polyline, t: float) -> Point3d """
        pass

    def ReduceSegments(self, tolerance):
        """ ReduceSegments(self: Polyline, tolerance: float) -> int """
        pass

    def SegmentAt(self, index):
        """ SegmentAt(self: Polyline, index: int) -> Line """
        pass

    def Smooth(self, amount):
        """ Smooth(self: Polyline, amount: float) -> bool """
        pass

    def TangentAt(self, t):
        """ TangentAt(self: Polyline, t: float) -> Vector3d """
        pass

    def ToNurbsCurve(self):
        """ ToNurbsCurve(self: Polyline) -> NurbsCurve """
        pass

    def Trim(self, domain):
        """ Trim(self: Polyline, domain: Interval) -> Polyline """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, initialCapacity: int)
        __new__(cls: type, collection: IEnumerable[Point3d])
        """
        pass

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsClosed(self: Polyline) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Polyline) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Polyline) -> float

"""

    SegmentCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentCount(self: Polyline) -> int

"""



class PolylineCurve(Curve):
    """
    PolylineCurve()
    PolylineCurve(other: PolylineCurve)
    PolylineCurve(points: IEnumerable[Point3d])
    """
    def Dispose(self):
        """ Dispose(self: Curve, disposing: bool) """
        pass

    def Point(self, index):
        """ Point(self: PolylineCurve, index: int) -> Point3d """
        pass

    def SetPoint(self, index, point):
        """ SetPoint(self: PolylineCurve, index: int, point: Point3d) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, other: PolylineCurve)
        __new__(cls: type, points: IEnumerable[Point3d])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    PointCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointCount(self: PolylineCurve) -> int

"""



class Quaternion(object):
    """ Quaternion(a: float, b: float, c: float, d: float) """
    @staticmethod
    def CrossProduct(p, q):
        """ CrossProduct(p: Quaternion, q: Quaternion) -> Quaternion """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Quaternion, other: Quaternion, epsilon: float) -> bool """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Quaternion, obj: object) -> bool
        Equals(self: Quaternion, other: Quaternion) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Quaternion) -> int """
        pass

    def Invert(self):
        """ Invert(self: Quaternion) -> bool """
        pass

    def MatrixForm(self):
        """ MatrixForm(self: Quaternion) -> Transform """
        pass

    @staticmethod
    def Product(p, q):
        """ Product(p: Quaternion, q: Quaternion) -> Quaternion """
        pass

    @staticmethod
    def Rotation(angle, axisOfRotation):
        """ Rotation(angle: float, axisOfRotation: Vector3d) -> Quaternion """
        pass

    def Set(self, a, b, c, d):
        """ Set(self: Quaternion, a: float, b: float, c: float, d: float) """
        pass

    def SetRotation(self, angle, axisOfRotation):
        """ SetRotation(self: Quaternion, angle: float, axisOfRotation: Vector3d) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*yx.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, a, b, c, d):
        """
        __new__[Quaternion]() -> Quaternion
        
        __new__(cls: type, a: float, b: float, c: float, d: float)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(a: Quaternion, b: Quaternion) -> Quaternion """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(a: Quaternion, b: Quaternion) -> Quaternion """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(a: Quaternion, b: Quaternion) -> Quaternion """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    A = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: A(self: Quaternion) -> float

Set: A(self: Quaternion) = value
"""

    B = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: B(self: Quaternion) -> float

Set: B(self: Quaternion) = value
"""

    C = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: C(self: Quaternion) -> float

Set: C(self: Quaternion) = value
"""

    Conjugate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Conjugate(self: Quaternion) -> Quaternion

"""

    D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: D(self: Quaternion) -> float

Set: D(self: Quaternion) = value
"""

    Inverse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Inverse(self: Quaternion) -> Quaternion

"""

    IsScalar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsScalar(self: Quaternion) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Quaternion) -> bool

"""

    IsVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVector(self: Quaternion) -> bool

"""

    IsZero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsZero(self: Quaternion) -> bool

"""

    LengthSquared = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LengthSquared(self: Quaternion) -> float

"""

    Scalar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scalar(self: Quaternion) -> float

"""

    Vector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vector(self: Quaternion) -> Vector3d

"""


    I = None
    Identity = None
    J = None
    K = None
    Zero = None


class RadialDimension(AnnotationBase):
    """
    RadialDimension(center: Point3d, arrowTip: Point3d, xAxis: Vector3d, normal: Vector3d, offsetDistance: float)
    RadialDimension(circle: Circle, arrowTip: Point3d, offsetDistance: float)
    """
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, center: Point3d, arrowTip: Point3d, xAxis: Vector3d, normal: Vector3d, offsetDistance: float)
        __new__(cls: type, circle: Circle, arrowTip: Point3d, offsetDistance: float)
        """
        pass

    IsDiameterDimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDiameterDimension(self: RadialDimension) -> bool

"""



class Ray3d(object):
    """ Ray3d(position: Point3d, direction: Vector3d) """
    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Ray3d, other: Ray3d, epsilon: float) -> bool """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Ray3d, ray: Ray3d) -> bool
        Equals(self: Ray3d, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Ray3d) -> int """
        pass

    def PointAt(self, t):
        """ PointAt(self: Ray3d, t: float) -> Point3d """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, position, direction):
        """
        __new__[Ray3d]() -> Ray3d
        
        __new__(cls: type, position: Point3d, direction: Vector3d)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: Ray3d) -> Vector3d

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: Ray3d) -> Point3d

"""



class Rectangle3d(object):
    """
    Rectangle3d(plane: Plane, width: float, height: float)
    Rectangle3d(plane: Plane, width: Interval, height: Interval)
    Rectangle3d(plane: Plane, cornerA: Point3d, cornerB: Point3d)
    """
    def ClosestPoint(self, point, includeInterior=None):
        """
        ClosestPoint(self: Rectangle3d, point: Point3d, includeInterior: bool) -> Point3d
        ClosestPoint(self: Rectangle3d, point: Point3d) -> Point3d
        """
        pass

    def Contains(self, *__args):
        """
        Contains(self: Rectangle3d, x: float, y: float) -> PointContainment
        Contains(self: Rectangle3d, pt: Point3d) -> PointContainment
        """
        pass

    def Corner(self, index):
        """ Corner(self: Rectangle3d, index: int) -> Point3d """
        pass

    @staticmethod
    def CreateFromPolyline(polyline, deviation=None, angleDeviation=None):
        """
        CreateFromPolyline(polyline: IEnumerable[Point3d]) -> (Rectangle3d, float, float)
        CreateFromPolyline(polyline: IEnumerable[Point3d]) -> Rectangle3d
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Rectangle3d, other: Rectangle3d, epsilon: float) -> bool """
        pass

    def MakeIncreasing(self):
        """ MakeIncreasing(self: Rectangle3d) """
        pass

    def PointAt(self, *__args):
        """
        PointAt(self: Rectangle3d, t: float) -> Point3d
        PointAt(self: Rectangle3d, x: float, y: float) -> Point3d
        """
        pass

    def RecenterPlane(self, *__args):
        """ RecenterPlane(self: Rectangle3d, origin: Point3d)RecenterPlane(self: Rectangle3d, index: int) """
        pass

    def ToNurbsCurve(self):
        """ ToNurbsCurve(self: Rectangle3d) -> NurbsCurve """
        pass

    def ToPolyline(self):
        """ ToPolyline(self: Rectangle3d) -> Polyline """
        pass

    def Transform(self, xform):
        """ Transform(self: Rectangle3d, xform: Transform) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, plane, *__args):
        """
        __new__[Rectangle3d]() -> Rectangle3d
        
        __new__(cls: type, plane: Plane, width: float, height: float)
        __new__(cls: type, plane: Plane, width: Interval, height: Interval)
        __new__(cls: type, plane: Plane, cornerA: Point3d, cornerB: Point3d)
        """
        pass

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Area(self: Rectangle3d) -> float

"""

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: Rectangle3d) -> BoundingBox

"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Center(self: Rectangle3d) -> Point3d

"""

    Circumference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Circumference(self: Rectangle3d) -> float

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: Rectangle3d) -> float

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Rectangle3d) -> bool

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: Rectangle3d) -> Plane

Set: Plane(self: Rectangle3d) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: Rectangle3d) -> float

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Rectangle3d) -> Interval

Set: X(self: Rectangle3d) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Rectangle3d) -> Interval

Set: Y(self: Rectangle3d) = value
"""


    Unset = None


class RegionContainment(Enum):
    """ enum RegionContainment, values: AInsideB (2), BInsideA (3), Disjoint (0), MutualIntersection (1) """
    AInsideB = None
    BInsideA = None
    Disjoint = None
    MutualIntersection = None
    value__ = None


class RevSurface(Surface):
    # no doc
    @staticmethod
    def Create(*__args):
        """
        Create(revoluteLine: Line, axisOfRevolution: Line) -> RevSurface
        Create(revolutePolyline: Polyline, axisOfRevolution: Line, startAngleRadians: float, endAngleRadians: float) -> RevSurface
        Create(revolutePolyline: Polyline, axisOfRevolution: Line) -> RevSurface
        Create(revoluteCurve: Curve, axisOfRevolution: Line, startAngleRadians: float, endAngleRadians: float) -> RevSurface
        Create(revoluteCurve: Curve, axisOfRevolution: Line) -> RevSurface
        Create(revoluteLine: Line, axisOfRevolution: Line, startAngleRadians: float, endAngleRadians: float) -> RevSurface
        """
        pass

    @staticmethod
    def CreateFromCone(cone):
        """ CreateFromCone(cone: Cone) -> RevSurface """
        pass

    @staticmethod
    def CreateFromCylinder(cylinder):
        """ CreateFromCylinder(cylinder: Cylinder) -> RevSurface """
        pass

    @staticmethod
    def CreateFromSphere(sphere):
        """ CreateFromSphere(sphere: Sphere) -> RevSurface """
        pass

    @staticmethod
    def CreateFromTorus(torus):
        """ CreateFromTorus(torus: Torus) -> RevSurface """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class RTree(object):
    """ RTree() """
    def Clear(self):
        """ Clear(self: RTree) """
        pass

    @staticmethod
    def CreateMeshFaceTree(mesh):
        """ CreateMeshFaceTree(mesh: Mesh) -> RTree """
        pass

    @staticmethod
    def CreatePointCloudTree(cloud):
        """ CreatePointCloudTree(cloud: PointCloud) -> RTree """
        pass

    def Dispose(self):
        """ Dispose(self: RTree) """
        pass

    def Insert(self, *__args):
        """
        Insert(self: RTree, box: BoundingBox, elementId: IntPtr) -> bool
        Insert(self: RTree, point: Point2d, elementId: int) -> bool
        Insert(self: RTree, point: Point2d, elementId: IntPtr) -> bool
        Insert(self: RTree, point: Point3d, elementId: int) -> bool
        Insert(self: RTree, point: Point3d, elementId: IntPtr) -> bool
        Insert(self: RTree, box: BoundingBox, elementId: int) -> bool
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: RTree, box: BoundingBox, elementId: IntPtr) -> bool
        Remove(self: RTree, point: Point2d, elementId: int) -> bool
        Remove(self: RTree, box: BoundingBox, elementId: int) -> bool
        Remove(self: RTree, point: Point3d, elementId: int) -> bool
        Remove(self: RTree, point: Point3d, elementId: IntPtr) -> bool
        """
        pass

    def Search(self, *__args):
        """
        Search(self: RTree, sphere: Sphere, callback: EventHandler[RTreeEventArgs]) -> bool
        Search(self: RTree, sphere: Sphere, callback: EventHandler[RTreeEventArgs], tag: object) -> bool
        Search(self: RTree, box: BoundingBox, callback: EventHandler[RTreeEventArgs]) -> bool
        Search(self: RTree, box: BoundingBox, callback: EventHandler[RTreeEventArgs], tag: object) -> bool
        """
        pass

    @staticmethod
    def SearchOverlaps(treeA, treeB, tolerance, callback):
        """ SearchOverlaps(treeA: RTree, treeB: RTree, tolerance: float, callback: EventHandler[RTreeEventArgs]) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: RTree) -> int

"""



class RTreeEventArgs(EventArgs):
    # no doc
    Cancel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cancel(self: RTreeEventArgs) -> bool

Set: Cancel(self: RTreeEventArgs) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: RTreeEventArgs) -> int

"""

    IdB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IdB(self: RTreeEventArgs) -> int

"""

    IdBPtr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IdBPtr(self: RTreeEventArgs) -> IntPtr

"""

    IdPtr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IdPtr(self: RTreeEventArgs) -> IntPtr

"""

    SearchBoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SearchBoundingBox(self: RTreeEventArgs) -> BoundingBox

Set: SearchBoundingBox(self: RTreeEventArgs) = value
"""

    SearchSphere = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SearchSphere(self: RTreeEventArgs) -> Sphere

Set: SearchSphere(self: RTreeEventArgs) = value
"""

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tag(self: RTreeEventArgs) -> object

Set: Tag(self: RTreeEventArgs) = value
"""



class SpaceMorph(object):
    # no doc
    @staticmethod
    def IsMorphable(geometry):
        """ IsMorphable(geometry: GeometryBase) -> bool """
        pass

    def MorphPoint(self, point):
        """ MorphPoint(self: SpaceMorph, point: Point3d) -> Point3d """
        pass

    PreserveStructure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreserveStructure(self: SpaceMorph) -> bool

Set: PreserveStructure(self: SpaceMorph) = value
"""

    QuickPreview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuickPreview(self: SpaceMorph) -> bool

Set: QuickPreview(self: SpaceMorph) = value
"""

    Tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tolerance(self: SpaceMorph) -> float

Set: Tolerance(self: SpaceMorph) = value
"""



class Sphere(object):
    """
    Sphere(center: Point3d, radius: float)
    Sphere(equatorialPlane: Plane, radius: float)
    """
    def ClosestParameter(self, testPoint, longitudeRadians, latitudeRadians):
        """ ClosestParameter(self: Sphere, testPoint: Point3d) -> (bool, float, float) """
        pass

    def ClosestPoint(self, testPoint):
        """ ClosestPoint(self: Sphere, testPoint: Point3d) -> Point3d """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Sphere, other: Sphere, epsilon: float) -> bool """
        pass

    def LatitudeDegrees(self, degrees):
        """ LatitudeDegrees(self: Sphere, degrees: float) -> Circle """
        pass

    def LatitudeRadians(self, radians):
        """ LatitudeRadians(self: Sphere, radians: float) -> Circle """
        pass

    def LongitudeDegrees(self, degrees):
        """ LongitudeDegrees(self: Sphere, degrees: float) -> Circle """
        pass

    def LongitudeRadians(self, radians):
        """ LongitudeRadians(self: Sphere, radians: float) -> Circle """
        pass

    def NormalAt(self, longitudeRadians, latitudeRadians):
        """ NormalAt(self: Sphere, longitudeRadians: float, latitudeRadians: float) -> Vector3d """
        pass

    def PointAt(self, longitudeRadians, latitudeRadians):
        """ PointAt(self: Sphere, longitudeRadians: float, latitudeRadians: float) -> Point3d """
        pass

    def Rotate(self, *__args):
        """
        Rotate(self: Sphere, sinAngle: float, cosAngle: float, axisOfRotation: Vector3d, centerOfRotation: Point3d) -> bool
        Rotate(self: Sphere, angleRadians: float, axisOfRotation: Vector3d, centerOfRotation: Point3d) -> bool
        Rotate(self: Sphere, sinAngle: float, cosAngle: float, axisOfRotation: Vector3d) -> bool
        Rotate(self: Sphere, angleRadians: float, axisOfRotation: Vector3d) -> bool
        """
        pass

    def ToBrep(self):
        """ ToBrep(self: Sphere) -> Brep """
        pass

    def ToNurbsSurface(self):
        """ ToNurbsSurface(self: Sphere) -> NurbsSurface """
        pass

    def ToRevSurface(self):
        """ ToRevSurface(self: Sphere) -> RevSurface """
        pass

    def Transform(self, xform):
        """ Transform(self: Sphere, xform: Transform) -> bool """
        pass

    def Translate(self, delta):
        """ Translate(self: Sphere, delta: Vector3d) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Sphere]() -> Sphere
        
        __new__(cls: type, center: Point3d, radius: float)
        __new__(cls: type, equatorialPlane: Plane, radius: float)
        """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: Sphere) -> BoundingBox

"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Center(self: Sphere) -> Point3d

Set: Center(self: Sphere) = value
"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: Sphere) -> float

Set: Diameter(self: Sphere) = value
"""

    EquitorialPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EquitorialPlane(self: Sphere) -> Plane

Set: EquitorialPlane(self: Sphere) = value
"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Sphere) -> bool

"""

    NorthPole = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NorthPole(self: Sphere) -> Point3d

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: Sphere) -> float

Set: Radius(self: Sphere) = value
"""

    SouthPole = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SouthPole(self: Sphere) -> Point3d

"""


    Unset = None


class SumSurface(Surface):
    # no doc
    @staticmethod
    def Create(curveA, curveB):
        """ Create(curveA: Curve, curveB: Curve) -> SumSurface """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class SurfaceCurvature(object):
    # no doc
    def Direction(self, direction):
        """ Direction(self: SurfaceCurvature, direction: int) -> Vector3d """
        pass

    def Kappa(self, direction):
        """ Kappa(self: SurfaceCurvature, direction: int) -> float """
        pass

    def OsculatingCircle(self, direction):
        """ OsculatingCircle(self: SurfaceCurvature, direction: int) -> Circle """
        pass

    Gaussian = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Gaussian(self: SurfaceCurvature) -> float

"""

    Mean = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mean(self: SurfaceCurvature) -> float

"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Normal(self: SurfaceCurvature) -> Vector3d

"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: SurfaceCurvature) -> Point3d

"""

    UVPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UVPoint(self: SurfaceCurvature) -> Point2d

"""



class TextDot(GeometryBase):
    """ TextDot(text: str, location: Point3d) """
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, text, location):
        """
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, text: str, location: Point3d)
        """
        pass

    FontFace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FontFace(self: TextDot) -> str

Set: FontFace(self: TextDot) = value
"""

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FontHeight(self: TextDot) -> int

Set: FontHeight(self: TextDot) = value
"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: TextDot) -> Point3d

Set: Point(self: TextDot) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: TextDot) -> str

Set: Text(self: TextDot) = value
"""



class TextEntity(AnnotationBase):
    """ TextEntity() """
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    AnnotativeScalingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnnotativeScalingEnabled(self: TextEntity) -> bool

Set: AnnotativeScalingEnabled(self: TextEntity) = value
"""

    FontIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FontIndex(self: TextEntity) -> int

Set: FontIndex(self: TextEntity) = value
"""

    Justification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Justification(self: TextEntity) -> TextJustification

Set: Justification(self: TextEntity) = value
"""

    MaskColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaskColor(self: TextEntity) -> Color

Set: MaskColor(self: TextEntity) = value
"""

    MaskEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaskEnabled(self: TextEntity) -> bool

Set: MaskEnabled(self: TextEntity) = value
"""

    MaskOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaskOffset(self: TextEntity) -> float

Set: MaskOffset(self: TextEntity) = value
"""

    MaskUsesViewportColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaskUsesViewportColor(self: TextEntity) -> bool

Set: MaskUsesViewportColor(self: TextEntity) = value
"""



class TextJustification(Enum):
    """ enum (flags) TextJustification, values: Bottom (65536), BottomCenter (65538), BottomLeft (65537), BottomRight (65540), Center (2), Left (1), Middle (131072), MiddleCenter (131074), MiddleLeft (131073), MiddleRight (131076), None (0), Right (4), Top (262144), TopCenter (262146), TopLeft (262145), TopRight (262148) """
    Bottom = None
    BottomCenter = None
    BottomLeft = None
    BottomRight = None
    Center = None
    Left = None
    Middle = None
    MiddleCenter = None
    MiddleLeft = None
    MiddleRight = None
    None = None
    Right = None
    Top = None
    TopCenter = None
    TopLeft = None
    TopRight = None
    value__ = None


class Torus(object):
    """ Torus(basePlane: Plane, majorRadius: float, minorRadius: float) """
    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Torus, other: Torus, epsilon: float) -> bool """
        pass

    def ToNurbsSurface(self):
        """ ToNurbsSurface(self: Torus) -> NurbsSurface """
        pass

    def ToRevSurface(self):
        """ ToRevSurface(self: Torus) -> RevSurface """
        pass

    @staticmethod # known case of __new__
    def __new__(self, basePlane, majorRadius, minorRadius):
        """
        __new__[Torus]() -> Torus
        
        __new__(cls: type, basePlane: Plane, majorRadius: float, minorRadius: float)
        """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Torus) -> bool

"""

    MajorRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorRadius(self: Torus) -> float

Set: MajorRadius(self: Torus) = value
"""

    MinorRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorRadius(self: Torus) -> float

Set: MinorRadius(self: Torus) = value
"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: Torus) -> Plane

Set: Plane(self: Torus) = value
"""


    Unset = None


class Transform(object):
    """ Transform(diagonalValue: float) """
    @staticmethod
    def ChangeBasis(*__args):
        """
        ChangeBasis(initialBasisX: Vector3d, initialBasisY: Vector3d, initialBasisZ: Vector3d, finalBasisX: Vector3d, finalBasisY: Vector3d, finalBasisZ: Vector3d) -> Transform
        ChangeBasis(plane0: Plane, plane1: Plane) -> Transform
        """
        pass

    def CompareTo(self, other):
        """ CompareTo(self: Transform, other: Transform) -> int """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Transform, other: Transform) -> bool
        Equals(self: Transform, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Transform) -> int """
        pass

    @staticmethod
    def Mirror(*__args):
        """
        Mirror(mirrorPlane: Plane) -> Transform
        Mirror(pointOnMirrorPlane: Point3d, normalToMirrorPlane: Vector3d) -> Transform
        """
        pass

    @staticmethod
    def Multiply(a, b):
        """ Multiply(a: Transform, b: Transform) -> Transform """
        pass

    @staticmethod
    def PlanarProjection(plane):
        """ PlanarProjection(plane: Plane) -> Transform """
        pass

    @staticmethod
    def PlaneToPlane(plane0, plane1):
        """ PlaneToPlane(plane0: Plane, plane1: Plane) -> Transform """
        pass

    @staticmethod
    def Rotation(*__args):
        """
        Rotation(startDirection: Vector3d, endDirection: Vector3d, rotationCenter: Point3d) -> Transform
        Rotation(x0: Vector3d, y0: Vector3d, z0: Vector3d, x1: Vector3d, y1: Vector3d, z1: Vector3d) -> Transform
        Rotation(angleRadians: float, rotationAxis: Vector3d, rotationCenter: Point3d) -> Transform
        Rotation(sinAngle: float, cosAngle: float, rotationAxis: Vector3d, rotationCenter: Point3d) -> Transform
        Rotation(angleRadians: float, rotationCenter: Point3d) -> Transform
        """
        pass

    @staticmethod
    def Scale(*__args):
        """
        Scale(plane: Plane, xScaleFactor: float, yScaleFactor: float, zScaleFactor: float) -> Transform
        Scale(anchor: Point3d, scaleFactor: float) -> Transform
        """
        pass

    @staticmethod
    def Shear(plane, x, y, z):
        """ Shear(plane: Plane, x: Vector3d, y: Vector3d, z: Vector3d) -> Transform """
        pass

    def ToFloatArray(self, rowDominant):
        """ ToFloatArray(self: Transform, rowDominant: bool) -> Array[Single] """
        pass

    def ToString(self):
        """ ToString(self: Transform) -> str """
        pass

    def TransformBoundingBox(self, bbox):
        """ TransformBoundingBox(self: Transform, bbox: BoundingBox) -> BoundingBox """
        pass

    def TransformList(self, points):
        """ TransformList(self: Transform, points: IEnumerable[Point3d]) -> Array[Point3d] """
        pass

    @staticmethod
    def Translation(*__args):
        """
        Translation(dx: float, dy: float, dz: float) -> Transform
        Translation(motion: Vector3d) -> Transform
        """
        pass

    def Transpose(self):
        """ Transpose(self: Transform) -> Transform """
        pass

    def TryGetInverse(self, inverseTransform):
        """ TryGetInverse(self: Transform) -> (bool, Transform) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, diagonalValue):
        """
        __new__[Transform]() -> Transform
        
        __new__(cls: type, diagonalValue: float)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(a: Transform, b: Transform) -> Transform """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Determinant(self: Transform) -> float

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Transform) -> bool

"""

    M00 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M00(self: Transform) -> float

Set: M00(self: Transform) = value
"""

    M01 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M01(self: Transform) -> float

Set: M01(self: Transform) = value
"""

    M02 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M02(self: Transform) -> float

Set: M02(self: Transform) = value
"""

    M03 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M03(self: Transform) -> float

Set: M03(self: Transform) = value
"""

    M10 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M10(self: Transform) -> float

Set: M10(self: Transform) = value
"""

    M11 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M11(self: Transform) -> float

Set: M11(self: Transform) = value
"""

    M12 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M12(self: Transform) -> float

Set: M12(self: Transform) = value
"""

    M13 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M13(self: Transform) -> float

Set: M13(self: Transform) = value
"""

    M20 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M20(self: Transform) -> float

Set: M20(self: Transform) = value
"""

    M21 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M21(self: Transform) -> float

Set: M21(self: Transform) = value
"""

    M22 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M22(self: Transform) -> float

Set: M22(self: Transform) = value
"""

    M23 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M23(self: Transform) -> float

Set: M23(self: Transform) = value
"""

    M30 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M30(self: Transform) -> float

Set: M30(self: Transform) = value
"""

    M31 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M31(self: Transform) -> float

Set: M31(self: Transform) = value
"""

    M32 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M32(self: Transform) -> float

Set: M32(self: Transform) = value
"""

    M33 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M33(self: Transform) -> float

Set: M33(self: Transform) = value
"""

    SimilarityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SimilarityType(self: Transform) -> TransformSimilarityType

"""


    Identity = None
    Unset = None


class TransformSimilarityType(Enum):
    """ enum TransformSimilarityType, values: NotSimilarity (0), OrientationPreserving (1), OrientationReversing (-1) """
    NotSimilarity = None
    OrientationPreserving = None
    OrientationReversing = None
    value__ = None


class Vector2d(object):
    """ Vector2d(x: float, y: float) """
    def CompareTo(self, other):
        """ CompareTo(self: Vector2d, other: Vector2d) -> int """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Vector2d, other: Vector2d, epsilon: float) -> bool """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Vector2d, vector: Vector2d) -> bool
        Equals(self: Vector2d, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Vector2d) -> int """
        pass

    def ToString(self):
        """ ToString(self: Vector2d) -> str """
        pass

    def Unitize(self):
        """ Unitize(self: Vector2d) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    @staticmethod # known case of __new__
    def __new__(self, x, y):
        """
        __new__[Vector2d]() -> Vector2d
        
        __new__(cls: type, x: float, y: float)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Vector2d) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Vector2d) -> float

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Vector2d) -> float

Set: X(self: Vector2d) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Vector2d) -> float

Set: Y(self: Vector2d) = value
"""


    Unset = None
    Zero = None


class Vector2f(object):
    # no doc
    def CompareTo(self, other):
        """ CompareTo(self: Vector2f, other: Vector2f) -> int """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Vector2f, other: Vector2f, epsilon: Single) -> bool """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Vector2f, vector: Vector2f) -> bool
        Equals(self: Vector2f, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Vector2f) -> int """
        pass

    def ToString(self):
        """ ToString(self: Vector2f) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Vector2f) -> Single

Set: X(self: Vector2f) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Vector2f) -> Single

Set: Y(self: Vector2f) = value
"""



class Vector3d(object):
    """
    Vector3d(x: float, y: float, z: float)
    Vector3d(point: Point3d)
    Vector3d(vector: Vector3f)
    Vector3d(vector: Vector3d)
    """
    @staticmethod
    def Add(vector1, vector2):
        """ Add(vector1: Vector3d, vector2: Vector3d) -> Vector3d """
        pass

    def CompareTo(self, other):
        """ CompareTo(self: Vector3d, other: Vector3d) -> int """
        pass

    @staticmethod
    def CrossProduct(a, b):
        """ CrossProduct(a: Vector3d, b: Vector3d) -> Vector3d """
        pass

    @staticmethod
    def Divide(vector, t):
        """ Divide(vector: Vector3d, t: float) -> Vector3d """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Vector3d, other: Vector3d, epsilon: float) -> bool """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Vector3d, vector: Vector3d) -> bool
        Equals(self: Vector3d, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Vector3d) -> int """
        pass

    def IsParallelTo(self, other, angleTolerance=None):
        """
        IsParallelTo(self: Vector3d, other: Vector3d, angleTolerance: float) -> int
        IsParallelTo(self: Vector3d, other: Vector3d) -> int
        """
        pass

    def IsPerpendicularTo(self, other, angleTolerance=None):
        """
        IsPerpendicularTo(self: Vector3d, other: Vector3d, angleTolerance: float) -> bool
        IsPerpendicularTo(self: Vector3d, other: Vector3d) -> bool
        """
        pass

    def IsTiny(self, tolerance=None):
        """
        IsTiny(self: Vector3d) -> bool
        IsTiny(self: Vector3d, tolerance: float) -> bool
        """
        pass

    @staticmethod
    def Multiply(*__args):
        """
        Multiply(vector1: Vector3d, vector2: Vector3d) -> float
        Multiply(t: float, vector: Vector3d) -> Vector3d
        Multiply(vector: Vector3d, t: float) -> Vector3d
        """
        pass

    @staticmethod
    def Negate(vector):
        """ Negate(vector: Vector3d) -> Vector3d """
        pass

    def PerpendicularTo(self, other):
        """ PerpendicularTo(self: Vector3d, other: Vector3d) -> bool """
        pass

    def Reverse(self):
        """ Reverse(self: Vector3d) -> bool """
        pass

    def Rotate(self, angleRadians, rotationAxis):
        """ Rotate(self: Vector3d, angleRadians: float, rotationAxis: Vector3d) -> bool """
        pass

    @staticmethod
    def Subtract(vector1, vector2):
        """ Subtract(vector1: Vector3d, vector2: Vector3d) -> Vector3d """
        pass

    def ToString(self):
        """ ToString(self: Vector3d) -> str """
        pass

    def Transform(self, transformation):
        """ Transform(self: Vector3d, transformation: Transform) """
        pass

    def Unitize(self):
        """ Unitize(self: Vector3d) -> bool """
        pass

    @staticmethod
    def VectorAngle(a, b, plane=None):
        """
        VectorAngle(a: Vector3d, b: Vector3d, plane: Plane) -> float
        VectorAngle(a: Vector3d, b: Vector3d) -> float
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Vector3d]() -> Vector3d
        
        __new__(cls: type, x: float, y: float, z: float)
        __new__(cls: type, point: Point3d)
        __new__(cls: type, vector: Vector3f)
        __new__(cls: type, vector: Vector3d)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(vector1: Vector3d, vector2: Vector3d) -> Vector3d """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(vector1: Vector3d, vector2: Vector3d) -> float
        __rmul__(t: float, vector: Vector3d) -> Vector3d
        """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(vector1: Vector3d, vector2: Vector3d) -> Vector3d """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    IsUnitVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUnitVector(self: Vector3d) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Vector3d) -> bool

"""

    IsZero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsZero(self: Vector3d) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Vector3d) -> float

"""

    MaximumCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumCoordinate(self: Vector3d) -> float

"""

    MinimumCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumCoordinate(self: Vector3d) -> float

"""

    SquareLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SquareLength(self: Vector3d) -> float

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Vector3d) -> float

Set: X(self: Vector3d) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Vector3d) -> float

Set: Y(self: Vector3d) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: Vector3d) -> float

Set: Z(self: Vector3d) = value
"""


    Unset = None
    XAxis = None
    YAxis = None
    ZAxis = None
    Zero = None


class Vector3f(object):
    """ Vector3f(x: Single, y: Single, z: Single) """
    @staticmethod
    def Add(point, vector):
        """ Add(point: Point3f, vector: Vector3f) -> Point3f """
        pass

    def CompareTo(self, other):
        """ CompareTo(self: Vector3f, other: Vector3f) -> int """
        pass

    @staticmethod
    def CrossProduct(a, b):
        """ CrossProduct(a: Vector3f, b: Vector3f) -> Vector3f """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Vector3f, other: Vector3f, epsilon: Single) -> bool """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Vector3f, vector: Vector3f) -> bool
        Equals(self: Vector3f, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Vector3f) -> int """
        pass

    @staticmethod
    def Multiply(*__args):
        """
        Multiply(t: Single, vector: Vector3f) -> Vector3f
        Multiply(vector: Vector3f, t: Single) -> Vector3f
        """
        pass

    def PerpendicularTo(self, other):
        """ PerpendicularTo(self: Vector3f, other: Vector3f) -> bool """
        pass

    def Reverse(self):
        """ Reverse(self: Vector3f) -> bool """
        pass

    def Rotate(self, angleRadians, rotationAxis):
        """ Rotate(self: Vector3f, angleRadians: float, rotationAxis: Vector3f) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Vector3f) -> str """
        pass

    def Transform(self, transformation):
        """ Transform(self: Vector3f, transformation: Transform) """
        pass

    def Unitize(self):
        """ Unitize(self: Vector3f) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, x, y, z):
        """
        __new__[Vector3f]() -> Vector3f
        
        __new__(cls: type, x: Single, y: Single, z: Single)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(point: Point3f, vector: Vector3f) -> Point3f """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(t: Single, vector: Vector3f) -> Vector3f """
        pass

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Vector3f) -> Single

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Vector3f) -> Single

Set: X(self: Vector3f) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Vector3f) -> Single

Set: Y(self: Vector3f) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: Vector3f) -> Single

Set: Z(self: Vector3f) = value
"""


    Unset = None
    XAxis = None
    YAxis = None
    ZAxis = None
    Zero = None


# variables with complex values

