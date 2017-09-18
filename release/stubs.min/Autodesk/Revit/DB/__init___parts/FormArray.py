class FormArray(APIObject,IDisposable,IEnumerable):
 """
 An array that contains form objects.

 

 FormArray()
 """
 def Append(self,item):
  """ Append(self: FormArray,item: Form) """
  pass
 def Clear(self):
  """
  Clear(self: FormArray)

   Removes every form from the array,rendering it empty.
  """
  pass
 def Dispose(self):
  """ Dispose(self: FormArray,A_0: bool) """
  pass
 def ForwardIterator(self):
  """
  ForwardIterator(self: FormArray) -> FormArrayIterator

  

   Retrieve a forward moving iterator to the array.

   Returns: Returns a forward moving iterator to the array.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: FormArray) -> IEnumerator

  

   Retrieve a forward moving iterator to the array.

   Returns: Returns a forward moving iterator to the array.
  """
  pass
 def Insert(self,item,index):
  """ Insert(self: FormArray,item: Form,index: int) """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FormArray) """
  pass
 def ReverseIterator(self):
  """
  ReverseIterator(self: FormArray) -> FormArrayIterator

  

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



Get: IsEmpty(self: FormArray) -> bool



"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the number of forms that are in the array.



Get: Size(self: FormArray) -> int



"""


