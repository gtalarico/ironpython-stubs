class ToolStripGripRenderEventArgs(ToolStripRenderEventArgs):
 """
 Provides data for the System.Windows.Forms.ToolStripRenderer.RenderGrip event.

 

 ToolStripGripRenderEventArgs(g: Graphics,toolStrip: ToolStrip)
 """
 @staticmethod
 def __new__(self,g,toolStrip):
  """ __new__(cls: type,g: Graphics,toolStrip: ToolStrip) """
  pass
 GripBounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the rectangle representing the area in which to paint the move handle.



Get: GripBounds(self: ToolStripGripRenderEventArgs) -> Rectangle



"""

 GripDisplayStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the style that indicates whether the move handle is displayed vertically or horizontally.



Get: GripDisplayStyle(self: ToolStripGripRenderEventArgs) -> ToolStripGripDisplayStyle



"""

 GripStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the style that indicates whether or not the move handle is visible.



Get: GripStyle(self: ToolStripGripRenderEventArgs) -> ToolStripGripStyle



"""


