class DataGridViewTextBoxColumn(DataGridViewColumn, ICloneable, IDisposable, IComponent):
    """
    Hosts a collection of System.Windows.Forms.DataGridViewTextBoxCell cells.
    
    DataGridViewTextBoxColumn()
    """
    def Dispose(self):
        """
        Dispose(self: DataGridViewColumn, disposing: bool)
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def OnDataGridViewChanged(self, *args): #cannot find CLR method
        """
        OnDataGridViewChanged(self: DataGridViewBand)
            Called when the band is associated with a different System.Windows.Forms.DataGridView.
        """
        pass

    def RaiseCellClick(self, *args): #cannot find CLR method
        """
        RaiseCellClick(self: DataGridViewElement, e: DataGridViewCellEventArgs)
            Raises the System.Windows.Forms.DataGridView.CellClick event.
        
            e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
        """
        pass

    def RaiseCellContentClick(self, *args): #cannot find CLR method
        """
        RaiseCellContentClick(self: DataGridViewElement, e: DataGridViewCellEventArgs)
            Raises the System.Windows.Forms.DataGridView.CellContentClick event.
        
            e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
        """
        pass

    def RaiseCellContentDoubleClick(self, *args): #cannot find CLR method
        """
        RaiseCellContentDoubleClick(self: DataGridViewElement, e: DataGridViewCellEventArgs)
            Raises the System.Windows.Forms.DataGridView.CellContentDoubleClick event.
        
            e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
        """
        pass

    def RaiseCellValueChanged(self, *args): #cannot find CLR method
        """
        RaiseCellValueChanged(self: DataGridViewElement, e: DataGridViewCellEventArgs)
            Raises the System.Windows.Forms.DataGridView.CellValueChanged event.
        
            e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
        """
        pass

    def RaiseDataError(self, *args): #cannot find CLR method
        """
        RaiseDataError(self: DataGridViewElement, e: DataGridViewDataErrorEventArgs)
            Raises the System.Windows.Forms.DataGridView.DataError event.
        
            e: A System.Windows.Forms.DataGridViewDataErrorEventArgs that contains the event data.
        """
        pass

    def RaiseMouseWheel(self, *args): #cannot find CLR method
        """
        RaiseMouseWheel(self: DataGridViewElement, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseWheel event.
        
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def ToString(self):
        """
        ToString(self: DataGridViewTextBoxColumn) -> str
            Returns: A System.String that describes the column.
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

    def __str__(self, *args): #cannot find CLR method
        pass

    CellTemplate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the template used to model cell appearance.

Get: CellTemplate(self: DataGridViewTextBoxColumn) -> DataGridViewCell

Set: CellTemplate(self: DataGridViewTextBoxColumn) = value
"""

    HeaderCellCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the header cell of the System.Windows.Forms.DataGridViewBand.

"""

    IsRow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the band represents a row.

"""

    MaxInputLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum number of characters that can be entered into the text box.

Get: MaxInputLength(self: DataGridViewTextBoxColumn) -> int

Set: MaxInputLength(self: DataGridViewTextBoxColumn) = value
"""

    SortMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the sort mode for the column.

Get: SortMode(self: DataGridViewTextBoxColumn) -> DataGridViewColumnSortMode

Set: SortMode(self: DataGridViewTextBoxColumn) = value
"""


