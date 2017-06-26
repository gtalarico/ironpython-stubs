class InvalidateEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Forms.Control.Invalidated event.
    
    InvalidateEventArgs(invalidRect: Rectangle)
    """
    @staticmethod # known case of __new__
    def __new__(self, invalidRect):
        """ __new__(cls: type, invalidRect: Rectangle) """
        pass

    InvalidRect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Drawing.Rectangle that contains the invalidated window area.

Get: InvalidRect(self: InvalidateEventArgs) -> Rectangle

"""


