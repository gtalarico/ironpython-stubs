class Transform(object,IComparable[Transform],IEquatable[Transform]):
 """
 Represents the values in a 4x4 transform matrix.

    This is parallel to C++ ON_Xform.

 

 Transform(diagonalValue: float)
 """
 @staticmethod
 def ChangeBasis(*__args):
  """
  ChangeBasis(initialBasisX: Vector3d,initialBasisY: Vector3d,initialBasisZ: Vector3d,finalBasisX: Vector3d,finalBasisY: Vector3d,finalBasisZ: Vector3d) -> Transform

  

   Computes a change of basis transformation. A basis change is essentially a remapping 

      

      of geometry from one coordinate system to another.

  

  

   initialBasisX: can be any 3d basis.

   initialBasisY: can be any 3d basis.

   initialBasisZ: can be any 3d basis.

   finalBasisX: can be any 3d basis.

   finalBasisY: can be any 3d basis.

   finalBasisZ: can be any 3d basis.

   Returns: A transformation matrix which orients geometry from one coordinate system to another on success.


    
     Transform.Unset on failure.

  

  ChangeBasis(plane0: Plane,plane1: Plane) -> Transform

  

   Computes a change of basis transformation. A basis change is essentially a remapping 

      

      of geometry from one coordinate system to another.

  

  

   plane0: Coordinate system in which the geometry is currently described.

   plane1: Target coordinate system in which we want the geometry to be described.

   Returns: A transformation matrix which orients geometry from one coordinate system to another on success.


    
     Transform.Unset on failure.
  """
  pass
 def CompareTo(self,other):
  """
  CompareTo(self: Transform,other: Transform) -> int

  

   Compares this transform with another transform.

     M33 has highest value,then M32,

    etc..

  

  

   other: Another transform.

   Returns: -1 if this < other; 0 if both are equal; 1 otherwise.
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Transform,other: Transform) -> bool

  

   Determines if another transform equals this transform value.

  

   other: Another transform.

   Returns: true if other has the same value as this transform; otherwise,false.

  Equals(self: Transform,obj: object) -> bool

  

   Determines if another object is a transform and its value equals this transform value.

  

   obj: Another object.

   Returns: true if obj is a transform and has the same value as this transform; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Transform) -> int

  

   Gets a non-unique hashing code for this transform.

   Returns: A number that can be used to hash this transform in a dictionary.
  """
  pass
 @staticmethod
 def Mirror(*__args):
  """
  Mirror(mirrorPlane: Plane) -> Transform

  

   Constructs a new Mirror transformation.

  

   mirrorPlane: Plane that defines the mirror orientation and position.

   Returns: A transformation matrix which mirrors geometry in a specified plane.

  Mirror(pointOnMirrorPlane: Point3d,normalToMirrorPlane: Vector3d) -> Transform

  

   Create mirror transformation matrix

     The mirror transform maps a point Q to 

      

      Q - (2*(Q-P)oN)*N,where

     P=pointOnMirrorPlane and N=normalToMirrorPlane.

  

  

   pointOnMirrorPlane: Point on the mirror plane.

   normalToMirrorPlane: Normal vector to the mirror plane.

   Returns: A transformation matrix which mirrors geometry in a specified plane.
  """
  pass
 @staticmethod
 def Multiply(a,b):
  """
  Multiply(a: Transform,b: Transform) -> Transform

  

   Multiplies (combines) two transformations.

     This is the same as the * operator 

    between two transformations.

  

  

   a: First transformation.

   b: Second transformation.

   Returns: A transformation matrix that combines the effect of both input transformations. 

     

    The resulting Transform gives the same result as though you'd first apply A then B.
  """
  pass
 @staticmethod
 def PlanarProjection(plane):
  """
  PlanarProjection(plane: Plane) -> Transform

  

   Constructs a projection transformation.

  

   plane: Plane onto which everything will be perpendicularly projected.

   Returns: A transformation matrix which projects geometry onto a specified plane.
  """
  pass
 @staticmethod
 def PlaneToPlane(plane0,plane1):
  """ PlaneToPlane(plane0: Plane,plane1: Plane) -> Transform """
  pass
 @staticmethod
 def Rotation(*__args):
  """
  Rotation(startDirection: Vector3d,endDirection: Vector3d,rotationCenter: Point3d) -> Transform

  

   Constructs a new rotation transformation with start and end directions and rotation center.

  

   startDirection: A start direction.

   endDirection: An end direction.

   rotationCenter: A rotation center.

   Returns: A transformation matrix which rotates geometry around an anchor point.

  Rotation(x0: Vector3d,y0: Vector3d,z0: Vector3d,x1: Vector3d,y1: Vector3d,z1: Vector3d) -> Transform

  

   Constructs a transformation that maps X0 to X1,Y0 to Y1,Z0 to Z1.

  

   x0: First "from" vector.

   y0: Second "from" vector.

   z0: Third "from" vector.

   x1: First "to" vector.

   y1: Second "to" vector.

   z1: Third "to" vector.

   Returns: A rotation transformation value.

  Rotation(angleRadians: float,rotationAxis: Vector3d,rotationCenter: Point3d) -> Transform

  

   Constructs a new rotation transformation with specified angle,rotation center and rotation axis.

  

   angleRadians: Angle (in Radians) of the rotation.

   rotationAxis: Axis direction of rotation operation.

   rotationCenter: Center point of rotation. Rotation axis is vertical.

   Returns: A transformation matrix which rotates geometry around an anchor point.

  Rotation(sinAngle: float,cosAngle: float,rotationAxis: Vector3d,rotationCenter: Point3d) -> Transform

  

   Constructs a new rotation transformation with specified angle,rotation center and rotation axis.

  

   sinAngle: Sin of the rotation angle.

   cosAngle: Cos of the rotation angle.

   rotationAxis: Axis direction of rotation.

   rotationCenter: Center point of rotation.

   Returns: A transformation matrix which rotates geometry around an anchor point.

  Rotation(angleRadians: float,rotationCenter: Point3d) -> Transform

  

   Constructs a new rotation transformation with specified angle and rotation center.

  

   angleRadians: Angle (in Radians) of the rotation.

   rotationCenter: Center point of rotation. Rotation axis is vertical.

   Returns: A transformation matrix which rotates geometry around an anchor point.
  """
  pass
 @staticmethod
 def Scale(*__args):
  """
  Scale(plane: Plane,xScaleFactor: float,yScaleFactor: float,zScaleFactor: float) -> Transform

  

   Constructs a new non-uniform scaling transformation with a specified scaling anchor point.

  

   plane: Defines the center and orientation of the scaling operation.

   xScaleFactor: Scaling factor along the anchor plane X-Axis direction.

   yScaleFactor: Scaling factor along the anchor plane Y-Axis direction.

   zScaleFactor: Scaling factor along the anchor plane Z-Axis direction.

   Returns: A transformation matrix which scales geometry non-uniformly.

  Scale(anchor: Point3d,scaleFactor: float) -> Transform

  

   Constructs a new uniform scaling transformation with a specified scaling anchor point.

  

   anchor: Defines the anchor point of the scaling operation.

   scaleFactor: Scaling factor in all directions.

   Returns: A transform matrix which scales geometry uniformly around the anchor point.
  """
  pass
 @staticmethod
 def Shear(plane,x,y,z):
  """
  Shear(plane: Plane,x: Vector3d,y: Vector3d,z: Vector3d) -> Transform

  

   Constructs a Shear transformation.

  

   plane: Base plane for shear.

   x: Shearing vector along plane x-axis.

   y: Shearing vector along plane y-axis.

   z: Shearing vector along plane z-axis.

   Returns: A transformation matrix which shear geometry.
  """
  pass
 def ToFloatArray(self,rowDominant):
  """
  ToFloatArray(self: Transform,rowDominant: bool) -> Array[Single]

  

   Return the matrix as a linear array of 16 float values
  """
  pass
 def ToString(self):
  """
  ToString(self: Transform) -> str

  

   Returns a string representation of this transform.

   Returns: A textual representation.
  """
  pass
 def TransformBoundingBox(self,bbox):
  """
  TransformBoundingBox(self: Transform,bbox: BoundingBox) -> BoundingBox

  

   Computes a new boundingbox that is the smallest axis aligned

     boundingbox that 

    contains the transformed result of its 8 original corner

     points.

  

   Returns: A new bounding box.
  """
  pass
 def TransformList(self,points):
  """ TransformList(self: Transform,points: IEnumerable[Point3d]) -> Array[Point3d] """
  pass
 @staticmethod
 def Translation(*__args):
  """
  Translation(dx: float,dy: float,dz: float) -> Transform

  

   Constructs a new translation (move) tranformation. 

     Right column is (dx,dy,dz,

    1.0).

  

  

   dx: Distance to translate (move) geometry along the world X axis.

   dy: Distance to translate (move) geometry along the world Y axis.

   dz: Distance to translate (move) geometry along the world Z axis.

   Returns: A transform matrix which moves geometry with the specified distances.

  Translation(motion: Vector3d) -> Transform

  

   Constructs a new translation (move) transformation.

  

   motion: Translation (motion) vector.

   Returns: A transform matrix which moves geometry along the motion vector.
  """
  pass
 def Transpose(self):
  """
  Transpose(self: Transform) -> Transform

  

   Flip row/column values
  """
  pass
 def TryGetInverse(self,inverseTransform):
  """
  TryGetInverse(self: Transform) -> (bool,Transform)

  

   Attempts to get the inverse transform of this transform.

   Returns: true on success. 

     If false is returned and this Transform is Invalid,

    inserveTransform will be set to this Transform. 

     If false is returned and this 

    Transform is Valid,inverseTransform will be set to a pseudo inverse.
  """
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
  """
  __rmul__(a: Transform,b: Transform) -> Transform

  

   Multiplies (combines) two transformations.

  

   a: First transformation.

   b: Second transformation.

   Returns: A transformation matrix that combines the effect of both input transformations. 

     

    The resulting Transform gives the same result as though you'd first apply A then B.
  """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 def __str__(self,*args):
  pass
 Determinant=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The determinant of this 4x4 matrix.



