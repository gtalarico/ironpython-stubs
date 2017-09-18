# encoding: utf-8
# module Grasshopper.Kernel.Geometry.Delaunay calls itself Delaunay
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Connectivity(object):
    """ Connectivity() """
    def GetConnections(self, node_index):
        """ GetConnections(self: Connectivity, node_index: int) -> List[int] """
        pass

    def SolveConnectivity(self, nodes, faces, include_convex_hull_edges):
        """ SolveConnectivity(self: Connectivity, nodes: Node2List, faces: List[Face], include_convex_hull_edges: bool) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: Connectivity) -> int

"""



class Edge(object, IComparable[Edge]):
    """ Edge(nA: int, nB: int, nN: int) """
    def CompareTo(self, other):
        """ CompareTo(self: Edge, other: Edge) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, nA, nB, nN):
        """
        __new__(cls: type, nA: int, nB: int, nN: int)
        __new__[Edge]() -> Edge
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DebuggerDisplay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DebuggerDisplay(self: Edge) -> str

"""


    A = None
    B = None
    N = None


class EdgeList(object):
    """
    EdgeList()
    EdgeList(F: List[FaceEx])
    EdgeList(F: List[Face])
    """
    def AddEdge(self, *__args):
        """ AddEdge(self: EdgeList, E: Edge)AddEdge(self: EdgeList, A: int, B: int) """
        pass

    def Clear(self):
        """ Clear(self: EdgeList) """
        pass

    def ContainsEdge(self, *__args):
        """
        ContainsEdge(self: EdgeList, E: Edge) -> int
        ContainsEdge(self: EdgeList, A: int, B: int) -> int
        """
        pass

    def RemoveEdge(self, *__args):
        """
        RemoveEdge(self: EdgeList, E: Edge) -> bool
        RemoveEdge(self: EdgeList, A: int, B: int) -> bool
        """
        pass

    def TrimHighValenceEdges(self):
        """ TrimHighValenceEdges(self: EdgeList) -> int """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, F=None):
        """
        __new__(cls: type)
        __new__(cls: type, F: List[FaceEx])
        __new__(cls: type, F: List[Face])
        """
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Capacity(self: EdgeList) -> int

Set: Capacity(self: EdgeList) = value
"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: EdgeList) -> int

"""


    m_E = None


class Face(object):
    """
    Face()
    Face(nA: int, nB: int, nC: int)
    Face(other: Face)
    """
    def ContainsEdge(self, E0, E1):
        """ ContainsEdge(self: Face, E0: int, E1: int) -> bool """
        pass

    def ContainsVertex(self, index):
        """ ContainsVertex(self: Face, index: int) -> bool """
        pass

    def Duplicate(self):
        """ Duplicate(self: Face) -> Face """
        pass

    def Set(self, *__args):
        """ Set(self: Face, other: Face)Set(self: Face, nA: int, nB: int, nC: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, nA: int, nB: int, nC: int)
        __new__(cls: type, other: Face)
        """
        pass

    DebuggerDisplay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DebuggerDisplay(self: Face) -> str

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Face) -> bool

"""


    A = None
    B = None
    C = None


class FaceEx(Face):
    """
    FaceEx()
    FaceEx(nA: int, nB: int, nC: int)
    FaceEx(other: Face)
    """
    def ComputeBC(self, *__args):
        """ ComputeBC(self: FaceEx, D: Node2, E: Node2, F: Node2)ComputeBC(self: FaceEx, Nodes: Node2List) """
        pass

    def ContainsInBoundingCircle(self, *__args):
        """
        ContainsInBoundingCircle(self: FaceEx, x: float, y: float) -> bool
        ContainsInBoundingCircle(self: FaceEx, N: Node2) -> bool
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, nA: int, nB: int, nC: int)
        __new__(cls: type, other: Face)
        """
        pass

    Front = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Front(self: FaceEx) -> float

"""


    center = None
    radius = None
    radius_squared = None


class FaceExList(object):
    """
    FaceExList()
    FaceExList(initial_capacity: int)
    """
    def AddFace(self, *__args):
        """ AddFace(self: FaceExList, F: FaceEx)AddFace(self: FaceExList, A: int, B: int, C: int, Nodes: Node2List) """
        pass

    def Clear(self):
        """ Clear(self: FaceExList) """
        pass

    def CullFaces(self, x, y, F):
        """ CullFaces(self: FaceExList, x: float, y: float, F: List[FaceEx]) -> int """
        pass

    def InsertFaces(self, nodes):
        """ InsertFaces(self: FaceExList, nodes: Node2List) """
        pass

    def MigrateRemainingFaces(self, static_list):
        """ MigrateRemainingFaces(self: FaceExList, static_list: List[Face]) """
        pass

    def MigrateStaticFaces(self, static_list, wave_front):
        """ MigrateStaticFaces(self: FaceExList, static_list: List[Face], wave_front: float) -> int """
        pass

    def TrimNulls(self):
        """ TrimNulls(self: FaceExList) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, initial_capacity=None):
        """
        __new__(cls: type)
        __new__(cls: type, initial_capacity: int)
        """
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Capacity(self: FaceExList) -> int

Set: Capacity(self: FaceExList) = value
"""


    CompareFaceFront = None
    m_compare_front = None
    m_F = None


class Solver(object):
    # no doc
    @staticmethod
    def Solve_Connectivity(nodes, jitter_amount, include_convex_hull_edges):
        """ Solve_Connectivity(nodes: Node2List, jitter_amount: float, include_convex_hull_edges: bool) -> Connectivity """
        pass

    @staticmethod
    def Solve_Faces(nodes, jitter_amount):
        """ Solve_Faces(nodes: Node2List, jitter_amount: float) -> List[Face] """
        pass

    @staticmethod
    def Solve_Mesh(nodes, jitter_amount, faces):
        """ Solve_Mesh(nodes: Node2List, jitter_amount: float, faces: List[Face]) -> (Mesh, List[Face]) """
        pass


