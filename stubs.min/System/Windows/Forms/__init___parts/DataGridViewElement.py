class DataGridViewElement(object):
    """
    Provides the base class for elements of a System.Windows.Forms.DataGridView control.
    
    DataGridViewElement()
    """
    def OnDataGridViewChanged(self, *args): #cannot find CLR method
        """
        OnDataGridViewChanged(self: DataGridViewElement)
            Called when the element is associated with a different System.Windows.Forms.DataGridView.
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

    DataGridView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Forms.DataGridView control associated with this element.

Get: DataGridView(self: DataGridViewElement) -> DataGridView

"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the user interface (UI) state of the element.

Get: State(self: DataGridViewElement) -> DataGridViewElementStates

"""


