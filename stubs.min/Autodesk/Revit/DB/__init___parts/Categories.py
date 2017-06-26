class Categories(CategoryNameMap,IDisposable,IEnumerable):
 """ The Categories object is a map that contains all the top-level Category objects within the Document. """
 def Contains(self,name):
  """
  Contains(self: Categories,name: str) -> bool
  
   Identifies if a category which has the specified name is in the list of 
    top-level categories.
  
  
   name: The name of the category to be retrieved.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Categories,A_0: bool) """
  pass
 def ForwardIterator(self):
  """
  ForwardIterator(self: Categories) -> CategoryNameMapIterator
  
   Retrieves a forward moving iterator to the map.
   Returns: A forward moving iterator to the map.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: Categories) -> IEnumerator
  
   Retrieves a forward moving iterator to the map.
   Returns: A forward moving iterator to the map.
  """
  pass
 def Insert(self,key,item):
  """
  Insert(self: Categories,key: str,item: Category) -> bool
  
   Inserts the specified category with the specified name into the map.
  
   key: The name to be used for inserting the category into the map.
   item: The category to be inserted into the map.
   Returns: Whether or not the category was inserted into the map.
  """
  pass
 def NewSubcategory(self,parentCategory,name):
  """
  NewSubcategory(self: Categories,parentCategory: Category,name: str) -> Category
  
   Add a new subcategory into the Autodesk Revit document.
  
   parentCategory: The parent category.
   name: The new category name.
   Returns: If successful,the newly created subcategory.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
  pass
 def ReverseIterator(self):
  """
  ReverseIterator(self: Categories) -> CategoryNameMapIterator
  
   Retrieves a backward moving iterator to the map.
   Returns: A backward moving iterator to the map.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether or not the list of top-level categories is empty.

Get: IsEmpty(self: Categories) -> bool

"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The total number of top-level categories in the document.

Get: Size(self: Categories) -> int

"""


