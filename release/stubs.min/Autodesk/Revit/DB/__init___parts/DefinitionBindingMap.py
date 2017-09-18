class DefinitionBindingMap(APIObject,IDisposable,IEnumerable):
 """
 A map that contains mappings of parameter definitions to parameter bindings.

 

 DefinitionBindingMap()
 """
 def Clear(self):
  """
  Clear(self: DefinitionBindingMap)

   Removes every binding from the map,rendering it empty.
  """
  pass
 def Contains(self,key):
  """ Contains(self: DefinitionBindingMap,key: Definition) -> bool """
  pass
 def Dispose(self):
  """ Dispose(self: DefinitionBindingMap,A_0: bool) """
  pass
 def Erase(self,key):
  """ Erase(self: DefinitionBindingMap,key: Definition) -> int """
  pass
 def ForwardIterator(self):
  """
  ForwardIterator(self: DefinitionBindingMap) -> DefinitionBindingMapIterator

  

   Retrieve a forward moving iterator to the map.

   Returns: Returns a forward moving iterator to the map.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: DefinitionBindingMap) -> IEnumerator

  

   Retrieve a forward moving iterator to the map.

   Returns: Returns a forward moving iterator to the map.
  """
  pass
 def Insert(self,key,item):
  """ Insert(self: DefinitionBindingMap,key: Definition,item: Binding) -> bool """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
  pass
 def ReverseIterator(self):
  """
  ReverseIterator(self: DefinitionBindingMap) -> DefinitionBindingMapIterator

  

   Retrieve a backward moving iterator to the map.

   Returns: Returns a backward moving iterator to the map.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Test to see if the map is empty.



Get: IsEmpty(self: DefinitionBindingMap) -> bool



"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the number of bindings that are in the map.



Get: Size(self: DefinitionBindingMap) -> int



"""


