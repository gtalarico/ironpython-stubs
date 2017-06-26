class SpatialElementTag(Element,IDisposable):
 """ A tag attached to an SpatialElement (room,space or area) in Autodesk Revit. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 HasLeader=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if a leader is displayed for the tag or not.

Get: HasLeader(self: SpatialElementTag) -> bool

Set: HasLeader(self: SpatialElementTag)=value
"""

 IsOrphaned=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the tag is orphaned or not.

Get: IsOrphaned(self: SpatialElementTag) -> bool

"""

 IsTaggingLink=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the tag has reference to an object in a linked document or not.

Get: IsTaggingLink(self: SpatialElementTag) -> bool

"""

 LeaderElbow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The position of the leader's elbow (middle point).

Get: LeaderElbow(self: SpatialElementTag) -> XYZ

Set: LeaderElbow(self: SpatialElementTag)=value
"""

 LeaderEnd=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The position of the leader's end.

Get: LeaderEnd(self: SpatialElementTag) -> XYZ

Set: LeaderEnd(self: SpatialElementTag)=value
"""

 Location=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The location of the tag.

Get: Location(self: SpatialElementTag) -> Location

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name associated with the tag.

Set: Name(self: SpatialElementTag)=value
"""

 TagHeadPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The position of the tag's head.

Get: TagHeadPosition(self: SpatialElementTag) -> XYZ

Set: TagHeadPosition(self: SpatialElementTag)=value
"""

 TagOrientation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The orientation of the tag.

Get: TagOrientation(self: SpatialElementTag) -> SpatialElementTagOrientation

Set: TagOrientation(self: SpatialElementTag)=value
"""

 View=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The view in which the tag was placed.

Get: View(self: SpatialElementTag) -> View

"""


