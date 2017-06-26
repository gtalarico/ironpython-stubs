class SurfaceCurvature(object):
 # no doc
 def Direction(self,direction):
  """ Direction(self: SurfaceCurvature,direction: int) -> Vector3d """
  pass
 def Kappa(self,direction):
  """ Kappa(self: SurfaceCurvature,direction: int) -> float """
  pass
 def OsculatingCircle(self,direction):
  """ OsculatingCircle(self: SurfaceCurvature,direction: int) -> Circle """
  pass
 Gaussian=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Gaussian(self: SurfaceCurvature) -> float

"""

 Mean=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Mean(self: SurfaceCurvature) -> float

"""

 Normal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Normal(self: SurfaceCurvature) -> Vector3d

"""

 Point=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Point(self: SurfaceCurvature) -> Point3d

"""

 UVPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UVPoint(self: SurfaceCurvature) -> Point2d

"""


