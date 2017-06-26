class ToolStripItemEventArgs(EventArgs):
    """
    Provides data for System.Windows.Forms.ToolStripItem events.
    
    ToolStripItemEventArgs(item: ToolStripItem)
    """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, item):
        """ __new__(cls: type, item: ToolStripItem) """
        pass

    Item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Windows.Forms.ToolStripItem for which to handle events.

Get: Item(self: ToolStripItemEventArgs) -> ToolStripItem

"""


