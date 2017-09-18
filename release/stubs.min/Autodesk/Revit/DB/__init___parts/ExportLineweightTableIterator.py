class ExportLineweightTableIterator(object,IEnumerator[KeyValuePair[ExportLineweightKey,ExportLineweightInfo]],IDisposable,IEnumerator):
 """ An iterator to a set of line weight table. """
 def Dispose(self):
  """ Dispose(self: ExportLineweightTableIterator) """
  pass
 def IsDone(self):
  """
  IsDone(self: ExportLineweightTableIterator) -> bool

  

   Identifies if the iteration has completed.

   Returns: True if the iteration has no more items. False if there are more items to be 

    iterated.
  """
  pass
 def MoveNext(self):
  """
  MoveNext(self: ExportLineweightTableIterator) -> bool

  

   Increments the iterator to the next item.

   Returns: True if the iteration has no more items. False if there are more items to be 

    iterated.
  """
  pass
 def next(self,*args):
  """ next(self: object) -> object """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ExportLineweightTableIterator,disposing: bool) """
  pass
 def Reset(self):
  """
  Reset(self: ExportLineweightTableIterator)

   Resets the iterator to the initial state.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[KeyValuePair[ExportLineweightKey,ExportLineweightInfo]](enumerator: IEnumerator[KeyValuePair[ExportLineweightKey,ExportLineweightInfo]],value: KeyValuePair[ExportLineweightKey,ExportLineweightInfo]) -> bool """
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



Get: Current(self: ExportLineweightTableIterator) -> KeyValuePair[ExportLineweightKey,ExportLineweightInfo]



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: ExportLineweightTableIterator) -> bool



"""


