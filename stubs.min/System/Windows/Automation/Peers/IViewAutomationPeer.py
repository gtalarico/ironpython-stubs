class IViewAutomationPeer:
    """ Allows a customized view of a System.Windows.Controls.ListView that derives from System.Windows.Controls.ViewBase to implement automation peer features that are specific to the custom view. """
    def CreateItemAutomationPeer(self, item):
        """
        CreateItemAutomationPeer(self: IViewAutomationPeer, item: object) -> ItemAutomationPeer
        
            Creates a new instance of the System.Windows.Automation.Peers.ItemAutomationPeer class.
        
            item: The System.Windows.Controls.ListViewItem that is associated with the System.Windows.Controls.ListView that is used by this System.Windows.Automation.Peers.IViewAutomationPeer.
            Returns: The new System.Windows.Automation.Peers.ItemAutomationPeer instance.
        """
        pass

    def GetAutomationControlType(self):
        """
        GetAutomationControlType(self: IViewAutomationPeer) -> AutomationControlType
        
            Gets the control type for the element that is associated with this System.Windows.Automation.Peers.IViewAutomationPeer.
            Returns: A value in the System.Windows.Automation.Peers.AutomationControlType enumeration.
        """
        pass

    def GetChildren(self, children):
        """ GetChildren(self: IViewAutomationPeer, children: List[AutomationPeer]) -> List[AutomationPeer] """
        pass

    def GetPattern(self, patternInterface):
        """
        GetPattern(self: IViewAutomationPeer, patternInterface: PatternInterface) -> object
        
            Gets the control pattern that is associated with the specified patternInterface.
        
            patternInterface: A value in the enumeration.
            Returns: Return the object that implements the control pattern. If this method returns null, the return value from 
             System.Windows.Automation.Peers.IViewAutomationPeer.GetPattern(System.Windows.Automation.Peers.PatternInterface) is used.
        """
        pass

    def ItemsChanged(self, e):
        """
        ItemsChanged(self: IViewAutomationPeer, e: NotifyCollectionChangedEventArgs)
            Called by System.Windows.Controls.ListView when the collection of items changes.
        
            e: A System.Collections.Specialized.NotifyCollectionChangedEventArgs that contains the event data.
        """
        pass

    def ViewDetached(self):
        """
        ViewDetached(self: IViewAutomationPeer)
            Called when the custom view is no longer applied to the System.Windows.Controls.ListView.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

