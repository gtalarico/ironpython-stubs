class DataGridColumnHeaderItemAutomationPeer(ItemAutomationPeer, IVirtualizedItemProvider, IInvokeProvider, IScrollItemProvider, ITransformProvider):
    """
    Exposes the System.Windows.Controls.DataGridColumn.Header of a System.Windows.Controls.DataGridColumn that is in a System.Windows.Controls.DataGrid to UI Automation.
    
    DataGridColumnHeaderItemAutomationPeer(item: object, column: DataGridColumn, peer: DataGridColumnHeadersPresenterAutomationPeer)
    """
    def GetAcceleratorKeyCore(self, *args): #cannot find CLR method
        """
        GetAcceleratorKeyCore(self: ItemAutomationPeer) -> str
        
            Gets the accelerator key for the System.Windows.UIElement that corresponds to the data item in the System.Windows.Controls.ItemsControl.Items collection that is associated with this 
             System.Windows.Automation.Peers.ItemAutomationPeer.
        
            Returns: The accelerator key.
        """
        pass

    def GetAccessKeyCore(self, *args): #cannot find CLR method
        """
        GetAccessKeyCore(self: ItemAutomationPeer) -> str
        
            Gets the access key for the System.Windows.UIElement that corresponds to the data item in the System.Windows.Controls.ItemsControl.Items collection that is associated with this 
             System.Windows.Automation.Peers.ItemAutomationPeer.
        
            Returns: The access key.
        """
        pass

    def GetAutomationControlTypeCore(self, *args): #cannot find CLR method
        """
        GetAutomationControlTypeCore(self: DataGridColumnHeaderItemAutomationPeer) -> AutomationControlType
        
            Gets the control type for the header that is associated with this System.Windows.Automation.Peers.DataGridColumnHeaderItemAutomationPeer. This method is called by 
             System.Windows.Automation.Peers.AutomationPeer.GetAutomationControlType.
        
            Returns: The System.Windows.Automation.Peers.AutomationControlType.HeaderItem enumeration value.
        """
        pass

    def GetAutomationIdCore(self, *args): #cannot find CLR method
        """
        GetAutomationIdCore(self: ItemAutomationPeer) -> str
        
            Gets the string that uniquely identifies the System.Windows.UIElement that corresponds to the data item in the System.Windows.Controls.ItemsControl.Items collection that is associated with this 
             System.Windows.Automation.Peers.ItemAutomationPeer.
        
            Returns: A string that contains the UI Automation�identifier.
        """
        pass

    def GetBoundingRectangleCore(self, *args): #cannot find CLR method
        """
        GetBoundingRectangleCore(self: ItemAutomationPeer) -> Rect
        
            Gets the System.Windows.Rect that represents the bounding rectangle of the specified System.Windows.UIElement.
            Returns: The bounding rectangle.
        """
        pass

    def GetChildrenCore(self, *args): #cannot find CLR method
        """
        GetChildrenCore(self: ItemAutomationPeer) -> List[AutomationPeer]
        
            Gets the collection of child elements of the System.Windows.UIElement that corresponds to the data item in the System.Windows.Controls.ItemsControl.Items collection that is associated with this 
             System.Windows.Automation.Peers.ItemAutomationPeer.
        
            Returns: The collection of child elements.
        """
        pass

    def GetClassNameCore(self, *args): #cannot find CLR method
        """
        GetClassNameCore(self: DataGridColumnHeaderItemAutomationPeer) -> str
        
            Gets a name that differentiates the header that is represented by this System.Windows.Automation.Peers.DataGridColumnHeaderItemAutomationPeer. This method is called by 
             System.Windows.Automation.Peers.AutomationPeer.GetClassName.
        
            Returns: The type name of the System.Windows.Controls.DataGridColumn.Header property that is associated with this System.Windows.Automation.Peers.DataGridColumnHeaderItemAutomationPeer.
        """
        pass

    def GetClickablePointCore(self, *args): #cannot find CLR method
        """
        GetClickablePointCore(self: ItemAutomationPeer) -> Point
        
            Gets a System.Windows.Point that represents the clickable space that is on the specified System.Windows.UIElement.
            Returns: The point that represents the clickable space that is on the specified System.Windows.UIElement.
        """
        pass

    def GetHelpTextCore(self, *args): #cannot find CLR method
        """
        GetHelpTextCore(self: ItemAutomationPeer) -> str
        
            Gets the string that describes the functionality of the System.Windows.UIElement that corresponds to the data item in the System.Windows.Controls.ItemsControl.Items collection that is associated with this 
             System.Windows.Automation.Peers.ItemAutomationPeer.
        
            Returns: The help text.
        """
        pass

    def GetHostRawElementProviderCore(self, *args): #cannot find CLR method
        """
        GetHostRawElementProviderCore(self: AutomationPeer) -> HostedWindowWrapper
        
            Tells UI Automation where in the UI Automation tree to place the hwnd being hosted by a Windows Presentation Foundation (WPF) element.
            Returns: This method returns the hosted hwnd to UI Automation for controls that host hwnd objects.
        """
        pass

    def GetItemStatusCore(self, *args): #cannot find CLR method
        """
        GetItemStatusCore(self: ItemAutomationPeer) -> str
        
            Gets a string that conveys the visual status of the specified System.Windows.UIElement.
            Returns: The status. Examples include "Busy" or "Online".
        """
        pass

    def GetItemTypeCore(self, *args): #cannot find CLR method
        """
        GetItemTypeCore(self: ItemAutomationPeer) -> str
        
            Gets a human-readable string that contains the type of item that the specified System.Windows.UIElement represents.
            Returns: The item type. An example includes "Mail Message" or "Contact".
        """
        pass

    def GetLabeledByCore(self, *args): #cannot find CLR method
        """
        GetLabeledByCore(self: ItemAutomationPeer) -> AutomationPeer
        
            Gets the System.Windows.Automation.Peers.AutomationPeer for the System.Windows.Controls.Label that is targeted to the specified System.Windows.UIElement.
            Returns: The System.Windows.Automation.Peers.LabelAutomationPeer for the element that is targeted by the System.Windows.Controls.Label.
        """
        pass

    def GetLocalizedControlTypeCore(self, *args): #cannot find CLR method
        """
        GetLocalizedControlTypeCore(self: AutomationPeer) -> str
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.GetLocalizedControlType.
            Returns: The type of the control.
        """
        pass

    def GetNameCore(self, *args): #cannot find CLR method
        """
        GetNameCore(self: ItemAutomationPeer) -> str
        
            Gets the text label of the System.Windows.UIElement that corresponds to the data item in the System.Windows.Controls.ItemsControl.Items collection that is associated with this 
             System.Windows.Automation.Peers.ItemAutomationPeer.
        
            Returns: The text label.
        """
        pass

    def GetOrientationCore(self, *args): #cannot find CLR method
        """
        GetOrientationCore(self: ItemAutomationPeer) -> AutomationOrientation
        
            Gets a value that indicates whether the specified System.Windows.UIElement is laid out in a particular direction.
            Returns: The direction of the specified System.Windows.UIElement. Optionally, the method returns System.Windows.Automation.Peers.AutomationOrientation.None if the System.Windows.UIElement is not laid out in a 
             particular direction.
        """
        pass

    def GetPattern(self, patternInterface):
        """
        GetPattern(self: DataGridColumnHeaderItemAutomationPeer, patternInterface: PatternInterface) -> object
        
            Returns the object that supports the specified control pattern of the element that is associated with this automation peer.
        
            patternInterface: An enumeration value that specifies the control pattern.
            Returns: The current System.Windows.Automation.Peers.DataGridColumnHeaderItemAutomationPeer object, if patternInterface is a supported value; otherwise, null. For more information, see Remarks.
        """
        pass

    def GetPeerFromPointCore(self, *args): #cannot find CLR method
        """ GetPeerFromPointCore(self: AutomationPeer, point: Point) -> AutomationPeer """
        pass

    def HasKeyboardFocusCore(self, *args): #cannot find CLR method
        """
        HasKeyboardFocusCore(self: ItemAutomationPeer) -> bool
        
            Gets a value that indicates whether the specified System.Windows.UIElement currently has keyboard input focus.
            Returns: true if the specified System.Windows.UIElement has keyboard input focus; otherwise, false.
        """
        pass

    def IsContentElementCore(self, *args): #cannot find CLR method
        """
        IsContentElementCore(self: DataGridColumnHeaderItemAutomationPeer) -> bool
        
            Gets a value that indicates whether the element that is associated with this automation peer contains data that is presented to the user.
            Returns: false in all cases.
        """
        pass

    def IsControlElementCore(self, *args): #cannot find CLR method
        """
        IsControlElementCore(self: ItemAutomationPeer) -> bool
        
            Gets a value that indicates whether the System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.ItemAutomationPeer is understood by the end user as interactive.
            Returns: true if the element is a control; otherwise, false.
        """
        pass

    def IsEnabledCore(self, *args): #cannot find CLR method
        """
        IsEnabledCore(self: ItemAutomationPeer) -> bool
        
            Gets a value that indicates whether the specified System.Windows.UIElement can receive and send events.
            Returns: true if the UI Automation�peer can receive and send events; otherwise, false.
        """
        pass

    def IsKeyboardFocusableCore(self, *args): #cannot find CLR method
        """
        IsKeyboardFocusableCore(self: ItemAutomationPeer) -> bool
        
            Gets a value that indicates whether the specified System.Windows.UIElement can accept keyboard focus.
            Returns: true if the element can accept keyboard focus; otherwise, false.
        """
        pass

    def IsOffscreenCore(self, *args): #cannot find CLR method
        """
        IsOffscreenCore(self: ItemAutomationPeer) -> bool
        
            Gets a value that indicates whether the specified System.Windows.UIElement is off the screen.
            Returns: true if the specified System.Windows.UIElement is not on the screen; otherwise, false.
        """
        pass

    def IsPasswordCore(self, *args): #cannot find CLR method
        """
        IsPasswordCore(self: ItemAutomationPeer) -> bool
        
            Gets a value that indicates whether the specified System.Windows.UIElement contains protected content.
            Returns: true if the specified System.Windows.UIElement contains protected content; otherwise, false.
        """
        pass

    def IsRequiredForFormCore(self, *args): #cannot find CLR method
        """
        IsRequiredForFormCore(self: ItemAutomationPeer) -> bool
        
            Gets a value that indicates whether the specified System.Windows.UIElement is required to be completed on a form.
            Returns: true if the specified System.Windows.UIElement is required to be completed; otherwise, false.
        """
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
        """
        SetFocusCore(self: ItemAutomationPeer)
            Sets the keyboard input focus on the specified System.Windows.UIElement. The System.Windows.UIElement corresponds to the data item in the System.Windows.Controls.ItemsControl.Items collection that is 
             associated with this System.Windows.Automation.Peers.ItemAutomationPeer.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, item, column, peer):
        """ __new__(cls: type, item: object, column: DataGridColumn, peer: DataGridColumnHeadersPresenterAutomationPeer) """
        pass

    IsHwndHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


