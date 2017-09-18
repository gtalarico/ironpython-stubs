class IndependentTag(Element,IDisposable):
 """ Represents an IndependentTag within Autodesk Revit. """
 def CanLeaderEndConditionBeAssigned(self,leaderEndCondition):
  """
  CanLeaderEndConditionBeAssigned(self: IndependentTag,leaderEndCondition: LeaderEndCondition) -> bool

  

   Checks whether the LeaderEndCondition can be assigned.

  

   leaderEndCondition: The leader end condition to check.

   Returns: True if the leader end condition of the tag can be assigned,or false otherwise.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetTaggedLocalElement(self):
  """
  GetTaggedLocalElement(self: IndependentTag) -> Element

  

   Get the tagged local element if any.

   Returns: The tagged local element,or ll for orphan tags and tagged elements in links.
  """
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
 """Whether the tag has a leader or not.



Get: HasLeader(self: IndependentTag) -> bool



Set: HasLeader(self: IndependentTag)=value

"""

 IsMaterialTag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if it is a material tag or not.



Get: IsMaterialTag(self: IndependentTag) -> bool



"""

 IsMulticategoryTag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if it is a multi-category tag or not.



Get: IsMulticategoryTag(self: IndependentTag) -> bool



"""

 IsOrphaned=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the tag is orphaned or not.



Get: IsOrphaned(self: IndependentTag) -> bool



"""

 LeaderElbow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the position of the elbow of leader.



Get: LeaderElbow(self: IndependentTag) -> XYZ



Set: LeaderElbow(self: IndependentTag)=value

"""

 LeaderEnd=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the position of the end of leader.



Get: LeaderEnd(self: IndependentTag) -> XYZ



Set: LeaderEnd(self: IndependentTag)=value

"""

 LeaderEndCondition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The leader end condition of the tag.



Get: LeaderEndCondition(self: IndependentTag) -> LeaderEndCondition



Set: LeaderEndCondition(self: IndependentTag)=value

"""

 MultiReferenceAnnotationId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The multi-reference annotation which owns this tag.



Get: MultiReferenceAnnotationId(self: IndependentTag) -> ElementId



"""

 TaggedElementId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The LinkElementId of the tagged element.



Get: TaggedElementId(self: IndependentTag) -> LinkElementId



"""

 TaggedLocalElementId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the tagged local element if any.



Get: TaggedLocalElementId(self: IndependentTag) -> ElementId



"""

 TagHeadPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the position of the head of tag.



Get: TagHeadPosition(self: IndependentTag) -> XYZ



Set: TagHeadPosition(self: IndependentTag)=value

"""

 TagOrientation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The tag orientation of the tag.



Get: TagOrientation(self: IndependentTag) -> TagOrientation



Set: TagOrientation(self: IndependentTag)=value

"""

 TagText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The text associated with the tag. If there are several strings assiciated with the tag,the strings will be returned concatenated.



Get: TagText(self: IndependentTag) -> str



"""


