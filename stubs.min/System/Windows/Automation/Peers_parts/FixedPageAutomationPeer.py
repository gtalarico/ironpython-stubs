class FixedPageAutomationPeer(FrameworkElementAutomationPeer):
    """
    Exposes System.Windows.Documents.FixedPage types to UI Automation.
    
    FixedPageAutomationPeer(owner: FixedPage)
    """
    @staticmethod # known case of __new__
    def __new__(self, owner):
        """ __new__(cls: type, owner: FixedPage) """
        pass

    IsHwndHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


