class Box(object, IEpsilonComparable[Box]):
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
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

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
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

