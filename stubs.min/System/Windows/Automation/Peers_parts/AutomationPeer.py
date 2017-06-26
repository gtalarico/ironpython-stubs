class AutomationPeer(DispatcherObject):
    """ Provides a base class that exposes an element to UI Automation. """
    def GetAcceleratorKey(self):
        """
        GetAcceleratorKey(self: AutomationPeer) -> str
        
            Gets the accelerator key combinations for the element that is associated with the UI Automation peer.
            Returns: The accelerator key.
        """
        pass

    def GetAcceleratorKeyCore(self, *args): #cannot find CLR method
        """
        GetAcceleratorKeyCore(self: AutomationPeer) -> str
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.GetAcceleratorKey.
            Returns: The accelerator key.
        """
        pass

    def GetAccessKey(self):
        """
        GetAccessKey(self: AutomationPeer) -> str
        
            Gets the access key for the element that is associated with the automation peer.
            Returns: The string that contains the access key.
        """
        pass

    def GetAccessKeyCore(self, *args): #cannot find CLR method
        """
        GetAccessKeyCore(self: AutomationPeer) -> str
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.GetAccessKey.
            Returns: The string that contains the access key.
        """
        pass

    def GetAutomationControlType(self):
        """
        GetAutomationControlType(self: AutomationPeer) -> AutomationControlType
        
            Gets the control type for the element that is associated with the UI Automation peer.
            Returns: The control type.
        """
        pass

    def GetAutomationControlTypeCore(self, *args): #cannot find CLR method
        """
        GetAutomationControlTypeCore(self: AutomationPeer) -> AutomationControlType
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.GetAutomationControlType.
            Returns: The control type.
        """
        pass

    def GetAutomationId(self):
        """
        GetAutomationId(self: AutomationPeer) -> str
        
            Gets the System.Windows.Automation.AutomationProperties.AutomationId of the element that is associated with the automation peer.
            Returns: The identifier.
        """
        pass

    def GetAutomationIdCore(self, *args): #cannot find CLR method
        """
        GetAutomationIdCore(self: AutomationPeer) -> str
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.GetAutomationId.
            Returns: The string that contains the identifier.
        """
        pass

    def GetBoundingRectangle(self):
        """
        GetBoundingRectangle(self: AutomationPeer) -> Rect
        
            Gets the System.Windows.Rect object that represents the screen coordinates of the element that is associated with the automation peer.
            Returns: The bounding rectangle.
        """
        pass

    def GetBoundingRectangleCore(self, *args): #cannot find CLR method
        """
        GetBoundingRectangleCore(self: AutomationPeer) -> Rect
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.GetBoundingRectangle.
            Returns: The bounding rectangle.
        """
        pass

    def GetChildren(self):
        """
        GetChildren(self: AutomationPeer) -> List[AutomationPeer]
        
            Gets the collection of System.Windows.Automation.Peers.AutomationPeer.GetChildren elements that are represented in the UI Automation tree as immediate child elements of the automation peer.
            Returns: The collection of child elements.
        """
        pass

    def GetChildrenCore(self, *args): #cannot find CLR method
        """
        GetChildrenCore(self: AutomationPeer) -> List[AutomationPeer]
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.GetChildren.
            Returns: The collection of child elements.
        """
        pass

    def GetClassName(self):
        """
        GetClassName(self: AutomationPeer) -> str
        
            Gets a name that is used with System.Windows.Automation.Peers.AutomationControlType, to differentiate the control that is represented by this System.Windows.Automation.Peers.AutomationPeer.
            Returns: The class name.
        """
        pass

    def GetClassNameCore(self, *args): #cannot find CLR method
        """
        GetClassNameCore(self: AutomationPeer) -> str
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.GetClassName.
            Returns: The class name.
        """
        pass

    def GetClickablePoint(self):
        """
        GetClickablePoint(self: AutomationPeer) -> Point
        
            Gets a System.Windows.Point on the element that is associated with the automation peer that responds to a mouse click.
            Returns: A point in the clickable area of the element.
        """
        pass

    def GetClickablePointCore(self, *args): #cannot find CLR method
        """
        GetClickablePointCore(self: AutomationPeer) -> Point
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.GetClickablePoint.
            Returns: A point within the clickable area of the element.
        """
        pass

    def GetHelpText(self):
        """
        GetHelpText(self: AutomationPeer) -> str
        
            Gets text that describes the functionality of the control that is associated with the automation peer.
            Returns: The help text.
        """
        pass

    def GetHelpTextCore(self, *args): #cannot find CLR method
        """
        GetHelpTextCore(self: AutomationPeer) -> str
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.GetHelpText.
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

    def GetItemStatus(self):
        """
        GetItemStatus(self: AutomationPeer) -> str
        
            Gets text that conveys the visual status of the element that is associated with this automation peer.
            Returns: The status.
        """
        pass

    def GetItemStatusCore(self, *args): #cannot find CLR method
        """
        GetItemStatusCore(self: AutomationPeer) -> str
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.GetItemStatus.
            Returns: The status.
        """
        pass

    def GetItemType(self):
        """
        GetItemType(self: AutomationPeer) -> str
        
            Gets a string that describes what kind of item an object represents.
            Returns: The kind of item.
        """
        pass

    def GetItemTypeCore(self, *args): #cannot find CLR method
        """
        GetItemTypeCore(self: AutomationPeer) -> str
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.GetItemType.
            Returns: The kind of item.
        """
        pass

    def GetLabeledBy(self):
        """
        GetLabeledBy(self: AutomationPeer) -> AutomationPeer
        
            Gets the System.Windows.Automation.Peers.AutomationPeer for the System.Windows.Controls.Label that is targeted to the element.
            Returns: The System.Windows.Automation.Peers.LabelAutomationPeer for the element that is targeted by the System.Windows.Controls.Label.
        """
        pass

    def GetLabeledByCore(self, *args): #cannot find CLR method
        """
        GetLabeledByCore(self: AutomationPeer) -> AutomationPeer
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.GetLabeledBy.
            Returns: The System.Windows.Automation.Peers.LabelAutomationPeer for the element that is targeted by the System.Windows.Controls.Label.
        """
        pass

    def GetLocalizedControlType(self):
        """
        GetLocalizedControlType(self: AutomationPeer) -> str
        
            Gets a human-readable localized string that represents the System.Windows.Automation.Peers.AutomationControlType value for the control that is associated with this automation peer.
            Returns: The type of the control.
        """
        pass

    def GetLocalizedControlTypeCore(self, *args): #cannot find CLR method
        """
        GetLocalizedControlTypeCore(self: AutomationPeer) -> str
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.GetLocalizedControlType.
            Returns: The type of the control.
        """
        pass

    def GetName(self):
        """
        GetName(self: AutomationPeer) -> str
        
            Gets text that describes the element that is associated with this automation peer.
            Returns: The name.
        """
        pass

    def GetNameCore(self, *args): #cannot find CLR method
        """
        GetNameCore(self: AutomationPeer) -> str
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.GetName.
            Returns: The string that contains the label.
        """
        pass

    def GetOrientation(self):
        """
        GetOrientation(self: AutomationPeer) -> AutomationOrientation
        
            Gets a value that indicates the explicit control orientation, if any.
            Returns: The orientation of the control.
        """
        pass

    def GetOrientationCore(self, *args): #cannot find CLR method
        """
        GetOrientationCore(self: AutomationPeer) -> AutomationOrientation
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.GetOrientation.
            Returns: The orientation of the control.
        """
        pass

    def GetParent(self):
        """
        GetParent(self: AutomationPeer) -> AutomationPeer
        
            Gets the System.Windows.Automation.Peers.AutomationPeer that is the parent of this System.Windows.Automation.Peers.AutomationPeer.
            Returns: The parent automation peer.
        """
        pass

    def GetPattern(self, patternInterface):
        """
        GetPattern(self: AutomationPeer, patternInterface: PatternInterface) -> object
        
            When overridden in a derived class, gets the control pattern that is associated with the specified System.Windows.Automation.Peers.PatternInterface.
        
            patternInterface: A value from the System.Windows.Automation.Peers.PatternInterface enumeration.
            Returns: The object that implements the pattern interface; null if this peer does not support this interface.
        """
        pass

    def GetPeerFromPoint(self, point):
        """ GetPeerFromPoint(self: AutomationPeer, point: Point) -> AutomationPeer """
        pass

    def GetPeerFromPointCore(self, *args): #cannot find CLR method
        """ GetPeerFromPointCore(self: AutomationPeer, point: Point) -> AutomationPeer """
        pass

    def HasKeyboardFocus(self):
        """
        HasKeyboardFocus(self: AutomationPeer) -> bool
        
            Gets a value that indicates whether the element that is associated with this automation peer currently has keyboard focus.
            Returns: true if the element has keyboard focus; otherwise, false.
        """
        pass

    def HasKeyboardFocusCore(self, *args): #cannot find CLR method
        """
        HasKeyboardFocusCore(self: AutomationPeer) -> bool
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.HasKeyboardFocus.
            Returns: true if the element has keyboard focus; otherwise, false.
        """
        pass

    def InvalidatePeer(self):
        """
        InvalidatePeer(self: AutomationPeer)
            Triggers recalculation of the main properties of the System.Windows.Automation.Peers.AutomationPeer and raises the System.ComponentModel.INotifyPropertyChanged.PropertyChanged notification to the 
             Automation Client if the properties changed.
        """
        pass

    def IsContentElement(self):
        """
        IsContentElement(self: AutomationPeer) -> bool
        
            Gets a value that indicates whether the element that is associated with this automation peer contains data that is presented to the user.
            Returns: true if the element is a content element; otherwise, false.
        """
        pass

    def IsContentElementCore(self, *args): #cannot find CLR method
        """
        IsContentElementCore(self: AutomationPeer) -> bool
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.IsContentElement.
            Returns: true if the element is a content element; otherwise, false.
        """
        pass

    def IsControlElement(self):
        """
        IsControlElement(self: AutomationPeer) -> bool
        
            Gets a value that indicates whether the element is understood by the user as interactive or as contributing to the logical structure of the control in the GUI.
            Returns: true if the element is a control; otherwise, false.
        """
        pass

    def IsControlElementCore(self, *args): #cannot find CLR method
        """
        IsControlElementCore(self: AutomationPeer) -> bool
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.IsControlElement.
            Returns: true if the element is a control; otherwise, false.
        """
        pass

    def IsEnabled(self):
        """
        IsEnabled(self: AutomationPeer) -> bool
        
            Gets a value that indicates whether the element associated with this automation peer supports interaction.
            Returns: true if the element supports interaction; otherwise, false.
        """
        pass

    def IsEnabledCore(self, *args): #cannot find CLR method
        """
        IsEnabledCore(self: AutomationPeer) -> bool
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.IsEnabled.
            Returns: true if the automation peer can receive and send events; otherwise, false.
        """
        pass

    def IsKeyboardFocusable(self):
        """
        IsKeyboardFocusable(self: AutomationPeer) -> bool
        
            Gets a value that indicates whether the element can accept keyboard focus.
            Returns: true if the element can accept keyboard focus; otherwise, false.
        """
        pass

    def IsKeyboardFocusableCore(self, *args): #cannot find CLR method
        """
        IsKeyboardFocusableCore(self: AutomationPeer) -> bool
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.IsKeyboardFocusable.
            Returns: true if the element can accept keyboard focus; otherwise, false.
        """
        pass

    def IsOffscreen(self):
        """
        IsOffscreen(self: AutomationPeer) -> bool
        
            Gets a value that indicates whether an element is off the screen.
            Returns: true if the element is not on the screen; otherwise, false.
        """
        pass

    def IsOffscreenCore(self, *args): #cannot find CLR method
        """
        IsOffscreenCore(self: AutomationPeer) -> bool
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.IsOffscreen.
            Returns: true if the element is not on the screen; otherwise, false.
        """
        pass

    def IsPassword(self):
        """
        IsPassword(self: AutomationPeer) -> bool
        
            Gets a value that indicates whether the element contains sensitive content.
            Returns: true if the element contains sensitive content such as a password; otherwise, false.
        """
        pass

    def IsPasswordCore(self, *args): #cannot find CLR method
        """
        IsPasswordCore(self: AutomationPeer) -> bool
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.IsPassword.
            Returns: true if the element contains sensitive content; otherwise, false.
        """
        pass

    def IsRequiredForForm(self):
        """
        IsRequiredForForm(self: AutomationPeer) -> bool
        
            Gets a value that indicates whether the element that is associated with this peer must be completed on a form.
            Returns: true if the element must be completed; otherwise, false.
        """
        pass

    def IsRequiredForFormCore(self, *args): #cannot find CLR method
        """
        IsRequiredForFormCore(self: AutomationPeer) -> bool
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.IsRequiredForForm.
            Returns: true if the element is must be completed; otherwise, false.
        """
        pass

    @staticmethod
    def ListenerExists(eventId):
        """
        ListenerExists(eventId: AutomationEvents) -> bool
        
            Gets a value that indicates whether UI Automation is listening for the specified event.
        
            eventId: One of the enumeration values.
            Returns: A boolean that indicates whether UI Automation is listening for the event.
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

    def RaiseAsyncContentLoadedEvent(self, args):
        """
        RaiseAsyncContentLoadedEvent(self: AutomationPeer, args: AsyncContentLoadedEventArgs)
            Called by the System.Windows.Automation.Peers.AutomationPeer to raise the System.Windows.Automation.AutomationElement.AsyncContentLoadedEvent event.
        
            args: The event data.
        """
        pass

    def RaiseAutomationEvent(self, eventId):
        """
        RaiseAutomationEvent(self: AutomationPeer, eventId: AutomationEvents)
            Raises an automation event.
        
            eventId: The event identifier.
        """
        pass

    def RaisePropertyChangedEvent(self, property, oldValue, newValue):
        """
        RaisePropertyChangedEvent(self: AutomationPeer, property: AutomationProperty, oldValue: object, newValue: object)
            Raises an event to notify the automation client of a changed property value.
        
            property: The property that changed.
            oldValue: The previous value of the property.
            newValue: The new value of the property.
        """
        pass

    def ResetChildrenCache(self):
        """
        ResetChildrenCache(self: AutomationPeer)
            Synchronously resets the tree of child elements by calling System.Windows.Automation.Peers.AutomationPeer.GetChildrenCore.
        """
        pass

    def SetFocus(self):
        """
        SetFocus(self: AutomationPeer)
            Sets the keyboard focus on the element that is associated with this automation peer.
        """
        pass

    def SetFocusCore(self, *args): #cannot find CLR method
        """
        SetFocusCore(self: AutomationPeer)
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.SetFocus.
        """
        pass

    EventsSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an System.Windows.Automation.Peers.AutomationPeer that is reported to the automation client as a source for all the events that come from this System.Windows.Automation.Peers.AutomationPeer.

Get: EventsSource(self: AutomationPeer) -> AutomationPeer

Set: EventsSource(self: AutomationPeer) = value
"""

    IsHwndHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


