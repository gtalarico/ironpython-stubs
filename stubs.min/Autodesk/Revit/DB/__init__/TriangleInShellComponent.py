class TriangleInShellComponent(object, IDisposable):
    """
    This class represents a triangle in a TriangulatedShellComponent object. The triangle is
       defined by its vertices, which are specified by their indices in the
       TriangulatedShellComponent's array of vertices.
    
    TriangleInShellComponent(other: TriangleInShellComponent)
    """
    def Dispose(self):
        """ Dispose(self: TriangleInShellComponent) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: TriangleInShellComponent, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, other):
        """ __new__(cls: type, other: TriangleInShellComponent) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: TriangleInShellComponent) -> bool

"""

    VertexIndex0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index of the triangle's first vertex in the TriangulatedShellComponent's array of vertices.

Get: VertexIndex0(self: TriangleInShellComponent) -> int

"""

    VertexIndex1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index of the triangle's second vertex in the TriangulatedShellComponent's array of vertices.

Get: VertexIndex1(self: TriangleInShellComponent) -> int

"""

    VertexIndex2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index of the triangle's third vertex in the TriangulatedShellComponent's array of vertices.

Get: VertexIndex2(self: TriangleInShellComponent) -> int

"""


