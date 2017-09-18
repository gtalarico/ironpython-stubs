class MediaElementAutomationPeer(FrameworkElementAutomationPeer):
 """
 Exposes System.Windows.Controls.MediaElement types to UI Automation.
 
 MediaElementAutomationPeer(owner: MediaElement)
 """
 @staticmethod
 def __new__(self,owner):
  """ __new__(cls: type,owner: MediaElement) """
  pass
 IsHwndHost=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""


