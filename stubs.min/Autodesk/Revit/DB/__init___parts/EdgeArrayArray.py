class EdgeArrayArray(APIObject,IDisposable,IEnumerable):
 """
 An array of edge arrays.
 
 EdgeArrayArray()
 """
 def Append(self,item):
  """
  Append(self: EdgeArrayArray,item: EdgeArray)
   Add the edge array to the end of the array.
  
   item: The edge array to be added.
  """
  pass
 def Clear(self):
  """
  Clear(self: EdgeArrayArray)
   Removes every edge array from the array,rendering it empty.
  """
  pass
 def Dispose(self):
  """ Dispose(self: EdgeArrayArray,A_0: bool) """
  pass
 def ForwardIterator(self):
  """
  ForwardIterator(self: EdgeArrayArray) -> EdgeArrayArrayIterator
  
   Retrieve a forward moving iterator to the array.
   Returns: Returns a forward moving iterator to the array.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: EdgeArrayArray) -> IEnumerator
  
   Retrieve a forward moving iterator to the array.
   Returns: Returns a forward moving iterator to the array.
  """
  pass
 def Insert(self,item,index):
  """
  Insert(self: EdgeArrayArray,item: EdgeArray,index: int)
   Insert the specified edge array into the array.
  
   item: The edge array to be inserted into the array.
   index: The edge array will be inserted before this index.
   Returns: Returns whether the edge array was inserted into the array.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
  pass
 def ReverseIterator(self):
  """
  ReverseIterator(self: EdgeArrayArray) -> EdgeArrayArrayIterator
  
   Retrieve a backward moving iterator to the array.
   Returns: Returns a backward moving iterator to the array.
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
 """Test to see if the array is empty.

Get: IsEmpty(self: EdgeArrayArray) -> bool

"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the number of edge arrays that are in the array.

Get: Size(self: EdgeArrayArray) -> int

"""


