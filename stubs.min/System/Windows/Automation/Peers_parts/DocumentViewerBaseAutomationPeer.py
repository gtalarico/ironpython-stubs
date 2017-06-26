class DocumentViewerBaseAutomationPeer(FrameworkElementAutomationPeer):
    """
    Exposes System.Windows.Controls.Primitives.DocumentViewerBase types to UI Automation.
    
    DocumentViewerBaseAutomationPeer(owner: DocumentViewerBase)
    """
    def GetPattern(self, patternInterface):
        """
        GetPattern(self: DocumentViewerBaseAutomationPeer, patternInterface: PatternInterface) -> object
        
            Gets the control pattern for the System.Windows.Controls.Primitives.DocumentViewerBase that is associated with this System.Windows.Automation.Peers.DocumentViewerBaseAutomationPeer.
        
            patternInterface: One of the enumeration values.
            Returns: If patternInterface is System.Windows.Automation.Peers.PatternInterface.Text, this method returns an System.Windows.Automation.Provider.ITextProvider reference.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, owner):
        """ __new__(cls: type, owner: DocumentViewerBase) """
        pass

    IsHwndHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


