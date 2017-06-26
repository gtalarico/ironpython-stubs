class FlowDocumentScrollViewerAutomationPeer(FrameworkElementAutomationPeer):
 """
 Exposes System.Windows.Controls.FlowDocumentScrollViewer types to UI Automation.
 
 FlowDocumentScrollViewerAutomationPeer(owner: FlowDocumentScrollViewer)
 """
 def GetPattern(self,patternInterface):
  """
  GetPattern(self: FlowDocumentScrollViewerAutomationPeer,patternInterface: PatternInterface) -> object
  
   Gets the control pattern for the 
    System.Windows.Controls.FlowDocumentScrollViewer that is associated with this 
    System.Windows.Automation.Peers.FlowDocumentScrollViewerAutomationPeer.
  
  
   patternInterface: One of the enumeration values.
   Returns: An object that supports the control pattern if patternInterface is a supported 
    value; otherwise,null.
  """
  pass
 @staticmethod
 def __new__(self,owner):
  """ __new__(cls: type,owner: FlowDocumentScrollViewer) """
  pass
 IsHwndHost=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


