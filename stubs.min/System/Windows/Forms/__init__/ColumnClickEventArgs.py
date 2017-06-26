class ColumnClickEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Forms.ListView.ColumnClick event.
    
    ColumnClickEventArgs(column: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, column):
        """ __new__(cls: type, column: int) """
        pass

    Column = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the zero-based index of the column that is clicked.

Get: Column(self: ColumnClickEventArgs) -> int

"""


