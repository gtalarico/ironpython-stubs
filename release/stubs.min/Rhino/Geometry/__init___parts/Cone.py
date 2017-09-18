class Cone(object,IEpsilonComparable[Cone]):
 """
 Represents the center plane,radius and height values in a right circular cone.

 

 Cone(plane: Plane,height: float,radius: float)
 """
 def AngleInDegrees(self):
  """
  AngleInDegrees(self: Cone) -> float

  

   Computes the angle (in degrees) between the axis and the 

     side of the cone.

      

      The angle and the height have the same sign.

  

   Returns: An angle in degrees.
  """
  pass
 def AngleInRadians(self):
  """
  AngleInRadians(self: Cone) -> float

  

   Computes the angle (in radians) between the axis and the 

     side of the cone.

      

      The angle and the height have the same sign.

  

   Returns: Math.Atan(Radius / Height) if the height is not 0; 0 if the radius is 0; Math.PI otherwise.
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Cone,other: Cone,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def ToBrep(self,capBottom):
  """
  ToBrep(self: Cone,capBottom: bool) -> Brep

  

   Gets a Brep representation of the cone with a single

     face for the cone,an edge 

    along the cone seam,

     and vertices at the base and apex ends of this seam edge.

     

       The optional cap is a single face with one circular edge 

     starting and 

    ending at the base vertex.

  

  

   capBottom: true if the bottom should be filled with a surface. false otherwise.

   Returns: A brep (polysurface) representation of this cone values.
  """
  pass
 def ToNurbsSurface(self):
  """
  ToNurbsSurface(self: Cone) -> NurbsSurface

  

   Constructs a Nurbs surface representation of this Cone. 

     This is synonymous with 

    calling NurbsSurface.CreateFromCone().

  

   Returns: A Nurbs surface representation of the cone or null.
  """
  pass
 def ToRevSurface(self):
  """
  ToRevSurface(self: Cone) -> RevSurface

  

   Constructs a RevSurface representation of this Cone. 

     This is synonymous with 

    calling RevSurface.CreateFromCone().

  

   Returns: A RevSurface representation of the cone or null.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,plane,height,radius):
  """
  __new__[Cone]() -> Cone

  

  __new__(cls: type,plane: Plane,height: float,radius: float)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 ApexPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Point at tip of the cone.



Get: ApexPoint(self: Cone) -> Point3d



"""

 Axis=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Unit vector axis of cone.



Get: Axis(self: Cone) -> Vector3d



"""

 BasePoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Center of base circle.



Get: BasePoint(self: Cone) -> Point3d



"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of the circular right cone.



Get: Height(self: Cone) -> float



Set: Height(self: Cone)=value

"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """true if plane is valid,height is not zero and radius is not zero.



Get: IsValid(self: Cone) -> bool



"""

 Plane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the base plane of the cone.



Get: Plane(self: Cone) -> Plane



Set: Plane(self: Cone)=value

"""

 Radius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the radius of the cone.



Get: Radius(self: Cone) -> float



Set: Radius(self: Cone)=value

"""


 Unset=None

