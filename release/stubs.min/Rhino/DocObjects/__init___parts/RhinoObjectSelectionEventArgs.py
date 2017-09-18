class RhinoObjectSelectionEventArgs(EventArgs):
 # no doc
 Document=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Document(self: RhinoObjectSelectionEventArgs) -> RhinoDoc



"""

 RhinoObjects=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: RhinoObjects(self: RhinoObjectSelectionEventArgs) -> Array[RhinoObject]



"""

 Selected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns true if objects are being selected.

   Returns false if objects are being deseleced.



Get: Selected(self: RhinoObjectSelectionEventArgs) -> bool



"""


