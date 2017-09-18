class SurfaceObject(RhinoObject):
 """ Represents a Rhino.Geometry.Surfacesurface in a document. """
 def DuplicateSurfaceGeometry(self):
  """
  DuplicateSurfaceGeometry(self: SurfaceObject) -> Surface

  

   Constructs a new deep copy of the surface geometry.

   Returns: The copy of the geometry.
  """
  pass
 SurfaceGeometry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the surface geometry linked with this object.



Get: SurfaceGeometry(self: SurfaceObject) -> Surface



"""


