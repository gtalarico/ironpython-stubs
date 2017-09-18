class ToolStripItemImageRenderEventArgs(ToolStripItemRenderEventArgs):
 """
 Provides data for the System.Windows.Forms.ToolStripRenderer.RenderItemImage event.

 

 ToolStripItemImageRenderEventArgs(g: Graphics,item: ToolStripItem,imageRectangle: Rectangle)

 ToolStripItemImageRenderEventArgs(g: Graphics,item: ToolStripItem,image: Image,imageRectangle: Rectangle)
 """
 @staticmethod
 def __new__(self,g,item,*__args):
  """
  __new__(cls: type,g: Graphics,item: ToolStripItem,imageRectangle: Rectangle)

  __new__(cls: type,g: Graphics,item: ToolStripItem,image: Image,imageRectangle: Rectangle)
  """
  pass
 Image=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the image painted on the System.Windows.Forms.ToolStrip.



Get: Image(self: ToolStripItemImageRenderEventArgs) -> Image



"""

 ImageRectangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the rectangle that represents the bounding area of the image.



Get: ImageRectangle(self: ToolStripItemImageRenderEventArgs) -> Rectangle



"""


