class TextBoxData(RibbonItemData):
    """
    This class contains information necessary to construct a text box in the Ribbon.
    
    TextBoxData(name: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, name):
        """ __new__(cls: type, name: str) """
        pass

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The image of the TextBox.

Get: Image(self: TextBoxData) -> ImageSource

Set: Image(self: TextBoxData) = value
"""


