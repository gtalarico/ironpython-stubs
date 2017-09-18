# encoding: utf-8
# module GH_Util.MetaBall calls itself MetaBall
# from GH_Util, Version=1.0.0.0, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_CellInfo(object):
    """
    GH_CellInfo()
    GH_CellInfo(nX: int, nY: int)
    GH_CellInfo(nX: int, nY: int, na: float, nb: float, nc: float, nd: float)
    """
    def DetermineMask(self, threshold):
        """ DetermineMask(self: GH_CellInfo, threshold: float) """
        pass

    def DetermineRealBox(self, accuracy):
        """ DetermineRealBox(self: GH_CellInfo, accuracy: float) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, nX=None, nY=None, na=None, nb=None, nc=None, nd=None):
        """
        __new__(cls: type)
        __new__(cls: type, nX: int, nY: int)
        __new__(cls: type, nX: int, nY: int, na: float, nb: float, nc: float, nd: float)
        """
        pass

    edge_b = None
    edge_l = None
    edge_r = None
    edge_t = None
    mask = None
    va = None
    vb = None
    vc = None
    vd = None
    x = None
    y = None


class GH_Context(object):
    """ GH_Context() """
    def AddParticle(self, particle_x, particle_y, *__args):
        """ AddParticle(self: GH_Context, particle_x: float, particle_y: float, particle_z: float, particle_charge: float, particle_radius: float)AddParticle(self: GH_Context, particle_x: float, particle_y: float, particle_charge: float, particle_radius: float)AddParticle(self: GH_Context, particle_x: float, particle_y: float) """
        pass

    def ClosestParticle(self, sample_x, sample_y, *__args):
        """
        ClosestParticle(self: GH_Context, sample_x: float, sample_y: float, sample_z: float) -> (int, float)
        ClosestParticle(self: GH_Context, sample_x: float, sample_y: float) -> (int, float)
        """
        pass

    @staticmethod
    def InverseSquareSolver(context, x, y):
        """ InverseSquareSolver(context: GH_Context, x: float, y: float) -> float """
        pass

    def Particle(self, index):
        """ Particle(self: GH_Context, index: int) -> GH_Particle """
        pass

    def Potential(self, x, y):
        """ Potential(self: GH_Context, x: float, y: float) -> float """
        pass

    def RemoveParticle(self, index):
        """ RemoveParticle(self: GH_Context, index: int) """
        pass

    @staticmethod
    def SineFallOffSolver(context, x, y):
        """ SineFallOffSolver(context: GH_Context, x: float, y: float) -> float """
        pass

    def SolveIsoSurfaces(self, threshold, history=None):
        """
        SolveIsoSurfaces(self: GH_Context, threshold: float) -> (List[GH_IsoSurface], GH_2DSparseArray[bool])
        SolveIsoSurfaces(self: GH_Context, threshold: float) -> List[GH_IsoSurface]
        """
        pass

    Accuracy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Accuracy(self: GH_Context) -> float

Set: Accuracy(self: GH_Context) = value
"""

    Affinity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Affinity(self: GH_Context) -> float

Set: Affinity(self: GH_Context) = value
"""

    ParticleCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParticleCount(self: GH_Context) -> int

"""

    SolverDelegate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SolverDelegate(self: GH_Context) -> FieldSolver

Set: SolverDelegate(self: GH_Context) = value
"""


    FieldSolver = None


class GH_Direction(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_Direction, values: down (3), invalid (0), left (1), right (2), up (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
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

    def __str__(self, *args): #cannot find CLR method
        pass

    down = None
    invalid = None
    left = None
    right = None
    up = None
    value__ = None


class GH_IsoSurface(List[GH_Vertex], IList[GH_Vertex], ICollection[GH_Vertex], IEnumerable[GH_Vertex], IEnumerable, IList, ICollection, IReadOnlyList[GH_Vertex], IReadOnlyCollection[GH_Vertex]):
    """
    GH_IsoSurface()
    GH_IsoSurface(initial_capacity: int)
    """
    def Smooth(self):
        """ Smooth(self: GH_IsoSurface) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, initial_capacity=None):
        """
        __new__(cls: type)
        __new__(cls: type, initial_capacity: int)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsClosed(self: GH_IsoSurface) -> bool

"""



class GH_Mask(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_Mask, values: _0000 (0), _0001 (1), _0010 (2), _0011 (3), _0100 (4), _0101 (5), _0110 (6), _0111 (7), _1000 (8), _1001 (9), _1010 (10), _1011 (11), _1100 (12), _1101 (13), _1110 (14), _1111 (15) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
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

    def __str__(self, *args): #cannot find CLR method
        pass

    value__ = None
    _0000 = None
    _0001 = None
    _0010 = None
    _0011 = None
    _0100 = None
    _0101 = None
    _0110 = None
    _0111 = None
    _1000 = None
    _1001 = None
    _1010 = None
    _1011 = None
    _1100 = None
    _1101 = None
    _1110 = None
    _1111 = None


class GH_Particle(object):
    """
    GH_Particle()
    GH_Particle(nx: float, ny: float, nz: float, nc: float, nr: float)
    """
    @staticmethod # known case of __new__
    def __new__(self, nx=None, ny=None, nz=None, nc=None, nr=None):
        """
        __new__(cls: type)
        __new__(cls: type, nx: float, ny: float, nz: float, nc: float, nr: float)
        """
        pass

    c = None
    r = None
    x = None
    y = None
    z = None


class GH_Vertex(object, IComparable[GH_Vertex]):
    """
    GH_Vertex()
    GH_Vertex(vx: float, vy: float)
    GH_Vertex(pt: PointF)
    GH_Vertex(other: GH_Vertex)
    """
    def Equals(self, obj):
        """ Equals(self: GH_Vertex, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: GH_Vertex) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, vx: float, vy: float)
        __new__(cls: type, pt: PointF)
        __new__(cls: type, other: GH_Vertex)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    X = None
    Y = None


