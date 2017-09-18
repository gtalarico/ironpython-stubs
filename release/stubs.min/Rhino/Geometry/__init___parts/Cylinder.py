class Cylinder(object,IEpsilonComparable[Cylinder]):
 """
 Represents the values of a plane,a radius and two heights -on top and beneath-

    that define a right circular cylinder.

 

 Cylinder(baseCircle: Circle)

 Cylinder(baseCircle: Circle,height: float)
 """
 def CircleAt(self,linearParameter):
  """
  CircleAt(self: Cylinder,linearParameter: float) -> Circle

  

   Compute the circle at the given elevation parameter.

  

   linearParameter: Height parameter for circle section.
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Cylinder,other: Cylinder,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def LineAt(self,angularParameter):
  """
  LineAt(self: Cylinder,angularParameter: float) -> Line

  

   Compute the line at the given angle parameter. This line will be degenerate if the cylinder is 

    infite.

  

  

   angularParameter: Angle parameter for line section.
  """
  pass
 def ToBrep(self,capBottom,capTop):
  """
  ToBrep(self: Cylinder,capBottom: bool,capTop: bool) -> Brep

  

   Constructs a Brep representation of this Cylinder. 

     This is synonymous with calling 

    NurbsSurface.CreateFromCylinder().

  

  

   capBottom: If true,the bottom of the cylinder will be capped.

   capTop: If true,the top of the cylinder will be capped.

   Returns: A Brep representation of the cylinder or null.
  """
  pass
 def ToNurbsSurface(self):
  """
  ToNurbsSurface(self: Cylinder) -> NurbsSurface

  

   Constructs a Nurbs surface representation of this cylinder. 

     This is synonymous 

    with calling NurbsSurface.CreateFromCylinder().

  

   Returns: A Nurbs surface representation of the cylinder or null.
  """
  pass
 def ToRevSurface(self):
  """
  ToRevSurface(self: Cylinder) -> RevSurface

  

   Constructs a RevSurface representation of this Cylinder. 

     This is synonymous with 

    calling RevSurface.CreateFromCylinder().

  

   Returns: A RevSurface representation of the cylinder or null.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,baseCircle,height=None):
  """
  __new__[Cylinder]() -> Cylinder

  

  __new__(cls: type,baseCircle: Circle)

  __new__(cls: type,baseCircle: Circle,height: float)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Axis=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the axis direction of the cylinder.



Get: Axis(self: Cylinder) -> Vector3d



"""

 Center=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the center point of the defining circle.



Get: Center(self: Cylinder) -> Point3d



"""

 Height1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the start height of the cylinder.



Get: Height1(self: Cylinder) -> float



Set: Height1(self: Cylinder)=value

"""

 Height2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the end height of the cylinder. 

   If the end height equals the start height,the cylinder is 

   presumed to be infinite.



Get: Height2(self: Cylinder) -> float



Set: Height2(self: Cylinder)=value

"""

 IsFinite=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """true if the cylinder is finite (Height0 != Height1)

   false if the cylinder is infinite.



Get: IsFinite(self: Cylinder) -> bool



"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a boolean value indicating whether this cylinder is valid.

   A valid cylinder is represented by a valid circle and two valid heights.



Get: IsValid(self: Cylinder) -> bool



"""

 TotalHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the height of the cylinder. 

   Infinite cylinders have a height of zero,not Double.PositiveInfinity.



Get: TotalHeight(self: Cylinder) -> float



"""


 Unset=None

