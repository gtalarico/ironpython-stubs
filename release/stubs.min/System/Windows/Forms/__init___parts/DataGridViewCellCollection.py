class DataGridViewCellCollection(BaseCollection,ICollection,IEnumerable,IList):
 """
 Represents a collection of cells in a System.Windows.Forms.DataGridViewRow.

 

 DataGridViewCellCollection(dataGridViewRow: DataGridViewRow)
 """
 def Add(self,dataGridViewCell):
  """
  Add(self: DataGridViewCellCollection,dataGridViewCell: DataGridViewCell) -> int

  

   Adds a cell to the collection.

  

   dataGridViewCell: A System.Windows.Forms.DataGridViewCell to add to the collection.

   Returns: The position in which to insert the new element.
  """
  pass
 def AddRange(self,dataGridViewCells):
  """
  AddRange(self: DataGridViewCellCollection,*dataGridViewCells: Array[DataGridViewCell])

   Adds an array of cells to the collection.

  

   dataGridViewCells: The array of System.Windows.Forms.DataGridViewCell objects to add to the collection.
  """
  pass
 def Clear(self):
  """
  Clear(self: DataGridViewCellCollection)

   Clears all cells from the collection.
  """
  pass
 def Contains(self,dataGridViewCell):
  """
  Contains(self: DataGridViewCellCollection,dataGridViewCell: DataGridViewCell) -> bool

  

   Determines whether the specified cell is contained in the collection.

  

   dataGridViewCell: A System.Windows.Forms.DataGridViewCell to locate in the collection.

   Returns: true if dataGridViewCell is in the collection; otherwise,false.
  """
  pass
 def CopyTo(self,*__args):
  """
  CopyTo(self: DataGridViewCellCollection,array: Array[DataGridViewCell],index: int)

   Copies the entire collection of cells into an array at a specified location within the array.

  

   array: The destination array to which the contents will be copied.

   index: The index of the element in array at which to start copying.
  """
  pass
 def IndexOf(self,dataGridViewCell):
  """
  IndexOf(self: DataGridViewCellCollection,dataGridViewCell: DataGridViewCell) -> int

  

   Returns the index of the specified cell.

  

   dataGridViewCell: The cell to locate in the collection.

   Returns: The zero-based index of the value of dataGridViewCell parameter,if it is found in the 

    collection; otherwise,-1.
  """
  pass
 def Insert(self,index,dataGridViewCell):
  """
  Insert(self: DataGridViewCellCollection,index: int,dataGridViewCell: DataGridViewCell)

   Inserts a cell into the collection at the specified index.

  

   index: The zero-based index at which to place dataGridViewCell.

   dataGridViewCell: The System.Windows.Forms.DataGridViewCell to insert.
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
  OnCollectionChanged(self: DataGridViewCellCollection,e: CollectionChangeEventArgs)

   Raises the System.Windows.Forms.DataGridViewCellCollection.CollectionChanged event.

  

   e: A System.ComponentModel.CollectionChangeEventArgs that contains the event data.
  """
  pass
 def Remove(self,cell):
  """
  Remove(self: DataGridViewCellCollection,cell: DataGridViewCell)

   Removes the specified cell from the collection.

  

   cell: The System.Windows.Forms.DataGridViewCell to remove from the collection.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: DataGridViewCellCollection,index: int)

   Removes the cell at the specified index.

  

   index: The zero-based index of the System.Windows.Forms.DataGridViewCell to be removed.
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
 @staticmethod
 def __new__(self,dataGridViewRow):
  """ __new__(cls: type,dataGridViewRow: DataGridViewRow) """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]=x.__setitem__(i,y) <==> x[i]= """
  pass
 List=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an System.Collections.ArrayList containing System.Windows.Forms.DataGridViewCellCollection objects.



"""


 CollectionChanged=None

