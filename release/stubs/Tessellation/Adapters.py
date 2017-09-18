# encoding: utf-8
# module Tessellation.Adapters calls itself Adapters
# from Tessellation, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Cell2(TriangulationCell[Vertex2, Cell2]):
    """ Cell2() """
    Centroid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Centroid(self: Cell2) -> Point

"""

    Circumcenter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Circumcenter(self: Cell2) -> Point

"""



class Vertex2(object, IVertex, IGraphicItem):
    """ Vertex2(x: float, y: float) """
    def AsPoint(self):
        """ AsPoint(self: Vertex2) -> Point """
        pass

    def AsVector(self):
        """ AsVector(self: Vertex2) -> Vector """
        pass

    @staticmethod
    def FromUV(uv):
        """ FromUV(uv: UV) -> Vertex2 """
        pass

    def Tessellate(self, package, parameters):
        """ Tessellate(self: Vertex2, package: IRenderPackage, parameters: TessellationParameters) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, x, y):
        """ __new__(cls: type, x: float, y: float) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: Vertex2) -> Array[float]

Set: Position(self: Vertex2) = value
"""



