class GroupItemAutomationPeer(FrameworkElementAutomationPeer):
    """
    Exposes System.Windows.Controls.GroupItem types to UI Automation.
    
    GroupItemAutomationPeer(owner: GroupItem)
    """
    def GetPattern(self, patternInterface):
        """ GetPattern(self: GroupItemAutomationPeer, patternInterface: PatternInterface) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, owner):
        """ __new__(cls: type, owner: GroupItem) """
        pass

    IsHwndHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


