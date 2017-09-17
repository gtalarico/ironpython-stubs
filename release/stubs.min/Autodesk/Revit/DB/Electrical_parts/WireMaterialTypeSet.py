class WireMaterialTypeSet(APIObject,IDisposable,IEnumerable):
 """
 A set that contains wire material types.
 
 WireMaterialTypeSet()
 """
 def Clear(self):
  """
  Clear(self: WireMaterialTypeSet)
   Removes every wire material type from the set,rendering it empty.
  """
  pass
 def Contains(self,item):
  """
  Contains(self: WireMaterialTypeSet,item: WireMaterialType) -> bool
  
   Tests for the existence of a wire material type within the set.
  
   item: The wire material type to be searched for.
   Returns: The Contains method returns True if the wire material type is within the set,
    otherwise False.
  """
  pass
 def Dispose(self):
  """ Dispose(self: WireMaterialTypeSet,A_0: bool) """
  pass
 def Erase(self,item):
  """
  Erase(self: WireMaterialTypeSet,item: WireMaterialType) -> int
  
   Removes a specified wire material type from the set.
  
   item: The wire material type to be erased.
   Returns: The number of wire material types that were erased from the set.
  """
  pass
 def ForwardIterator(self):
  """
  ForwardIterator(self: WireMaterialTypeSet) -> WireMaterialTypeSetIterator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: WireMaterialTypeSet) -> IEnumerator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def Insert(self,item):
  """
  Insert(self: WireMaterialTypeSet,item: WireMaterialType) -> bool
  
   Insert the specified wire material type into the set.
  
   item: The wire material type to be inserted into the set.
   Returns: Returns whether the wire material type was inserted into the set.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: WireMaterialTypeSet) """
  pass
 def ReverseIterator(self):
  """
  ReverseIterator(self: WireMaterialTypeSet) -> WireMaterialTypeSetIterator
  
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

Get: IsEmpty(self: WireMaterialTypeSet) -> bool

"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the number of wire material types that are in the set.

Get: Size(self: WireMaterialTypeSet) -> int

"""


