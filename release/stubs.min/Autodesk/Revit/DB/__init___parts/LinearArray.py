class LinearArray(BaseArray,IDisposable):
 """ An object that represents an Array created linearly within the Revit project. """
 @staticmethod
 def ArrayElementsWithoutAssociation(aDoc,dBView,ids,count,translationToAnchorMember,anchorMember):
  """ ArrayElementsWithoutAssociation(aDoc: Document,dBView: View,ids: ICollection[ElementId],count: int,translationToAnchorMember: XYZ,anchorMember: ArrayAnchorMember) -> ICollection[ElementId] """
  pass
 @staticmethod
 def ArrayElementWithoutAssociation(aDoc,dBView,id,count,translationToAnchorMember,anchorMember):
  """
  ArrayElementWithoutAssociation(aDoc: Document,dBView: View,id: ElementId,count: int,translationToAnchorMember: XYZ,anchorMember: ArrayAnchorMember) -> ICollection[ElementId]
  
   Creates a new linear array from a single element.
  
   aDoc: The document.
   dBView: The view. If it is a 2d view,translation vector must be in the view plane if 
    the element is a view-specific element.
  
   id: The element to array.
   count: The number of array members to create including the initial
     element 
    grouping. Must between 2 and 200.
  
   translationToAnchorMember: The translation vector for the array.
   anchorMember: Indicates if the translation vector specifies the location of the second member
    
     of the array,or the last member of the array.
  
   Returns: The ids of the elements created during the operation.
  """
  pass
 @staticmethod
 def Create(aDoc,dBView,*__args):
  """
  Create(aDoc: Document,dBView: View,ids: ICollection[ElementId],count: int,translationToAnchorMember: XYZ,anchorMember: ArrayAnchorMember) -> LinearArray
  Create(aDoc: Document,dBView: View,id: ElementId,count: int,translationToAnchorMember: XYZ,anchorMember: ArrayAnchorMember) -> LinearArray
  
   Creates a new linear array element from a single element.
  
   aDoc: The document.
   dBView: The view. If it is a 2d view,translation vector must be in the view plane if 
    the element is a view-specific element.
  
   id: The element to array.
   count: The number of array members to create including the initial
     element 
    grouping. Must between 2 and 200.
  
   translationToAnchorMember: The translation vector for the array.
   anchorMember: Indicates if the translation vector specifies the location of the second member
    
     of the array,or the last member of the array.
  
   Returns: The new linear array element.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetCopiedMemberIds(self):
  """
  GetCopiedMemberIds(self: LinearArray) -> ICollection[ElementId]
  
   Retrieves the copied member Ids of the Array.
   Returns: The copied member Ids of the Array
  """
  pass
 def GetOriginalMemberIds(self):
  """
  GetOriginalMemberIds(self: LinearArray) -> ICollection[ElementId]
  
   Retrieves the original member Ids of the Array.
   Returns: The original member Ids of the Array
  """
  pass
 @staticmethod
 def IsElementArrayable(aDoc,id):
  """
  IsElementArrayable(aDoc: Document,id: ElementId) -> bool
  
   Indicates whether the input element is arrayable.
  
   aDoc: The document.
   id: The element id.
   Returns: True if the input element is arrayable,false otherwise.
  """
  pass
 @staticmethod
 def IsValidArraySize(count):
  """
  IsValidArraySize(count: int) -> bool
  
   This indicates whether the input count is valid.
  
   count: The count.
   Returns: True if the input count is between 2 and 200,false otherwise.
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
 NumMembers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves or changes the number of the arrayed members.

Get: NumMembers(self: LinearArray) -> int

Set: NumMembers(self: LinearArray)=value
"""


