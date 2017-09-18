class DataGridViewRowHeightInfoNeededEventArgs(EventArgs):
 """ Provides data for the System.Windows.Forms.DataGridView.RowHeightInfoNeeded event of a System.Windows.Forms.DataGridView. """
 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of the row the event occurred for.



Get: Height(self: DataGridViewRowHeightInfoNeededEventArgs) -> int



Set: Height(self: DataGridViewRowHeightInfoNeededEventArgs)=value

"""

 MinimumHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the minimum height of the row the event occurred for.



Get: MinimumHeight(self: DataGridViewRowHeightInfoNeededEventArgs) -> int



Set: MinimumHeight(self: DataGridViewRowHeightInfoNeededEventArgs)=value

"""

 RowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the row associated with this System.Windows.Forms.DataGridViewRowHeightInfoNeededEventArgs.



Get: RowIndex(self: DataGridViewRowHeightInfoNeededEventArgs) -> int



"""


