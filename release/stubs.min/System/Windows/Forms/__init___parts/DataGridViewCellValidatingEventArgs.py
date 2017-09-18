class DataGridViewCellValidatingEventArgs(CancelEventArgs):
 """ Provides data for the System.Windows.Forms.DataGridView.CellValidating event of a System.Windows.Forms.DataGridView control. """
 ColumnIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the column index of the cell that needs to be validated.



Get: ColumnIndex(self: DataGridViewCellValidatingEventArgs) -> int



"""

 FormattedValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the formatted contents of the cell that needs to be validated.



Get: FormattedValue(self: DataGridViewCellValidatingEventArgs) -> object



"""

 RowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the row index of the cell that needs to be validated.



Get: RowIndex(self: DataGridViewCellValidatingEventArgs) -> int



"""


