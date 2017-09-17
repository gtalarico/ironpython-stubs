class PointCloud(GeometryBase,IDisposable,ISerializable,IEnumerable[PointCloudItem],IEnumerable):
 """
 PointCloud()
 PointCloud(other: PointCloud)
 PointCloud(points: IEnumerable[Point3d])
 """
 def Add(self,point,*__args):
  """ Add(self: PointCloud,point: Point3d,color: Color)Add(self: PointCloud,point: Point3d,normal: Vector3d,color: Color)Add(self: PointCloud,point: Point3d)Add(self: PointCloud,point: Point3d,normal: Vector3d) """
  pass
 def AddRange(self,points):
  """ AddRange(self: PointCloud,points: IEnumerable[Point3d]) """
  pass
 def AppendNew(self):
  """ AppendNew(self: PointCloud) -> PointCloudItem """
  pass
 def ClearColors(self):
  """ ClearColors(self: PointCloud) """
  pass
 def ClearHiddenFlags(self):
  """ ClearHiddenFlags(self: PointCloud) """
  pass
 def ClearNormals(self):
  """ ClearNormals(self: PointCloud) """
  pass
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 def Dispose(self):
  """ Dispose(self: CommonObject,disposing: bool) """
  pass
 def GetColors(self):
  """ GetColors(self: PointCloud) -> Array[Color] """
  pass
 def GetEnumerator(self):
  """ GetEnumerator(self: PointCloud) -> IEnumerator[PointCloudItem] """
  pass
 def GetNormals(self):
  """ GetNormals(self: PointCloud) -> Array[Vector3d] """
  pass
 def GetPoints(self):
  """ GetPoints(self: PointCloud) -> Array[Point3d] """
  pass
 def Insert(self,index,point,*__args):
  """ Insert(self: PointCloud,index: int,point: Point3d,color: Color)Insert(self: PointCloud,index: int,point: Point3d,normal: Vector3d,color: Color)Insert(self: PointCloud,index: int,point: Point3d)Insert(self: PointCloud,index: int,point: Point3d,normal: Vector3d) """
  pass
 def InsertNew(self,index):
  """ InsertNew(self: PointCloud,index: int) -> PointCloudItem """
  pass
 def InsertRange(self,index,points):
  """ InsertRange(self: PointCloud,index: int,points: IEnumerable[Point3d]) """
  pass
 def Merge(self,other):
  """ Merge(self: PointCloud,other: PointCloud) """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: CommonObject) """
  pass
 def OnSwitchToNonConst(self,*args):
  """ OnSwitchToNonConst(self: GeometryBase) """
  pass
 def RemoveAt(self,index):
  """ RemoveAt(self: PointCloud,index: int) """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """ __contains__[PointCloudItem](enumerable: IEnumerable[PointCloudItem],value: PointCloudItem) -> bool """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
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
 """Get: ContainsColors(self: PointCloud) -> bool

"""

 ContainsHiddenFlags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ContainsHiddenFlags(self: PointCloud) -> bool

"""

 ContainsNormals=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ContainsNormals(self: PointCloud) -> bool

"""

 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Count(self: PointCloud) -> int

"""

 HiddenPointCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HiddenPointCount(self: PointCloud) -> int

"""


