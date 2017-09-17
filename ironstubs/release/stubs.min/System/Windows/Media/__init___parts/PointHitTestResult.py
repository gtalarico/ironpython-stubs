class PointHitTestResult(HitTestResult):
 """
 Represents the results of a hit test that uses a System.Windows.Point as a hit test parameter.
 
 PointHitTestResult(visualHit: Visual,pointHit: Point)
 """
 @staticmethod
 def __new__(self,visualHit,pointHit):
  """ __new__(cls: type,visualHit: Visual,pointHit: Point) """
  pass
 PointHit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the point value that is returned from a hit test result.

Get: PointHit(self: PointHitTestResult) -> Point

"""

 VisualHit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the visual object that is returned from a hit test result.

Get: VisualHit(self: PointHitTestResult) -> Visual

"""


