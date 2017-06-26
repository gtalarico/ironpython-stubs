class QueryCursorEventArgs(MouseEventArgs):
    """
    Provides data for the System.Windows.Input.Mouse.QueryCursor event.
    
    QueryCursorEventArgs(mouse: MouseDevice, timestamp: int)
    QueryCursorEventArgs(mouse: MouseDevice, timestamp: int, stylusDevice: StylusDevice)
    """
    @staticmethod # known case of __new__
    def __new__(self, mouse, timestamp, stylusDevice=None):
        """
        __new__(cls: type, mouse: MouseDevice, timestamp: int)
        __new__(cls: type, mouse: MouseDevice, timestamp: int, stylusDevice: StylusDevice)
        """
        pass

    Cursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the cursor associated with this event.

Get: Cursor(self: QueryCursorEventArgs) -> Cursor

Set: Cursor(self: QueryCursorEventArgs) = value
"""


