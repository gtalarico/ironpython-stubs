class DataGridViewRowEventArgs(EventArgs):
 """
 Provides data for row-related System.Windows.Forms.DataGridView events.

 

 DataGridViewRowEventArgs(dataGridViewRow: DataGridViewRow)
 """
 @staticmethod
 def __new__(self,dataGridViewRow):
  """ __new__(cls: type,dataGridViewRow: DataGridViewRow) """
  pass
 Row=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.DataGridViewRow associated with the event.



Get: Row(self: DataGridViewRowEventArgs) -> DataGridViewRow



"""


