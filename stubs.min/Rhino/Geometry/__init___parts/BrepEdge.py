class BrepEdge(CurveProxy, IDisposable, ISerializable):
    # no doc
    def AdjacentFaces(self):
        """ AdjacentFaces(self: BrepEdge) -> Array[int] """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """ ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: Curve, disposing: bool) """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """ NonConstOperation(self: Curve) """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """ OnSwitchToNonConst(self: GeometryBase) """
        pass

    def SetEdgeCurve(self, curve3dIndex, subDomain=None):
        """
        SetEdgeCurve(self: BrepEdge, curve3dIndex: int, subDomain: Interval) -> bool
        SetEdgeCurve(self: BrepEdge, curve3dIndex: int) -> bool
        """
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

    Brep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Brep(self: BrepEdge) -> Brep

"""

    EdgeIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeIndex(self: BrepEdge) -> int

"""

    EndVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndVertex(self: BrepEdge) -> BrepVertex

"""

    StartVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartVertex(self: BrepEdge) -> BrepVertex

"""

    Tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tolerance(self: BrepEdge) -> float

Set: Tolerance(self: BrepEdge) = value
"""

    TrimCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TrimCount(self: BrepEdge) -> int

"""

    Valence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Valence(self: BrepEdge) -> EdgeAdjacency

"""


