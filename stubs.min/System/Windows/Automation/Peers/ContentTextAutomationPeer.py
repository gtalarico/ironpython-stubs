class ContentTextAutomationPeer(FrameworkContentElementAutomationPeer):
    """ Represents a base class for exposing System.Windows.Automation.TextPattern types to UI Automation. """
    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, owner: FrameworkContentElement) """
        pass

    IsHwndHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


