class Vector2f(object, IEquatable[Vector2f], IComparable[Vector2f], IComparable, IEpsilonFComparable[Vector2f]):
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Vector2f) -> Single

Set: X(self: Vector2f) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Vector2f) -> Single

Set: Y(self: Vector2f) = value
"""


