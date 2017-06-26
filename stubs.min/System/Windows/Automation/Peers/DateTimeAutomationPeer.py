class DateTimeAutomationPeer(AutomationPeer, IGridItemProvider, ISelectionItemProvider, ITableItemProvider, IInvokeProvider, IVirtualizedItemProvider):
    """ Exposes System.Windows.Controls.Primitives.CalendarDayButton and System.Windows.Controls.Primitives.CalendarButton types to UI Automation. """
    def GetAcceleratorKeyCore(self, *args): #cannot find CLR method
        """ GetAcceleratorKeyCore(self: DateTimeAutomationPeer) -> str """
        pass

    def GetAccessKeyCore(self, *args): #cannot find CLR method
        """ GetAccessKeyCore(self: DateTimeAutomationPeer) -> str """
        pass

    def GetAutomationControlTypeCore(self, *args): #cannot find CLR method
        """ GetAutomationControlTypeCore(self: DateTimeAutomationPeer) -> AutomationControlType """
        pass

    def GetAutomationIdCore(self, *args): #cannot find CLR method
        """ GetAutomationIdCore(self: DateTimeAutomationPeer) -> str """
        pass

    def GetBoundingRectangleCore(self, *args): #cannot find CLR method
        """ GetBoundingRectangleCore(self: DateTimeAutomationPeer) -> Rect """
        pass

    def GetChildrenCore(self, *args): #cannot find CLR method
        """ GetChildrenCore(self: DateTimeAutomationPeer) -> List[AutomationPeer] """
        pass

    def GetClassNameCore(self, *args): #cannot find CLR method
        """ GetClassNameCore(self: DateTimeAutomationPeer) -> str """
        pass

    def GetClickablePointCore(self, *args): #cannot find CLR method
        """ GetClickablePointCore(self: DateTimeAutomationPeer) -> Point """
        pass

    def GetHelpTextCore(self, *args): #cannot find CLR method
        """ GetHelpTextCore(self: DateTimeAutomationPeer) -> str """
        pass

    def GetHostRawElementProviderCore(self, *args): #cannot find CLR method
        """
        GetHostRawElementProviderCore(self: AutomationPeer) -> HostedWindowWrapper
        
            Tells UI Automation where in the UI Automation tree to place the hwnd being hosted by a Windows Presentation Foundation (WPF) element.
            Returns: This method returns the hosted hwnd to UI Automation for controls that host hwnd objects.
        """
        pass

    def GetItemStatusCore(self, *args): #cannot find CLR method
        """ GetItemStatusCore(self: DateTimeAutomationPeer) -> str """
        pass

    def GetItemTypeCore(self, *args): #cannot find CLR method
        """ GetItemTypeCore(self: DateTimeAutomationPeer) -> str """
        pass

    def GetLabeledByCore(self, *args): #cannot find CLR method
        """ GetLabeledByCore(self: DateTimeAutomationPeer) -> AutomationPeer """
        pass

    def GetLocalizedControlTypeCore(self, *args): #cannot find CLR method
        """ GetLocalizedControlTypeCore(self: DateTimeAutomationPeer) -> str """
        pass

    def GetNameCore(self, *args): #cannot find CLR method
        """ GetNameCore(self: DateTimeAutomationPeer) -> str """
        pass

    def GetOrientationCore(self, *args): #cannot find CLR method
        """ GetOrientationCore(self: DateTimeAutomationPeer) -> AutomationOrientation """
        pass

    def GetPattern(self, patternInterface):
        """
        GetPattern(self: DateTimeAutomationPeer, patternInterface: PatternInterface) -> object
        
            Gets the control pattern implementation for this System.Windows.Automation.Peers.DateTimeAutomationPeer.
        
            patternInterface: The type of pattern implemented by the element to retrieve.
            Returns: The object that implements the pattern interface, or null if the specified pattern interface is not implemented by this peer.
        """
        pass

    def GetPeerFromPointCore(self, *args): #cannot find CLR method
        """ GetPeerFromPointCore(self: AutomationPeer, point: Point) -> AutomationPeer """
        pass

    def HasKeyboardFocusCore(self, *args): #cannot find CLR method
        """ HasKeyboardFocusCore(self: DateTimeAutomationPeer) -> bool """
        pass

    def IsContentElementCore(self, *args): #cannot find CLR method
        """ IsContentElementCore(self: DateTimeAutomationPeer) -> bool """
        pass

    def IsControlElementCore(self, *args): #cannot find CLR method
        """ IsControlElementCore(self: DateTimeAutomationPeer) -> bool """
        pass

    def IsEnabledCore(self, *args): #cannot find CLR method
        """ IsEnabledCore(self: DateTimeAutomationPeer) -> bool """
        pass

    def IsKeyboardFocusableCore(self, *args): #cannot find CLR method
        """ IsKeyboardFocusableCore(self: DateTimeAutomationPeer) -> bool """
        pass

    def IsOffscreenCore(self, *args): #cannot find CLR method
        """ IsOffscreenCore(self: DateTimeAutomationPeer) -> bool """
        pass

    def IsPasswordCore(self, *args): #cannot find CLR method
        """ IsPasswordCore(self: DateTimeAutomationPeer) -> bool """
        pass

    def IsRequiredForFormCore(self, *args): #cannot find CLR method
        """ IsRequiredForFormCore(self: DateTimeAutomationPeer) -> bool """
        pass

    def PeerFromProvider(self, *args): #cannot find CLR method
        """
        PeerFromProvider(self: AutomationPeer, provider: IRawElementProviderSimple) -> AutomationPeer
        
            Gets an System.Windows.Automation.Peers.AutomationPeer for the specified System.Windows.Automation.Provider.IRawElementProviderSimple proxy.
        
            provider: The class that implements System.Windows.Automation.Provider.IRawElementProviderSimple.
            Returns: The System.Windows.Automation.Peers.AutomationPeer.
        """
        pass

    def ProviderFromPeer(self, *args): #cannot find CLR method
        """
        ProviderFromPeer(self: AutomationPeer, peer: AutomationPeer) -> IRawElementProviderSimple
        
            Gets the System.Windows.Automation.Provider.IRawElementProviderSimple for the specified System.Windows.Automation.Peers.AutomationPeer.
        
            peer: The automation peer.
            Returns: The proxy.
        """
        pass

    def SetFocusCore(self, *args): #cannot find CLR method
        """ SetFocusCore(self: DateTimeAutomationPeer) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsHwndHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


