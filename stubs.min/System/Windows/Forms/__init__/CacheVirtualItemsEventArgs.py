class CacheVirtualItemsEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Forms.ListView.CacheVirtualItems event.
    
    CacheVirtualItemsEventArgs(startIndex: int, endIndex: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, startIndex, endIndex):
        """ __new__(cls: type, startIndex: int, endIndex: int) """
        pass

    EndIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the ending index for the range of values needed by a System.Windows.Forms.ListView control in virtual mode.

Get: EndIndex(self: CacheVirtualItemsEventArgs) -> int

"""

    StartIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the starting index for a range of values needed by a System.Windows.Forms.ListView control in virtual mode.

Get: StartIndex(self: CacheVirtualItemsEventArgs) -> int

"""


