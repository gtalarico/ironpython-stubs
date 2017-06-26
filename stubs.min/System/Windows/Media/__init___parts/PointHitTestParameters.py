class PointHitTestParameters(HitTestParameters):
 """
 Specifies a System.Windows.Point as the parameter to be used for hit testing of a visual object.
 
 PointHitTestParameters(point: Point)
 """
 @staticmethod
 def __new__(self,point):
  """ __new__(cls: type,point: Point) """
  pass
 HitPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Point against which to hit test.

Get: HitPoint(self: PointHitTestParameters) -> Point

"""


