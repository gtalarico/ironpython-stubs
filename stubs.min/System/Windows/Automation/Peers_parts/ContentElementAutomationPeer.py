class ContentElementAutomationPeer(AutomationPeer):
    """
    Exposes System.Windows.ContentElement types to UI Automation.
    
    ContentElementAutomationPeer(owner: ContentElement)
    """
    @staticmethod
    def CreatePeerForElement(element):
        """
        CreatePeerForElement(element: ContentElement) -> AutomationPeer
        
            Creates a System.Windows.Automation.Peers.ContentElementAutomationPeer for the specified System.Windows.ContentElement.
        
            element: The System.Windows.ContentElement that is associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer.
            Returns: The System.Windows.Automation.Peers.ContentElementAutomationPeer for the specified System.Windows.ContentElement.
        """
        pass

    @staticmethod
    def FromElement(element):
        """
        FromElement(element: ContentElement) -> AutomationPeer
        
            Gets the System.Windows.Automation.Peers.ContentElementAutomationPeer for the specified System.Windows.ContentElement.
        
            element: The System.Windows.ContentElement that is associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer.
            Returns: The System.Windows.Automation.Peers.ContentElementAutomationPeer for the specified System.Windows.ContentElement, or null if the System.Windows.Automation.Peers.ContentElementAutomationPeer has not been 
             created by the System.Windows.Automation.Peers.ContentElementAutomationPeer.CreatePeerForElement(System.Windows.ContentElement) method.
        """
        pass

    def GetPattern(self, patternInterface):
        """
        GetPattern(self: ContentElementAutomationPeer, patternInterface: PatternInterface) -> object
        
            Gets the control pattern for the System.Windows.ContentElement that is associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer.
        
            patternInterface: One of the enumeration values.
            Returns: An object that implements the System.Windows.Automation.Provider.ISynchronizedInputProvider interface if patternInterface is System.Windows.Automation.Peers.PatternInterface.SynchronizedInput; otherwise, 
             null.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, owner):
        """ __new__(cls: type, owner: ContentElement) """
        pass

    IsHwndHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.ContentElement that is associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer.

Get: Owner(self: ContentElementAutomationPeer) -> ContentElement

"""


