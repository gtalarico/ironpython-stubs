class DataGridViewRowCancelEventArgs(CancelEventArgs):
 """
 Provides data for the System.Windows.Forms.DataGridView.UserDeletingRow event of a System.Windows.Forms.DataGridView.
 
 DataGridViewRowCancelEventArgs(dataGridViewRow: DataGridViewRow)
 """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return DataGridViewRowCancelEventArgs()

 @staticmethod
 def __new__(self,dataGridViewRow):
  """ __new__(cls: type,dataGridViewRow: DataGridViewRow) """
  pass
 Row=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the row that the user is deleting.

Get: Row(self: DataGridViewRowCancelEventArgs) -> DataGridViewRow

"""


