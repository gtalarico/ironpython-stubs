class Curve(GeometryBase, IDisposable, ISerializable):
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

    def ConstructConstObject(self, *args): #cannot find CLR method
        """ ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int) """
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """ NonConstOperation(self: Curve) """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """ OnSwitchToNonConst(self: GeometryBase) """
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

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
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


