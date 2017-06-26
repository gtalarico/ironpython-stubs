class TableCellAutomationPeer(TextElementAutomationPeer, IGridItemProvider):
    """
    Exposes System.Windows.Documents.TableCell types to UI Automation.
    
    TableCellAutomationPeer(owner: TableCell)
    """
    def GetAcceleratorKeyCore(self, *args): #cannot find CLR method
        """
        GetAcceleratorKeyCore(self: ContentElementAutomationPeer) -> str
        
            Gets the accelerator key for the element associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer. Called by System.Windows.Automation.Peers.AutomationPeer.GetAcceleratorKey.
            Returns: System.String.Empty.
        """
        pass

    def GetAccessKeyCore(self, *args): #cannot find CLR method
        """
        GetAccessKeyCore(self: ContentElementAutomationPeer) -> str
        
            Gets the access key for the System.Windows.ContentElement that is associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer. Called by 
             System.Windows.Automation.Peers.AutomationPeer.GetAccessKey.
        
            Returns: The access key for this System.Windows.ContentElement.
        """
        pass

    def GetAutomationControlTypeCore(self, *args): #cannot find CLR method
        """
        GetAutomationControlTypeCore(self: TableCellAutomationPeer) -> AutomationControlType
        
            Gets the control type for the System.Windows.Documents.TableCell that is associated with this System.Windows.Automation.Peers.TableCellAutomationPeer. This method is called by 
             System.Windows.Automation.Peers.AutomationPeer.GetAutomationControlType.
        
            Returns: The System.Windows.Automation.Peers.AutomationControlType.Custom enumeration value.
        """
        pass

    def GetAutomationIdCore(self, *args): #cannot find CLR method
        """
        GetAutomationIdCore(self: FrameworkContentElementAutomationPeer) -> str
        
            Gets the string that uniquely identifies the System.Windows.FrameworkContentElement that is associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer. This method is called by 
             System.Windows.Automation.Peers.AutomationPeer.GetAutomationId.
        
            Returns: The System.Windows.Automation.AutomationIdentifier.
        """
        pass

    def GetBoundingRectangleCore(self, *args): #cannot find CLR method
        """
        GetBoundingRectangleCore(self: TextElementAutomationPeer) -> Rect
        
            Gets the System.Windows.Rect representing the bounding rectangle of the System.Windows.Documents.TextElement that is associated with this System.Windows.Automation.Peers.TextElementAutomationPeer. Called 
             by System.Windows.Automation.Peers.AutomationPeer.GetBoundingRectangle.
        
            Returns: The System.Windows.Rect that contains the coordinates of the element, or System.Windows.Rect.Empty if the element is not a System.Windows.Interop.HwndSource and a System.Windows.PresentationSource.
        """
        pass

    def GetChildrenCore(self, *args): #cannot find CLR method
        """
        GetChildrenCore(self: TextElementAutomationPeer) -> List[AutomationPeer]
        
            Gets the collection of child elements of the System.Windows.Documents.TextElement that is associated with this System.Windows.Automation.Peers.TextElementAutomationPeer. Called by 
             System.Windows.Automation.Peers.AutomationPeer.GetChildren.
        
            Returns: null.
        """
        pass

    def GetClassNameCore(self, *args): #cannot find CLR method
        """
        GetClassNameCore(self: TableCellAutomationPeer) -> str
        
            Gets the name of the System.Windows.Documents.TableCell that is associated with this System.Windows.Automation.Peers.TableCellAutomationPeer. This method is called by 
             System.Windows.Automation.Peers.AutomationPeer.GetClassName.
        
            Returns: A string that contains "TableCell".
        """
        pass

    def GetClickablePointCore(self, *args): #cannot find CLR method
        """
        GetClickablePointCore(self: TextElementAutomationPeer) -> Point
        
            Gets a System.Windows.Point that represents the clickable space that is on the System.Windows.Documents.TextElement that is associated with this System.Windows.Automation.Peers.TextElementAutomationPeer. 
             Called by System.Windows.Automation.Peers.AutomationPeer.GetClickablePoint.
        
            Returns: The System.Windows.Point on the element that allows a click. The point values are (System.Double.NaN, System.Double.NaN) if the element is not a System.Windows.Interop.HwndSource and a 
             System.Windows.PresentationSource.
        """
        pass

    def GetHelpTextCore(self, *args): #cannot find CLR method
        """
        GetHelpTextCore(self: FrameworkContentElementAutomationPeer) -> str
        
            Gets the string that describes the functionality of the System.Windows.FrameworkContentElement that is associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer. This method is 
             called by System.Windows.Automation.Peers.AutomationPeer.GetHelpText.
        
            Returns: The string describing the functionality of the element.
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
        GetItemStatusCore(self: ContentElementAutomationPeer) -> str
        
            Gets a string that conveys the visual status of the System.Windows.ContentElement that is associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer. Called by 
             System.Windows.Automation.Peers.AutomationPeer.GetItemStatus.
        
            Returns: A string containing the status.
        """
        pass

    def GetItemTypeCore(self, *args): #cannot find CLR method
        """
        GetItemTypeCore(self: ContentElementAutomationPeer) -> str
        
            Gets a human-readable string that contains the type of the item that the System.Windows.ContentElement that is associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer represents. 
             Called by System.Windows.Automation.Peers.AutomationPeer.GetItemType.
        
            Returns: The string that contains the item type.
        """
        pass

    def GetLabeledByCore(self, *args): #cannot find CLR method
        """
        GetLabeledByCore(self: FrameworkContentElementAutomationPeer) -> AutomationPeer
        
            Gets the System.Windows.Automation.Peers.LabelAutomationPeer for the System.Windows.Controls.Label that is targeted to the System.Windows.FrameworkContentElement that is associated with this 
             System.Windows.Automation.Peers.FrameworkContentElementAutomationPeer. This method is called by System.Windows.Automation.Peers.AutomationPeer.GetLabeledBy.
        
            Returns: The System.Windows.Automation.Peers.LabelAutomationPeer for the element that is targeted by the System.Windows.Controls.Label.
        """
        pass

    def GetLocalizedControlTypeCore(self, *args): #cannot find CLR method
        """
        GetLocalizedControlTypeCore(self: TableCellAutomationPeer) -> str
        
            Gets the localized version of the control type for the System.Windows.Documents.TableCell that is associated with this System.Windows.Automation.Peers.TableCellAutomationPeer.
            Returns: A string that contains "cell".
        """
        pass

    def GetNameCore(self, *args): #cannot find CLR method
        """
        GetNameCore(self: ContentElementAutomationPeer) -> str
        
            Gets the text label of the System.Windows.ContentElement that is associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer. Called by 
             System.Windows.Automation.Peers.AutomationPeer.GetName.
        
            Returns: The string that contains the label.
        """
        pass

    def GetOrientationCore(self, *args): #cannot find CLR method
        """
        GetOrientationCore(self: ContentElementAutomationPeer) -> AutomationOrientation
        
            Gets a value that indicates whether the System.Windows.ContentElement that is associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer is laid out in a specific direction. Called 
             by System.Windows.Automation.Peers.AutomationPeer.GetOrientation.
        
            Returns: System.Windows.Automation.Peers.AutomationOrientation.None.
        """
        pass

    def GetPattern(self, patternInterface):
        """
        GetPattern(self: TableCellAutomationPeer, patternInterface: PatternInterface) -> object
        
            Gets the control pattern for the System.Windows.Documents.TableCell that is associated with this System.Windows.Automation.Peers.TableCellAutomationPeer.
        
            patternInterface: A value from the enumeration.
            Returns: If patternInterface is System.Windows.Automation.Peers.PatternInterface.GridItem, this method returns the current instance of the System.Windows.Automation.Peers.TableCellAutomationPeer; otherwise, this 
             method returns null.
        """
        pass

    def GetPeerFromPointCore(self, *args): #cannot find CLR method
        """ GetPeerFromPointCore(self: AutomationPeer, point: Point) -> AutomationPeer """
        pass

    def HasKeyboardFocusCore(self, *args): #cannot find CLR method
        """
        HasKeyboardFocusCore(self: ContentElementAutomationPeer) -> bool
        
            Gets a value that indicates whether the System.Windows.ContentElement that is associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer currently has keyboard input focus. Called by 
             System.Windows.Automation.Peers.AutomationPeer.HasKeyboardFocus.
        
            Returns: true if the element has keyboard input focus; otherwise, false.
        """
        pass

    def IsContentElementCore(self, *args): #cannot find CLR method
        """
        IsContentElementCore(self: ContentElementAutomationPeer) -> bool
        
            Gets a value that indicates whether the System.Windows.ContentElement that is associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer is an element that contains data that is 
             presented to the user. Called by System.Windows.Automation.Peers.AutomationPeer.IsContentElement.
        
            Returns: false.
        """
        pass

    def IsControlElementCore(self, *args): #cannot find CLR method
        """
        IsControlElementCore(self: TableCellAutomationPeer) -> bool
        
            Gets or sets a value that indicates whether the System.Windows.Documents.TableCell that is associated with this System.Windows.Automation.Peers.TableCellAutomationPeer is understood by the end user as 
             interactive or as contributing to the logical structure of the control in the GUI. This method is called by System.Windows.Automation.Peers.AutomationPeer.IsControlElement.
        
            Returns: true.
        """
        pass

    def IsEnabledCore(self, *args): #cannot find CLR method
        """
        IsEnabledCore(self: ContentElementAutomationPeer) -> bool
        
            Gets a value that indicates whether this automation peer can receive and send events to the associated element. Called by System.Windows.Automation.Peers.AutomationPeer.IsEnabled.
            Returns: true if the automation peer can receive and send events; otherwise, false.
        """
        pass

    def IsKeyboardFocusableCore(self, *args): #cannot find CLR method
        """
        IsKeyboardFocusableCore(self: ContentElementAutomationPeer) -> bool
        
            Gets a value that indicates whether the System.Windows.ContentElement that is associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer can accept keyboard focus. Called by 
             System.Windows.Automation.Peers.AutomationPeer.IsKeyboardFocusable.
        
            Returns: false.
        """
        pass

    def IsOffscreenCore(self, *args): #cannot find CLR method
        """
        IsOffscreenCore(self: TextElementAutomationPeer) -> bool
        
            Gets a value that indicates whether System.Windows.Documents.TextElement that is associated with this System.Windows.Automation.Peers.TextElementAutomationPeer is off of the screen. Called by 
             System.Windows.Automation.Peers.AutomationPeer.IsOffscreen.
        
            Returns: true if the element is not on the screen; otherwise, false.
        """
        pass

    def IsPasswordCore(self, *args): #cannot find CLR method
        """
        IsPasswordCore(self: ContentElementAutomationPeer) -> bool
        
            Gets a value that indicates whether the System.Windows.ContentElement that is associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer contains protected content. Called by 
             System.Windows.Automation.Peers.AutomationPeer.IsPassword.
        
            Returns: false.
        """
        pass

    def IsRequiredForFormCore(self, *args): #cannot find CLR method
        """
        IsRequiredForFormCore(self: ContentElementAutomationPeer) -> bool
        
            Gets a value that indicates whether the System.Windows.ContentElement that is associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer is required to be filled out on a form. 
             Called by System.Windows.Automation.Peers.AutomationPeer.IsRequiredForForm.
        
            Returns: false.
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
        SetFocusCore(self: ContentElementAutomationPeer)
            Sets the keyboard input focus on the System.Windows.ContentElement that is associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer. Called by 
             System.Windows.Automation.Peers.AutomationPeer.SetFocus.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, owner):
        """ __new__(cls: type, owner: TableCell) """
        pass

    IsHwndHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


