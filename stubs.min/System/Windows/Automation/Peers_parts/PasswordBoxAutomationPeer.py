class PasswordBoxAutomationPeer(TextAutomationPeer,IValueProvider):
 """
 Exposes System.Windows.Controls.PasswordBox types to UI Automation.
 
 PasswordBoxAutomationPeer(owner: PasswordBox)
 """
 def GetAcceleratorKeyCore(self,*args):
  """
  GetAcceleratorKeyCore(self: UIElementAutomationPeer) -> str
  
   Gets the accelerator key for the System.Windows.UIElement that is associated 
    with this System.Windows.Automation.Peers.UIElementAutomationPeer. This method 
    is called by System.Windows.Automation.Peers.AutomationPeer.GetAcceleratorKey.
  
   Returns: The System.Windows.Automation.AutomationProperties.AcceleratorKey that is 
    returned by 
    System.Windows.Automation.AutomationProperties.GetAcceleratorKey(System.Windows.
    DependencyObject).
  """
  pass
 def GetAccessKeyCore(self,*args):
  """
  GetAccessKeyCore(self: UIElementAutomationPeer) -> str
  
   Gets the access key for the System.Windows.UIElement that is associated with 
    this System.Windows.Automation.Peers.UIElementAutomationPeer.This method is 
    called by System.Windows.Automation.Peers.AutomationPeer.GetAccessKey.
  
   Returns: The access key for the System.Windows.UIElement that is associated with this 
    System.Windows.Automation.Peers.UIElementAutomationPeer.
  """
  pass
 def GetAutomationControlTypeCore(self,*args):
  """
  GetAutomationControlTypeCore(self: PasswordBoxAutomationPeer) -> AutomationControlType
  
   Gets the control type for the System.Windows.Controls.PasswordBox that is 
    associated with this System.Windows.Automation.Peers.PasswordBoxAutomationPeer. 
    This method is called by 
    System.Windows.Automation.Peers.AutomationPeer.GetAutomationControlType.
  
   Returns: The System.Windows.Automation.Peers.AutomationControlType.Edit enumeration 
    value.
  """
  pass
 def GetAutomationIdCore(self,*args):
  """
  GetAutomationIdCore(self: FrameworkElementAutomationPeer) -> str
  
   Gets the string that uniquely identifies the System.Windows.FrameworkElement 
    that is associated with this 
    System.Windows.Automation.Peers.FrameworkElementAutomationPeer. Called by 
    System.Windows.Automation.Peers.AutomationPeer.GetAutomationId.
  
   Returns: The automation identifier for the element associated with the 
    System.Windows.Automation.Peers.FrameworkElementAutomationPeer,or 
    System.String.Empty if there isn't an automation identifier.
  """
  pass
 def GetBoundingRectangleCore(self,*args):
  """
  GetBoundingRectangleCore(self: UIElementAutomationPeer) -> Rect
  
   Gets the System.Windows.Rect that represents the bounding rectangle of the 
    System.Windows.UIElement that is associated with this 
    System.Windows.Automation.Peers.UIElementAutomationPeer. This method is called 
    by System.Windows.Automation.Peers.AutomationPeer.GetBoundingRectangle.
  
   Returns: The System.Windows.Rect that contains the coordinates of the element. 
    Optionally,if the element is not both a System.Windows.Interop.HwndSource and 
    a System.Windows.PresentationSource,this method returns 
    System.Windows.Rect.Empty.
  """
  pass
 def GetChildrenCore(self,*args):
  """
  GetChildrenCore(self: UIElementAutomationPeer) -> List[AutomationPeer]
  
   Gets the collection of child elements of the System.Windows.UIElement that is 
    associated with this System.Windows.Automation.Peers.UIElementAutomationPeer. 
    This method is called by 
    System.Windows.Automation.Peers.AutomationPeer.GetChildren.
  
   Returns: A list of child System.Windows.Automation.Peers.AutomationPeer elements.
  """
  pass
 def GetClassNameCore(self,*args):
  """
  GetClassNameCore(self: PasswordBoxAutomationPeer) -> str
  
   Gets the name of the System.Windows.Controls.PasswordBox that is associated 
    with this System.Windows.Automation.Peers.PasswordBoxAutomationPeer. This 
    method is called by 
    System.Windows.Automation.Peers.AutomationPeer.GetClassName.
  
   Returns: A string that contains "PasswordBox".
  """
  pass
 def GetClickablePointCore(self,*args):
  """
  GetClickablePointCore(self: UIElementAutomationPeer) -> Point
  
   Gets a System.Windows.Point that represents the clickable space that is on the 
    System.Windows.UIElement that is associated with this 
    System.Windows.Automation.Peers.UIElementAutomationPeer. This method is called 
    by System.Windows.Automation.Peers.AutomationPeer.GetClickablePoint.
  
   Returns: The System.Windows.Point on the element that allows a click. The point values 
    are (System.Double.NaN,System.Double.NaN) if the element is not both a 
    System.Windows.Interop.HwndSource and a System.Windows.PresentationSource.
  """
  pass
 def GetHelpTextCore(self,*args):
  """
  GetHelpTextCore(self: FrameworkElementAutomationPeer) -> str
  
   Gets the string that describes the functionality of the 
    System.Windows.ContentElement that is associated with this 
    System.Windows.Automation.Peers.ContentElementAutomationPeer. Called by 
    System.Windows.Automation.Peers.AutomationPeer.GetHelpText.
  
   Returns: The help text,usually from the System.Windows.Controls.ToolTip,or 
    System.String.Empty if there is no help text.
  """
  pass
 def GetHostRawElementProviderCore(self,*args):
  """
  GetHostRawElementProviderCore(self: AutomationPeer) -> HostedWindowWrapper
  
   Tells UI Automation where in the UI Automation tree to place the hwnd being 
    hosted by a Windows Presentation Foundation (WPF) element.
  
   Returns: This method returns the hosted hwnd to UI Automation for controls that host 
    hwnd objects.
  """
  pass
 def GetItemStatusCore(self,*args):
  """
  GetItemStatusCore(self: UIElementAutomationPeer) -> str
  
   Gets a string that communicates the visual status of the 
    System.Windows.UIElement that is associated with this 
    System.Windows.Automation.Peers.UIElementAutomationPeer. This method is called 
    by System.Windows.Automation.Peers.AutomationPeer.GetItemStatus.
  
   Returns: The string that contains the 
    System.Windows.Automation.AutomationProperties.ItemStatus that is returned by 
    System.Windows.Automation.AutomationProperties.GetItemStatus(System.Windows.Depe
    ndencyObject).
  """
  pass
 def GetItemTypeCore(self,*args):
  """
  GetItemTypeCore(self: UIElementAutomationPeer) -> str
  
   Gets a human-readable string that contains the item type that the 
    System.Windows.UIElement for this 
    System.Windows.Automation.Peers.UIElementAutomationPeer represents. This method 
    is called by System.Windows.Automation.Peers.AutomationPeer.GetItemType.
  
   Returns: The string that contains the 
    System.Windows.Automation.AutomationProperties.ItemType that is returned by 
    System.Windows.Automation.AutomationProperties.GetItemType(System.Windows.Depend
    encyObject).
  """
  pass
 def GetLabeledByCore(self,*args):
  """
  GetLabeledByCore(self: UIElementAutomationPeer) -> AutomationPeer
  
   Gets the System.Windows.Automation.Peers.AutomationPeer for the element that is 
    targeted to the System.Windows.UIElement for this 
    System.Windows.Automation.Peers.UIElementAutomationPeer. This method is called 
    by System.Windows.Automation.Peers.AutomationPeer.GetLabeledBy.
  
   Returns: The System.Windows.Automation.Peers.AutomationPeer for the element that is 
    targeted to the System.Windows.UIElement for this 
    System.Windows.Automation.Peers.UIElementAutomationPeer.
  """
  pass
 def GetLocalizedControlTypeCore(self,*args):
  """
  GetLocalizedControlTypeCore(self: AutomationPeer) -> str
  
   When overridden in a derived class,is called by 
    System.Windows.Automation.Peers.AutomationPeer.GetLocalizedControlType.
  
   Returns: The type of the control.
  """
  pass
 def GetNameCore(self,*args):
  """
  GetNameCore(self: TextAutomationPeer) -> str
  
   Gets the text label of the element that is associated with this 
    System.Windows.Automation.Peers.TextAutomationPeer. Called by 
    System.Windows.Automation.Peers.AutomationPeer.GetName.
  
   Returns: The value of System.Windows.Automation.AutomationProperties.Name or 
    System.Windows.Automation.AutomationProperties.LabeledBy if either is set; 
    otherwise this method returns an empty string.
  """
  pass
 def GetOrientationCore(self,*args):
  """
  GetOrientationCore(self: UIElementAutomationPeer) -> AutomationOrientation
  
   Gets a value that indicates whether the System.Windows.UIElement that is 
    associated with this System.Windows.Automation.Peers.UIElementAutomationPeer is 
    laid out in a specific direction. This method is called by 
    System.Windows.Automation.Peers.AutomationPeer.GetOrientation.
  
   Returns: The System.Windows.Automation.Peers.AutomationOrientation.None enumeration 
    value.
  """
  pass
 def GetPattern(self,patternInterface):
  """
  GetPattern(self: PasswordBoxAutomationPeer,patternInterface: PatternInterface) -> object
  
   Gets the control pattern for the System.Windows.Controls.PasswordBox that is 
    associated with this System.Windows.Automation.Peers.PasswordBoxAutomationPeer.
  
  
   patternInterface: A value in the enumeration.
   Returns: The System.Windows.Automation.Peers.PatternInterface.Value enumeration value.
  """
  pass
 def GetPeerFromPointCore(self,*args):
  """ GetPeerFromPointCore(self: AutomationPeer,point: Point) -> AutomationPeer """
  pass
 def HasKeyboardFocusCore(self,*args):
  """
  HasKeyboardFocusCore(self: UIElementAutomationPeer) -> bool
  
   Gets a value that indicates whether the System.Windows.UIElement that is 
    associated with this System.Windows.Automation.Peers.UIElementAutomationPeer 
    currently has keyboard input focus. This method is called by 
    System.Windows.Automation.Peers.AutomationPeer.HasKeyboardFocus.
  
   Returns: true if the element has keyboard input focus; otherwise,false.
  """
  pass
 def IsContentElementCore(self,*args):
  """
  IsContentElementCore(self: UIElementAutomationPeer) -> bool
  
   Gets a value that indicates whether the System.Windows.UIElement that is 
    associated with this System.Windows.Automation.Peers.UIElementAutomationPeer is 
    an element that contains data that is presented to the user. This method is 
    called by System.Windows.Automation.Peers.AutomationPeer.IsContentElement.
  
   Returns: true.
  """
  pass
 def IsControlElementCore(self,*args):
  """
  IsControlElementCore(self: UIElementAutomationPeer) -> bool
  
   Gets or sets a value that indicates whether the System.Windows.UIElement that 
    is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer 
    is understood by the end user as interactive. Optionally,the user might 
    understand the System.Windows.UIElement as contributing to the logical 
    structure of the control in the GUI. This method is called by 
    System.Windows.Automation.Peers.AutomationPeer.IsControlElement.
  
   Returns: true.
  """
  pass
 def IsEnabledCore(self,*args):
  """
  IsEnabledCore(self: UIElementAutomationPeer) -> bool
  
   Gets a value that indicates whether the System.Windows.UIElement that is 
    associated with this System.Windows.Automation.Peers.UIElementAutomationPeer 
    can accept keyboard focus. This method is called by 
    System.Windows.Automation.Peers.AutomationPeer.IsKeyboardFocusable.
  
   Returns: A boolean that contains the value of System.Windows.UIElement.IsEnabled.
  """
  pass
 def IsKeyboardFocusableCore(self,*args):
  """
  IsKeyboardFocusableCore(self: UIElementAutomationPeer) -> bool
  
   Gets a value that indicates whether the System.Windows.UIElement that is 
    associated with this System.Windows.Automation.Peers.UIElementAutomationPeer 
    can accept keyboard focus. This method is called by 
    System.Windows.Automation.Peers.AutomationPeer.IsKeyboardFocusable.
  
   Returns: true if the element is focusable by the keyboard; otherwise false.
  """
  pass
 def IsOffscreenCore(self,*args):
  """
  IsOffscreenCore(self: UIElementAutomationPeer) -> bool
  
   Gets a value that indicates whether the System.Windows.UIElement that is 
    associated with this System.Windows.Automation.Peers.UIElementAutomationPeer is 
    off the screen. This method is called by 
    System.Windows.Automation.Peers.AutomationPeer.IsOffscreen.
  
   Returns: true if the element is not on the screen; otherwise,false.
  """
  pass
 def IsPasswordCore(self,*args):
  """
  IsPasswordCore(self: PasswordBoxAutomationPeer) -> bool
  
   Gets a value that indicates whether the System.Windows.Controls.PasswordBox 
    that is associated with this 
    System.Windows.Automation.Peers.PasswordBoxAutomationPeer contains protected 
    content. This method is called by 
    System.Windows.Automation.Peers.AutomationPeer.IsPassword.
  
   Returns: true.
  """
  pass
 def IsRequiredForFormCore(self,*args):
  """
  IsRequiredForFormCore(self: UIElementAutomationPeer) -> bool
  
   Gets a value that indicates whether the System.Windows.UIElement that is 
    associated with this System.Windows.Automation.Peers.UIElementAutomationPeer is 
    required to be completed on a form. This method is called by 
    System.Windows.Automation.Peers.AutomationPeer.IsRequiredForForm.
  
   Returns: A boolean that contains the value that is returned by 
    System.Windows.Automation.AutomationProperties.GetIsRequiredForForm(System.Windo
    ws.DependencyObject),if it's set; otherwise false.
  """
  pass
 def PeerFromProvider(self,*args):
  """
  PeerFromProvider(self: AutomationPeer,provider: IRawElementProviderSimple) -> AutomationPeer
  
   Gets an System.Windows.Automation.Peers.AutomationPeer for the specified 
    System.Windows.Automation.Provider.IRawElementProviderSimple proxy.
  
  
   provider: The class that implements 
    System.Windows.Automation.Provider.IRawElementProviderSimple.
  
   Returns: The System.Windows.Automation.Peers.AutomationPeer.
  """
  pass
 def ProviderFromPeer(self,*args):
  """
  ProviderFromPeer(self: AutomationPeer,peer: AutomationPeer) -> IRawElementProviderSimple
  
   Gets the System.Windows.Automation.Provider.IRawElementProviderSimple for the 
    specified System.Windows.Automation.Peers.AutomationPeer.
  
  
   peer: The automation peer.
   Returns: The proxy.
  """
  pass
 def SetFocusCore(self,*args):
  """
  SetFocusCore(self: UIElementAutomationPeer)
   Sets the keyboard input focus on the System.Windows.UIElement that is 
    associated with this System.Windows.Automation.Peers.UIElementAutomationPeer. 
    This method is called by 
    System.Windows.Automation.Peers.AutomationPeer.SetFocus.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,owner):
  """ __new__(cls: type,owner: PasswordBox) """
  pass
 IsHwndHost=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


