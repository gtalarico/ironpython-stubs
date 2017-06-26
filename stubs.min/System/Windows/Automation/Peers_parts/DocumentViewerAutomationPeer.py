class DocumentViewerAutomationPeer(DocumentViewerBaseAutomationPeer):
 """
 Exposes System.Windows.Controls.DocumentViewer types to UI Automation.
 
 DocumentViewerAutomationPeer(owner: DocumentViewer)
 """
 def GetPattern(self,patternInterface):
  """
  GetPattern(self: DocumentViewerAutomationPeer,patternInterface: PatternInterface) -> object
  
   Gets the control pattern for the System.Windows.Controls.DocumentViewer that is 
    associated with this 
    System.Windows.Automation.Peers.DocumentViewerAutomationPeer.
  
  
   patternInterface: One of the enumeration values.
   Returns: If patternInterface is 
    System.Windows.Automation.Peers.PatternInterface.ScrollItem,this method 
    returns the System.Windows.Automation.Peers.ScrollViewerAutomationPeer for this 
    System.Windows.Automation.Peers.DocumentViewerAutomationPeer. This method also 
    sets System.Windows.Automation.Peers.DocumentViewerAutomationPeer as the 
    System.Windows.Automation.Peers.AutomationPeer.EventsSource.
  """
  pass
 @staticmethod
 def __new__(self,owner):
  """ __new__(cls: type,owner: DocumentViewer) """
  pass
 IsHwndHost=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


