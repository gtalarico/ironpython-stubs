class UIElementAutomationPeer(AutomationPeer):
    """
    Exposes System.Windows.UIElement types to UI Automation.
    
    UIElementAutomationPeer(owner: UIElement)
    """
    @staticmethod
    def CreatePeerForElement(element):
        """
        CreatePeerForElement(element: UIElement) -> AutomationPeer
        
            Creates a System.Windows.Automation.Peers.UIElementAutomationPeer for the specified System.Windows.UIElement.
        
            element: The System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer.
            Returns: A System.Windows.Automation.Peers.UIElementAutomationPeer.
        """
        pass

    @staticmethod
    def FromElement(element):
        """
        FromElement(element: UIElement) -> AutomationPeer
        
            Gets the System.Windows.Automation.Peers.UIElementAutomationPeer for the specified System.Windows.UIElement.
        
            element: The System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer.
            Returns: The System.Windows.Automation.Peers.UIElementAutomationPeer; or null, if the System.Windows.Automation.Peers.UIElementAutomationPeer was not created by the 
             System.Windows.Automation.Peers.UIElementAutomationPeer.CreatePeerForElement(System.Windows.UIElement) method.
        """
        pass

    def GetPattern(self, patternInterface):
        """
        GetPattern(self: UIElementAutomationPeer, patternInterface: PatternInterface) -> object
        
            Gets the control pattern for the System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer.
        
            patternInterface: A value from the enumeration.
            Returns: An object that implements the System.Windows.Automation.Provider.ISynchronizedInputProvider interface if patternInterface is System.Windows.Automation.Peers.PatternInterface.SynchronizedInput; otherwise, 
             null.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, owner):
        """ __new__(cls: type, owner: UIElement) """
        pass

    IsHwndHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer.

Get: Owner(self: UIElementAutomationPeer) -> UIElement

"""


