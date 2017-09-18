class BrepObject(RhinoObject):
 """ Represents a Rhino.Geometry.Brepbrep in a document. """
 def DuplicateBrepGeometry(self):
  """
  DuplicateBrepGeometry(self: BrepObject) -> Brep

  

   Constructs a new deep copy of the brep geometry.

   Returns: The copy of the geometry.
  """
  pass
 BrepGeometry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the brep geometry linked with this object.



Get: BrepGeometry(self: BrepObject) -> Brep



"""


