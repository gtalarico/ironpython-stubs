class EdgeArrayIterator(APIObject,IDisposable,IEnumerator):
 """
 An iterator to an edge array.
 
 EdgeArrayIterator()
 """
 def Dispose(self):
  """ Dispose(self: EdgeArrayIterator,A_0: bool) """
  pass
 def MoveNext(self):
  """
  MoveNext(self: EdgeArrayIterator) -> bool
  
   Move the iterator one item forward.
   Returns: Returns True if the iterator was successfully moved forward one item and the 
    Current
     property will return a valid item. False will be returned 
    it the iterator has reached the end of
     the array.
  """
  pass
 def next(self,*args):
  """ next(self: object) -> object """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
  pass
 def Reset(self):
  """
  Reset(self: EdgeArrayIterator)
   Bring the iterator back to the start of the array.
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
  """ __iter__(self: IEnumerator) -> object """
  pass
 Current=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves the item that is the current focus of the iterator.

Get: Current(self: EdgeArrayIterator) -> object

"""


