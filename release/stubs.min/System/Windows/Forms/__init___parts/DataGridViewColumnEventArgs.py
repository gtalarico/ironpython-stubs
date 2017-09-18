class DataGridViewColumnEventArgs(EventArgs):
 """
 Provides data for column-related events of a System.Windows.Forms.DataGridView.

 

 DataGridViewColumnEventArgs(dataGridViewColumn: DataGridViewColumn)
 """
 @staticmethod
 def __new__(self,dataGridViewColumn):
  """ __new__(cls: type,dataGridViewColumn: DataGridViewColumn) """
  pass
 Column=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the column that the event occurs for.



Get: Column(self: DataGridViewColumnEventArgs) -> DataGridViewColumn



"""


