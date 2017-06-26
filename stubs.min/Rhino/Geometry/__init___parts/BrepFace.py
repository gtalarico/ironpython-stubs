class BrepFace(SurfaceProxy, IDisposable, ISerializable):
    # no doc
    def AdjacentEdges(self):
        """ AdjacentEdges(self: BrepFace) -> Array[int] """
        pass

    def AdjacentFaces(self):
        """ AdjacentFaces(self: BrepFace) -> Array[int] """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """ ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int) """
        pass

    def CreateExtrusion(self, pathCurve, cap):
        """ CreateExtrusion(self: BrepFace, pathCurve: Curve, cap: bool) -> Brep """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def DuplicateFace(self, duplicateMeshes):
        """ DuplicateFace(self: BrepFace, duplicateMeshes: bool) -> Brep """
        pass

    def DuplicateSurface(self):
        """ DuplicateSurface(self: BrepFace) -> Surface """
        pass

    def GetMesh(self, meshType):
        """ GetMesh(self: BrepFace, meshType: MeshType) -> Mesh """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """ NonConstOperation(self: CommonObject) """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """ OnSwitchToNonConst(self: GeometryBase) """
        pass

    def SetDomain(self, direction, domain):
        """ SetDomain(self: BrepFace, direction: int, domain: Interval) -> bool """
        pass

    def SetMesh(self, meshType, mesh):
        """ SetMesh(self: BrepFace, meshType: MeshType, mesh: Mesh) -> bool """
        pass

    def UnderlyingSurface(self):
        """ UnderlyingSurface(self: BrepFace) -> Surface """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    FaceIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FaceIndex(self: BrepFace) -> int

"""

    IsSurface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSurface(self: BrepFace) -> bool

"""

    Loops = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loops(self: BrepFace) -> BrepLoopList

"""

    OrientationIsReversed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrientationIsReversed(self: BrepFace) -> bool

Set: OrientationIsReversed(self: BrepFace) = value
"""

    OuterLoop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OuterLoop(self: BrepFace) -> BrepLoop

"""

    SurfaceIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceIndex(self: BrepFace) -> int

"""


