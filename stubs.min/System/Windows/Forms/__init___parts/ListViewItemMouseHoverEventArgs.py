class ListViewItemMouseHoverEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Forms.ListView.ItemMouseHover event.
    
    ListViewItemMouseHoverEventArgs(item: ListViewItem)
    """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, item):
        """ __new__(cls: type, item: ListViewItem) """
        pass

    Item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the item the mouse pointer is currently hovering over.

Get: Item(self: ListViewItemMouseHoverEventArgs) -> ListViewItem

"""


