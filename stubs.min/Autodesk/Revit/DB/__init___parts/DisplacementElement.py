class DisplacementElement(Element,IDisposable):
 """
 A view-specific element that causes other elements to appear to be displaced from their
    actual locations.
 """
 @staticmethod
 def CanCategoryBeDisplaced(categoryId):
  """
  CanCategoryBeDisplaced(categoryId: ElementId) -> bool
  
   Indicates whether elements of the specified category are eligible as displaced 
    elements.
  
  
   categoryId: Category id of element to be replaced.
   Returns: Returns true if elements of this category can be displaced,and false otherwise.
  """
  pass
 def CanElementsBeAddedToDisplacementSet(self,toDisplace):
  """ CanElementsBeAddedToDisplacementSet(self: DisplacementElement,toDisplace: ICollection[ElementId]) -> bool """
  pass
 @staticmethod
 def CanElementsBeDisplaced(view,elementIds,commonDisplacedElementId=None):
  """
  CanElementsBeDisplaced(view: View,elementIds: ICollection[ElementId]) -> (bool,ElementId)
  CanElementsBeDisplaced(view: View,elementIds: ICollection[ElementId]) -> bool
  """
  pass
 @staticmethod
 def Create(document,elementsToDisplace,displacement,ownerDBView,parentDisplacementElement):
  """ Create(document: Document,elementsToDisplace: ICollection[ElementId],displacement: XYZ,ownerDBView: View,parentDisplacementElement: DisplacementElement) -> DisplacementElement """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def GetAbsoluteDisplacement(self):
  """
  GetAbsoluteDisplacement(self: DisplacementElement) -> XYZ
  
   The absolute displacement applied to the displaced elements.
   Returns: The absolute displacement.
  """
  pass
 @staticmethod
 def GetAdditionalElementsToDisplace(document,view,idToDisplace):
  """
  GetAdditionalElementsToDisplace(document: Document,view: View,idToDisplace: ElementId) -> ICollection[ElementId]
  
   Identify a set of elements that potentially should be displaced along with a 
    given element.
  
  
   document: the document
   view: the view
   idToDisplace: element id of element to displace
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetChildren(self):
  """
  GetChildren(self: DisplacementElement) -> IList[DisplacementElement]
  
   Returns a set of DisplacementElements which have this
     DisplacementElement 
    as a parent.
  
   Returns: The returned array is sorted by element id.
  """
  pass
 def GetDisplacedElementIds(self,view=None):
  """
  GetDisplacedElementIds(view: View) -> ICollection[ElementId]
  
   Returns the element ids of all displaced elements in the specified view.
  
   view: The view.
   Returns: The element ids.
  GetDisplacedElementIds(self: DisplacementElement) -> ICollection[ElementId]
  
   The ids of the elements affected by this DisplacementElement.
   Returns: The element ids.
  """
  pass
 def GetDisplacedElementIdsFromAllChildren(self):
  """
  GetDisplacedElementIdsFromAllChildren(self: DisplacementElement) -> ICollection[ElementId]
  
   The element ids of elements displaced by this DisplacementElement and any
     
    DisplacementElement which declare this one as parent.
  
   Returns: The element ids.
  """
  pass
 @staticmethod
 def GetDisplacementElementId(view,id):
  """
  GetDisplacementElementId(view: View,id: ElementId) -> ElementId
  
   The element id of the DisplacementElement that includes the specified element.
  
   view: The view.
   id: The element id.
   Returns: The element id of DisplacementElement that includes the specified element id.
  """
  pass
 @staticmethod
 def GetDisplacementElementIds(view):
  """
  GetDisplacementElementIds(view: View) -> ICollection[ElementId]
  
   The element ids of all DisplacementElements owned by the specified view.
  
   view: The view.
   Returns: The element ids.
  """
  pass
 def GetRelativeDisplacement(self):
  """
  GetRelativeDisplacement(self: DisplacementElement) -> XYZ
  
   The relative displacement applied to the displaced elements by this 
    DisplacementElement.
  
   Returns: The relative displacement.
  """
  pass
 @staticmethod
 def IsAllowedAsDisplacedElement(element):
  """
  IsAllowedAsDisplacedElement(element: Element) -> bool
  
   Indicates if the specified element is allowed to be displaced.
  
   element: Any element.
   Returns: Returns true if the element is eligible to be assigned to a DisplacementElement.
  """
  pass
 @staticmethod
 def IsElementDisplacedInView(view,id):
  """
  IsElementDisplacedInView(view: View,id: ElementId) -> bool
  
   Indicates if the specified element displaced in the specified View.
  
   view: The view.
   id: The element id.
  """
  pass
 @staticmethod
 def IsNotEmpty(elementIds):
  """ IsNotEmpty(elementIds: ICollection[ElementId]) -> bool """
  pass
 @staticmethod
 def IsValidAsParentInView(view,parent):
  """
  IsValidAsParentInView(view: View,parent: DisplacementElement) -> bool
  
   Indicates whether the specified DisplacementElement can be used as a parent 
    when
     creating a DisplacementElement in the specified view.
  
  
   view: A view.
   parent: A DisplacementElement.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RemoveDisplacedElement(self,ElemToRemove):
  """
  RemoveDisplacedElement(self: DisplacementElement,ElemToRemove: Element)
   Remove a displaced element from this DisplacementElement.
  
   ElemToRemove: The element to remove.
  """
  pass
 def ResetDisplacedElements(self):
  """
  ResetDisplacedElements(self: DisplacementElement)
   Sets the translation of the DisplacementElement to (0,0,0).
     The 
    DisplacementElement continues to exist,but its elements are displayed in their 
    actual location.
  """
  pass
 def SetDisplacedElementIds(self,displacedElemIds):
  """ SetDisplacedElementIds(self: DisplacementElement,displacedElemIds: ICollection[ElementId]) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetRelativeDisplacement(self,displacement):
  """
  SetRelativeDisplacement(self: DisplacementElement,displacement: XYZ)
   Sets the relative displacement applied to the displaced elements by this 
    DisplacementElement.
  
  
   displacement: The relative displacement.
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
 ParentId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The element id of the parent DisplacementElement. This DisplacementElement's relative transform
   will be concatenated with the absolute transform of its parent.

Get: ParentId(self: DisplacementElement) -> ElementId

"""


