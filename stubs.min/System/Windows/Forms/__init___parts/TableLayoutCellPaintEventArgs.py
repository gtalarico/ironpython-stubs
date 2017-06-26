class TableLayoutCellPaintEventArgs(PaintEventArgs, IDisposable):
    """
    Provides data for the System.Windows.Forms.TableLayoutPanel.CellPaint event.
    
    TableLayoutCellPaintEventArgs(g: Graphics, clipRectangle: Rectangle, cellBounds: Rectangle, column: int, row: int)
    """
    def Dispose(self):
        """
        Dispose(self: PaintEventArgs, disposing: bool)
            Releases the unmanaged resources used by the System.Windows.Forms.PaintEventArgs and optionally releases the managed resources.
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, g, clipRectangle, cellBounds, column, row):
        """ __new__(cls: type, g: Graphics, clipRectangle: Rectangle, cellBounds: Rectangle, column: int, row: int) """
        pass

    CellBounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size and location of the cell.

Get: CellBounds(self: TableLayoutCellPaintEventArgs) -> Rectangle

"""

    Column = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the column of the cell.

Get: Column(self: TableLayoutCellPaintEventArgs) -> int

"""

    Row = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the row of the cell.

Get: Row(self: TableLayoutCellPaintEventArgs) -> int

"""


