class DataGridViewCellContextMenuStripNeededEventArgs(DataGridViewCellEventArgs):
    """
    Provides data for the System.Windows.Forms.DataGridView.CellContextMenuStripNeeded event.
    
    DataGridViewCellContextMenuStripNeededEventArgs(columnIndex: int, rowIndex: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, columnIndex, rowIndex):
        """ __new__(cls: type, columnIndex: int, rowIndex: int) """
        pass

    ContextMenuStrip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the shortcut menu for the cell that raised the System.Windows.Forms.DataGridView.CellContextMenuStripNeeded event.

Get: ContextMenuStrip(self: DataGridViewCellContextMenuStripNeededEventArgs) -> ContextMenuStrip

Set: ContextMenuStrip(self: DataGridViewCellContextMenuStripNeededEventArgs) = value
"""


