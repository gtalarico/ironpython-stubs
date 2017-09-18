class Quaternion(object,IEquatable[Quaternion],IEpsilonComparable[Quaternion]):
 """
 Represents the four coefficient values in a quaternion.

    The first value a is the real part,

    while the rest multipies i,j and k,that are imaginary.quaternion=a + bi + cj + dk

 

 Quaternion(a: float,b: float,c: float,d: float)
 """
 @staticmethod
 def CrossProduct(p,q):
  """
  CrossProduct(p: Quaternion,q: Quaternion) -> Quaternion

  

   Computes the vector cross product of p and q=(0,x,y,z),

     where (x,y,z)=

    Rhino.Geometry.Vector3d.CrossProduct(Rhino.Geometry.Vector3d,Rhino.Geometry.Vector3d)CrossProduct

    (p.Rhino.Geometry.Quaternion.VectorVector,q.Rhino.Geometry.Quaternion.VectorVector).This is not 

    the same as the quaternion product p*q.

  

  

   p: A quaternion.

   q: Another quaternion.

   Returns: A new quaternion.
  """
  pass
 @staticmethod
 def Distance(p,q):
  """
  Distance(p: Quaternion,q: Quaternion) -> float

  

   Returns the distance or norm of the difference between two quaternions.

  

   p: A quaternion.

   q: Another quaternion.

   Returns: (p - q).Length()
  """
  pass
 def DistanceTo(self,q):
  """
  DistanceTo(self: Quaternion,q: Quaternion) -> float

  

   Computes the distance or norm of the difference between this and another quaternion.

  

   q: Another quaternion.

   Returns: (this - q).Length.
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Quaternion,other: Quaternion,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Quaternion,obj: object) -> bool

  

   Determines whether an object is a quaternion and has the same value of this quaternion.

  

   obj: Another object to compare.

   Returns: true if obj is a quaternion and has exactly equal coefficients; otherwise false.

  Equals(self: Quaternion,other: Quaternion) -> bool

  

   Determines whether this quaternion has the same value of another quaternion.

  

   other: Another quaternion to compare.

   Returns: true if the quaternions have exactly equal coefficients; otherwise false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Quaternion) -> int

  

   Gets a non-unique but repeatable hashing code for this quaternion.

   Returns: A signed number.
  """
  pass
 def GetRotation(self,*__args):
  """
  GetRotation(self: Quaternion) -> (bool,Plane)

  

   Returns the frame created by applying the quaternion's rotation

     to the canonical 

    world frame (1,0,0),(0,1,0),(0,0,1).

  

   Returns: true if the operation succeeded; otherwise,false.

  GetRotation(self: Quaternion) -> (bool,float,Vector3d)

  

   Returns the rotation defined by the quaternion.

   Returns: True if the operation succeeded; otherwise,false.
  """
  pass
 def Invert(self):
  """
  Invert(self: Quaternion) -> bool

  

   Modifies this quaternion to become

     (a/L2,-b/L2,-c/L2,-d/L2),where L2=length 

    squared=(a*a + b*b + c*c + d*d).This is the multiplicative inverse,i.e.,

     

    (a,b,c,d)*(a/L2,-b/L2,-c/L2,-d/L2)=(1,0,0,0).

  

   Returns: true if successful. false if the quaternion is zero and cannot be inverted.
  """
  pass
 def MatrixForm(self):
  """
  MatrixForm(self: Quaternion) -> Transform

  

   Returns 4x4 real valued matrix form of the quaternion

     a  b  c  d

     -b  a 

    -d  c

     -c  d  a -b

     -d -c  b  a

     which has the same 

    arithmetic properties as the quaternion.

  

   Returns: A transform value.
  """
  pass
 @staticmethod
 def Product(p,q):
  """
  Product(p: Quaternion,q: Quaternion) -> Quaternion

  

   The quaternion product of p and q.  This is the same value as p*q.

  

   p: The first trasform.

   q: The second trasform.

   Returns: A transform value.
  """
  pass
 def Rotate(self,v):
  """
  Rotate(self: Quaternion,v: Vector3d) -> Vector3d

  

   Rotates a 3d vector. This operation is also called conjugation,

     because the result 

    is the same as

     (q.Conjugate()*(0,x,y,x)*q/q.LengthSquared).Vector.

  

  

   v: The vector to be rotated.

   Returns: R*v,where R is the rotation defined by the unit quaternion.

     This is mathematically 

    the same as the values

     (Inverse(q)*(0,x,y,z)*q).Vector

     and

       

     (q.Conjugate()*(0,x,y,x)*q/q.LengthSquared).Vector.
  """
  pass
 @staticmethod
 def Rotation(*__args):
  """
  Rotation(plane0: Plane,plane1: Plane) -> Quaternion

  

   Returns the unit quaternion that represents the the rotation that maps

     plane0.xaxis 

    to plane1.xaxis,plane0.yaxis to plane1.yaxis,and 

     plane0.zaxis to plane1.zaxis.

  

  

   plane0: The first plane.

   plane1: The second plane.

   Returns: A quaternion value.

  Rotation(angle: float,axisOfRotation: Vector3d) -> Quaternion

  

   Returns the unit quaternion

     cos(angle/2),sin(angle/2)*x,sin(angle/2)*y,

    sin(angle/2)*z

     where (x,y,z) is the unit vector parallel to axis.  This is the

   

      unit quaternion that represents the rotation of angle about axis.

  

  

   angle: An angle in radians.

   axisOfRotation: The axis of rotation.

   Returns: A new quaternion.
  """
  pass
 def Set(self,a,b,c,d):
  """
  Set(self: Quaternion,a: float,b: float,c: float,d: float)

   Sets all coefficients of the quaternion.
  """
  pass
 def SetRotation(self,*__args):
  """
  SetRotation(self: Quaternion,plane0: Plane,plane1: Plane)

   Sets the quaternion to the unit quaternion which rotates

     plane0.xaxis to 

    plane1.xaxis,plane0.yaxis to plane1.yaxis,

     and plane0.zaxis to plane1.zaxis.

  

  

   plane0: The "from" rotation plane. Origin point is ignored.

   plane1: The "to" rotation plane. Origin point is ignored.

  SetRotation(self: Quaternion,angle: float,axisOfRotation: Vector3d)

   Sets the quaternion to cos(angle/2),sin(angle/2)*x,sin(angle/2)*y,sin(angle/2)*z

     

    where (x,y,z) is the unit vector parallel to axis.  This is the unit quaternion

     

    that represents the rotation of angle about axis.

  

  

   angle: in radians.

   axisOfRotation: The direction of the axis of rotation.
  """
  pass
 def Unitize(self):
  """
  Unitize(self: Quaternion) -> bool

  

   Scales the quaternion's coordinates so that a*a + b*b + c*c + d*d=1.

   Returns: true if successful.  false if the quaternion is zero and cannot be unitized.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __div__(self,*args):
  """ x.__div__(y) <==> x/y """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __mul__(self,*args):
  """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*yx.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
  pass
 @staticmethod
 def __new__(self,a,b,c,d):
  """
  __new__[Quaternion]() -> Quaternion

  

  __new__(cls: type,a: float,b: float,c: float,d: float)
  """
  pass
 def __ne__(self,*args):
  pass
 def __radd__(self,*args):
  """
  __radd__(a: Quaternion,b: Quaternion) -> Quaternion

  

   Adds two quaternions.

     This sums each quaternion coefficient with its correspondant 

    and returns

     a new result quaternion.

  

  

   a: A quaternion.

   b: Another quaternion.

   Returns: A new quaternion.
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rmul__(self,*args):
  """
  __rmul__(a: Quaternion,b: Quaternion) -> Quaternion

  

   Multiplies a quaternion with another one.

     Quaternion multiplication (Hamilton 

    product) is not commutative.

  

  

   a: The first term.

   b: The second term.

   Returns: A new quaternion.
  """
  pass
 def __rsub__(self,*args):
  """
  __rsub__(a: Quaternion,b: Quaternion) -> Quaternion

  

   Subtracts a quaternion from another one.

     This computes the difference of each 

    quaternion coefficient with its

     correspondant and returns a new result quaternion.

  

  

   a: A quaternion.

   b: Another quaternion.

   Returns: A new quaternion.
  """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 A=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the real part of the quaternion.



Get: A(self: Quaternion) -> float



Set: A(self: Quaternion)=value

"""

 B=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the first imaginary coefficient of the quaternion.



