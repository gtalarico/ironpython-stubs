class FilteredElementIterator(object,IEnumerator[Element],IDisposable,IEnumerator):
 """ An iterator to a set of element ids filtered by the settings of a FilteredElementCollector. """
 def Dispose(self):
  """ Dispose(self: FilteredElementIterator) """
  pass
 def GetCurrent(self):
  """
  GetCurrent(self: FilteredElementIterator) -> Element
  
   The current element found by the iterator.
   Returns: The element.
  """
  pass
 def IsDone(self):
  """
  IsDone(self: FilteredElementIterator) -> bool
  
   Identifies if the iteration has completed.
   Returns: True if the iteration has no more matching elements.  False if there are more 
    element ids to be iterated.
  """
  pass
 def MoveNext(self):
  """
  MoveNext(self: FilteredElementIterator) -> bool
  
   Increments the iterator to the next element passing the filter.
   Returns: True if there is another available element passing the filter in this iterator.
    
     False if the iterator has completed all available elements.
  """
  pass
 def next(self,*args):
  """ next(self: object) -> object """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FilteredElementIterator,disposing: bool) """
  pass
 def Reset(self):
  """
  Reset(self: FilteredElementIterator)
   Resets the iterator to the beginning.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[Element](enumerator: IEnumerator[Element],value: Element) -> bool """
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

Get: Current(self: FilteredElementIterator) -> Element

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FilteredElementIterator) -> bool

"""


