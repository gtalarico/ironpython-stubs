class SelectedGridItemChangedEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Forms.PropertyGrid.SelectedGridItemChanged event of the System.Windows.Forms.PropertyGrid control.
    
    SelectedGridItemChangedEventArgs(oldSel: GridItem, newSel: GridItem)
    """
    @staticmethod # known case of __new__
    def __new__(self, oldSel, newSel):
        """ __new__(cls: type, oldSel: GridItem, newSel: GridItem) """
        pass

    NewSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the newly selected System.Windows.Forms.GridItem.

Get: NewSelection(self: SelectedGridItemChangedEventArgs) -> GridItem

"""

    OldSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the previously selected System.Windows.Forms.GridItem.

Get: OldSelection(self: SelectedGridItemChangedEventArgs) -> GridItem

"""


