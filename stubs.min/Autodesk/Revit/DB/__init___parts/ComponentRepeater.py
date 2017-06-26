class ComponentRepeater(Element,IDisposable,IEnumerable[ComponentRepeaterSlot],IEnumerable):
 """ An element that contains and manages a set of repeated components. """
 @staticmethod
 def CanElementBeRepeated(ADoc,elementId):
  """
  CanElementBeRepeated(ADoc: Document,elementId: ElementId) -> bool
  
   Determines whether an element can be repeated using the RepeatElements method.
  
   ADoc: The document containing the element.
   elementId: The element to be tested.
   Returns: True if the element can be repeated.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: ComponentRepeater) -> IEnumerator[ComponentRepeaterSlot]
  
   Returns an enumerator that iterates through a collection.
   Returns: An IEnumerator object that can be used to iterate through the collection.
  """
  pass
 def IsTypeValidForRepeater(self,typeId):
  """
  IsTypeValidForRepeater(self: ComponentRepeater,typeId: ElementId) -> bool
  
   Determines whether given family type can be used as the default type for the 
    repeater.
  
  
   typeId: The element id of the type.
   Returns: True if the family type can be used as the default type for the repeater.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 @staticmethod
 def RemoveRepeaters(document,elementIds):
  """ RemoveRepeaters(document: Document,elementIds: ISet[ElementId]) -> ISet[ElementId] """
  pass
 @staticmethod
 def RepeatElements(document,elementIds):
  """ RepeatElements(document: Document,elementIds: ICollection[ElementId]) -> IList[ComponentRepeater] """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def __contains__(self,*args):
  """ __contains__[ComponentRepeaterSlot](enumerable: IEnumerable[ComponentRepeaterSlot],value: ComponentRepeaterSlot) -> bool """
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
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 DefaultFamilyType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The default family type for the component repeater.

Get: DefaultFamilyType(self: ComponentRepeater) -> ElementId

Set: DefaultFamilyType(self: ComponentRepeater)=value
"""

 DimensionCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The dimension count of the component repeater.

Get: DimensionCount(self: ComponentRepeater) -> int

"""


