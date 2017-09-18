class TraceListenerCollection(object,IList,ICollection,IEnumerable):
 """ Provides a thread-safe list of System.Diagnostics.TraceListener objects. """
 def Add(self,listener):
  """
  Add(self: TraceListenerCollection,listener: TraceListener) -> int

  

   Adds a System.Diagnostics.TraceListener to the list.

  

   listener: A System.Diagnostics.TraceListener to add to the list.

   Returns: The position at which the new listener was inserted.
  """
  pass
 def AddRange(self,value):
  """
  AddRange(self: TraceListenerCollection,value: TraceListenerCollection)

   Adds the contents of another System.Diagnostics.TraceListenerCollection to the list.

  

   value: Another System.Diagnostics.TraceListenerCollection whose contents are added to the list.

  AddRange(self: TraceListenerCollection,value: Array[TraceListener])

   Adds an array of System.Diagnostics.TraceListener objects to the list.

  

   value: An array of System.Diagnostics.TraceListener objects to add to the list.
  """
  pass
 def Clear(self):
  """
  Clear(self: TraceListenerCollection)

   Clears all the listeners from the list.
  """
  pass
 def Contains(self,listener):
  """
  Contains(self: TraceListenerCollection,listener: TraceListener) -> bool

  

   Checks whether the list contains the specified listener.

  

   listener: A System.Diagnostics.TraceListener to find in the list.

   Returns: true if the listener is in the list; otherwise,false.
  """
  pass
 def CopyTo(self,listeners,index):
  """
  CopyTo(self: TraceListenerCollection,listeners: Array[TraceListener],index: int)

   Copies a section of the current System.Diagnostics.TraceListenerCollection list to the specified 

    array at the specified index.

  

  

   listeners: An array of type System.Array to copy the elements into.

   index: The starting index number in the current list to copy from.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: TraceListenerCollection) -> IEnumerator

  

   Gets an enumerator for this list.

   Returns: An enumerator of type System.Collections.IEnumerator.
  """
  pass
 def IndexOf(self,listener):
  """
  IndexOf(self: TraceListenerCollection,listener: TraceListener) -> int

  

   Gets the index of the specified listener.

  

   listener: A System.Diagnostics.TraceListener to find in the list.

   Returns: The index of the listener,if it can be found in the list; otherwise,-1.
  """
  pass
 def Insert(self,index,listener):
  """
  Insert(self: TraceListenerCollection,index: int,listener: TraceListener)

   Inserts the listener at the specified index.

  

   index: The position in the list to insert the new System.Diagnostics.TraceListener.

   listener: A System.Diagnostics.TraceListener to insert in the list.
  """
  pass
 def Remove(self,*__args):
  """
  Remove(self: TraceListenerCollection,name: str)

   Removes from the collection the first System.Diagnostics.TraceListener with the specified name.

  

   name: The name of the System.Diagnostics.TraceListener to remove from the list.

  Remove(self: TraceListenerCollection,listener: TraceListener)

   Removes from the collection the specified System.Diagnostics.TraceListener.

  

   listener: A System.Diagnostics.TraceListener to remove from the list.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: TraceListenerCollection,index: int)

   Removes from the collection the System.Diagnostics.TraceListener at the specified index.

  

   index: The zero-based index of the System.Diagnostics.TraceListener to remove from the list.
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
  """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
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
 """Gets the number of listeners in the list.



Get: Count(self: TraceListenerCollection) -> int



"""


