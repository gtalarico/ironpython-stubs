class Surface(GeometryBase, IDisposable, ISerializable):
    # no doc
    def ConstructConstObject(self, *args): #cannot find CLR method
        """ ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int) """
        pass

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

    def NonConstOperation(self, *args): #cannot find CLR method
        """ NonConstOperation(self: CommonObject) """
        pass

    def NormalAt(self, u, v):
        """ NormalAt(self: Surface, u: float, v: float) -> Vector3d """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """ OnSwitchToNonConst(self: GeometryBase) """
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

    IsSolid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSolid(self: Surface) -> bool

"""


