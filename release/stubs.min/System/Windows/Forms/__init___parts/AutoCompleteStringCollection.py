class AutoCompleteStringCollection(object,IList,ICollection,IEnumerable):
 """
 Contains a collection of strings to use for the auto-complete feature on certain Windows Forms controls.

 

 AutoCompleteStringCollection()
 """
 def Add(self,value):
  """
  Add(self: AutoCompleteStringCollection,value: str) -> int

  

   Inserts a new System.String into the collection.

  

   value: The System.String to add to the collection.

   Returns: The position in the collection where the System.String was added.
  """
  pass
 def AddRange(self,value):
  """
  AddRange(self: AutoCompleteStringCollection,value: Array[str])

   Adds the elements of a System.String collection to the end.

  

   value: The strings to add to the collection.
  """
  pass
 def Clear(self):
  """
  Clear(self: AutoCompleteStringCollection)

   Removes all strings from the collection.
  """
  pass
 def Contains(self,value):
  """
  Contains(self: AutoCompleteStringCollection,value: str) -> bool

  

   Indicates whether the System.String exists within the collection.

  

   value: The System.String for which to search.

   Returns: true if the System.String exists within the collection; otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: AutoCompleteStringCollection,array: Array[str],index: int)

   Copies an array of System.String objects into the collection,starting at the specified position.

  

   array: The System.String objects to add to the collection.

   index: The position within the collection at which to start the insertion.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: AutoCompleteStringCollection) -> IEnumerator

  

   Returns an enumerator that iterates through the 

    System.Windows.Forms.AutoCompleteStringCollection.

  

   Returns: An enumerator that iterates through the collection.
  """
  pass
 def IndexOf(self,value):
  """
  IndexOf(self: AutoCompleteStringCollection,value: str) -> int

  

   Obtains the position of the specified string within the collection.

  

   value: The System.String for which to search.

   Returns: The index for the specified item.
  """
  pass
 def Insert(self,index,value):
  """
  Insert(self: AutoCompleteStringCollection,index: int,value: str)

   Inserts the string into a specific index in the collection.

  

   index: The position at which to insert the string.

   value: The string to insert.
  """
  pass
 def OnCollectionChanged(self,*args):
  """
  OnCollectionChanged(self: AutoCompleteStringCollection,e: CollectionChangeEventArgs)

   Raises the System.Windows.Forms.AutoCompleteStringCollection.CollectionChanged event.

  

   e: A System.ComponentModel.CollectionChangeEventArgs that contains the event data.
  """
  pass
 def Remove(self,value):
  """
  Remove(self: AutoCompleteStringCollection,value: str)

   Removes a string from the collection.

  

   value: The System.String to remove.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: AutoCompleteStringCollection,index: int)

   Removes the string at the specified index.

  

   index: The zero-based index of the string to remove.
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
 """Gets the number of items in the System.Windows.Forms.AutoCompleteStringCollection .



Get: Count(self: AutoCompleteStringCollection) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the contents of the collection are read-only.



Get: IsReadOnly(self: AutoCompleteStringCollection) -> bool



"""

 IsSynchronized=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether access to the System.Windows.Forms.AutoCompleteStringCollection is synchronized (thread safe).



Get: IsSynchronized(self: AutoCompleteStringCollection) -> bool



"""

 SyncRoot=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an object that can be used to synchronize access to the System.Windows.Forms.AutoCompleteStringCollection.



Get: SyncRoot(self: AutoCompleteStringCollection) -> object



"""


 CollectionChanged=None

