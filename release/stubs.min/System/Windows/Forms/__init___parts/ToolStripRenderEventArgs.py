class ToolStripRenderEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.ToolStripRenderer.OnRenderImageMargin(System.Windows.Forms.ToolStripRenderEventArgs),System.Windows.Forms.ToolStripRenderer.OnRenderToolStripBorder(System.Windows.Forms.ToolStripRenderEventArgs),and System.Windows.Forms.ToolStripRenderer.OnRenderToolStripBackground(System.Windows.Forms.ToolStripRenderEventArgs) methods.

 

 ToolStripRenderEventArgs(g: Graphics,toolStrip: ToolStrip)

 ToolStripRenderEventArgs(g: Graphics,toolStrip: ToolStrip,affectedBounds: Rectangle,backColor: Color)
 """
 @staticmethod
 def __new__(self,g,toolStrip,affectedBounds=None,backColor=None):
  """
  __new__(cls: type,g: Graphics,toolStrip: ToolStrip)

  __new__(cls: type,g: Graphics,toolStrip: ToolStrip,affectedBounds: Rectangle,backColor: Color)
  """
  pass
 AffectedBounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Drawing.Rectangle representing the bounds of the area to be painted.



Get: AffectedBounds(self: ToolStripRenderEventArgs) -> Rectangle



"""

 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Drawing.Color that the background of the System.Windows.Forms.ToolStrip is painted with.



Get: BackColor(self: ToolStripRenderEventArgs) -> Color



"""

 ConnectedArea=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Drawing.Rectangle representing the overlap area between a System.Windows.Forms.ToolStripDropDown and its System.Windows.Forms.ToolStripDropDown.OwnerItem.



Get: ConnectedArea(self: ToolStripRenderEventArgs) -> Rectangle



"""

 Graphics=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Drawing.Graphics used to paint.



Get: Graphics(self: ToolStripRenderEventArgs) -> Graphics



"""

 ToolStrip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.ToolStrip to be painted.



Get: ToolStrip(self: ToolStripRenderEventArgs) -> ToolStrip



"""


