# encoding: utf-8
# module Autodesk.DesignScript.Geometry.TSpline calls itself TSpline
# from ProtoGeometry, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class TSplineEdge(Edge):
    # no doc
    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def Info(self):
        """ Info(self: TSplineEdge) -> Dictionary[str, object] """
        pass

    def ToString(self):
        """ ToString(self: TSplineEdge) -> str """
        pass

    AdjacentFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdjacentFaces(self: TSplineEdge) -> Array[TSplineFace]

"""

    EndVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndVertex(self: TSplineEdge) -> TSplineVertex

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: TSplineEdge) -> int

"""

    IsBorder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBorder(self: TSplineEdge) -> bool

"""

    IsManifold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsManifold(self: TSplineEdge) -> bool

"""

    StartVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartVertex(self: TSplineEdge) -> TSplineVertex

"""

    UVNFrame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UVNFrame(self: TSplineEdge) -> TSplineUVNFrame

"""


    mConstructor = None


class TSplineFace(Face):
    # no doc
    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def Info(self):
        """ Info(self: TSplineFace) -> Dictionary[str, object] """
        pass

    def ToString(self):
        """ ToString(self: TSplineFace) -> str """
        pass

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edges(self: TSplineFace) -> Array[TSplineEdge]

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: TSplineFace) -> int

"""

    Sides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Sides(self: TSplineFace) -> int

"""

    UVNFrame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UVNFrame(self: TSplineFace) -> TSplineUVNFrame

"""

    Valence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Valence(self: TSplineFace) -> int

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: TSplineFace) -> Array[TSplineVertex]

"""


    mConstructor = None


class TSplineInitialSymmetry(DesignScriptEntity):
    # no doc
    @staticmethod
    def ByAxial(xAxis, yAxis, zAxis):
        """ ByAxial(xAxis: bool, yAxis: bool, zAxis: bool) -> TSplineInitialSymmetry """
        pass

    @staticmethod
    def ByRadial(symmetricFaces):
        """ ByRadial(symmetricFaces: int) -> TSplineInitialSymmetry """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: TSplineInitialSymmetry) -> str """
        pass

    IsRadial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRadial(self: TSplineInitialSymmetry) -> bool

"""

    RadialSymmetryFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RadialSymmetryFaces(self: TSplineInitialSymmetry) -> int

"""

    XAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XAxis(self: TSplineInitialSymmetry) -> bool

"""

    YAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YAxis(self: TSplineInitialSymmetry) -> bool

"""

    ZAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZAxis(self: TSplineInitialSymmetry) -> bool

"""


    mConstructor = None


class TSplineReflection(DesignScriptEntity):
    # no doc

class TSplineTopology(Topology):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class TSplineSurface(TSplineTopology):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'LibG.Interface, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class TSplineUVNFrame(DesignScriptEntity):
    # no doc

class TSplineVertex(Vertex):
    # no doc
    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def Info(self):
        """ Info(self: TSplineVertex) -> Dictionary[str, object] """
        pass

    def ToString(self):
        """ ToString(self: TSplineVertex) -> str """
        pass

    AdjacentEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdjacentEdges(self: TSplineVertex) -> Array[TSplineEdge]

"""

    AdjacentFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdjacentFaces(self: TSplineVertex) -> Array[TSplineFace]

"""

    FunctionalValence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FunctionalValence(self: TSplineVertex) -> int

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: TSplineVertex) -> int

"""

    IsManifold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsManifold(self: TSplineVertex) -> bool

"""

    IsStarPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStarPoint(self: TSplineVertex) -> bool

"""

    IsTPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTPoint(self: TSplineVertex) -> bool

"""

    UVNFrame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UVNFrame(self: TSplineVertex) -> TSplineUVNFrame

"""

    Valence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Valence(self: TSplineVertex) -> int

"""


    mConstructor = None


