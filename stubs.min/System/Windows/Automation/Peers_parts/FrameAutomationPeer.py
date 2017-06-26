class FrameAutomationPeer(FrameworkElementAutomationPeer):
 """
 Exposes System.Windows.Controls.Frame types to UI Automation.
 
 FrameAutomationPeer(owner: Frame)
 """
 @staticmethod
 def __new__(self,owner):
  """ __new__(cls: type,owner: Frame) """
  pass
 IsHwndHost=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


