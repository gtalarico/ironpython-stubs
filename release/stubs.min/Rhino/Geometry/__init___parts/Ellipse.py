class Ellipse(object,IEpsilonComparable[Ellipse]):
 """
 Represents the values of a plane and the two semiaxes radii in an ellipse.

 

 Ellipse(plane: Plane,radius1: float,radius2: float)

 Ellipse(center: Point3d,second: Point3d,third: Point3d)
 """
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Ellipse,other: Ellipse,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def ToNurbsCurve(self):
  """
  ToNurbsCurve(self: Ellipse) -> NurbsCurve

  

   Constructs a nurbs curve representation of this ellipse. 

     This is equivalent to 

    calling NurbsCurve.CreateFromEllipse().

  

   Returns: A nurbs curve representation of this ellipse or null if no such representation could be made.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[Ellipse]() -> Ellipse

  

  __new__(cls: type,plane: Plane,radius1: float,radius2: float)

  __new__(cls: type,center: Point3d,second: Point3d,third: Point3d)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Plane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the base plane of the ellipse.



Get: Plane(self: Ellipse) -> Plane



Set: Plane(self: Ellipse)=value

"""

 Radius1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the radius of the ellipse along the base plane X semiaxis.



Get: Radius1(self: Ellipse) -> float



Set: Radius1(self: Ellipse)=value

"""

 Radius2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the radius of the ellipse along the base plane Y semiaxis.



Get: Radius2(self: Ellipse) -> float



Set: Radius2(self: Ellipse)=value

"""


