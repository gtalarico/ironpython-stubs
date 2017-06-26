class DataGridViewCellParsingEventArgs(ConvertEventArgs):
    """
    Provides data for the System.Windows.Forms.DataGridView.CellParsing event of a System.Windows.Forms.DataGridView control.
    
    DataGridViewCellParsingEventArgs(rowIndex: int, columnIndex: int, value: object, desiredType: Type, inheritedCellStyle: DataGridViewCellStyle)
    """
    @staticmethod # known case of __new__
    def __new__(self, rowIndex, columnIndex, value, desiredType, inheritedCellStyle):
        """ __new__(cls: type, rowIndex: int, columnIndex: int, value: object, desiredType: Type, inheritedCellStyle: DataGridViewCellStyle) """
        pass

    ColumnIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the column index of the cell data that requires parsing.

Get: ColumnIndex(self: DataGridViewCellParsingEventArgs) -> int

"""

    InheritedCellStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the style applied to the edited cell.

Get: InheritedCellStyle(self: DataGridViewCellParsingEventArgs) -> DataGridViewCellStyle

Set: InheritedCellStyle(self: DataGridViewCellParsingEventArgs) = value
"""

    ParsingApplied = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether a cell's value has been successfully parsed.

Get: ParsingApplied(self: DataGridViewCellParsingEventArgs) -> bool

Set: ParsingApplied(self: DataGridViewCellParsingEventArgs) = value
"""

    RowIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the row index of the cell that requires parsing.

Get: RowIndex(self: DataGridViewCellParsingEventArgs) -> int

"""


