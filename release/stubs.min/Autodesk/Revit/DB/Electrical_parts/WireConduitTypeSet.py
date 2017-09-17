class WireConduitTypeSet(APIObject,IDisposable,IEnumerable):
 """
 A set that contains conduit types.
 
 WireConduitTypeSet()
 """
 def Clear(self):
  """
  Clear(self: WireConduitTypeSet)
   Removes every conduit type from the set,rendering it empty.
  """
  pass
 def Contains(self,item):
  """
  Contains(self: WireConduitTypeSet,item: WireConduitType) -> bool
  
   Tests for the existence of a conduit type within the set.
  
   item: The conduit type to be searched for.
   Returns: The Contains method returns True if the conduit type is within the set,
    otherwise False.
  """
  pass
 def Dispose(self):
  """ Dispose(self: WireConduitTypeSet,A_0: bool) """
  pass
 def Erase(self,item):
  """
  Erase(self: WireConduitTypeSet,item: WireConduitType) -> int
  
   Removes a specified conduit type from the set.
  
   item: The conduit type to be erased.
   Returns: The number of conduit types that were erased from the set.
  """
  pass
 def ForwardIterator(self):
  """
  ForwardIterator(self: WireConduitTypeSet) -> WireConduitTypeSetIterator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: WireConduitTypeSet) -> IEnumerator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def Insert(self,item):
  """
  Insert(self: WireConduitTypeSet,item: WireConduitType) -> bool
  
   Insert the specified conduit type into the set.
  
   item: The conduit type to be inserted into the set.
   Returns: Returns whether the conduit type was inserted into the set.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: WireConduitTypeSet) """
  pass
 def ReverseIterator(self):
  """
  ReverseIterator(self: WireConduitTypeSet) -> WireConduitTypeSetIterator
  
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

Get: IsEmpty(self: WireConduitTypeSet) -> bool

"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the number of conduit types that are in the set.

Get: Size(self: WireConduitTypeSet) -> int

"""


