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


