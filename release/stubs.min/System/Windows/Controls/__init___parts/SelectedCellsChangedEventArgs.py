class SelectedCellsChangedEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Controls.DataGrid.SelectedCellsChanged event.

 

 SelectedCellsChangedEventArgs(addedCells: List[DataGridCellInfo],removedCells: List[DataGridCellInfo])

 SelectedCellsChangedEventArgs(addedCells: ReadOnlyCollection[DataGridCellInfo],removedCells: ReadOnlyCollection[DataGridCellInfo])
 """
 @staticmethod
 def __new__(self,addedCells,removedCells):
  """
  __new__(cls: type,addedCells: List[DataGridCellInfo],removedCells: List[DataGridCellInfo])

  __new__(cls: type,addedCells: ReadOnlyCollection[DataGridCellInfo],removedCells: ReadOnlyCollection[DataGridCellInfo])
  """
  pass
 AddedCells=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the cells that were added to the selection.



Get: AddedCells(self: SelectedCellsChangedEventArgs) -> IList[DataGridCellInfo]



"""

 RemovedCells=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of cells removed from the selection.



Get: RemovedCells(self: SelectedCellsChangedEventArgs) -> IList[DataGridCellInfo]



"""


