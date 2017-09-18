class DataGridViewColumnStateChangedEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.DataGridView.ColumnStateChanged event.

 

 DataGridViewColumnStateChangedEventArgs(dataGridViewColumn: DataGridViewColumn,stateChanged: DataGridViewElementStates)
 """
 @staticmethod
 def __new__(self,dataGridViewColumn,stateChanged):
  """ __new__(cls: type,dataGridViewColumn: DataGridViewColumn,stateChanged: DataGridViewElementStates) """
  pass
 Column=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the column whose state changed.



Get: Column(self: DataGridViewColumnStateChangedEventArgs) -> DataGridViewColumn



"""

 StateChanged=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the new column state.



Get: StateChanged(self: DataGridViewColumnStateChangedEventArgs) -> DataGridViewElementStates



"""


