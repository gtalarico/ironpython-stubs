class RhinoTransformObjectsEventArgs(EventArgs):
 """ EventArgs passed to RhinoDoc.BeforeTransform. """
 ObjectCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ObjectCount(self: RhinoTransformObjectsEventArgs) -> int



"""

 Objects=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Objects(self: RhinoTransformObjectsEventArgs) -> Array[RhinoObject]



"""

 ObjectsWillBeCopied=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ObjectsWillBeCopied(self: RhinoTransformObjectsEventArgs) -> bool



"""

 Transform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Transform(self: RhinoTransformObjectsEventArgs) -> Transform



"""


