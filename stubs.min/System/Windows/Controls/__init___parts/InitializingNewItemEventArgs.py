class InitializingNewItemEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Controls.DataGrid.InitializingNewItem event.
    
    InitializingNewItemEventArgs(newItem: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, newItem):
        """ __new__(cls: type, newItem: object) """
        pass

    NewItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the new item added to the System.Windows.Controls.DataGrid.

Get: NewItem(self: InitializingNewItemEventArgs) -> object

"""


