class WireSizeSet(APIObject,IDisposable,IEnumerable):
 """
 A set that contains wire sizes.
 
 WireSizeSet()
 """
 def Clear(self):
  """
  Clear(self: WireSizeSet)
   Removes every wire size from the set,rendering it empty.
  """
  pass
 def Contains(self,item):
  """
  Contains(self: WireSizeSet,item: WireSize) -> bool
  
   Tests for the existence of a wire size within the set.
  
   item: The wire size to be searched for.
   Returns: The Contains method returns True if the wire size is within the set,otherwise 
    False.
  """
  pass
 def Dispose(self):
  """ Dispose(self: WireSizeSet,A_0: bool) """
  pass
 def Erase(self,item):
  """
  Erase(self: WireSizeSet,item: WireSize) -> int
  
   Removes a specified wire size from the set.
  
   item: The wire size to be erased.
   Returns: The number of wire sizes that were erased from the set.
  """
  pass
 def ForwardIterator(self):
  """
  ForwardIterator(self: WireSizeSet) -> WireSizeSetIterator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: WireSizeSet) -> IEnumerator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def Insert(self,item):
  """
  Insert(self: WireSizeSet,item: WireSize) -> bool
  
   Insert the specified wire size into the set.
  
   item: The wire size to be inserted into the set.
   Returns: Returns whether the wire size was inserted into the set.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: WireSizeSet) """
  pass
 def ReverseIterator(self):
  """
  ReverseIterator(self: WireSizeSet) -> WireSizeSetIterator
  
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

Get: IsEmpty(self: WireSizeSet) -> bool

"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the number of wire sizes that are in the set.

Get: Size(self: WireSizeSet) -> int

"""


