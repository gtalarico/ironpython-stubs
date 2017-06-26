class DataObjectEventArgs(RoutedEventArgs):
    """ Provides an abstract base class for events associated with the System.Windows.DataObject class. """
    def CancelCommand(self):
        """
        CancelCommand(self: DataObjectEventArgs)
            Cancels the associated command or operation.
        """
        pass

    CommandCancelled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the associated command or operation has been canceled.

Get: CommandCancelled(self: DataObjectEventArgs) -> bool

"""

    IsDragDrop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the associated event is part of a drag-and-drop operation.

Get: IsDragDrop(self: DataObjectEventArgs) -> bool

"""


