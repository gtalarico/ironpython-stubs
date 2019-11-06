class ToolStripContentPanelRenderEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.ToolStripContentPanel.RendererChanged event.
 
 ToolStripContentPanelRenderEventArgs(g: Graphics,contentPanel: ToolStripContentPanel)
 """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return ToolStripContentPanelRenderEventArgs()

 @staticmethod
 def __new__(self,g,contentPanel):
  """ __new__(cls: type,g: Graphics,contentPanel: ToolStripContentPanel) """
  pass
 Graphics=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the object to use for drawing.

Get: Graphics(self: ToolStripContentPanelRenderEventArgs) -> Graphics

"""

 Handled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the event was handled.

Get: Handled(self: ToolStripContentPanelRenderEventArgs) -> bool

Set: Handled(self: ToolStripContentPanelRenderEventArgs)=value
"""

 ToolStripContentPanel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.ToolStripContentPanel affected by the click.

Get: ToolStripContentPanel(self: ToolStripContentPanelRenderEventArgs) -> ToolStripContentPanel

"""


