class Torus(object,IEpsilonComparable[Torus]):
 """ Torus(basePlane: Plane,majorRadius: float,minorRadius: float) """
 def EpsilonEquals(self,other,epsilon):
  """ EpsilonEquals(self: Torus,other: Torus,epsilon: float) -> bool """
  pass
 def ToNurbsSurface(self):
  """ ToNurbsSurface(self: Torus) -> NurbsSurface """
  pass
 def ToRevSurface(self):
  """ ToRevSurface(self: Torus) -> RevSurface """
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
 """Get: IsValid(self: Torus) -> bool

"""

 MajorRadius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MajorRadius(self: Torus) -> float

Set: MajorRadius(self: Torus)=value
"""

 MinorRadius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MinorRadius(self: Torus) -> float

Set: MinorRadius(self: Torus)=value
"""

 Plane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Plane(self: Torus) -> Plane

Set: Plane(self: Torus)=value
"""


 Unset=None

