class GridTableStylesCollection(BaseCollection,ICollection,IEnumerable,IList):
 """ Represents a collection of System.Windows.Forms.DataGridTableStyle objects in the System.Windows.Forms.DataGrid control. """
 def Add(self,table):
  """
  Add(self: GridTableStylesCollection,table: DataGridTableStyle) -> int

  

   Adds a System.Windows.Forms.DataGridTableStyle to this collection.

  

   table: The System.Windows.Forms.DataGridTableStyle to add to the collection.

   Returns: The index of the newly added object.
  """
  pass
 def AddRange(self,tables):
  """
  AddRange(self: GridTableStylesCollection,tables: Array[DataGridTableStyle])

   Adds an array of table styles to the collection.

  

   tables: An array of System.Windows.Forms.DataGridTableStyle objects.
  """
  pass
 def Clear(self):
  """
  Clear(self: GridTableStylesCollection)

   Clears the collection.
  """
  pass
 def Contains(self,*__args):
  """
  Contains(self: GridTableStylesCollection,name: str) -> bool

  

   Gets a value indicating whether the System.Windows.Forms.GridTableStylesCollection contains the 

    System.Windows.Forms.DataGridTableStyle specified by name.

  

  

   name: The System.Windows.Forms.DataGridTableStyle.MappingName of the 

    System.Windows.Forms.DataGridTableStyle to look for.

  

   Returns: true if the specified table style exists in the collection; otherwise,false.

  Contains(self: GridTableStylesCollection,table: DataGridTableStyle) -> bool

  

   Gets a value indicating whether the System.Windows.Forms.GridTableStylesCollection contains the 

    specified System.Windows.Forms.DataGridTableStyle.

  

  

   table: The System.Windows.Forms.DataGridTableStyle to look for.

   Returns: true if the specified table style exists in the collection; otherwise,false.
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
  OnCollectionChanged(self: GridTableStylesCollection,e: CollectionChangeEventArgs)

   Raises the System.Windows.Forms.GridTableStylesCollection.CollectionChanged event.

  

   e: A System.ComponentModel.CollectionChangeEventArgs containing the event data.
  """
  pass
 def Remove(self,table):
  """
  Remove(self: GridTableStylesCollection,table: DataGridTableStyle)

   Removes the specified System.Windows.Forms.DataGridTableStyle.

  

   table: The System.Windows.Forms.DataGridTableStyle to remove.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: GridTableStylesCollection,index: int)

   Removes a System.Windows.Forms.DataGridTableStyle at the specified index.

  

   index: The index of the System.Windows.Forms.DataGridTableStyle to remove.
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
 List=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the underlying list.



"""


 CollectionChanged=None

