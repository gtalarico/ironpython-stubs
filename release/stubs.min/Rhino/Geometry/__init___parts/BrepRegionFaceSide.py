class BrepRegionFaceSide(object):
 """ Represents a side of a Rhino.Geometry.BrepRegion entity. """
 Brep=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The brep this side belongs to.



Get: Brep(self: BrepRegionFaceSide) -> Brep



"""

 Face=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the face this side belongs to.



Get: Face(self: BrepRegionFaceSide) -> BrepFace



"""

 Region=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The region this side belongs to.



Get: Region(self: BrepRegionFaceSide) -> BrepRegion



"""

 SurfaceNormalPointsIntoRegion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets true if BrepFace's surface normal points into region; false otherwise.



Get: SurfaceNormalPointsIntoRegion(self: BrepRegionFaceSide) -> bool



"""


