class DataGridViewRowCollection(object,ICollection,IEnumerable,IList):
 """
 A collection of System.Windows.Forms.DataGridViewRow objects.

 

 DataGridViewRowCollection(dataGridView: DataGridView)
 """
 def Add(self,*__args):
  """
  Add(self: DataGridViewRowCollection,dataGridViewRow: DataGridViewRow) -> int

  

   Adds the specified System.Windows.Forms.DataGridViewRow to the collection.

  

   dataGridViewRow: The System.Windows.Forms.DataGridViewRow to add to the 

    System.Windows.Forms.DataGridViewRowCollection.

  

   Returns: The index of the new System.Windows.Forms.DataGridViewRow.

  Add(self: DataGridViewRowCollection,count: int) -> int

  

   Adds the specified number of new rows to the collection.

  

   count: The number of rows to add to the System.Windows.Forms.DataGridViewRowCollection.

   Returns: The index of the last row that was added.

  Add(self: DataGridViewRowCollection) -> int

  

   Adds a new row to the collection.

   Returns: The index of the new row.

  Add(self: DataGridViewRowCollection,*values: Array[object]) -> int

  

   Adds a new row to the collection,and populates the cells with the specified objects.

  

   values: A variable number of objects that populate the cells of the new 

    System.Windows.Forms.DataGridViewRow.

  

   Returns: The index of the new row.
  """
  pass
 def AddCopies(self,indexSource,count):
  """
  AddCopies(self: DataGridViewRowCollection,indexSource: int,count: int) -> int

  

   Adds the specified number of rows to the collection based on the row at the specified index.

  

   indexSource: The index of the row on which to base the new rows.

   count: The number of rows to add to the System.Windows.Forms.DataGridViewRowCollection.

   Returns: The index of the last row that was added.
  """
  pass
 def AddCopy(self,indexSource):
  """
  AddCopy(self: DataGridViewRowCollection,indexSource: int) -> int

  

   Adds a new row based on the row at the specified index.

  

   indexSource: The index of the row on which to base the new row.

   Returns: The index of the new row.
  """
  pass
 def AddRange(self,dataGridViewRows):
  """
  AddRange(self: DataGridViewRowCollection,*dataGridViewRows: Array[DataGridViewRow])

   Adds the specified System.Windows.Forms.DataGridViewRow objects to the collection.

  

   dataGridViewRows: An array of System.Windows.Forms.DataGridViewRow objects to be added to the 

    System.Windows.Forms.DataGridViewRowCollection.
  """
  pass
 def Clear(self):
  """
  Clear(self: DataGridViewRowCollection)

   Clears the collection.
  """
  pass
 def Contains(self,dataGridViewRow):
  """
  Contains(self: DataGridViewRowCollection,dataGridViewRow: DataGridViewRow) -> bool

  

   Determines whether the specified System.Windows.Forms.DataGridViewRow is in the collection.

  

   dataGridViewRow: The System.Windows.Forms.DataGridViewRow to locate in the 

    System.Windows.Forms.DataGridViewRowCollection.

  

   Returns: true if the System.Windows.Forms.DataGridViewRow is in the 

    System.Windows.Forms.DataGridViewRowCollection; otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: DataGridViewRowCollection,array: Array[DataGridViewRow],index: int)

   Copies the items from the collection into the specified System.Windows.Forms.DataGridViewRow 

    array,starting at the specified index.

  

  

   array: A System.Windows.Forms.DataGridViewRow array that is the destination of the items copied from 

    the System.Windows.Forms.DataGridViewRowCollection.

  

   index: The zero-based index in array at which copying begins.
  """
  pass
 def GetFirstRow(self,includeFilter,excludeFilter=None):
  """
  GetFirstRow(self: DataGridViewRowCollection,includeFilter: DataGridViewElementStates,excludeFilter: DataGridViewElementStates) -> int

  

   Returns the index of the first System.Windows.Forms.DataGridViewRow that meets the specified 

    inclusion and exclusion criteria.

  

  

   includeFilter: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values.

   excludeFilter: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values.

   Returns: The index of the first System.Windows.Forms.DataGridViewRow that has the attributes specified by 

    includeFilter,and does not have the attributes specified by excludeFilter; -1 if no row is 

    found.

  

  GetFirstRow(self: DataGridViewRowCollection,includeFilter: DataGridViewElementStates) -> int

  

   Returns the index of the first System.Windows.Forms.DataGridViewRow that meets the specified 

    criteria.

  

  

   includeFilter: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values.

   Returns: The index of the first System.Windows.Forms.DataGridViewRow that has the attributes specified by 

    includeFilter; -1 if no row is found.
  """
  pass
 def GetLastRow(self,includeFilter):
  """
  GetLastRow(self: DataGridViewRowCollection,includeFilter: DataGridViewElementStates) -> int

  

   Returns the index of the last System.Windows.Forms.DataGridViewRow that meets the specified 

    criteria.

  

  

   includeFilter: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values.

   Returns: The index of the last System.Windows.Forms.DataGridViewRow that has the attributes specified by 

    includeFilter; -1 if no row is found.
  """
  pass
 def GetNextRow(self,indexStart,includeFilter,excludeFilter=None):
  """
  GetNextRow(self: DataGridViewRowCollection,indexStart: int,includeFilter: DataGridViewElementStates,excludeFilter: DataGridViewElementStates) -> int

  

   Returns the index of the next System.Windows.Forms.DataGridViewRow that meets the specified 

    inclusion and exclusion criteria.

  

  

   indexStart: The index of the row where the method should begin to look for the next 

    System.Windows.Forms.DataGridViewRow.

  

   includeFilter: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values.

   excludeFilter: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values.

   Returns: The index of the next System.Windows.Forms.DataGridViewRow that has the attributes specified by 

    includeFilter,and does not have the attributes specified by excludeFilter; -1 if no row is 

    found.

  

  GetNextRow(self: DataGridViewRowCollection,indexStart: int,includeFilter: DataGridViewElementStates) -> int

  

   Returns the index of the next System.Windows.Forms.DataGridViewRow that meets the specified 

    criteria.

  

  

   indexStart: The index of the row where the method should begin to look for the next 

    System.Windows.Forms.DataGridViewRow.

  

   includeFilter: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values.

   Returns: The index of the first System.Windows.Forms.DataGridViewRow after indexStart that has the 

    attributes specified by includeFilter,or -1 if no row is found.
  """
  pass
 def GetPreviousRow(self,indexStart,includeFilter,excludeFilter=None):
  """
  GetPreviousRow(self: DataGridViewRowCollection,indexStart: int,includeFilter: DataGridViewElementStates,excludeFilter: DataGridViewElementStates) -> int

  

   Returns the index of the previous System.Windows.Forms.DataGridViewRow that meets the specified 

    inclusion and exclusion criteria.

  

  

   indexStart: The index of the row where the method should begin to look for the previous 

    System.Windows.Forms.DataGridViewRow.

  

   includeFilter: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values.

   excludeFilter: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values.

   Returns: The index of the previous System.Windows.Forms.DataGridViewRow that has the attributes specified 

    by includeFilter,and does not have the attributes specified by excludeFilter; -1 if no row is 

    found.

  

  GetPreviousRow(self: DataGridViewRowCollection,indexStart: int,includeFilter: DataGridViewElementStates) -> int

  

   Returns the index of the previous System.Windows.Forms.DataGridViewRow that meets the specified 

    criteria.

  

  

   indexStart: The index of the row where the method should begin to look for the previous 

    System.Windows.Forms.DataGridViewRow.

  

   includeFilter: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values.

   Returns: The index of the previous System.Windows.Forms.DataGridViewRow that has the attributes specified 

    by includeFilter; -1 if no row is found.
  """
  pass
 def GetRowCount(self,includeFilter):
  """
  GetRowCount(self: DataGridViewRowCollection,includeFilter: DataGridViewElementStates) -> int

  

   Returns the number of System.Windows.Forms.DataGridViewRow objects in the collection that meet 

    the specified criteria.

  

  

   includeFilter: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values.

   Returns: The number of System.Windows.Forms.DataGridViewRow objects in the 

    System.Windows.Forms.DataGridViewRowCollection that have the attributes specified by 

    includeFilter.
  """
  pass
 def GetRowsHeight(self,includeFilter):
  """
  GetRowsHeight(self: DataGridViewRowCollection,includeFilter: DataGridViewElementStates) -> int

  

   Returns the cumulative height of the System.Windows.Forms.DataGridViewRow objects that meet the 

    specified criteria.

  

  

   includeFilter: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values.

   Returns: The cumulative height of System.Windows.Forms.DataGridViewRow objects in the 

    System.Windows.Forms.DataGridViewRowCollection that have the attributes specified by 

    includeFilter.
  """
  pass
 def GetRowState(self,rowIndex):
  """
  GetRowState(self: DataGridViewRowCollection,rowIndex: int) -> DataGridViewElementStates

  

   Gets the state of the row with the specified index.

  

   rowIndex: The index of the row.

   Returns: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values indicating the 

    state of the specified row.
  """
  pass
 def IndexOf(self,dataGridViewRow):
  """
  IndexOf(self: DataGridViewRowCollection,dataGridViewRow: DataGridViewRow) -> int

  

   Returns the index of a specified item in the collection.

  

   dataGridViewRow: The System.Windows.Forms.DataGridViewRow to locate in the 

    System.Windows.Forms.DataGridViewRowCollection.

  

   Returns: The index of value if it is a System.Windows.Forms.DataGridViewRow found in the 

    System.Windows.Forms.DataGridViewRowCollection; otherwise,-1.
  """
  pass
 def Insert(self,rowIndex,*__args):
  """
  Insert(self: DataGridViewRowCollection,rowIndex: int,count: int)

   Inserts the specified number of rows into the collection at the specified location.

  

   rowIndex: The position at which to insert the rows.

   count: The number of rows to insert into the System.Windows.Forms.DataGridViewRowCollection.

  Insert(self: DataGridViewRowCollection,rowIndex: int,dataGridViewRow: DataGridViewRow)

   Inserts the specified System.Windows.Forms.DataGridViewRow into the collection.

  

   rowIndex: The position at which to insert the row.

   dataGridViewRow: The System.Windows.Forms.DataGridViewRow to insert into the 

    System.Windows.Forms.DataGridViewRowCollection.

  

  Insert(self: DataGridViewRowCollection,rowIndex: int,*values: Array[object])

   Inserts a row into the collection at the specified position,and populates the cells with the 

    specified objects.

  

  

   rowIndex: The position at which to insert the row.

   values: A variable number of objects that populate the cells of the new row.
  """
  pass
 def InsertCopies(self,indexSource,indexDestination,count):
  """
  InsertCopies(self: DataGridViewRowCollection,indexSource: int,indexDestination: int,count: int)

   Inserts rows into the collection at the specified position.

  

   indexSource: The index of the System.Windows.Forms.DataGridViewRow on which to base the new rows.

   indexDestination: The position at which to insert the rows.

   count: The number of System.Windows.Forms.DataGridViewRow objects to add to the 

    System.Windows.Forms.DataGridViewRowCollection.
  """
  pass
 def InsertCopy(self,indexSource,indexDestination):
  """
  InsertCopy(self: DataGridViewRowCollection,indexSource: int,indexDestination: int)

   Inserts a row into the collection at the specified position,based on the row at specified 

    position.

  

  

   indexSource: The index of the row on which to base the new row.

   indexDestination: The position at which to insert the row.
  """
  pass
 def InsertRange(self,rowIndex,dataGridViewRows):
  """
  InsertRange(self: DataGridViewRowCollection,rowIndex: int,*dataGridViewRows: Array[DataGridViewRow])

   Inserts the System.Windows.Forms.DataGridViewRow objects into the collection at the specified 

    position.

  

  

   rowIndex: The position at which to insert the rows.

   dataGridViewRows: An array of System.Windows.Forms.DataGridViewRow objects to add to the 

    System.Windows.Forms.DataGridViewRowCollection.
  """
  pass
 def OnCollectionChanged(self,*args):
  """
  OnCollectionChanged(self: DataGridViewRowCollection,e: CollectionChangeEventArgs)

   Raises the System.Windows.Forms.DataGridViewRowCollection.CollectionChanged event.

  

   e: A System.ComponentModel.CollectionChangeEventArgs that contains the event data.
  """
  pass
 def Remove(self,dataGridViewRow):
  """
  Remove(self: DataGridViewRowCollection,dataGridViewRow: DataGridViewRow)

   Removes the row from the collection.

  

   dataGridViewRow: The row to remove from the System.Windows.Forms.DataGridViewRowCollection.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: DataGridViewRowCollection,index: int)

   Removes the row at the specified position from the collection.

  

   index: The position of the row to remove.
  """
  pass
 def SharedRow(self,rowIndex):
  """
  SharedRow(self: DataGridViewRowCollection,rowIndex: int) -> DataGridViewRow

  

   Returns the System.Windows.Forms.DataGridViewRow at the specified index.

  

   rowIndex: The index of the System.Windows.Forms.DataGridViewRow to get.

   Returns: The System.Windows.Forms.DataGridViewRow positioned at the specified index.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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
 @staticmethod
 def __new__(self,dataGridView):
  """ __new__(cls: type,dataGridView: DataGridView) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of rows in the collection.



Get: Count(self: DataGridViewRowCollection) -> int



"""

 DataGridView=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.DataGridView that owns the collection.



"""

 List=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an array of System.Windows.Forms.DataGridViewRow objects.



"""


 CollectionChanged=None

