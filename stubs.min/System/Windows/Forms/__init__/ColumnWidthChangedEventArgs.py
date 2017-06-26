class ColumnWidthChangedEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Forms.ListView.ColumnWidthChanged event.
    
    ColumnWidthChangedEventArgs(columnIndex: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, columnIndex):
        """ __new__(cls: type, columnIndex: int) """
        pass

    ColumnIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the column index for the column whose width is being changed.

Get: ColumnIndex(self: ColumnWidthChangedEventArgs) -> int

"""


