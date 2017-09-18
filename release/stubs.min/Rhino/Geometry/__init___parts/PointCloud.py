class PointCloud(GeometryBase,IDisposable,ISerializable,IEnumerable[PointCloudItem],IEnumerable):
 """
 Represents a collection of coordinates with optional normal vectors and colors.

 

 PointCloud()

 PointCloud(other: PointCloud)

 PointCloud(points: IEnumerable[Point3d])
 """
 def Add(self,point,*__args):
  """
  Add(self: PointCloud,point: Point3d,color: Color)

   Append a new point to the end of the list.

  

   point: Point to append.

   color: Color of new point.

  Add(self: PointCloud,point: Point3d,normal: Vector3d,color: Color)

   Append a new point to the end of the list.

  

   point: Point to append.

   normal: Normal vector of new point.

   color: Color of new point.

  Add(self: PointCloud,point: Point3d)

   Append a new point to the end of the list.

  

   point: Point to append.

  Add(self: PointCloud,point: Point3d,normal: Vector3d)

   Append a new point to the end of the list.

  

   point: Point to append.

   normal: Normal vector of new point.
  """
  pass
 def AddRange(self,points):
  """ AddRange(self: PointCloud,points: IEnumerable[Point3d]) """
  pass
 def AppendNew(self):
  """
  AppendNew(self: PointCloud) -> PointCloudItem

  

   Appends a new PointCloudItem to the end of this point cloud.

   Returns: The newly appended item.
  """
  pass
 def ClearColors(self):
  """
  ClearColors(self: PointCloud)

   Destroys the color information in this point cloud.
  """
  pass
 def ClearHiddenFlags(self):
  """
  ClearHiddenFlags(self: PointCloud)

   Destroys the hidden flag information in this point cloud.
  """
  pass
 def ClearNormals(self):
  """
  ClearNormals(self: PointCloud)

   Destroys the normal vector information in this point cloud.
  """
  pass
 def ClosestPoint(self,testPoint):
  """
  ClosestPoint(self: PointCloud,testPoint: Point3d) -> int

  

   Returns index of the closest point in the point cloud to a given test point.

  

   testPoint: .

   Returns: Index of point in the point cloud on success. -1 on failure.
  """
  pass
 def ConstructConstObject(self,*args):
  """
  ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int)

   Assigns a parent object and a subobject index to this.

  

   parentObject: The parent object.

   subobject_index: The subobject index.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: CommonObject,disposing: bool)

   For derived class implementers.

     This method is called with argument true when class 

    user calls Dispose(),while with argument false when

     the Garbage Collector invokes 

    the finalizer,or Finalize() method.You must reclaim all used unmanaged resources in both cases,

    and can use this chance to call Dispose on disposable fields if the argument is true.Also,you 

    must call the base virtual method within your overriding method.

  

  

   disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 

    finalizer.
  """
  pass
 def GetColors(self):
  """
  GetColors(self: PointCloud) -> Array[Color]

  

   Copy all the point colors in this point cloud to an array.

   Returns: An array containing all the colors in this point cloud.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: PointCloud) -> IEnumerator[PointCloudItem]

  

   Gets an enumerator that allows to modify each pointcloud point.

   Returns: A instance of System.Collections.Generic.IEnumerator.
  """
  pass
 def GetNormals(self):
  """
  GetNormals(self: PointCloud) -> Array[Vector3d]

  

   Copy all the normal vectors in this point cloud to an array.

   Returns: An array containing all the normals in this point cloud.
  """
  pass
 def GetPoints(self):
  """
  GetPoints(self: PointCloud) -> Array[Point3d]

  

   Copy all the point coordinates in this point cloud to an array.

   Returns: An array containing all the points in this point cloud.
  """
  pass
 def Insert(self,index,point,*__args):
  """
  Insert(self: PointCloud,index: int,point: Point3d,color: Color)

   Inserts a new point into the point list.

  

   index: Insertion index.

   point: Point to append.

   color: Color of new point.

  Insert(self: PointCloud,index: int,point: Point3d,normal: Vector3d,color: Color)

   Inserts a new point into the point list.

  

   index: Insertion index.

   point: Point to append.

   normal: Normal vector of new point.

   color: Color of new point.

  Insert(self: PointCloud,index: int,point: Point3d)

   Inserts a new point into the point list.

  

   index: Insertion index.

   point: Point to append.

  Insert(self: PointCloud,index: int,point: Point3d,normal: Vector3d)

   Inserts a new point into the point list.

  

   index: Insertion index.

   point: Point to append.

   normal: Normal vector of new point.
  """
  pass
 def InsertNew(self,index):
  """
  InsertNew(self: PointCloud,index: int) -> PointCloudItem

  

   Inserts a new Rhino.Geometry.PointCloudItem at a specific position of the point cloud.

  

   index: Index of new item.

   Returns: The newly inserted item.
  """
  pass
 def InsertRange(self,index,points):
  """ InsertRange(self: PointCloud,index: int,points: IEnumerable[Point3d]) """
  pass
 def Merge(self,other):
  """
  Merge(self: PointCloud,other: PointCloud)

   Copies the point values of another pointcloud into this one.

  

   other: PointCloud to merge with this one.
  """
  pass
 def NonConstOperation(self,*args):
  """
  NonConstOperation(self: CommonObject)

   For derived classes implementers.

     Defines the necessary implementation to free the 

    instance from being const.
  """
  pass
 def OnSwitchToNonConst(self,*args):
  """
  OnSwitchToNonConst(self: GeometryBase)

   Is called when a non-const operation occurs.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: PointCloud,index: int)

   Remove the point at the given index.

  

   index: Index of point to remove.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """ __contains__[PointCloudItem](enumerable: IEnumerable[PointCloudItem],value: PointCloudItem) -> bool """
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
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,other: PointCloud)

  __new__(cls: type,points: IEnumerable[Point3d])

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 ContainsColors=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not the points in this 

   pointcloud have colors assigned to them.



Get: ContainsColors(self: PointCloud) -> bool



"""

 ContainsHiddenFlags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not the points in this 

   pointcloud have hidden flags assigned to them.



Get: ContainsHiddenFlags(self: PointCloud) -> bool



"""

 ContainsNormals=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not the points in this 

   pointcloud have normals assigned to them.



Get: ContainsNormals(self: PointCloud) -> bool



"""

 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of points in this pointcloud.



Get: Count(self: PointCloud) -> int



"""

 HiddenPointCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of points that have their Hidden flag set.



Get: HiddenPointCount(self: PointCloud) -> int



"""


