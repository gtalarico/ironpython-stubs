class TessellatedFace(object, IDisposable):
    """
    Defines a planar face bounded by a polyline in 3d space. A face
       consists of a single connected component and can have holes.
    
    TessellatedFace(allLoopVertices: IList[IList[XYZ]], materialId: ElementId)
    TessellatedFace(outerLoopVertices: IList[XYZ], materialId: ElementId)
    """
    def Dispose(self):
        """ Dispose(self: TessellatedFace) """
        pass

    def GetBoundaryLoops(self):
        """
        GetBoundaryLoops(self: TessellatedFace) -> IList[IList[XYZ]]
        
            Get loops bounding the face.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: TessellatedFace, disposing: bool) """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, allLoopVertices: IList[IList[XYZ]], materialId: ElementId)
        __new__(cls: type, outerLoopVertices: IList[XYZ], materialId: ElementId)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: TessellatedFace) -> bool

"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Material of the face.

Get: MaterialId(self: TessellatedFace) -> ElementId

Set: MaterialId(self: TessellatedFace) = value
"""