Get: Determinant(self: Transform) -> float



"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not this Transform is a valid matrix. 

   A valid transform matrix is not allowed to have any invalid numbers.



Get: IsValid(self: Transform) -> bool



"""

 M00=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets this[0,0].



Get: M00(self: Transform) -> float



Set: M00(self: Transform)=value

"""

 M01=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets this[0,1].



Get: M01(self: Transform) -> float



Set: M01(self: Transform)=value

"""

 M02=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets this[0,2].



Get: M02(self: Transform) -> float



Set: M02(self: Transform)=value

"""

 M03=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets this[0,3].



Get: M03(self: Transform) -> float



Set: M03(self: Transform)=value

"""

 M10=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets this[1,0].



Get: M10(self: Transform) -> float



Set: M10(self: Transform)=value

"""

 M11=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets this[1,1].



Get: M11(self: Transform) -> float



Set: M11(self: Transform)=value

"""

 M12=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets this[1,2].



Get: M12(self: Transform) -> float



Set: M12(self: Transform)=value

"""

 M13=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets this[1,3].



Get: M13(self: Transform) -> float



Set: M13(self: Transform)=value

"""

 M20=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets this[2,0].



Get: M20(self: Transform) -> float



Set: M20(self: Transform)=value

"""

 M21=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets this[2,1].



Get: M21(self: Transform) -> float



Set: M21(self: Transform)=value

"""

 M22=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets this[2,2].



Get: M22(self: Transform) -> float



Set: M22(self: Transform)=value

"""

 M23=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets this[2,3].



Get: M23(self: Transform) -> float



Set: M23(self: Transform)=value

"""

 M30=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets this[3,0].



Get: M30(self: Transform) -> float



Set: M30(self: Transform)=value

"""

 M31=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets this[3,1].



Get: M31(self: Transform) -> float



Set: M31(self: Transform)=value

"""

 M32=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets this[3,2].



Get: M32(self: Transform) -> float



Set: M32(self: Transform)=value

"""

 M33=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets this[3,3].



Get: M33(self: Transform) -> float



Set: M33(self: Transform)=value

"""

 SimilarityType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not the Transform maintains similarity. 

   The easiest way to think of Similarity is that any circle,when transformed,

   remains a circle. Whereas a non-similarity Transform deforms circles into ellipses.



Get: SimilarityType(self: Transform) -> TransformSimilarityType



"""


 Identity=None
 Unset=None

