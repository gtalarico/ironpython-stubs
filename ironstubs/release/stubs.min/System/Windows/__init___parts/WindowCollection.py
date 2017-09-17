class WindowCollection(object,ICollection,IEnumerable):
 """
 Represents a collection of System.Windows.Window objects. This class cannot be inherited.
 
 WindowCollection()
 """
 def CopyTo(self,array,index):
  """
  CopyTo(self: WindowCollection,array: Array[Window],index: int)
   Copies each System.Windows.Window object in the collection to an array,
    starting from the specified index.
  
  
   array: An array of type System.Windows.Window that the System.Windows.Window objects 
    in the collection are copied to.
  
   index: The position in the collection to start copying from.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: WindowCollection) -> IEnumerator
  
   Returns an System.Collections.IEnumerator that you can use to enumerate the 
    System.Windows.Window objects in the collection.
  
   Returns: An System.Collections.IEnumerator that you can use to enumerate the 
    System.Windows.Window objects in the collection.
  """
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
 def __len__(self,*args):
  """ x.__len__() <==> len(x) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of System.Windows.Window objects contained in the System.Windows.WindowCollection.

Get: Count(self: WindowCollection) -> int

"""

 IsSynchronized=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.WindowCollection object is thread safe.

Get: IsSynchronized(self: WindowCollection) -> bool

"""

 SyncRoot=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an object that can be used to synchronize access to the collection.

Get: SyncRoot(self: WindowCollection) -> object

"""


