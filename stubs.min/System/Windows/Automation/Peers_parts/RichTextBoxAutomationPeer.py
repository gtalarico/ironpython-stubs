class RichTextBoxAutomationPeer(TextAutomationPeer):
 """
 Exposes System.Windows.Controls.RichTextBox types to UI Automation.
 
 RichTextBoxAutomationPeer(owner: RichTextBox)
 """
 def GetPattern(self,patternInterface):
  """
  GetPattern(self: RichTextBoxAutomationPeer,patternInterface: PatternInterface) -> object
  
   Gets the control pattern for the System.Windows.Controls.RichTextBox that is 
    associated with this System.Windows.Automation.Peers.RichTextBoxAutomationPeer.
  
  
   patternInterface: A value in the enumeration.
   Returns: If patternInterface is System.Windows.Automation.Peers.PatternInterface.Text,
    this method returns an System.Windows.Automation.Provider.ITextProvider 
    reference. If patternInterface is 
    System.Windows.Automation.Peers.PatternInterface.Scroll,this method returns a 
    new System.Windows.Automation.Peers.ScrollViewerAutomationPeer.
  """
  pass
 @staticmethod
 def __new__(self,owner):
  """ __new__(cls: type,owner: RichTextBox) """
  pass
 IsHwndHost=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


