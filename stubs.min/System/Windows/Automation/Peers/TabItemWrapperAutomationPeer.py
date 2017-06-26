class TabItemWrapperAutomationPeer(FrameworkElementAutomationPeer):
    """
    Exposes the System.Windows.UIElement subtree for the data items in a System.Windows.Controls.TabControl to UI Automation.
    
    TabItemWrapperAutomationPeer(owner: TabItem)
    """
    @staticmethod # known case of __new__
    def __new__(self, owner):
        """ __new__(cls: type, owner: TabItem) """
        pass

    IsHwndHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


