class KeyBasedTreeEntries(object,IEnumerable[KeyBasedTreeEntry],IEnumerable,IDisposable):
 """ A collection of KeyBasedTreeEntry objects that make up the key-based tree. """
 def Dispose(self):
  """ Dispose(self: KeyBasedTreeEntries) """
  pass
 def FindEntry(self,key):
  """
  FindEntry(self: KeyBasedTreeEntries,key: str) -> KeyBasedTreeEntry

  

   Finds the KeyBasedTreeEntry associated with the given key value.

  

   key: The specified key value.

   Returns: The KeyBasedTreeEntry corresponds to the given key value.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: KeyBasedTreeEntries) -> IEnumerator[KeyBasedTreeEntry]

  

   Returns an enumerator that iterates through a collection.

   Returns: An IEnumerator object that can be used to iterate through the collection.
  """
  pass
 def GetKeyBasedTreeEntriesIterator(self):
  """
  GetKeyBasedTreeEntriesIterator(self: KeyBasedTreeEntries) -> KeyBasedTreeEntriesIterator

  

   Returns a KeyBasedTreeEntriesIterator that iterates through the collection.

   Returns: A KeyBasedTreeEntriesIterator object that can be used to iterate through 

    KeyBasedTreeEntry objects in the collection.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: KeyBasedTreeEntries,disposing: bool) """
  pass
 def __contains__(self,*args):
  """ __contains__[KeyBasedTreeEntry](enumerable: IEnumerable[KeyBasedTreeEntry],value: KeyBasedTreeEntry) -> bool """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: KeyBasedTreeEntries) -> bool



"""


