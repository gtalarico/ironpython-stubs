class AutoResizedEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Interop.HwndSource.AutoResized event raised by System.Windows.Interop.HwndSource.
    
    AutoResizedEventArgs(size: Size)
    """
    @staticmethod # known case of __new__
    def __new__(self, size):
        """ __new__(cls: type, size: Size) """
        pass

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the new size of the window after the auto resize operation.

Get: Size(self: AutoResizedEventArgs) -> Size

"""


