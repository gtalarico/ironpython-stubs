class DataGridCellItemAutomationPeer(AutomationPeer,IGridItemProvider,ITableItemProvider,IInvokeProvider,IScrollItemProvider,ISelectionItemProvider,IValueProvider,IVirtualizedItemProvider):
 """
 Exposes System.Windows.Controls.DataGridCell types to UI Automation.
 
 DataGridCellItemAutomationPeer(item: object,dataGridColumn: DataGridColumn)
 """
 def GetAcceleratorKeyCore(self,*args):
  """ GetAcceleratorKeyCore(self: DataGridCellItemAutomationPeer) -> str """
  pass
 def GetAccessKeyCore(self,*args):
  """ GetAccessKeyCore(self: DataGridCellItemAutomationPeer) -> str """
  pass
 def GetAutomationControlTypeCore(self,*args):
  """ GetAutomationControlTypeCore(self: DataGridCellItemAutomationPeer) -> AutomationControlType """
  pass
 def GetAutomationIdCore(self,*args):
  """ GetAutomationIdCore(self: DataGridCellItemAutomationPeer) -> str """
  pass
 def GetBoundingRectangleCore(self,*args):
  """ GetBoundingRectangleCore(self: DataGridCellItemAutomationPeer) -> Rect """
  pass
 def GetChildrenCore(self,*args):
  """ GetChildrenCore(self: DataGridCellItemAutomationPeer) -> List[AutomationPeer] """
  pass
 def GetClassNameCore(self,*args):
  """ GetClassNameCore(self: DataGridCellItemAutomationPeer) -> str """
  pass
 def GetClickablePointCore(self,*args):
  """ GetClickablePointCore(self: DataGridCellItemAutomationPeer) -> Point """
  pass
 def GetHelpTextCore(self,*args):
  """ GetHelpTextCore(self: DataGridCellItemAutomationPeer) -> str """
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
  """ GetItemStatusCore(self: DataGridCellItemAutomationPeer) -> str """
  pass
 def GetItemTypeCore(self,*args):
  """ GetItemTypeCore(self: DataGridCellItemAutomationPeer) -> str """
  pass
 def GetLabeledByCore(self,*args):
  """ GetLabeledByCore(self: DataGridCellItemAutomationPeer) -> AutomationPeer """
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
  """ GetNameCore(self: DataGridCellItemAutomationPeer) -> str """
  pass
 def GetOrientationCore(self,*args):
  """ GetOrientationCore(self: DataGridCellItemAutomationPeer) -> AutomationOrientation """
  pass
 def GetPattern(self,patternInterface):
  """
  GetPattern(self: DataGridCellItemAutomationPeer,patternInterface: PatternInterface) -> object
  
   Returns the object that supports the specified control pattern of the element 
    that is associated with this automation peer.
  
  
   patternInterface: An enumeration that specifies the control pattern.
   Returns: The current System.Windows.Automation.Peers.DataGridCellItemAutomationPeer 
    object,if patternInterface is a supported value; otherwise,null. For more 
    information,see Remarks.
  """
  pass
 def GetPeerFromPointCore(self,*args):
  """ GetPeerFromPointCore(self: AutomationPeer,point: Point) -> AutomationPeer """
  pass
 def HasKeyboardFocusCore(self,*args):
  """ HasKeyboardFocusCore(self: DataGridCellItemAutomationPeer) -> bool """
  pass
 def IsContentElementCore(self,*args):
  """ IsContentElementCore(self: DataGridCellItemAutomationPeer) -> bool """
  pass
 def IsControlElementCore(self,*args):
  """ IsControlElementCore(self: DataGridCellItemAutomationPeer) -> bool """
  pass
 def IsEnabledCore(self,*args):
  """ IsEnabledCore(self: DataGridCellItemAutomationPeer) -> bool """
  pass
 def IsKeyboardFocusableCore(self,*args):
  """ IsKeyboardFocusableCore(self: DataGridCellItemAutomationPeer) -> bool """
  pass
 def IsOffscreenCore(self,*args):
  """ IsOffscreenCore(self: DataGridCellItemAutomationPeer) -> bool """
  pass
 def IsPasswordCore(self,*args):
  """ IsPasswordCore(self: DataGridCellItemAutomationPeer) -> bool """
  pass
 def IsRequiredForFormCore(self,*args):
  """ IsRequiredForFormCore(self: DataGridCellItemAutomationPeer) -> bool """
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
  """ SetFocusCore(self: DataGridCellItemAutomationPeer) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,item,dataGridColumn):
  """ __new__(cls: type,item: object,dataGridColumn: DataGridColumn) """
  pass
 IsHwndHost=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


