class RebarContainerIterator(object,IEnumerator[RebarContainerItem],IDisposable,IEnumerator):
 """ An iterator to a Rebar Container. """
 def Dispose(self):
  """ Dispose(self: RebarContainerIterator) """
  pass
 def MoveNext(self):
  """
  MoveNext(self: RebarContainerIterator) -> bool
  
   Increments the iterator to the next item.
   Returns: True if there is a next available item in this iterator.
     False if the 
    iterator has completed all available items.
  """
  pass
 def next(self,*args):
  """ next(self: object) -> object """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RebarContainerIterator,disposing: bool) """
  pass
 def Reset(self):
  """
  Reset(self: RebarContainerIterator)
   Resets the iterator to the initial state.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[RebarContainerItem](enumerator: IEnumerator[RebarContainerItem],value: RebarContainerItem) -> bool """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Current=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the item at the current position of the iterator.

Get: Current(self: RebarContainerIterator) -> RebarContainerItem

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarContainerIterator) -> bool

"""


