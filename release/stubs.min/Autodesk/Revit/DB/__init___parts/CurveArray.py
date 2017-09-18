class CurveArray(APIObject,IDisposable,IEnumerable):
 """
 An array that can contain curves.

 

 CurveArray()
 """
 def Append(self,item):
  """
  Append(self: CurveArray,item: Curve)

   Add the curve to the end of the array.

  

   item: The curve to be added.
  """
  pass
 def Clear(self):
  """
  Clear(self: CurveArray)

   Removes every curve from the array,rendering it empty.
  """
  pass
 def Dispose(self):
  """ Dispose(self: CurveArray,A_0: bool) """
  pass
 def ForwardIterator(self):
  """
  ForwardIterator(self: CurveArray) -> CurveArrayIterator

  

   Retrieve a forward moving iterator to the array.

   Returns: Returns a forward moving iterator to the array.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: CurveArray) -> IEnumerator

  

   Retrieve a forward moving iterator to the array.

   Returns: Returns a forward moving iterator to the array.
  """
  pass
 def Insert(self,item,index):
  """
  Insert(self: CurveArray,item: Curve,index: int)

   Insert the specified curve into the array.

  

   item: The curve to be inserted into the array.

   index: The curve will be inserted before this index.

   Returns: Returns whether the curve was inserted into the array.
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
  ReverseIterator(self: CurveArray) -> CurveArrayIterator

  

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



Get: IsEmpty(self: CurveArray) -> bool



"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the number of curves that are in the array.



Get: Size(self: CurveArray) -> int



"""


