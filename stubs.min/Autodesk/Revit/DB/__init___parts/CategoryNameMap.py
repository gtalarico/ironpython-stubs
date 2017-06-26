class CategoryNameMap(APIObject,IDisposable,IEnumerable):
 """
 A map that contains a mapping of category name to its category object.
 
 CategoryNameMap()
 """
 def Clear(self):
  """
  Clear(self: CategoryNameMap)
   Removes every category from the map,rendering it empty.
  """
  pass
 def Contains(self,key):
  """
  Contains(self: CategoryNameMap,key: str) -> bool
  
   Tests for the existence of a category with that name within the map.
  
   key: The category name to be searched for.
   Returns: The Contains method returns True if the name is within the map,otherwise False.
  """
  pass
 def Dispose(self):
  """ Dispose(self: CategoryNameMap,A_0: bool) """
  pass
 def Erase(self,key):
  """
  Erase(self: CategoryNameMap,key: str) -> int
  
   Removes a category with the specified name from the map.
  
   key: The name of the category to be erased.
   Returns: The number of categories that were erased from the map.
  """
  pass
 def ForwardIterator(self):
  """
  ForwardIterator(self: CategoryNameMap) -> CategoryNameMapIterator
  
   Retrieve a forward moving iterator to the map.
   Returns: Returns a forward moving iterator to the map.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: CategoryNameMap) -> IEnumerator
  
   Retrieve a forward moving iterator to the map.
   Returns: Returns a forward moving iterator to the map.
  """
  pass
 def Insert(self,key,item):
  """
  Insert(self: CategoryNameMap,key: str,item: Category) -> bool
  
   Insert the specified category with the specified name into the map.
  
   key: The name to be used for inserting the category into the map.
   item: The category to be inserted into the map.
   Returns: Returns whether the category was inserted into the map.
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
  ReverseIterator(self: CategoryNameMap) -> CategoryNameMapIterator
  
   Retrieve a backward moving iterator to the map.
   Returns: Returns a backward moving iterator to the map.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
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
 """Test to see if the map is empty.

Get: IsEmpty(self: CategoryNameMap) -> bool

"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the number of categories that are in the map.

Get: Size(self: CategoryNameMap) -> int

"""


