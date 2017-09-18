class BrepRegion(object):
 """ Represents a brep topological region that has sides. """
 def BoundaryBrep(self):
  """
  BoundaryBrep(self: BrepRegion) -> Brep

  

   Gets the boundary of a region as a brep object. If the region is finite,

     the 

    boundary will be a closed  manifold brep. The boundary may have more than one

     

    connected component.

  

   Returns: A brep or null on error.
  """
  pass
 def GetFaceSides(self):
  """
  GetFaceSides(self: BrepRegion) -> Array[BrepRegionFaceSide]

  

   Gets an array of Rhino.Geometry.BrepRegionFaceSide entities delimiting this region.

   Returns: An array of region face sides. This array might be empty on failure.
  """
  pass
 BoundingBox=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the region bounding box.



Get: BoundingBox(self: BrepRegion) -> BoundingBox



"""

 Brep=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a reference to the Brep this region belongs to.



Get: Brep(self: BrepRegion) -> Brep



"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of region in the RegionTopology array.



Get: Index(self: BrepRegion) -> int



"""

 IsFinite=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this region is finite.



Get: IsFinite(self: BrepRegion) -> bool



"""


