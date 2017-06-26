class ToolBarAutomationPeer(FrameworkElementAutomationPeer):
    """
    Exposes System.Windows.Controls.ToolBar types to UI Automation.
    
    ToolBarAutomationPeer(owner: ToolBar)
    """
    @staticmethod # known case of __new__
    def __new__(self, owner):
        """ __new__(cls: type, owner: ToolBar) """
        pass

    IsHwndHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


