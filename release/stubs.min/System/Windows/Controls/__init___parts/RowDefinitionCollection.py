class RowDefinitionCollection(object,IList[RowDefinition],ICollection[RowDefinition],IEnumerable[RowDefinition],IEnumerable,IList,ICollection):
 """ Provides access to an ordered,strongly typed collection of System.Windows.Controls.RowDefinition objects. """
 def Add(self,value):
  """
  Add(self: RowDefinitionCollection,value: RowDefinition)

   Adds a System.Windows.Controls.RowDefinition element to a 

    System.Windows.Controls.RowDefinitionCollection.

  

  

   value: Identifies the System.Windows.Controls.RowDefinition to add to the collection.
  """
  pass
 def Clear(self):
  """
  Clear(self: RowDefinitionCollection)

   Clears the content of the System.Windows.Controls.RowDefinitionCollection.
  """
  pass
 def Contains(self,value):
  """
  Contains(self: RowDefinitionCollection,value: RowDefinition) -> bool

  

   Determines whether a given System.Windows.Controls.RowDefinition exists within a 

    System.Windows.Controls.RowDefinitionCollection.

  

  

   value: Identifies the System.Windows.Controls.RowDefinition that is being tested.

   Returns: true if the System.Windows.Controls.RowDefinition exists within the collection; otherwise false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: RowDefinitionCollection,array: Array[RowDefinition],index: int)

   Copies an array of System.Windows.Controls.RowDefinition objects to a given index position 

    within a System.Windows.Controls.RowDefinitionCollection.

  

  

   array: An array of System.Windows.Controls.RowDefinition objects.

   index: Identifies the index position within array to which the System.Windows.Controls.RowDefinition 

    objects are copied.
  """
  pass
 def IndexOf(self,value):
  """
  IndexOf(self: RowDefinitionCollection,value: RowDefinition) -> int

  

   Returns the index position of a given System.Windows.Controls.RowDefinition within a 

    System.Windows.Controls.RowDefinitionCollection.

  

  

   value: The System.Windows.Controls.RowDefinition whose index position is desired.

   Returns: The index of value if found in the collection; otherwise,-1.
  """
  pass
 def Insert(self,index,value):
  """
  Insert(self: RowDefinitionCollection,index: int,value: RowDefinition)

   Inserts a System.Windows.Controls.RowDefinition at the specified index position within a 

    System.Windows.Controls.RowDefinitionCollection.

  

  

   index: The position within the collection where the item is inserted.

   value: The System.Windows.Controls.RowDefinition to insert.
  """
  pass
 def Remove(self,value):
  """
  Remove(self: RowDefinitionCollection,value: RowDefinition) -> bool

  

   Removes a System.Windows.Controls.RowDefinition from a 

    System.Windows.Controls.RowDefinitionCollection.

  

  

   value: The System.Windows.Controls.RowDefinition to remove from the collection.

   Returns: true if the System.Windows.Controls.RowDefinition was found in the collection and removed; 

    otherwise,false.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: RowDefinitionCollection,index: int)

   Removes a System.Windows.Controls.RowDefinition from a 

    System.Windows.Controls.RowDefinitionCollection at the specified index position.

  

  

   index: The position within the collection at which the System.Windows.Controls.RowDefinition is removed.
  """
  pass
 def RemoveRange(self,index,count):
  """
  RemoveRange(self: RowDefinitionCollection,index: int,count: int)

   Removes a range of System.Windows.Controls.RowDefinition objects from a 

    System.Windows.Controls.RowDefinitionCollection.

  

  

   index: The position within the collection at which the first System.Windows.Controls.RowDefinition is 

    removed.

  

   count: The total number of System.Windows.Controls.RowDefinition objects to remove from the collection.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """
  __contains__(self: ICollection[RowDefinition],item: RowDefinition) -> bool

  __contains__(self: IList,value: object) -> bool

  

   Determines whether the System.Collections.IList contains a specific value.

  

   value: The object to locate in the System.Collections.IList.

   Returns: true if the System.Object is found in the System.Collections.IList; otherwise,false.
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
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total number of items within this instance of System.Windows.Controls.RowDefinitionCollection.



Get: Count(self: RowDefinitionCollection) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether a System.Windows.Controls.RowDefinitionCollection is read-only.



Get: IsReadOnly(self: RowDefinitionCollection) -> bool



"""

 IsSynchronized=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether access to this System.Windows.Controls.RowDefinitionCollection is synchronized (thread-safe).



Get: IsSynchronized(self: RowDefinitionCollection) -> bool



"""

 SyncRoot=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an object that can be used to synchronize access to the System.Windows.Controls.RowDefinitionCollection.



Get: SyncRoot(self: RowDefinitionCollection) -> object



"""


