class Point3d(object, ISerializable, IEquatable[Point3d], IComparable[Point3d], IComparable, IEpsilonComparable[Point3d]):
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
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

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
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

    def __str__(self, *args): #cannot find CLR method
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

