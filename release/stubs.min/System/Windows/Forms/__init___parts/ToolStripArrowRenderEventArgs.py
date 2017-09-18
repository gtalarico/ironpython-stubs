class ToolStripArrowRenderEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.ToolStripRenderer.RenderArrow event.

 

 ToolStripArrowRenderEventArgs(g: Graphics,toolStripItem: ToolStripItem,arrowRectangle: Rectangle,arrowColor: Color,arrowDirection: ArrowDirection)
 """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 @staticmethod
 def __new__(self,g,toolStripItem,arrowRectangle,arrowColor,arrowDirection):
  """ __new__(cls: type,g: Graphics,toolStripItem: ToolStripItem,arrowRectangle: Rectangle,arrowColor: Color,arrowDirection: ArrowDirection) """
  pass
 ArrowColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of the System.Windows.Forms.ToolStrip arrow.



Get: ArrowColor(self: ToolStripArrowRenderEventArgs) -> Color



Set: ArrowColor(self: ToolStripArrowRenderEventArgs)=value

"""

 ArrowRectangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the bounding area of the System.Windows.Forms.ToolStrip arrow.



Get: ArrowRectangle(self: ToolStripArrowRenderEventArgs) -> Rectangle



Set: ArrowRectangle(self: ToolStripArrowRenderEventArgs)=value

"""

 Direction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the direction in which the System.Windows.Forms.ToolStrip arrow points.



Get: Direction(self: ToolStripArrowRenderEventArgs) -> ArrowDirection



Set: Direction(self: ToolStripArrowRenderEventArgs)=value

"""

 Graphics=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the graphics used to paint the System.Windows.Forms.ToolStrip arrow.



Get: Graphics(self: ToolStripArrowRenderEventArgs) -> Graphics



"""

 Item=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.ToolStripItem on which to paint the arrow.



Get: Item(self: ToolStripArrowRenderEventArgs) -> ToolStripItem



"""


