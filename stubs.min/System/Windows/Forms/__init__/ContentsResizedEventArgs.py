class ContentsResizedEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Forms.RichTextBox.ContentsResized event.
    
    ContentsResizedEventArgs(newRectangle: Rectangle)
    """
    @staticmethod # known case of __new__
    def __new__(self, newRectangle):
        """ __new__(cls: type, newRectangle: Rectangle) """
        pass

    NewRectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents the requested size of the System.Windows.Forms.RichTextBox control.

Get: NewRectangle(self: ContentsResizedEventArgs) -> Rectangle

"""


