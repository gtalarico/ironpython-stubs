class CurrentChangingEventArgs(EventArgs):
    """
    Provides information for the System.ComponentModel.ICollectionView.CurrentChanging event.
    
    CurrentChangingEventArgs()
    CurrentChangingEventArgs(isCancelable: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, isCancelable=None):
        """
        __new__(cls: type)
        __new__(cls: type, isCancelable: bool)
        """
        pass

    Cancel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to cancel the event.

Get: Cancel(self: CurrentChangingEventArgs) -> bool

Set: Cancel(self: CurrentChangingEventArgs) = value
"""

    IsCancelable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the event is cancelable.

Get: IsCancelable(self: CurrentChangingEventArgs) -> bool

"""


