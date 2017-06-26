class BoundingBox(object):
 """
 BoundingBox(min: Point3d,max: Point3d)
 BoundingBox(minX: float,minY: float,minZ: float,maxX: float,maxY: float,maxZ: float)
 BoundingBox(points: IEnumerable[Point3d])
 """
 def ClosestPoint(self,point,includeInterior=None):
  """
  ClosestPoint(self: BoundingBox,point: Point3d,includeInterior: bool) -> Point3d
  ClosestPoint(self: BoundingBox,point: Point3d) -> Point3d
  """
  pass
 def Contains(self,*__args):
  """
  Contains(self: BoundingBox,box: BoundingBox) -> bool
  Contains(self: BoundingBox,box: BoundingBox,strict: bool) -> bool
  Contains(self: BoundingBox,point: Point3d) -> bool
  Contains(self: BoundingBox,point: Point3d,strict: bool) -> bool
  """
  pass
 def Corner(self,minX,minY,minZ):
  """ Corner(self: BoundingBox,minX: bool,minY: bool,minZ: bool) -> Point3d """
  pass
 def FurthestPoint(self,point):
  """ FurthestPoint(self: BoundingBox,point: Point3d) -> Point3d """
  pass
 def GetCorners(self):
  """ GetCorners(self: BoundingBox) -> Array[Point3d] """
  pass
 def GetEdges(self):
  """ GetEdges(self: BoundingBox) -> Array[Line] """
  pass
 def Inflate(self,*__args):
  """ Inflate(self: BoundingBox,xAmount: float,yAmount: float,zAmount: float)Inflate(self: BoundingBox,amount: float) """
  pass
 @staticmethod
 def Intersection(a,b):
  """ Intersection(a: BoundingBox,b: BoundingBox) -> BoundingBox """
  pass
 def IsDegenerate(self,tolerance):
  """ IsDegenerate(self: BoundingBox,tolerance: float) -> int """
  pass
 def MakeValid(self):
  """ MakeValid(self: BoundingBox) -> bool """
  pass
 def PointAt(self,tx,ty,tz):
  """ PointAt(self: BoundingBox,tx: float,ty: float,tz: float) -> Point3d """
  pass
 def ToBrep(self):
  """ ToBrep(self: BoundingBox) -> Brep """
  pass
 def ToString(self):
  """ ToString(self: BoundingBox) -> str """
  pass
 def Transform(self,xform):
  """ Transform(self: BoundingBox,xform: Transform) -> bool """
  pass
 def Union(self,*__args):
  """
  Union(a: BoundingBox,b: BoundingBox) -> BoundingBox
  Union(box: BoundingBox,point: Point3d) -> BoundingBox
  Union(self: BoundingBox,other: BoundingBox)Union(self: BoundingBox,point: Point3d)
  """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[BoundingBox]() -> BoundingBox
  
  __new__(cls: type,min: Point3d,max: Point3d)
  __new__(cls: type,minX: float,minY: float,minZ: float,maxX: float,maxY: float,maxZ: float)
  __new__(cls: type,points: IEnumerable[Point3d])
  """
  pass
 Center=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Center(self: BoundingBox) -> Point3d

"""

 Diagonal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Diagonal(self: BoundingBox) -> Vector3d

"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsValid(self: BoundingBox) -> bool

"""

 Max=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Max(self: BoundingBox) -> Point3d

Set: Max(self: BoundingBox)=value
"""

 Min=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Min(self: BoundingBox) -> Point3d

Set: Min(self: BoundingBox)=value
"""


 Empty=None
 Unset=None

