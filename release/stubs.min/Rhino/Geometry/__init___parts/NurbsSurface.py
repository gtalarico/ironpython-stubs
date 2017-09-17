class NurbsSurface(Surface,IDisposable,ISerializable,IEpsilonComparable[NurbsSurface]):
 """ NurbsSurface(other: NurbsSurface) """
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 def CopyFrom(self,other):
  """ CopyFrom(self: NurbsSurface,other: NurbsSurface) """
  pass
 @staticmethod
 def Create(dimension,isRational,order0,order1,controlPointCount0,controlPointCount1):
  """ Create(dimension: int,isRational: bool,order0: int,order1: int,controlPointCount0: int,controlPointCount1: int) -> NurbsSurface """
  pass
 @staticmethod
 def CreateFromCone(cone):
  """ CreateFromCone(cone: Cone) -> NurbsSurface """
  pass
 @staticmethod
 def CreateFromCylinder(cylinder):
  """ CreateFromCylinder(cylinder: Cylinder) -> NurbsSurface """
  pass
 @staticmethod
 def CreateFromSphere(sphere):
  """ CreateFromSphere(sphere: Sphere) -> NurbsSurface """
  pass
 @staticmethod
 def CreateFromTorus(torus):
  """ CreateFromTorus(torus: Torus) -> NurbsSurface """
  pass
 @staticmethod
 def CreateRuledSurface(curveA,curveB):
  """ CreateRuledSurface(curveA: Curve,curveB: Curve) -> NurbsSurface """
  pass
 def Dispose(self):
  """ Dispose(self: CommonObject,disposing: bool) """
  pass
 def EpsilonEquals(self,other,epsilon):
  """ EpsilonEquals(self: NurbsSurface,other: NurbsSurface,epsilon: float) -> bool """
  pass
 def IncreaseDegreeU(self,desiredDegree):
  """ IncreaseDegreeU(self: NurbsSurface,desiredDegree: int) -> bool """
  pass
 def IncreaseDegreeV(self,desiredDegree):
  """ IncreaseDegreeV(self: NurbsSurface,desiredDegree: int) -> bool """
  pass
 def MakeNonRational(self):
  """ MakeNonRational(self: NurbsSurface) -> bool """
  pass
 def MakeRational(self):
  """ MakeRational(self: NurbsSurface) -> bool """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: CommonObject) """
  pass
 def OnSwitchToNonConst(self,*args):
  """ OnSwitchToNonConst(self: GeometryBase) """
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
 @staticmethod
 def __new__(self,other):
  """
  __new__(cls: type,other: NurbsSurface)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 IsRational=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsRational(self: NurbsSurface) -> bool

"""

 KnotsU=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: KnotsU(self: NurbsSurface) -> NurbsSurfaceKnotList

"""

 KnotsV=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: KnotsV(self: NurbsSurface) -> NurbsSurfaceKnotList

"""

 OrderU=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderU(self: NurbsSurface) -> int

"""

 OrderV=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderV(self: NurbsSurface) -> int

"""

 Points=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Points(self: NurbsSurface) -> NurbsSurfacePointList

"""


