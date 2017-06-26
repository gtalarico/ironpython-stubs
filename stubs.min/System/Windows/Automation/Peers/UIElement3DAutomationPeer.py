class UIElement3DAutomationPeer(AutomationPeer):
    """
    Exposes System.Windows.UIElement3D types to UI Automation.
    
    UIElement3DAutomationPeer(owner: UIElement3D)
    """
    @staticmethod
    def CreatePeerForElement(element):
        """
        CreatePeerForElement(element: UIElement3D) -> AutomationPeer
        
            Creates a System.Windows.Automation.Peers.UIElement3DAutomationPeer for the specified System.Windows.UIElement3D.
        
            element: The System.Windows.UIElement3D that is associated with this System.Windows.Automation.Peers.UIElement3DAutomationPeer.
            Returns: A  System.Windows.Automation.Peers.UIElement3DAutomationPeer for the specified System.Windows.UIElement3D.
        """
        pass

    @staticmethod
    def FromElement(element):
        """
        FromElement(element: UIElement3D) -> AutomationPeer
        
            Returns the System.Windows.Automation.Peers.UIElement3DAutomationPeer for the specified System.Windows.UIElement3D.
        
            element: The System.Windows.UIElement3D that is associated with this System.Windows.Automation.Peers.UIElement3DAutomationPeer.
            Returns: The System.Windows.Automation.Peers.UIElement3DAutomationPeer, or null if the System.Windows.Automation.Peers.UIElement3DAutomationPeer was not created by the 
             System.Windows.Automation.Peers.UIElement3DAutomationPeer.CreatePeerForElement(System.Windows.UIElement3D) method.
        """
        pass

    def GetPattern(self, patternInterface):
        """
        GetPattern(self: UIElement3DAutomationPeer, patternInterface: PatternInterface) -> object
        
            Returns the control pattern for the System.Windows.UIElement3D that is associated with this System.Windows.Automation.Peers.UIElement3DAutomationPeer.
        
            patternInterface: One of the enumeration values.
            Returns: An object that implements the System.Windows.Automation.Provider.ISynchronizedInputProvider interface if patternInterface is System.Windows.Automation.Peers.PatternInterface.SynchronizedInput; otherwise, 
             null.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, owner):
        """ __new__(cls: type, owner: UIElement3D) """
        pass

    IsHwndHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.UIElement3D that is associated with this System.Windows.Automation.Peers.UIElement3DAutomationPeer.

Get: Owner(self: UIElement3DAutomationPeer) -> UIElement3D

"""


