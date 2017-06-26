class DistributionSysTypeSet(APIObject,IDisposable,IEnumerable):
 """
 A set that contains DistributionSys types.
 
 DistributionSysTypeSet()
 """
 def Clear(self):
  """
  Clear(self: DistributionSysTypeSet)
   Removes every DistributionSys type from the set,rendering it empty.
  """
  pass
 def Contains(self,item):
  """
  Contains(self: DistributionSysTypeSet,item: DistributionSysType) -> bool
  
   Tests for the existence of a DistributionSys type within the set.
  
   item: The DistributionSys type to be searched for.
   Returns: The Contains method returns True if the DistributionSys type is within the set,
    otherwise False.
  """
  pass
 def Dispose(self):
  """ Dispose(self: DistributionSysTypeSet,A_0: bool) """
  pass
 def Erase(self,item):
  """
  Erase(self: DistributionSysTypeSet,item: DistributionSysType) -> int
  
   Removes a specified DistributionSys type from the set.
  
   item: The DistributionSys type to be erased.
   Returns: The number of DistributionSys types that were erased from the set.
  """
  pass
 def ForwardIterator(self):
  """
  ForwardIterator(self: DistributionSysTypeSet) -> DistributionSysTypeSetIterator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: DistributionSysTypeSet) -> IEnumerator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def Insert(self,item):
  """
  Insert(self: DistributionSysTypeSet,item: DistributionSysType) -> bool
  
   Insert the specified DistributionSys type into the set.
  
   item: The DistributionSys type to be inserted into the set.
   Returns: Returns whether the DistributionSys type was inserted into the set.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: DistributionSysTypeSet) """
  pass
 def ReverseIterator(self):
  """
  ReverseIterator(self: DistributionSysTypeSet) -> DistributionSysTypeSetIterator
  
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

Get: IsEmpty(self: DistributionSysTypeSet) -> bool

"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the number of DistributionSys types that are in the set.

Get: Size(self: DistributionSysTypeSet) -> int

"""


