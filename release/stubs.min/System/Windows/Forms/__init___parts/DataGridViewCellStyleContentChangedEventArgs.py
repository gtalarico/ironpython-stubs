class DataGridViewCellStyleContentChangedEventArgs(EventArgs):
 """ Provides data for the System.Windows.Forms.DataGridView.CellStyleContentChanged event. """
 CellStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the changed System.Windows.Forms.DataGridViewCellStyle.



Get: CellStyle(self: DataGridViewCellStyleContentChangedEventArgs) -> DataGridViewCellStyle



"""

 CellStyleScope=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the scope that is affected by the changed cell style.



Get: CellStyleScope(self: DataGridViewCellStyleContentChangedEventArgs) -> DataGridViewCellStyleScopes



"""


