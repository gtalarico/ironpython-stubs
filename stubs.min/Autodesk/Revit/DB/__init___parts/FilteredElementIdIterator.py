class FilteredElementIdIterator(object,IEnumerator[ElementId],IDisposable,IEnumerator):
 """ An iterator to a set of element ids filtered by the settings of a FilteredElementCollector. """
 def Dispose(self):
  """ Dispose(self: FilteredElementIdIterator) """
  pass
 def GetCurrent(self):
  """
  GetCurrent(self: FilteredElementIdIterator) -> ElementId
  
   The current element id found by the iterator.
   Returns: The element id.
  """
  pass
 def IsDone(self):
  """
  IsDone(self: FilteredElementIdIterator) -> bool
  
   Identifies if the iteration has completed.
   Returns: True if the iteration has no more matching elements.  False if there are more 
    element ids to be iterated.
  """
  pass
 def MoveNext(self):
  """
  MoveNext(self: FilteredElementIdIterator) -> bool
  
   Increments the iterator to the next element id passing the filter.
   Returns: True if there is another available element id passing the filter in this 
    iterator.
     False if the iterator has completed all available element ids.
  """
  pass
 def next(self,*args):
  """ next(self: object) -> object """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FilteredElementIdIterator,disposing: bool) """
  pass
 def Reset(self):
  """
  Reset(self: FilteredElementIdIterator)
   Resets the iterator to the beginning.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[ElementId](enumerator: IEnumerator[ElementId],value: ElementId) -> bool """
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

Get: Current(self: FilteredElementIdIterator) -> ElementId

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FilteredElementIdIterator) -> bool

"""


