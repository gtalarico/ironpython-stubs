class ToolStripSeparatorRenderEventArgs(ToolStripItemRenderEventArgs):
 """
 Provides data for the System.Windows.Forms.ToolStripRenderer.RenderGrip event.

 

 ToolStripSeparatorRenderEventArgs(g: Graphics,separator: ToolStripSeparator,vertical: bool)
 """
 @staticmethod
 def __new__(self,g,separator,vertical):
  """ __new__(cls: type,g: Graphics,separator: ToolStripSeparator,vertical: bool) """
  pass
 Vertical=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the display style for the grip is vertical.



Get: Vertical(self: ToolStripSeparatorRenderEventArgs) -> bool



"""


