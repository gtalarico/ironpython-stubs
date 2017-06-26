class ToolStripDropDownClosingEventArgs(CancelEventArgs):
    """
    Provides data for the System.Windows.Forms.ToolStripDropDown.Closing event.
    
    ToolStripDropDownClosingEventArgs(reason: ToolStripDropDownCloseReason)
    """
    @staticmethod # known case of __new__
    def __new__(self, reason):
        """ __new__(cls: type, reason: ToolStripDropDownCloseReason) """
        pass

    CloseReason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the reason that the System.Windows.Forms.ToolStripDropDown is closing.

Get: CloseReason(self: ToolStripDropDownClosingEventArgs) -> ToolStripDropDownCloseReason

"""


