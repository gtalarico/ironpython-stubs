class CitySet(APIObject,IDisposable,IEnumerable):
 """
 An set that contains cities.
 
 CitySet()
 """
 def Clear(self):
  """
  Clear(self: CitySet)
   Removes every city from the set,rendering it empty.
  """
  pass
 def Contains(self,item):
  """
  Contains(self: CitySet,item: City) -> bool
  
   Tests for the existence of a city within the set.
  
   item: The city to be searched for.
   Returns: The Contains method returns True if the city is within the set,otherwise False.
  """
  pass
 def Dispose(self):
  """ Dispose(self: CitySet,A_0: bool) """
  pass
 def Erase(self,item):
  """
  Erase(self: CitySet,item: City) -> int
  
   Removes a specified city from the set.
  
   item: The city to be erased.
   Returns: The number of cities that were erased from the set.
  """
  pass
 def ForwardIterator(self):
  """
  ForwardIterator(self: CitySet) -> CitySetIterator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: CitySet) -> IEnumerator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def Insert(self,item):
  """
  Insert(self: CitySet,item: City) -> bool
  
   Insert the specified city into the set.
  
   item: The city to be inserted into the set.
   Returns: Returns whether the city was inserted into the set.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: CitySet) """
  pass
 def ReverseIterator(self):
  """
  ReverseIterator(self: CitySet) -> CitySetIterator
  
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

Get: IsEmpty(self: CitySet) -> bool

"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the number of cities that are in the set.

Get: Size(self: CitySet) -> int

"""


