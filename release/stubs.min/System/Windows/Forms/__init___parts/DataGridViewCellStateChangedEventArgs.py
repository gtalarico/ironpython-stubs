class DataGridViewCellStateChangedEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.DataGridView.CellStateChanged event.

 

 DataGridViewCellStateChangedEventArgs(dataGridViewCell: DataGridViewCell,stateChanged: DataGridViewElementStates)
 """
 @staticmethod
 def __new__(self,dataGridViewCell,stateChanged):
  """ __new__(cls: type,dataGridViewCell: DataGridViewCell,stateChanged: DataGridViewElementStates) """
  pass
 Cell=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.DataGridViewCell that has a changed state.



Get: Cell(self: DataGridViewCellStateChangedEventArgs) -> DataGridViewCell



"""

 StateChanged=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the state that has changed on the cell.



Get: StateChanged(self: DataGridViewCellStateChangedEventArgs) -> DataGridViewElementStates



"""


