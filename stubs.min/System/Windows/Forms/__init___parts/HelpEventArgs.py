class HelpEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Forms.Control.HelpRequested event.
    
    HelpEventArgs(mousePos: Point)
    """
    @staticmethod # known case of __new__
    def __new__(self, mousePos):
        """ __new__(cls: type, mousePos: Point) """
        pass

    Handled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the help event was handled.

Get: Handled(self: HelpEventArgs) -> bool

Set: Handled(self: HelpEventArgs) = value
"""

    MousePos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the screen coordinates of the mouse pointer.

Get: MousePos(self: HelpEventArgs) -> Point

"""


