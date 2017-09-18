class GeomCombinationSet(APIObject,IDisposable,IEnumerable):
 """
 A set that contains GeomCombination objects.

 

 GeomCombinationSet()
 """
 def Clear(self):
  """
  Clear(self: GeomCombinationSet)

   Removes every item GeomCombination the set,rendering it empty.
  """
  pass
 def Contains(self,item):
  """
  Contains(self: GeomCombinationSet,item: GeomCombination) -> bool

  

   Tests for the existence of an GeomCombination within the set.

  

   item: The element to be searched for.

   Returns: The Contains method returns True if the GeomCombination is within the set,

    otherwise False.
  """
  pass
 def Dispose(self):
  """ Dispose(self: GeomCombinationSet,A_0: bool) """
  pass
 def Erase(self,item):
  """
  Erase(self: GeomCombinationSet,item: GeomCombination) -> int

  

   Removes a specified GeomCombination from the set.

  

   item: The GeomCombination to be erased.

   Returns: The number of GeomCombinations that were erased from the set.
  """
  pass
 def ForwardIterator(self):
  """
  ForwardIterator(self: GeomCombinationSet) -> GeomCombinationSetIterator

  

   Retrieve a forward moving iterator to the set.

   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: GeomCombinationSet) -> IEnumerator

  

   Retrieve a forward moving iterator to the set.

   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def Insert(self,item):
  """
  Insert(self: GeomCombinationSet,item: GeomCombination) -> bool

  

   Insert the specified element into the set.

  

   item: The GeomCombination to be inserted into the set.

   Returns: Returns whether the GeomCombination was inserted into the set.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: GeomCombinationSet) """
  pass
 def ReverseIterator(self):
  """
  ReverseIterator(self: GeomCombinationSet) -> GeomCombinationSetIterator

  

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



Get: IsEmpty(self: GeomCombinationSet) -> bool



"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the number of GeomCombinations that are in the set.



Get: Size(self: GeomCombinationSet) -> int



"""


