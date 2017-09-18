class DataGridViewRowErrorTextNeededEventArgs(EventArgs):
 """ Provides data for the System.Windows.Forms.DataGridView.RowErrorTextNeeded event of a System.Windows.Forms.DataGridView control. """
 ErrorText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the error text for the row.



Get: ErrorText(self: DataGridViewRowErrorTextNeededEventArgs) -> str



Set: ErrorText(self: DataGridViewRowErrorTextNeededEventArgs)=value

"""

 RowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the row that raised the System.Windows.Forms.DataGridView.RowErrorTextNeeded event.



Get: RowIndex(self: DataGridViewRowErrorTextNeededEventArgs) -> int



"""


