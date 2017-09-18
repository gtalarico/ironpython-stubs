class ToolStripPanelRenderEventArgs(EventArgs):
 """
 Provides data for System.Windows.Forms.ToolStripPanel drawing.

 

 ToolStripPanelRenderEventArgs(g: Graphics,toolStripPanel: ToolStripPanel)
 """
 @staticmethod
 def __new__(self,g,toolStripPanel):
  """ __new__(cls: type,g: Graphics,toolStripPanel: ToolStripPanel) """
  pass
 Graphics=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the graphics used to paint the System.Windows.Forms.ToolStripPanel.



Get: Graphics(self: ToolStripPanelRenderEventArgs) -> Graphics



"""

 Handled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the event was handled.



Get: Handled(self: ToolStripPanelRenderEventArgs) -> bool



Set: Handled(self: ToolStripPanelRenderEventArgs)=value

"""

 ToolStripPanel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.ToolStripPanel to paint.



Get: ToolStripPanel(self: ToolStripPanelRenderEventArgs) -> ToolStripPanel



"""


