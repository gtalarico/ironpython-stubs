class ConnectorSet(APIObject,IDisposable,IEnumerable):
 """
 A set that can contain any type of object.
 
 ConnectorSet()
 """
 def Clear(self):
  """
  Clear(self: ConnectorSet)
   Removes every item from the set,rendering it empty.
  """
  pass
 def Contains(self,item):
  """ Contains(self: ConnectorSet,item: Connector) -> bool """
  pass
 def Dispose(self):
  """ Dispose(self: ConnectorSet,A_0: bool) """
  pass
 def Erase(self,item):
  """ Erase(self: ConnectorSet,item: Connector) -> int """
  pass
 def ForwardIterator(self):
  """
  ForwardIterator(self: ConnectorSet) -> ConnectorSetIterator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: ConnectorSet) -> IEnumerator
  
   Retrieve a forward moving iterator to the set.
   Returns: Returns a forward moving iterator to the set.
  """
  pass
 def Insert(self,item):
  """ Insert(self: ConnectorSet,item: Connector) -> bool """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ConnectorSet) """
  pass
 def ReverseIterator(self):
  """
  ReverseIterator(self: ConnectorSet) -> ConnectorSetIterator
  
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

Get: IsEmpty(self: ConnectorSet) -> bool

"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the number of objects that are in the set.

Get: Size(self: ConnectorSet) -> int

"""


