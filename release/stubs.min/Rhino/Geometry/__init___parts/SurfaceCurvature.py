class SurfaceCurvature(object):
 """ Maintains computed information for surface curvature evaluation. """
 def Direction(self,direction):
  """
  Direction(self: SurfaceCurvature,direction: int) -> Vector3d

  

   Gets the principal curvature direction vector.

  

   direction: Direction index,valid values are 0 and 1.

   Returns: The specified direction vector.
  """
  pass
 def Kappa(self,direction):
  """
  Kappa(self: SurfaceCurvature,direction: int) -> float

  

   Gets the Kappa curvature value.

  

   direction: Kappa index,valid values are 0 and 1.

   Returns: The specified kappa value.
  """
  pass
 def OsculatingCircle(self,direction):
  """
  OsculatingCircle(self: SurfaceCurvature,direction: int) -> Circle

  

   Computes the osculating circle along the given direction.

  

   direction: Direction index,valid values are 0 and 1.

   Returns: The osculating circle in the given direction or Circle.Unset on failure.
  """
  pass
 Gaussian=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Gaussian curvature value at UV.



Get: Gaussian(self: SurfaceCurvature) -> float



"""

 Mean=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Mean curvature value at UV.



Get: Mean(self: SurfaceCurvature) -> float



"""

 Normal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the surface normal at UV.



Get: Normal(self: SurfaceCurvature) -> Vector3d



"""

 Point=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the surface point at UV.



Get: Point(self: SurfaceCurvature) -> Point3d



"""

 UVPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the UV location where the curvature was computed.



Get: UVPoint(self: SurfaceCurvature) -> Point2d



"""


