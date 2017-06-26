class DataGridPreparingCellForEditEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Controls.DataGrid.PreparingCellForEdit event.
    
    DataGridPreparingCellForEditEventArgs(column: DataGridColumn, row: DataGridRow, editingEventArgs: RoutedEventArgs, editingElement: FrameworkElement)
    """
    @staticmethod # known case of __new__
    def __new__(self, column, row, editingEventArgs, editingElement):
        """ __new__(cls: type, column: DataGridColumn, row: DataGridRow, editingEventArgs: RoutedEventArgs, editingElement: FrameworkElement) """
        pass

    Column = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the column that contains the cell to be edited.

Get: Column(self: DataGridPreparingCellForEditEventArgs) -> DataGridColumn

"""

    EditingElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the element that the column displays for a cell in editing mode.

Get: EditingElement(self: DataGridPreparingCellForEditEventArgs) -> FrameworkElement

"""

    EditingEventArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets information about the user gesture that caused the cell to enter edit mode.

Get: EditingEventArgs(self: DataGridPreparingCellForEditEventArgs) -> RoutedEventArgs

"""

    Row = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the row that contains the cell to be edited.

Get: Row(self: DataGridPreparingCellForEditEventArgs) -> DataGridRow

"""


