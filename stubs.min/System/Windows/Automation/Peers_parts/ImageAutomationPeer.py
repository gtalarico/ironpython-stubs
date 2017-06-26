class ImageAutomationPeer(FrameworkElementAutomationPeer):
    """
    Exposes System.Windows.Controls.Image types to UI Automation.
    
    ImageAutomationPeer(owner: Image)
    """
    @staticmethod # known case of __new__
    def __new__(self, owner):
        """ __new__(cls: type, owner: Image) """
        pass

    IsHwndHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


