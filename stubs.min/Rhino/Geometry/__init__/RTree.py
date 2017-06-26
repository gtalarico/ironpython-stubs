class RTree(object, IDisposable):
    """ RTree() """
    def Clear(self):
        """ Clear(self: RTree) """
        pass

    @staticmethod
    def CreateMeshFaceTree(mesh):
        """ CreateMeshFaceTree(mesh: Mesh) -> RTree """
        pass

    @staticmethod
    def CreatePointCloudTree(cloud):
        """ CreatePointCloudTree(cloud: PointCloud) -> RTree """
        pass

    def Dispose(self):
        """ Dispose(self: RTree) """
        pass

    def Insert(self, *__args):
        """
        Insert(self: RTree, box: BoundingBox, elementId: IntPtr) -> bool
        Insert(self: RTree, point: Point2d, elementId: int) -> bool
        Insert(self: RTree, point: Point2d, elementId: IntPtr) -> bool
        Insert(self: RTree, point: Point3d, elementId: int) -> bool
        Insert(self: RTree, point: Point3d, elementId: IntPtr) -> bool
        Insert(self: RTree, box: BoundingBox, elementId: int) -> bool
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: RTree, box: BoundingBox, elementId: IntPtr) -> bool
        Remove(self: RTree, point: Point2d, elementId: int) -> bool
        Remove(self: RTree, box: BoundingBox, elementId: int) -> bool
        Remove(self: RTree, point: Point3d, elementId: int) -> bool
        Remove(self: RTree, point: Point3d, elementId: IntPtr) -> bool
        """
        pass

    def Search(self, *__args):
        """
        Search(self: RTree, sphere: Sphere, callback: EventHandler[RTreeEventArgs]) -> bool
        Search(self: RTree, sphere: Sphere, callback: EventHandler[RTreeEventArgs], tag: object) -> bool
        Search(self: RTree, box: BoundingBox, callback: EventHandler[RTreeEventArgs]) -> bool
        Search(self: RTree, box: BoundingBox, callback: EventHandler[RTreeEventArgs], tag: object) -> bool
        """
        pass

    @staticmethod
    def SearchOverlaps(treeA, treeB, tolerance, callback):
        """ SearchOverlaps(treeA: RTree, treeB: RTree, tolerance: float, callback: EventHandler[RTreeEventArgs]) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: RTree) -> int

"""


