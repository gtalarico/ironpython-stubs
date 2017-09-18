class EventLogPermissionEntryCollection(CollectionBase,IList,ICollection,IEnumerable):
 """ Contains a strongly typed collection of System.Diagnostics.EventLogPermissionEntry objects. """
 def Add(self,value):
  """
  Add(self: EventLogPermissionEntryCollection,value: EventLogPermissionEntry) -> int

  

   Adds a specified System.Diagnostics.EventLogPermissionEntry to this collection.

  

   value: The System.Diagnostics.EventLogPermissionEntry to add.

   Returns: The zero-based index of the added System.Diagnostics.EventLogPermissionEntry.
  """
  pass
 def AddRange(self,value):
  """
  AddRange(self: EventLogPermissionEntryCollection,value: EventLogPermissionEntryCollection)

   Appends a set of specified permission entries to this collection.

  

   value: A System.Diagnostics.EventLogPermissionEntryCollection that contains the permission entries to 

    add.

  

  AddRange(self: EventLogPermissionEntryCollection,value: Array[EventLogPermissionEntry])

   Appends a set of specified permission entries to this collection.

  

   value: An array of type System.Diagnostics.EventLogPermissionEntry objects that contains the permission 

    entries to add.
  """
  pass
 def Contains(self,value):
  """
  Contains(self: EventLogPermissionEntryCollection,value: EventLogPermissionEntry) -> bool

  

   Determines whether this collection contains a specified 

    System.Diagnostics.EventLogPermissionEntry.

  

  

   value: The System.Diagnostics.EventLogPermissionEntry to find.

   Returns: true if the specified System.Diagnostics.EventLogPermissionEntry belongs to this collection; 

    otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: EventLogPermissionEntryCollection,array: Array[EventLogPermissionEntry],index: int)

   Copies the permission entries from this collection to an array,starting at a particular index 

    of the array.

  

  

   array: An array of type System.Diagnostics.EventLogPermissionEntry that receives this collection's 

    permission entries.

  

   index: The zero-based index at which to begin copying the permission entries.
  """
  pass
 def IndexOf(self,value):
  """
  IndexOf(self: EventLogPermissionEntryCollection,value: EventLogPermissionEntry) -> int

  

   Determines the index of a specified permission entry in this collection.

  

   value: The permission entry to search for.

   Returns: The zero-based index of the specified permission entry,or -1 if the permission entry was not 

    found in the collection.
  """
  pass
 def Insert(self,index,value):
  """
  Insert(self: EventLogPermissionEntryCollection,index: int,value: EventLogPermissionEntry)

   Inserts a permission entry into this collection at a specified index.

  

   index: The zero-based index of the collection at which to insert the permission entry.

   value: The permission entry to insert into this collection.
  """
  pass
 def OnClear(self,*args):
  """
  OnClear(self: EventLogPermissionEntryCollection)

   Performs additional custom processes after clearing the contents of the collection.
  """
  pass
 def OnClearComplete(self,*args):
  """
  OnClearComplete(self: CollectionBase)

   Performs additional custom processes after clearing the contents of the 

    System.Collections.CollectionBase instance.
  """
  pass
 def OnInsert(self,*args):
  """
  OnInsert(self: EventLogPermissionEntryCollection,index: int,value: object)

   Performs additional custom processes before a new permission entry is inserted into the 

    collection.

  

  

   index: The zero-based index at which to insert value.

   value: The new value of the permission entry at index.
  """
  pass
 def OnInsertComplete(self,*args):
  """
  OnInsertComplete(self: CollectionBase,index: int,value: object)

   Performs additional custom processes after inserting a new element into the 

    System.Collections.CollectionBase instance.

  

  

   index: The zero-based index at which to insert value.

   value: The new value of the element at index.
  """
  pass
 def OnRemove(self,*args):
  """
  OnRemove(self: EventLogPermissionEntryCollection,index: int,value: object)

   Performs additional custom processes when removing a new permission entry from the collection.

  

   index: The zero-based index at which value can be found.

   value: The permission entry to remove from index.
  """
  pass
 def OnRemoveComplete(self,*args):
  """
  OnRemoveComplete(self: CollectionBase,index: int,value: object)

   Performs additional custom processes after removing an element from the 

    System.Collections.CollectionBase instance.

  

  

   index: The zero-based index at which value can be found.

   value: The value of the element to remove from index.
  """
  pass
 def OnSet(self,*args):
  """
  OnSet(self: EventLogPermissionEntryCollection,index: int,oldValue: object,newValue: object)

   Performs additional custom processes before setting a value in the collection.

  

   index: The zero-based index at which oldValue can be found.

   oldValue: The value to replace with newValue.

   newValue: The new value of the permission entry at index.
  """
  pass
 def OnSetComplete(self,*args):
  """
  OnSetComplete(self: CollectionBase,index: int,oldValue: object,newValue: object)

   Performs additional custom processes after setting a value in the 

    System.Collections.CollectionBase instance.

  

  

   index: The zero-based index at which oldValue can be found.

   oldValue: The value to replace with newValue.

   newValue: The new value of the element at index.
  """
  pass
 def OnValidate(self,*args):
  """
  OnValidate(self: CollectionBase,value: object)

   Performs additional custom processes when validating a value.

  

   value: The object to validate.
  """
  pass
 def Remove(self,value):
  """
  Remove(self: EventLogPermissionEntryCollection,value: EventLogPermissionEntry)

   Removes a specified permission entry from this collection.

  

   value: The permission entry to remove.
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
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 InnerList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.



"""

 List=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.



"""


