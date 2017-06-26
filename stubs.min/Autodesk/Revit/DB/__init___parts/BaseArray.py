class BaseArray(Element,IDisposable):
 """ An abstract base class that represents an array within the Revit project. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetCopiedMemberIds(self):
  """
  GetCopiedMemberIds(self: BaseArray) -> ICollection[ElementId]
  
   Retrieves the copied member Ids of the Array.
   Returns: The copied member Ids of the Array
  """
  pass
 def GetOriginalMemberIds(self):
  """
  GetOriginalMemberIds(self: BaseArray) -> ICollection[ElementId]
  
   Retrieves the original member Ids of the Array.
   Returns: The original member Ids of the Array
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
 Label=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The family parameter label of the BaseArray.

Get: Label(self: BaseArray) -> FamilyParameter

Set: Label(self: BaseArray)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get and Set the Name property

Set: Name(self: BaseArray)=value
"""

 NumMembers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves or changes the number of the arrayed members.

Get: NumMembers(self: BaseArray) -> int

Set: NumMembers(self: BaseArray)=value
"""


