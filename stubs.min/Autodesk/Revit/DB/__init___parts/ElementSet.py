class ElementSet(APIObject,IDisposable,IEnumerable):
 """
 A set that contains element objects.
 
 ElementSet()
 """
 def Clear(self):
  """
  Clear(self: ElementSet)
   Removes every item element the set,rendering it empty.
  """
  pass
 def Contains(self,item):
  """
  Contains(self: ElementSet,item: Element) -> bool
  
   Tests for the existence of an element within the set.
  
   item: The element to be searched for.
   Returns: The Contains method returns True if the element is within the set,otherwise 
    False.
  """
  pass
 def Dispose(self):
  """ Dispose(self: ElementSet,A_0: bool) """
  pass
 def Erase(self,item):
  """
  Erase(self: ElementSet,item: Element) -> int
  
   Removes a specified element from the set.
  
   item: The element to be erased.
   Returns: The number of elements that were erased from the set.
  """
  pass
 def ForwardIterator(self):
  """
  ForwardIterator(self: ElementSet) -> ElementSetIterator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: ElementSet) -> IEnumerator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def Insert(self,item):
  """
  Insert(self: ElementSet,item: Element) -> bool
  
   Insert the specified element into the set.
  
   item: The element to be inserted into the set.
   Returns: Returns whether the element was inserted into the set.
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
  ReverseIterator(self: ElementSet) -> ElementSetIterator
  
   Retrieve a backward moving iterator to the set.
   Returns: Returns a backward moving iterator to the set.
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
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Test to see if the set is empty.

Get: IsEmpty(self: ElementSet) -> bool

"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the number of elements that are in the set.

Get: Size(self: ElementSet) -> int

"""


