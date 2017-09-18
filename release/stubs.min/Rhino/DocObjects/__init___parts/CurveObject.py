class CurveObject(RhinoObject):
 """ A Rhino Object that represents curve geometry and attributes """
 def DuplicateCurveGeometry(self):
  """ DuplicateCurveGeometry(self: CurveObject) -> Curve """
  pass
 CurveGeometry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CurveGeometry(self: CurveObject) -> Curve



"""


