class VisualCollection(object,ICollection,IEnumerable):
 """
 Represents an ordered collection of System.Windows.Media.Visual objects.
 
 VisualCollection(parent: Visual)
 """
 def Add(self,visual):
  """
  Add(self: VisualCollection,visual: Visual) -> int
  
   Appends a System.Windows.Media.Visual to the end of the 
    System.Windows.Media.VisualCollection.
  
  
   visual: The System.Windows.Media.Visual to append to the 
    System.Windows.Media.VisualCollection.
  
   Returns: The index in the collection at which visual was added.
  """
  pass
 def Clear(self):
  """
  Clear(self: VisualCollection)
   Removes all elements from the System.Windows.Media.VisualCollection.
  """
  pass
 def Contains(self,visual):
  """
  Contains(self: VisualCollection,visual: Visual) -> bool
  
   Returns a System.Boolean value that indicates whether the specified 
    System.Windows.Media.Visual is contained in the collection.
  
  
   visual: The System.Windows.Media.Visual to search for in the collection.
   Returns: true if visual is contained in the collection; otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: VisualCollection,array: Array[Visual],index: int)
   Copies the current collection into the passed System.Windows.Media.Visual array.
  
   array: An array of System.Windows.Media.Visual objects (which must have zero-based 
    indexing).
  
   index: The index to start copying from within array.
  CopyTo(self: VisualCollection,array: Array,index: int)
   Copies the items in the collection to an array,starting at a specific array 
    index.
  
  
   array: The one-dimensional System.Array that is the destination of the elements that 
    are copied from the System.Windows.Media.VisualCollection.
  
   index: The zero-based index in array at which copying begins.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: VisualCollection) -> Enumerator
  
   Retrieves an enumerator that can iterate through the 
    System.Windows.Media.VisualCollection.
  
   Returns: An enumerator that can be used to iterate through the collection.
  """
  pass
 def IndexOf(self,visual):
  """
  IndexOf(self: VisualCollection,visual: Visual) -> int
  
   Returns the zero-based index of the System.Windows.Media.Visual.
  
   visual: The System.Windows.Media.Visual to locate in the 
    System.Windows.Media.VisualCollection.
  
   Returns: The index of the System.Windows.Media.Visual.
  """
  pass
 def Insert(self,index,visual):
  """
  Insert(self: VisualCollection,index: int,visual: Visual)
   Inserts an element into the System.Windows.Media.VisualCollection at the 
    specified index.
  
  
   index: The zero-based index at which the value should be inserted.
   visual: The System.Windows.Media.Visual to insert into the 
    System.Windows.Media.VisualCollection.
  """
  pass
 def Remove(self,visual):
  """
  Remove(self: VisualCollection,visual: Visual)
   Removes the specified System.Windows.Media.Visual object from the 
    System.Windows.Media.VisualCollection.
  
  
   visual: The System.Windows.Media.Visual to remove from the 
    System.Windows.Media.VisualCollection.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: VisualCollection,index: int)
   Removes the visual object at the specified index in the 
    System.Windows.Media.VisualCollection.
  
  
   index: The zero-based index of the visual to remove.
  """
  pass
 def RemoveRange(self,index,count):
  """
  RemoveRange(self: VisualCollection,index: int,count: int)
   Removes a range of visual objects from the 
    System.Windows.Media.VisualCollection.
  
  
   index: The zero-based index of the range of elements to remove.
   count: The number of elements to remove.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
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
 @staticmethod
 def __new__(self,parent):
  """ __new__(cls: type,parent: Visual) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Capacity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of elements that the System.Windows.Media.VisualCollection can contain.

Get: Capacity(self: VisualCollection) -> int

Set: Capacity(self: VisualCollection)=value
"""

 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of elements in the collection.

Get: Count(self: VisualCollection) -> int

"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.Windows.Media.VisualCollection is read-only.

Get: IsReadOnly(self: VisualCollection) -> bool

"""

 IsSynchronized=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether access to the System.Windows.Media.VisualCollection is synchronized (thread-safe).

Get: IsSynchronized(self: VisualCollection) -> bool

"""

 SyncRoot=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an object that can be used to synchronize access to the System.Windows.Media.VisualCollection.

Get: SyncRoot(self: VisualCollection) -> object

"""


 Enumerator=None

