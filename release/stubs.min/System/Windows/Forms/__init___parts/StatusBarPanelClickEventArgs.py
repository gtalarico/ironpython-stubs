class StatusBarPanelClickEventArgs(MouseEventArgs):
 """
 Provides data for the System.Windows.Forms.StatusBar.PanelClick event.
 
 StatusBarPanelClickEventArgs(statusBarPanel: StatusBarPanel,button: MouseButtons,clicks: int,x: int,y: int)
 """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return StatusBarPanelClickEventArgs()

 @staticmethod
 def __new__(self,statusBarPanel,button,clicks,x,y):
  """ __new__(cls: type,statusBarPanel: StatusBarPanel,button: MouseButtons,clicks: int,x: int,y: int) """
  pass
 StatusBarPanel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.StatusBarPanel to draw.

Get: StatusBarPanel(self: StatusBarPanelClickEventArgs) -> StatusBarPanel

"""


