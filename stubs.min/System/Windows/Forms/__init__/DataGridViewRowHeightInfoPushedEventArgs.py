class DataGridViewRowHeightInfoPushedEventArgs(HandledEventArgs):
    """ Provides data for the System.Windows.Forms.DataGridView.RowHeightInfoPushed event of a System.Windows.Forms.DataGridView. """
    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the height of the row the event occurred for.

Get: Height(self: DataGridViewRowHeightInfoPushedEventArgs) -> int

"""

    MinimumHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the minimum height of the row the event occurred for.

Get: MinimumHeight(self: DataGridViewRowHeightInfoPushedEventArgs) -> int

"""

    RowIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of the row the event occurred for.

Get: RowIndex(self: DataGridViewRowHeightInfoPushedEventArgs) -> int

"""


