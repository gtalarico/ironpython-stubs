class FamilySizeTable(object, IDisposable):
    """ Contains size information for a family. """
    def AsValueString(self, row, column):
        """
        AsValueString(self: FamilySizeTable, row: int, column: int) -> str
        
            Gets the table cell value as a string.
        
            row: The table row.
            column: The table column.
            Returns: The table cell value as a string.
        """
        pass

    def Dispose(self):
        """ Dispose(self: FamilySizeTable) """
        pass

    def GetColumnHeader(self, index):
        """
        GetColumnHeader(self: FamilySizeTable, index: int) -> FamilySizeTableColumn
        
            Gets a column of the table at at given index.
        
            index: Index of the column.
            Returns: The column at the given index.
        """
        pass

    def IsValidColumnIndex(self, index):
        """
        IsValidColumnIndex(self: FamilySizeTable, index: int) -> bool
        
            Checks if the column index is valid.
        
            index: The index of the column.
            Returns: True if the column index is valid, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FamilySizeTable, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FamilySizeTable) -> bool

"""

    NumberOfColumns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of columns in the table.

Get: NumberOfColumns(self: FamilySizeTable) -> int

"""

    NumberOfRows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of rows in the table.

Get: NumberOfRows(self: FamilySizeTable) -> int

"""


