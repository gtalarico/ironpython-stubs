class PanelTypeSet(APIObject,IDisposable,IEnumerable):
 """
 A set that contains panel types.
 
 PanelTypeSet()
 """
 def Clear(self):
  """
  Clear(self: PanelTypeSet)
   Removes every panel type from the set,rendering it empty.
  """
  pass
 def Contains(self,item):
  """
  Contains(self: PanelTypeSet,item: PanelType) -> bool
  
   Tests for the existence of a panel type within the set.
  
   item: The panel type to be searched for.
   Returns: The Contains method returns True if the panel type is within the set,otherwise 
    False.
  """
  pass
 def Dispose(self):
  """ Dispose(self: PanelTypeSet,A_0: bool) """
  pass
 def Erase(self,item):
  """
  Erase(self: PanelTypeSet,item: PanelType) -> int
  
   Removes a specified panel type from the set.
  
   item: The panel type to be erased.
   Returns: The number of panel types that were erased from the set.
  """
  pass
 def ForwardIterator(self):
  """
  ForwardIterator(self: PanelTypeSet) -> PanelTypeSetIterator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: PanelTypeSet) -> IEnumerator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def Insert(self,item):
  """
  Insert(self: PanelTypeSet,item: PanelType) -> bool
  
   Insert the specified panel type into the set.
  
   item: The panel type to be inserted into the set.
   Returns: Returns whether the panel type was inserted into the set.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: PanelTypeSet) """
  pass
 def ReverseIterator(self):
  """
  ReverseIterator(self: PanelTypeSet) -> PanelTypeSetIterator
  
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

Get: IsEmpty(self: PanelTypeSet) -> bool

"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the number of panel types that are in the set.

Get: Size(self: PanelTypeSet) -> int

"""


