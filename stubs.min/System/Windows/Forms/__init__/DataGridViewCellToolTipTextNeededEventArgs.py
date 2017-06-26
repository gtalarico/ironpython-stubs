class DataGridViewCellToolTipTextNeededEventArgs(DataGridViewCellEventArgs):
    """ Provides data for the System.Windows.Forms.DataGridView.CellToolTipTextNeeded event. """
    ToolTipText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the ToolTip text.

Get: ToolTipText(self: DataGridViewCellToolTipTextNeededEventArgs) -> str

Set: ToolTipText(self: DataGridViewCellToolTipTextNeededEventArgs) = value
"""


