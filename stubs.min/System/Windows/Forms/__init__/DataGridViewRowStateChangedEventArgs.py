class DataGridViewRowStateChangedEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Forms.DataGridView.RowStateChanged event of a System.Windows.Forms.DataGridView.
    
    DataGridViewRowStateChangedEventArgs(dataGridViewRow: DataGridViewRow, stateChanged: DataGridViewElementStates)
    """
    @staticmethod # known case of __new__
    def __new__(self, dataGridViewRow, stateChanged):
        """ __new__(cls: type, dataGridViewRow: DataGridViewRow, stateChanged: DataGridViewElementStates) """
        pass

    Row = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Forms.DataGridViewRow that has a changed state.

Get: Row(self: DataGridViewRowStateChangedEventArgs) -> DataGridViewRow

"""

    StateChanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the state that has changed on the row.

Get: StateChanged(self: DataGridViewRowStateChangedEventArgs) -> DataGridViewElementStates

"""


