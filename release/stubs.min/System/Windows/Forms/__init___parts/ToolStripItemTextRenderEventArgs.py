class ToolStripItemTextRenderEventArgs(ToolStripItemRenderEventArgs):
 """
 Provides data for the System.Windows.Forms.ToolStripRenderer.RenderItemText event.

 

 ToolStripItemTextRenderEventArgs(g: Graphics,item: ToolStripItem,text: str,textRectangle: Rectangle,textColor: Color,textFont: Font,format: TextFormatFlags)

 ToolStripItemTextRenderEventArgs(g: Graphics,item: ToolStripItem,text: str,textRectangle: Rectangle,textColor: Color,textFont: Font,textAlign: ContentAlignment)
 """
 @staticmethod
 def __new__(self,g,item,text,textRectangle,textColor,textFont,*__args):
  """
  __new__(cls: type,g: Graphics,item: ToolStripItem,text: str,textRectangle: Rectangle,textColor: Color,textFont: Font,format: TextFormatFlags)

  __new__(cls: type,g: Graphics,item: ToolStripItem,text: str,textRectangle: Rectangle,textColor: Color,textFont: Font,textAlign: ContentAlignment)
  """
  pass
 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text to be drawn on the System.Windows.Forms.ToolStripItem.



Get: Text(self: ToolStripItemTextRenderEventArgs) -> str



Set: Text(self: ToolStripItemTextRenderEventArgs)=value

"""

 TextColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of the System.Windows.Forms.ToolStripItem text.



Get: TextColor(self: ToolStripItemTextRenderEventArgs) -> Color



Set: TextColor(self: ToolStripItemTextRenderEventArgs)=value

"""

 TextDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether the text is drawn vertically or horizontally.



Get: TextDirection(self: ToolStripItemTextRenderEventArgs) -> ToolStripTextDirection



Set: TextDirection(self: ToolStripItemTextRenderEventArgs)=value

"""

 TextFont=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the font of the text drawn on the System.Windows.Forms.ToolStripItem.



Get: TextFont(self: ToolStripItemTextRenderEventArgs) -> Font



Set: TextFont(self: ToolStripItemTextRenderEventArgs)=value

"""

 TextFormat=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the display and layout information of the text drawn on the System.Windows.Forms.ToolStripItem.



Get: TextFormat(self: ToolStripItemTextRenderEventArgs) -> TextFormatFlags



Set: TextFormat(self: ToolStripItemTextRenderEventArgs)=value

"""

 TextRectangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the rectangle that represents the bounds to draw the text in.



Get: TextRectangle(self: ToolStripItemTextRenderEventArgs) -> Rectangle



Set: TextRectangle(self: ToolStripItemTextRenderEventArgs)=value

"""


