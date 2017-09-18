class GeometryHitTestParameters(HitTestParameters):
 """
 Specifies a System.Windows.Media.Geometry as the parameter to be used for hit testing a visual tree.
 
 GeometryHitTestParameters(geometry: Geometry)
 """
 @staticmethod
 def __new__(self,geometry):
  """ __new__(cls: type,geometry: Geometry) """
  pass
 HitGeometry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Media.Geometry that defines the hit test geometry for this System.Windows.Media.GeometryHitTestParameters instance.

Get: HitGeometry(self: GeometryHitTestParameters) -> Geometry

"""


