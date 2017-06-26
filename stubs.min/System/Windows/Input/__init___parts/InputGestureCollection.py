class InputGestureCollection(object,IList,ICollection,IEnumerable):
 """
 Represents an ordered collection of System.Windows.Input.InputGesture objects.
 
 InputGestureCollection()
 InputGestureCollection(inputGestures: IList)
 """
 def Add(self,inputGesture):
  """
  Add(self: InputGestureCollection,inputGesture: InputGesture) -> int
  
   Adds the specified System.Windows.Input.InputGesture to this 
    System.Windows.Input.InputGestureCollection.
  
  
   inputGesture: The gesture to add to the collection.
   Returns: 0,if the operation was successful (note that this is not the index of the 
    added item).
  """
  pass
 def AddRange(self,collection):
  """
  AddRange(self: InputGestureCollection,collection: ICollection)
   Adds the elements of the specified System.Collections.ICollection to the end of 
    this System.Windows.Input.InputGestureCollection.
  
  
   collection: The collection of items to add to the end of this 
    System.Windows.Input.InputGestureCollection.
  """
  pass
 def Clear(self):
  """
  Clear(self: InputGestureCollection)
   Removes all elements from the System.Windows.Input.InputGestureCollection.
  """
  pass
 def Contains(self,key):
  """
  Contains(self: InputGestureCollection,key: InputGesture) -> bool
  
   Determines whether the specified System.Windows.Input.InputGesture is in the 
    collection.
  
  
   key: The gesture to locate in the collection.
   Returns: true if the gesture is in the collection; otherwise,false.
  """
  pass
 def CopyTo(self,inputGestures,index):
  """
  CopyTo(self: InputGestureCollection,inputGestures: Array[InputGesture],index: int)
   Copies all of the items in the System.Windows.Input.InputGestureCollection to 
    the specified one-dimensional array,starting at the specified index of the 
    target array.
  
  
   inputGestures: An array into which the collection is copied.
   index: The index position in the inputGestures at which copying begins.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: InputGestureCollection) -> IEnumerator
  
   Gets an enumerator that iterates through this 
    System.Windows.Input.InputGestureCollection.
  
   Returns: The enumerator for this collection.
  """
  pass
 def IndexOf(self,value):
  """
  IndexOf(self: InputGestureCollection,value: InputGesture) -> int
  
   Searches for the first occurrence of the specified 
    System.Windows.Input.InputGesture in this 
    System.Windows.Input.InputGestureCollection.
  
  
   value: The gesture to locate in the collection.
   Returns: The index of the first occurrence of value,if found; otherwise,-1.
  """
  pass
 def Insert(self,index,inputGesture):
  """
  Insert(self: InputGestureCollection,index: int,inputGesture: InputGesture)
   Inserts the specified System.Windows.Input.InputGesture into this 
    System.Windows.Input.InputGestureCollection at the specified index.
  
  
   index: Index at which to insert inputGesture.
   inputGesture: The gesture to insert.
  """
  pass
 def Remove(self,inputGesture):
  """
  Remove(self: InputGestureCollection,inputGesture: InputGesture)
   Removes the first occurrence of the specified System.Windows.Input.InputGesture 
    from this System.Windows.Input.InputGestureCollection.
  
  
   inputGesture: The gesture to remove.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: InputGestureCollection,index: int)
   Removes the specified System.Windows.Input.InputGesture at the specified index 
    of this System.Windows.Input.InputGestureCollection.
  
  
   index: The zero-based index of the gesture to remove.
  """
  pass
 def Seal(self):
  """
  Seal(self: InputGestureCollection)
   Sets this System.Windows.Input.InputGestureCollection to read-only.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """
  __contains__(self: IList,value: object) -> bool
  
   Determines whether the System.Collections.IList contains a specific value.
  
   value: The object to locate in the System.Collections.IList.
   Returns: true if the System.Object is found in the System.Collections.IList; otherwise,
    false.
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
 @staticmethod
 def __new__(self,inputGestures=None):
  """
  __new__(cls: type)
  __new__(cls: type,inputGestures: IList)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of System.Windows.Input.InputGesture items in this System.Windows.Input.InputGestureCollection.

Get: Count(self: InputGestureCollection) -> int

"""

 IsFixedSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this System.Windows.Input.InputGestureCollection has a fixed size.

Get: IsFixedSize(self: InputGestureCollection) -> bool

"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this System.Windows.Input.InputGestureCollection is read-only.  The default value is false.

Get: IsReadOnly(self: InputGestureCollection) -> bool

"""

 IsSynchronized=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this System.Windows.Input.InputGestureCollection is synchronized (thread safe).

Get: IsSynchronized(self: InputGestureCollection) -> bool

"""

 SyncRoot=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an object that can be used to synchronize access to this System.Windows.Input.InputGestureCollection.

Get: SyncRoot(self: InputGestureCollection) -> object

"""


