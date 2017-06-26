class ItemCheckedEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Forms.ListView.ItemChecked event of the System.Windows.Forms.ListView control.
    
    ItemCheckedEventArgs(item: ListViewItem)
    """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, item):
        """ __new__(cls: type, item: ListViewItem) """
        pass

    Item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Forms.ListViewItem whose checked state is changing.

Get: Item(self: ItemCheckedEventArgs) -> ListViewItem

"""


