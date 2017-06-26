class GroupSet(APIObject,IDisposable,IEnumerable):
 """
 An set that contains groups.
 
 GroupSet()
 """
 def Clear(self):
  """
  Clear(self: GroupSet)
   Removes every group from the set,rendering it empty.
  """
  pass
 def Contains(self,item):
  """
  Contains(self: GroupSet,item: Group) -> bool
  
   Tests for the existence of a group within the set.
  
   item: The group to be searched for.
   Returns: The Contains method returns True if the group is within the set,otherwise 
    False.
  """
  pass
 def Dispose(self):
  """ Dispose(self: GroupSet,A_0: bool) """
  pass
 def Erase(self,item):
  """
  Erase(self: GroupSet,item: Group) -> int
  
   Removes a specified group from the set.
  
   item: The group to be erased.
   Returns: The number of groups that were erased from the set.
  """
  pass
 def ForwardIterator(self):
  """
  ForwardIterator(self: GroupSet) -> GroupSetIterator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: GroupSet) -> IEnumerator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def Insert(self,item):
  """
  Insert(self: GroupSet,item: Group) -> bool
  
   Insert the specified group into the set.
  
   item: The group to be inserted into the set.
   Returns: Returns whether the group was inserted into the set.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: GroupSet) """
  pass
 def ReverseIterator(self):
  """
  ReverseIterator(self: GroupSet) -> GroupSetIterator
  
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

Get: IsEmpty(self: GroupSet) -> bool

"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the number of groups that are in the set.

Get: Size(self: GroupSet) -> int

"""


