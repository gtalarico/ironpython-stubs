class StatusBarPanelClickEventArgs(MouseEventArgs):
    """
    Provides data for the System.Windows.Forms.StatusBar.PanelClick event.
    
    StatusBarPanelClickEventArgs(statusBarPanel: StatusBarPanel, button: MouseButtons, clicks: int, x: int, y: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, statusBarPanel, button, clicks, x, y):
        """ __new__(cls: type, statusBarPanel: StatusBarPanel, button: MouseButtons, clicks: int, x: int, y: int) """
        pass

    StatusBarPanel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Forms.StatusBarPanel to draw.

Get: StatusBarPanel(self: StatusBarPanelClickEventArgs) -> StatusBarPanel

"""


