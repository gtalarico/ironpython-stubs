class Torus(object,IEpsilonComparable[Torus]):
 """
 Represents the value of a plane and two radii in a torus that is oriented in three-dimensional space.

 

 Torus(basePlane: Plane,majorRadius: float,minorRadius: float)
 """
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Torus,other: Torus,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def ToNurbsSurface(self):
  """
  ToNurbsSurface(self: Torus) -> NurbsSurface

  

   Converts this torus to its nurbs surface representation. 

     This is synonymous with 

    calling NurbsSurface.CreateFromTorus().

  

   Returns: A nurbs surface representation of this torus,or null on error.
  """
  pass
 def ToRevSurface(self):
  """
  ToRevSurface(self: Torus) -> RevSurface

  

   Convert this torus to a surface of revolution representation. 

     This is synonymous 

    with calling RevSurface.CreateFromTorus().

  

   Returns: A surface of revolution representation of this torus,or null on error.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,basePlane,majorRadius,minorRadius):
  """
  __new__[Torus]() -> Torus

  

  __new__(cls: type,basePlane: Plane,majorRadius: float,minorRadius: float)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this torus is valid.



Get: IsValid(self: Torus) -> bool



"""

 MajorRadius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the radius of the circle that lies at the heart of the torus.



Get: MajorRadius(self: Torus) -> float



Set: MajorRadius(self: Torus)=value

"""

 MinorRadius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the radius of the torus section.



Get: MinorRadius(self: Torus) -> float



Set: MinorRadius(self: Torus)=value

"""

 Plane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the plane for the torus large circle.



Get: Plane(self: Torus) -> Plane



Set: Plane(self: Torus)=value

"""


 Unset=None

