class ClippingPlaneObject(RhinoObject):
 """
 Represents the object of a Rhino.Geometry.ClippingPlaneSurfaceclipping plane,

    stored in the Rhino document and with attributes.
 """
 ClippingPlaneGeometry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the clipping plane surface.



Get: ClippingPlaneGeometry(self: ClippingPlaneObject) -> ClippingPlaneSurface



"""


