class DataGridViewColumnCollection(BaseCollection,ICollection,IEnumerable,IList):
 """
 Represents a collection of System.Windows.Forms.DataGridViewColumn objects in a System.Windows.Forms.DataGridView control.

 

 DataGridViewColumnCollection(dataGridView: DataGridView)
 """
 def Add(self,*__args):
  """
  Add(self: DataGridViewColumnCollection,dataGridViewColumn: DataGridViewColumn) -> int

  

   Adds the given column to the collection.

  

   dataGridViewColumn: The System.Windows.Forms.DataGridViewColumn to add.

   Returns: The index of the column.

  Add(self: DataGridViewColumnCollection,columnName: str,headerText: str) -> int

  

   Adds a System.Windows.Forms.DataGridViewTextBoxColumn with the given column name and column 

    header text to the collection.

  

  

   columnName: The name by which the column will be referred.

   headerText: The text for the column's header.

   Returns: The index of the column.
  """
  pass
 def AddRange(self,dataGridViewColumns):
  """
  AddRange(self: DataGridViewColumnCollection,*dataGridViewColumns: Array[DataGridViewColumn])

   Adds a range of columns to the collection.

  

   dataGridViewColumns: An array of System.Windows.Forms.DataGridViewColumn objects to add.
  """
  pass
 def Clear(self):
  """
  Clear(self: DataGridViewColumnCollection)

   Clears the collection.
  """
  pass
 def Contains(self,*__args):
  """
  Contains(self: DataGridViewColumnCollection,columnName: str) -> bool

  

   Determines whether the collection contains the column referred to by the given name.

  

   columnName: The name of the column to look for.

   Returns: true if the column is contained in the collection; otherwise,false.

  Contains(self: DataGridViewColumnCollection,dataGridViewColumn: DataGridViewColumn) -> bool

  

   Determines whether the collection contains the given column.

  

   dataGridViewColumn: The System.Windows.Forms.DataGridViewColumn to look for.

   Returns: true if the given column is in the collection; otherwise,false.
  """
  pass
 def CopyTo(self,*__args):
  """
  CopyTo(self: DataGridViewColumnCollection,array: Array[DataGridViewColumn],index: int)

   Copies the items from the collection to the given array.

  

   array: The destination System.Windows.Forms.DataGridViewColumn array.

   index: The index of the destination array at which to start copying.
  """
  pass
 def GetColumnCount(self,includeFilter):
  """
  GetColumnCount(self: DataGridViewColumnCollection,includeFilter: DataGridViewElementStates) -> int

  

   Returns the number of columns that meet the given filter requirements.

  

   includeFilter: A bitwise combination of the System.Windows.Forms.DataGridViewElementStates values that 

    represent the filter for inclusion.

  

   Returns: The number of columns that meet the filter requirements.
  """
  pass
 def GetColumnsWidth(self,includeFilter):
  """
  GetColumnsWidth(self: DataGridViewColumnCollection,includeFilter: DataGridViewElementStates) -> int

  

   Returns the width,in pixels,required to display all of the columns that meet the given filter 

    requirements.

  

  

   includeFilter: A bitwise combination of the System.Windows.Forms.DataGridViewElementStates values that 

    represent the filter for inclusion.

  

   Returns: The width,in pixels,that is necessary to display all of the columns that meet the filter 

    requirements.
  """
  pass
 def GetFirstColumn(self,includeFilter,excludeFilter=None):
  """
  GetFirstColumn(self: DataGridViewColumnCollection,includeFilter: DataGridViewElementStates,excludeFilter: DataGridViewElementStates) -> DataGridViewColumn

  

   Returns the first column in display order that meets the given inclusion-filter and 

    exclusion-filter requirements.

  

  

   includeFilter: A bitwise combination of the System.Windows.Forms.DataGridViewElementStates values that 

    represent the filter to apply for inclusion.

  

   excludeFilter: A bitwise combination of the System.Windows.Forms.DataGridViewElementStates values that 

    represent the filter to apply for exclusion.

  

   Returns: The first column in display order that meets the given filter requirements,or null if no column 

    is found.

  

  GetFirstColumn(self: DataGridViewColumnCollection,includeFilter: DataGridViewElementStates) -> DataGridViewColumn

  

   Returns the first column in display order that meets the given inclusion-filter requirements.

  

   includeFilter: A bitwise combination of the System.Windows.Forms.DataGridViewElementStates values that 

    represents the filter for inclusion.

  

   Returns: The first column in display order that meets the given filter requirements,or null if no column 

    is found.
  """
  pass
 def GetLastColumn(self,includeFilter,excludeFilter):
  """
  GetLastColumn(self: DataGridViewColumnCollection,includeFilter: DataGridViewElementStates,excludeFilter: DataGridViewElementStates) -> DataGridViewColumn

  

   Returns the last column in display order that meets the given filter requirements.

  

   includeFilter: A bitwise combination of the System.Windows.Forms.DataGridViewElementStates values that 

    represent the filter to apply for inclusion.

  

   excludeFilter: A bitwise combination of the System.Windows.Forms.DataGridViewElementStates values that 

    represent the filter to apply for exclusion.

  

   Returns: The last displayed column in display order that meets the given filter requirements,or null if 

    no column is found.
  """
  pass
 def GetNextColumn(self,dataGridViewColumnStart,includeFilter,excludeFilter):
  """
  GetNextColumn(self: DataGridViewColumnCollection,dataGridViewColumnStart: DataGridViewColumn,includeFilter: DataGridViewElementStates,excludeFilter: DataGridViewElementStates) -> DataGridViewColumn

  

   Gets the first column after the given column in display order that meets the given filter 

    requirements.

  

  

   dataGridViewColumnStart: The column from which to start searching for the next column.

   includeFilter: A bitwise combination of the System.Windows.Forms.DataGridViewElementStates values that 

    represent the filter to apply for inclusion.

  

   excludeFilter: A bitwise combination of the System.Windows.Forms.DataGridViewElementStates values that 

    represent the filter to apply for exclusion.

  

   Returns: The next column that meets the given filter requirements,or null if no column is found.
  """
  pass
 def GetPreviousColumn(self,dataGridViewColumnStart,includeFilter,excludeFilter):
  """
  GetPreviousColumn(self: DataGridViewColumnCollection,dataGridViewColumnStart: DataGridViewColumn,includeFilter: DataGridViewElementStates,excludeFilter: DataGridViewElementStates) -> DataGridViewColumn

  

   Gets the last column prior to the given column in display order that meets the given filter 

    requirements.

  

  

   dataGridViewColumnStart: The column from which to start searching for the previous column.

   includeFilter: A bitwise combination of the System.Windows.Forms.DataGridViewElementStates values that 

    represent the filter to apply for inclusion.

  

   excludeFilter: A bitwise combination of the System.Windows.Forms.DataGridViewElementStates values that 

    represent the filter to apply for exclusion.

  

   Returns: The previous column that meets the given filter requirements,or null if no column is found.
  """
  pass
 def IndexOf(self,dataGridViewColumn):
  """
  IndexOf(self: DataGridViewColumnCollection,dataGridViewColumn: DataGridViewColumn) -> int

  

   Gets the index of the given System.Windows.Forms.DataGridViewColumn in the collection.

  

   dataGridViewColumn: The System.Windows.Forms.DataGridViewColumn to return the index of.

   Returns: The index of the given System.Windows.Forms.DataGridViewColumn.
  """
  pass
 def Insert(self,columnIndex,dataGridViewColumn):
  """
  Insert(self: DataGridViewColumnCollection,columnIndex: int,dataGridViewColumn: DataGridViewColumn)

   Inserts a column at the given index in the collection.

  

   columnIndex: The zero-based index at which to insert the given column.

   dataGridViewColumn: The System.Windows.Forms.DataGridViewColumn to insert.
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
  OnCollectionChanged(self: DataGridViewColumnCollection,e: CollectionChangeEventArgs)

   Raises the System.Windows.Forms.DataGridViewColumnCollection.CollectionChanged event.

  

   e: A System.ComponentModel.CollectionChangeEventArgs that contains the event data.
  """
  pass
 def Remove(self,*__args):
  """
  Remove(self: DataGridViewColumnCollection,columnName: str)

   Removes the column with the specified name from the collection.

  

   columnName: The name of the column to delete.

  Remove(self: DataGridViewColumnCollection,dataGridViewColumn: DataGridViewColumn)

   Removes the specified column from the collection.

  

   dataGridViewColumn: The column to delete.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: DataGridViewColumnCollection,index: int)

   Removes the column at the given index in the collection.

  

   index: The index of the column to delete.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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
 def __new__(self,dataGridView):
  """ __new__(cls: type,dataGridView: DataGridView) """
  pass
 DataGridView=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.DataGridView upon which the collection performs column-related operations.



"""

 List=property(lambda self: object(),lambda self,v: None,lambda self: None)


 CollectionChanged=None

