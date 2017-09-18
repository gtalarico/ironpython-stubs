class GridColumnStylesCollection(BaseCollection,ICollection,IEnumerable,IList):
 """ Represents a collection of System.Windows.Forms.DataGridColumnStyle objects in the System.Windows.Forms.DataGrid control. """
 def Add(self,column):
  """
  Add(self: GridColumnStylesCollection,column: DataGridColumnStyle) -> int

  

   Adds a column style to the collection.

  

   column: The System.Windows.Forms.DataGridColumnStyle to add.

   Returns: The index of the new System.Windows.Forms.DataGridColumnStyle.
  """
  pass
 def AddRange(self,columns):
  """
  AddRange(self: GridColumnStylesCollection,columns: Array[DataGridColumnStyle])

   Adds an array of column style objects to the collection.

  

   columns: An array of System.Windows.Forms.DataGridColumnStyle objects to add to the collection.
  """
  pass
 def Clear(self):
  """
  Clear(self: GridColumnStylesCollection)

   Clears the collection of System.Windows.Forms.DataGridColumnStyle objects.
  """
  pass
 def Contains(self,*__args):
  """
  Contains(self: GridColumnStylesCollection,name: str) -> bool

  

   Gets a value indicating whether the System.Windows.Forms.GridColumnStylesCollection contains the 

    System.Windows.Forms.DataGridColumnStyle with the specified name.

  

  

   name: The System.Windows.Forms.DataGridColumnStyle.MappingName of the desired 

    System.Windows.Forms.DataGridColumnStyle.

  

   Returns: true if the collection contains the System.Windows.Forms.DataGridColumnStyle; otherwise,false.

  Contains(self: GridColumnStylesCollection,column: DataGridColumnStyle) -> bool

  

   Gets a value indicating whether the System.Windows.Forms.GridColumnStylesCollection contains the 

    specified System.Windows.Forms.DataGridColumnStyle.

  

  

   column: The desired System.Windows.Forms.DataGridColumnStyle.

   Returns: true if the collection contains the System.Windows.Forms.DataGridColumnStyle; otherwise,false.

  Contains(self: GridColumnStylesCollection,propertyDescriptor: PropertyDescriptor) -> bool

  

   Gets a value indicating whether the System.Windows.Forms.GridColumnStylesCollection contains a 

    System.Windows.Forms.DataGridColumnStyle associated with the specified 

    System.ComponentModel.PropertyDescriptor.

  

  

   propertyDescriptor: The System.ComponentModel.PropertyDescriptor associated with the desired 

    System.Windows.Forms.DataGridColumnStyle.

  

   Returns: true if the collection contains the System.Windows.Forms.DataGridColumnStyle; otherwise,false.
  """
  pass
 def IndexOf(self,element):
  """
  IndexOf(self: GridColumnStylesCollection,element: DataGridColumnStyle) -> int

  

   Gets the index of a specified System.Windows.Forms.DataGridColumnStyle.

  

   element: The System.Windows.Forms.DataGridColumnStyle to find.

   Returns: The zero-based index of the System.Windows.Forms.DataGridColumnStyle within the 

    System.Windows.Forms.GridColumnStylesCollection or -1 if no corresponding 

    System.Windows.Forms.DataGridColumnStyle exists.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject

  

   Creates a shallow copy of the current System.MarshalByRefObject object.

  

   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the 

    object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 

    false is usually appropriate. true to copy the current System.MarshalByRefObject object's 

    identity to its clone,which will cause remoting client calls to be routed to the remote server 

    object.

  

   Returns: A shallow copy of the current System.MarshalByRefObject object.

  MemberwiseClone(self: object) -> object

  

   Creates a shallow copy of the current System.Object.

   Returns: A shallow copy of the current System.Object.
  """
  pass
 def OnCollectionChanged(self,*args):
  """
  OnCollectionChanged(self: GridColumnStylesCollection,e: CollectionChangeEventArgs)

   Raises the System.Windows.Forms.GridColumnStylesCollection.CollectionChanged event.

  

   e: A System.ComponentModel.CollectionChangeEventArgs that contains the event data event.
  """
  pass
 def Remove(self,column):
  """
  Remove(self: GridColumnStylesCollection,column: DataGridColumnStyle)

   Removes the specified System.Windows.Forms.DataGridColumnStyle from the 

    System.Windows.Forms.GridColumnStylesCollection.

  

  

   column: The System.Windows.Forms.DataGridColumnStyle to remove from the collection.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: GridColumnStylesCollection,index: int)

   Removes the System.Windows.Forms.DataGridColumnStyle with the specified index from the 

    System.Windows.Forms.GridColumnStylesCollection.

  

  

   index: The zero-based index of the System.Windows.Forms.DataGridColumnStyle to remove.
  """
  pass
 def ResetPropertyDescriptors(self):
  """
  ResetPropertyDescriptors(self: GridColumnStylesCollection)

   Sets the System.ComponentModel.PropertyDescriptor for each column style in the collection to 

    null.
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
  """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
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
 List=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of items in the collection.



"""


 CollectionChanged=None

