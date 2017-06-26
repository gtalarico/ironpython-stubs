class DataGridViewRowCancelEventArgs(CancelEventArgs):
    """
    Provides data for the System.Windows.Forms.DataGridView.UserDeletingRow event of a System.Windows.Forms.DataGridView.
    
    DataGridViewRowCancelEventArgs(dataGridViewRow: DataGridViewRow)
    """
    @staticmethod # known case of __new__
    def __new__(self, dataGridViewRow):
        """ __new__(cls: type, dataGridViewRow: DataGridViewRow) """
        pass

    Row = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the row that the user is deleting.

Get: Row(self: DataGridViewRowCancelEventArgs) -> DataGridViewRow

"""