Get: B(self: Quaternion) -> float



Set: B(self: Quaternion)=value

"""

 C=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the second imaginary coefficient of the quaternion.



Get: C(self: Quaternion) -> float



Set: C(self: Quaternion)=value

"""

 Conjugate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a new quaternion that is the conjugate of this quaternion.

   This is (a,-b,-c,-d)



Get: Conjugate(self: Quaternion) -> Quaternion



"""

 D=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the third imaginary coefficient of the quaternion.



Get: D(self: Quaternion) -> float



Set: D(self: Quaternion)=value

"""

 Inverse=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Computes a new inverted quaternion,

   (a/L2,-b/L2,-c/L2,-d/L2),where L2=length squared=(a*a + b*b + c*c + d*d).

   This is the multiplicative inverse,i.e.,

   (a,b,c,d)*(a/L2,-b/L2,-c/L2,-d/L2)=(1,0,0,0).

   If this is the zero quaternion,then the zero quaternion is returned.



Get: Inverse(self: Quaternion) -> Quaternion



"""

 IsScalar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """true if b,c,and d are all zero.



Get: IsScalar(self: Quaternion) -> bool



"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if the four coefficients are valid numbers within RhinoCommon.

   See Rhino.RhinoMath.IsValidDouble(System.Double).



Get: IsValid(self: Quaternion) -> bool



"""

 IsVector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """true if a=0 and at least one of b,c,or d is not zero.



Get: IsVector(self: Quaternion) -> bool



"""

 IsZero=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """true if a,b,c,and d are all zero.



Get: IsZero(self: Quaternion) -> bool



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the length or norm of the quaternion.



Get: Length(self: Quaternion) -> float



"""

 LengthSquared=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the result of (a^2 + b^2 + c^2 + d^2).



Get: LengthSquared(self: Quaternion) -> float



"""

 Scalar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The real (scalar) part of the quaternion

   This is Rhino.Geometry.Quaternion.A.



Get: Scalar(self: Quaternion) -> float



"""

 Vector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The imaginary part of the quaternion

   (B,C,D)



Get: Vector(self: Quaternion) -> Vector3d



"""


 I=None
 Identity=None
 J=None
 K=None
 Zero=None

