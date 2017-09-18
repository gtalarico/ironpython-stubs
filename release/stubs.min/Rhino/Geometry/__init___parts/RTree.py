class RTree(object,IDisposable):
 """
 Represents a spatial search structure based on implementations of the

    R-tree algorithm by Toni Gutman.

 

 RTree()
 """
 def Clear(self):
  """
  Clear(self: RTree)

   Removes all elements.
  """
  pass
 @staticmethod
 def CreateMeshFaceTree(mesh):
  """
  CreateMeshFaceTree(mesh: Mesh) -> RTree

  

   Constructs a new tree with an element for each face in the mesh.

     The element id is 

    set to the index of the face.

  

  

   mesh: A mesh.

   Returns: A new tree,or null on error.
  """
  pass
 @staticmethod
 def CreatePointCloudTree(cloud):
  """
  CreatePointCloudTree(cloud: PointCloud) -> RTree

  

   Constructs a new tree with an element for each pointcloud point.

  

   cloud: A pointcloud.

   Returns: A new tree,or null on error.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: RTree)

   Actively reclaims unmanaged resources that this instance uses.
  """
  pass
 def Insert(self,*__args):
  """
  Insert(self: RTree,box: BoundingBox,elementId: IntPtr) -> bool

  

   Inserts an element into the tree.

  

   box: A bounding box.

   elementId: A pointer.

   Returns: true if element was successfully inserted.

  Insert(self: RTree,point: Point2d,elementId: int) -> bool

  

   Inserts an element into the tree.

  

   point: A point.

   elementId: A number.

   Returns: true if element was successfully inserted.

  Insert(self: RTree,point: Point2d,elementId: IntPtr) -> bool

  

   Inserts an element into the tree.

  

   point: A point.

   elementId: A pointer.

   Returns: true if element was successfully inserted.

  Insert(self: RTree,point: Point3d,elementId: int) -> bool

  

   Inserts an element into the tree.

  

   point: A point.

   elementId: A number.

   Returns: true if element was successfully inserted.

  Insert(self: RTree,point: Point3d,elementId: IntPtr) -> bool

  

   Inserts an element into the tree.

  

   point: A point.

   elementId: A pointer.

   Returns: true if element was successfully inserted.

  Insert(self: RTree,box: BoundingBox,elementId: int) -> bool

  

   Inserts an element into the tree.

  

   box: A bounding box.

   elementId: A number.

   Returns: true if element was successfully inserted.
  """
  pass
 def Remove(self,*__args):
  """
  Remove(self: RTree,box: BoundingBox,elementId: IntPtr) -> bool

  

   Removes an element from the tree.

  

   box: A bounding box.

   elementId: A pointer.

   Returns: true if element was successfully removed.

  Remove(self: RTree,point: Point2d,elementId: int) -> bool

  

   Removes an element from the tree.

  

   point: A point.

   elementId: A number.

   Returns: true if element was successfully removed.

  Remove(self: RTree,box: BoundingBox,elementId: int) -> bool

  

   Removes an element from the tree.

  

   box: A bounding box.

   elementId: A number.

   Returns: true if element was successfully removed.

  Remove(self: RTree,point: Point3d,elementId: int) -> bool

  

   Removes an element from the tree.

  

   point: A point.

   elementId: A number.

   Returns: true if element was successfully removed.

  Remove(self: RTree,point: Point3d,elementId: IntPtr) -> bool

  

   Removes an element from the tree.

  

   point: A point.

   elementId: A pointer.

   Returns: true if element was successfully removed.
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
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of items in this tree.



Get: Count(self: RTree) -> int



"""


