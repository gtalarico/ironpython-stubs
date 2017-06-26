class Point2d(object, ISerializable, IEquatable[Point2d], IComparable[Point2d], IComparable, IEpsilonComparable[Point2d]):
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

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
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

    def __str__(self, *args): #cannot find CLR method
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

