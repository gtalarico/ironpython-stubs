class GroupBoxAutomationPeer(FrameworkElementAutomationPeer):
 """
 Exposes System.Windows.Controls.GroupBox types to UI Automation.
 
 GroupBoxAutomationPeer(owner: GroupBox)
 """
 @staticmethod
 def __new__(self,owner):
  """ __new__(cls: type,owner: GroupBox) """
  pass
 IsHwndHost=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


