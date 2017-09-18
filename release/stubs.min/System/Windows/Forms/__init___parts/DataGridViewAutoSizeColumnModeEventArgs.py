class DataGridViewAutoSizeColumnModeEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.DataGridView.AutoSizeColumnModeChanged event.

 

 DataGridViewAutoSizeColumnModeEventArgs(dataGridViewColumn: DataGridViewColumn,previousMode: DataGridViewAutoSizeColumnMode)
 """
 @staticmethod
 def __new__(self,dataGridViewColumn,previousMode):
  """ __new__(cls: type,dataGridViewColumn: DataGridViewColumn,previousMode: DataGridViewAutoSizeColumnMode) """
  pass
 Column=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the column with the System.Windows.Forms.DataGridViewColumn.AutoSizeMode property that changed.



Get: Column(self: DataGridViewAutoSizeColumnModeEventArgs) -> DataGridViewColumn



"""

 PreviousMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the previous value of the System.Windows.Forms.DataGridViewColumn.AutoSizeMode property of the column.



Get: PreviousMode(self: DataGridViewAutoSizeColumnModeEventArgs) -> DataGridViewAutoSizeColumnMode



"""


