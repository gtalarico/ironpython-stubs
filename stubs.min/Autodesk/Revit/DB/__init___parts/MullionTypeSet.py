class MullionTypeSet(APIObject,IDisposable,IEnumerable):
 """
 A set that contains mullion types.
 
 MullionTypeSet()
 """
 def Clear(self):
  """
  Clear(self: MullionTypeSet)
   Removes every mullion type from the set,rendering it empty.
  """
  pass
 def Contains(self,item):
  """
  Contains(self: MullionTypeSet,item: MullionType) -> bool
  
   Tests for the existence of a mullion type within the set.
  
   item: The mullion type to be searched for.
   Returns: The Contains method returns True if the mullion type is within the set,
    otherwise False.
  """
  pass
 def Dispose(self):
  """ Dispose(self: MullionTypeSet,A_0: bool) """
  pass
 def Erase(self,item):
  """
  Erase(self: MullionTypeSet,item: MullionType) -> int
  
   Removes a specified mullion type from the set.
  
   item: The mullion type to be erased.
   Returns: The number of mullion types that were erased from the set.
  """
  pass
 def ForwardIterator(self):
  """
  ForwardIterator(self: MullionTypeSet) -> MullionTypeSetIterator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: MullionTypeSet) -> IEnumerator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def Insert(self,item):
  """
  Insert(self: MullionTypeSet,item: MullionType) -> bool
  
   Insert the specified mullion type into the set.
  
   item: The mullion type to be inserted into the set.
   Returns: Returns whether the mullion type was inserted into the set.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: MullionTypeSet) """
  pass
 def ReverseIterator(self):
  """
  ReverseIterator(self: MullionTypeSet) -> MullionTypeSetIterator
  
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

Get: IsEmpty(self: MullionTypeSet) -> bool

"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the number of mullion types that are in the set.

Get: Size(self: MullionTypeSet) -> int

"""


