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

