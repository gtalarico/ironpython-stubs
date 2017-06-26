class Quaternion(object, IEquatable[Quaternion], IEpsilonComparable[Quaternion]):
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
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

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(a: Quaternion, b: Quaternion) -> Quaternion """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(a: Quaternion, b: Quaternion) -> Quaternion """
        pass

    def __str__(self, *args): #cannot find CLR method
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

