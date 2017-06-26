class RTree(object,IDisposable):
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
 def Insert(self,*__args):
  """
  Insert(self: RTree,box: BoundingBox,elementId: IntPtr) -> bool
  Insert(self: RTree,point: Point2d,elementId: int) -> bool
  Insert(self: RTree,point: Point2d,elementId: IntPtr) -> bool
  Insert(self: RTree,point: Point3d,elementId: int) -> bool
  Insert(self: RTree,point: Point3d,elementId: IntPtr) -> bool
  Insert(self: RTree,box: BoundingBox,elementId: int) -> bool
  """
  pass
 def Remove(self,*__args):
  """
  Remove(self: RTree,box: BoundingBox,elementId: IntPtr) -> bool
  Remove(self: RTree,point: Point2d,elementId: int) -> bool
  Remove(self: RTree,box: BoundingBox,elementId: int) -> bool
  Remove(self: RTree,point: Point3d,elementId: int) -> bool
  Remove(self: RTree,point: Point3d,elementId: IntPtr) -> bool
  """
  pass
 def Search(self,*__args):
  """
  Search(self: RTree,sphere: Sphere,callback: EventHandler[RTreeEventArgs]) -> bool
  Search(self: RTree,sphere: Sphere,callback: EventHandler[RTreeEventArgs],tag: object) -> bool
  Search(self: RTree,box: BoundingBox,callback: EventHandler[RTreeEventArgs]) -> bool
  Search(self: RTree,box: BoundingBox,callback: EventHandler[RTreeEventArgs],tag: object) -> bool
  """
  pass
 @staticmethod
 def SearchOverlaps(treeA,treeB,tolerance,callback):
  """ SearchOverlaps(treeA: RTree,treeB: RTree,tolerance: float,callback: EventHandler[RTreeEventArgs]) -> bool """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Count(self: RTree) -> int

"""


