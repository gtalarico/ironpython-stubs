class DocumentAutomationPeer(ContentTextAutomationPeer):
    """
    Exposes System.Windows.Automation.ControlType.Document�control types to UI Automation.
    
    DocumentAutomationPeer(owner: FrameworkContentElement)
    """
    def GetPattern(self, patternInterface):
        """
        GetPattern(self: DocumentAutomationPeer, patternInterface: PatternInterface) -> object
        
            Gets the control pattern for the System.Windows.FrameworkContentElement that is associated with this System.Windows.Automation.Peers.DocumentAutomationPeer.
        
            patternInterface: One of the enumeration values.
            Returns: If patternInterface is System.Windows.Automation.Peers.PatternInterface.Text, this method returns an System.Windows.Automation.Provider.ITextProvider.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, owner):
        """ __new__(cls: type, owner: FrameworkContentElement) """
        pass

    IsHwndHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


