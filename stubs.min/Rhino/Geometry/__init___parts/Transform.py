class Transform(object,IComparable[Transform],IEquatable[Transform]):
 """ Transform(diagonalValue: float) """
 @staticmethod
 def ChangeBasis(*__args):
  """
  ChangeBasis(initialBasisX: Vector3d,initialBasisY: Vector3d,initialBasisZ: Vector3d,finalBasisX: Vector3d,finalBasisY: Vector3d,finalBasisZ: Vector3d) -> Transform
  ChangeBasis(plane0: Plane,plane1: Plane) -> Transform
  """
  pass
 def CompareTo(self,other):
  """ CompareTo(self: Transform,other: Transform) -> int """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Transform,other: Transform) -> bool
  Equals(self: Transform,obj: object) -> bool
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: Transform) -> int """
  pass
 @staticmethod
 def Mirror(*__args):
  """
  Mirror(mirrorPlane: Plane) -> Transform
  Mirror(pointOnMirrorPlane: Point3d,normalToMirrorPlane: Vector3d) -> Transform
  """
  pass
 @staticmethod
 def Multiply(a,b):
  """ Multiply(a: Transform,b: Transform) -> Transform """
  pass
 @staticmethod
 def PlanarProjection(plane):
  """ PlanarProjection(plane: Plane) -> Transform """
  pass
 @staticmethod
 def PlaneToPlane(plane0,plane1):
  """ PlaneToPlane(plane0: Plane,plane1: Plane) -> Transform """
  pass
 @staticmethod
 def Rotation(*__args):
  """
  Rotation(startDirection: Vector3d,endDirection: Vector3d,rotationCenter: Point3d) -> Transform
  Rotation(x0: Vector3d,y0: Vector3d,z0: Vector3d,x1: Vector3d,y1: Vector3d,z1: Vector3d) -> Transform
  Rotation(angleRadians: float,rotationAxis: Vector3d,rotationCenter: Point3d) -> Transform
  Rotation(sinAngle: float,cosAngle: float,rotationAxis: Vector3d,rotationCenter: Point3d) -> Transform
  Rotation(angleRadians: float,rotationCenter: Point3d) -> Transform
  """
  pass
 @staticmethod
 def Scale(*__args):
  """
  Scale(plane: Plane,xScaleFactor: float,yScaleFactor: float,zScaleFactor: float) -> Transform
  Scale(anchor: Point3d,scaleFactor: float) -> Transform
  """
  pass
 @staticmethod
 def Shear(plane,x,y,z):
  """ Shear(plane: Plane,x: Vector3d,y: Vector3d,z: Vector3d) -> Transform """
  pass
 def ToFloatArray(self,rowDominant):
  """ ToFloatArray(self: Transform,rowDominant: bool) -> Array[Single] """
  pass
 def ToString(self):
  """ ToString(self: Transform) -> str """
  pass
 def TransformBoundingBox(self,bbox):
  """ TransformBoundingBox(self: Transform,bbox: BoundingBox) -> BoundingBox """
  pass
 def TransformList(self,points):
  """ TransformList(self: Transform,points: IEnumerable[Point3d]) -> Array[Point3d] """
  pass
 @staticmethod
 def Translation(*__args):
  """
  Translation(dx: float,dy: float,dz: float) -> Transform
  Translation(motion: Vector3d) -> Transform
  """
  pass
 def Transpose(self):
  """ Transpose(self: Transform) -> Transform """
  pass
 def TryGetInverse(self,inverseTransform):
  """ TryGetInverse(self: Transform) -> (bool,Transform) """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __mul__(self,*args):
  """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
  pass
 @staticmethod
 def __new__(self,diagonalValue):
  """
  __new__[Transform]() -> Transform
  
  __new__(cls: type,diagonalValue: float)
  """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rmul__(self,*args):
  """ __rmul__(a: Transform,b: Transform) -> Transform """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 def __str__(self,*args):
  pass
 Determinant=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Determinant(self: Transform) -> float

"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsValid(self: Transform) -> bool

"""

 M00=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: M00(self: Transform) -> float

Set: M00(self: Transform)=value
"""

 M01=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: M01(self: Transform) -> float

Set: M01(self: Transform)=value
"""

 M02=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: M02(self: Transform) -> float

Set: M02(self: Transform)=value
"""

 M03=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: M03(self: Transform) -> float

Set: M03(self: Transform)=value
"""

 M10=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: M10(self: Transform) -> float

Set: M10(self: Transform)=value
"""

 M11=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: M11(self: Transform) -> float

Set: M11(self: Transform)=value
"""

 M12=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: M12(self: Transform) -> float

Set: M12(self: Transform)=value
"""

 M13=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: M13(self: Transform) -> float

Set: M13(self: Transform)=value
"""

 M20=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: M20(self: Transform) -> float

Set: M20(self: Transform)=value
"""

 M21=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: M21(self: Transform) -> float

Set: M21(self: Transform)=value
"""

 M22=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: M22(self: Transform) -> float

Set: M22(self: Transform)=value
"""

 M23=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: M23(self: Transform) -> float

Set: M23(self: Transform)=value
"""

 M30=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: M30(self: Transform) -> float

Set: M30(self: Transform)=value
"""

 M31=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: M31(self: Transform) -> float

Set: M31(self: Transform)=value
"""

 M32=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: M32(self: Transform) -> float

Set: M32(self: Transform)=value
"""

 M33=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: M33(self: Transform) -> float

Set: M33(self: Transform)=value
"""

 SimilarityType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SimilarityType(self: Transform) -> TransformSimilarityType

"""


 Identity=None
 Unset=None

