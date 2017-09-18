class FilteredElementCollector(object,IEnumerable[Element],IEnumerable,IDisposable):
 """
 This class is used to search,filter and iterate through a set of elements.
 
 FilteredElementCollector(document: Document,viewId: ElementId)
 FilteredElementCollector(document: Document,elementIds: ICollection[ElementId])
 FilteredElementCollector(document: Document)
 """
 def ContainedInDesignOption(self,designOptionId):
  """
  ContainedInDesignOption(self: FilteredElementCollector,designOptionId: ElementId) -> FilteredElementCollector
  
   Applies an ElementDesignOptionFilter to the collector.
  
   designOptionId: The design option id.
   Returns: A handle to this collector.  This is the same collector that has just been 
    modified,returned
     so you can chain multiple calls together in one line.
  """
  pass
 def Dispose(self):
  """ Dispose(self: FilteredElementCollector) """
  pass
 def Excluding(self,idsToExclude):
  """ Excluding(self: FilteredElementCollector,idsToExclude: ICollection[ElementId]) -> FilteredElementCollector """
  pass
 def FirstElement(self):
  """
  FirstElement(self: FilteredElementCollector) -> Element
  
   Returns the first element to pass the filter(s).
   Returns: The first element.
  """
  pass
 def FirstElementId(self):
  """
  FirstElementId(self: FilteredElementCollector) -> ElementId
  
   Returns the id of the first element to pass the filter(s).
   Returns: The first element id.
  """
  pass
 def GetElementCount(self):
  """
  GetElementCount(self: FilteredElementCollector) -> int
  
   Gets the number of elements in your current filter.
   Returns: The number of elements
  """
  pass
 def GetElementIdIterator(self):
  """
  GetElementIdIterator(self: FilteredElementCollector) -> FilteredElementIdIterator
  
   Returns an element id iterator to the elements passing the filters.
  """
  pass
 def GetElementIterator(self):
  """
  GetElementIterator(self: FilteredElementCollector) -> FilteredElementIterator
  
   Returns an element iterator to the elements passing the filters.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: FilteredElementCollector) -> IEnumerator[Element]
  
   Returns an enumerator that iterates through a collection.
   Returns: An IEnumerator object that can be used to iterate through the collection.
  """
  pass
 def IntersectWith(self,other):
  """
  IntersectWith(self: FilteredElementCollector,other: FilteredElementCollector) -> FilteredElementCollector
  
   Intersects the set of elements passing the filter in this collector
     with 
    the set of elements passing the filter in another collector.
  
  
   other: The other collector
   Returns: A handle to this collector.  This is the same collector that has just been 
    modified,returned
     so you can chain multiple calls together in one line.
  """
  pass
 @staticmethod
 def IsViewValidForElementIteration(document,viewId):
  """
  IsViewValidForElementIteration(document: Document,viewId: ElementId) -> bool
  
   Identifies if the particular element is valid for iteration of drawn elements.
  
   document: The document.
   viewId: The view id.
   Returns: True if the element is valid for iteration.
  """
  pass
 def OfCategory(self,category):
  """
  OfCategory(self: FilteredElementCollector,category: BuiltInCategory) -> FilteredElementCollector
  
   Applies an ElementCategoryFilter to the collector.
  
   category: The category.
   Returns: This collector.
  """
  pass
 def OfCategoryId(self,categoryId):
  """
  OfCategoryId(self: FilteredElementCollector,categoryId: ElementId) -> FilteredElementCollector
  
   Applies an ElementCategoryFilter to the collector.
  
   categoryId: The category id.
   Returns: A handle to this collector.  This is the same collector that has just been 
    modified,returned
     so you can chain multiple calls together in one line.
  """
  pass
 def OfClass(self,type):
  """
  OfClass(self: FilteredElementCollector,type: Type) -> FilteredElementCollector
  
   Applies an ElementClassFilter to the collector.
  
   type: The element type.
   Returns: A handle to this collector.  This is the same collector that has just been 
    modified,returned
     so you can chain multiple calls together in one line.
  """
  pass
 def OwnedByView(self,viewId):
  """
  OwnedByView(self: FilteredElementCollector,viewId: ElementId) -> FilteredElementCollector
  
   Applies an ElementOwnerViewFilter to the collector.
  
   viewId: The view id of the owner view.
   Returns: A handle to this collector.  This is the same collector that has just been 
    modified,returned
     so you can chain multiple calls together in one line.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FilteredElementCollector,disposing: bool) """
  pass
 def ToElementIds(self):
  """
  ToElementIds(self: FilteredElementCollector) -> ICollection[ElementId]
  
   Returns the complete set of element ids that pass the filter(s).
   Returns: The complete set of element ids.
  """
  pass
 def ToElements(self):
  """
  ToElements(self: FilteredElementCollector) -> IList[Element]
  
   Returns the complete set of elements that pass the filter(s).
   Returns: The complete set of element ids.
  """
  pass
 def UnionWith(self,other):
  """
  UnionWith(self: FilteredElementCollector,other: FilteredElementCollector) -> FilteredElementCollector
  
   Unites the set of elements passing the filter in this collector
     with the 
    set of elements passing the filter in another collector.
  
  
   other: The other collector
   Returns: A handle to this collector.  This is the same collector that has just been 
    modified,returned
     so you can chain multiple calls together in one line.
  """
  pass
 def WhereElementIsCurveDriven(self):
  """
  WhereElementIsCurveDriven(self: FilteredElementCollector) -> FilteredElementCollector
  
   Applies an ElementIsCurveDrivenFilter to the collector.
   Returns: A handle to this collector.  This is the same collector that has just been 
    modified,returned
     so you can chain multiple calls together in one line.
  """
  pass
 def WhereElementIsElementType(self):
  """
  WhereElementIsElementType(self: FilteredElementCollector) -> FilteredElementCollector
  
   Applies an ElementIsElementTypeFilter to the collector.
   Returns: A handle to this collector.  This is the same collector that has just been 
    modified,returned
     so you can chain multiple calls together in one line.
  """
  pass
 def WhereElementIsNotElementType(self):
  """
  WhereElementIsNotElementType(self: FilteredElementCollector) -> FilteredElementCollector
  
   Applies an inverted ElementIsElementTypeFilter to the collector.
   Returns: A handle to this collector.  This is the same collector that has just been 
    modified,returned
     so you can chain multiple calls together in one line.
  """
  pass
 def WhereElementIsViewIndependent(self):
  """
  WhereElementIsViewIndependent(self: FilteredElementCollector) -> FilteredElementCollector
  
   Applies an ElementOwnerViewFilter to the collector.
   Returns: A handle to this collector.  This is the same collector that has just been 
    modified,returned
     so you can chain multiple calls together in one line.
  """
  pass
 def WherePasses(self,filter):
  """
  WherePasses(self: FilteredElementCollector,filter: ElementFilter) -> FilteredElementCollector
  
   Applies an element filter to the collector.
  
   filter: The element filter.
   Returns: A handle to this collector.  This is the same collector that has just been 
    modified,returned
     so you can chain multiple calls together in one line.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[Element](enumerable: IEnumerable[Element],value: Element) -> bool """
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
 @staticmethod
 def __new__(self,document,*__args):
  """
  __new__(cls: type,document: Document,viewId: ElementId)
  __new__(cls: type,document: Document,elementIds: ICollection[ElementId])
  __new__(cls: type,document: Document)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FilteredElementCollector) -> bool

"""


