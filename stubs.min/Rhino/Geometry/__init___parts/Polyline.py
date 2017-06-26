class Polyline(Point3dList,IList[Point3d],ICollection[Point3d],IEnumerable[Point3d],IEnumerable,IList,ICollection):
 """
 Polyline()
 Polyline(initialCapacity: int)
 Polyline(collection: IEnumerable[Point3d])
 """
 def BreakAtAngles(self,angle):
  """ BreakAtAngles(self: Polyline,angle: float) -> Array[Polyline] """
  pass
 def CenterPoint(self):
  """ CenterPoint(self: Polyline) -> Point3d """
  pass
 def ClosestParameter(self,testPoint):
  """ ClosestParameter(self: Polyline,testPoint: Point3d) -> float """
  pass
 def ClosestPoint(self,testPoint):
  """ ClosestPoint(self: Polyline,testPoint: Point3d) -> Point3d """
  pass
 def CollapseShortSegments(self,tolerance):
  """ CollapseShortSegments(self: Polyline,tolerance: float) -> int """
  pass
 def DeleteShortSegments(self,tolerance):
  """ DeleteShortSegments(self: Polyline,tolerance: float) -> int """
  pass
 def GetSegments(self):
  """ GetSegments(self: Polyline) -> Array[Line] """
  pass
 def IsClosedWithinTolerance(self,tolerance):
  """ IsClosedWithinTolerance(self: Polyline,tolerance: float) -> bool """
  pass
 def PointAt(self,t):
  """ PointAt(self: Polyline,t: float) -> Point3d """
  pass
 def ReduceSegments(self,tolerance):
  """ ReduceSegments(self: Polyline,tolerance: float) -> int """
  pass
 def SegmentAt(self,index):
  """ SegmentAt(self: Polyline,index: int) -> Line """
  pass
 def Smooth(self,amount):
  """ Smooth(self: Polyline,amount: float) -> bool """
  pass
 def TangentAt(self,t):
  """ TangentAt(self: Polyline,t: float) -> Vector3d """
  pass
 def ToNurbsCurve(self):
  """ ToNurbsCurve(self: Polyline) -> NurbsCurve """
  pass
 def Trim(self,domain):
  """ Trim(self: Polyline,domain: Interval) -> Polyline """
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
  __new__(cls: type,initialCapacity: int)
  __new__(cls: type,collection: IEnumerable[Point3d])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 IsClosed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsClosed(self: Polyline) -> bool

"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsValid(self: Polyline) -> bool

"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Length(self: Polyline) -> float

"""

 SegmentCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SegmentCount(self: Polyline) -> int

"""


