class Group(Element,IDisposable):
 """ This object represents a group of elements within the project. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetMemberIds(self):
  """
  GetMemberIds(self: Group) -> IList[ElementId]

  

   Retrieves all the member ElementIds of the group.

   Returns: An ordered list of the members within the group. The order of this

  list can be 

    used to match members between other instances of the group.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def UngroupMembers(self):
  """
  UngroupMembers(self: Group) -> ICollection[ElementId]

  

   Ungroups the group.

   Returns: If successful,the ids of the members of group are returned.
  """
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
 GroupType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or set the type of the group.



Get: GroupType(self: Group) -> GroupType



Set: GroupType(self: Group)=value

"""

 Location=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is used to find the physical location of a group within project.



Get: Location(self: Group) -> Location



"""


