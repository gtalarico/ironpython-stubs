class ToolStripItemRenderEventArgs(EventArgs):
 """
 Provides data for the events that render the background of objects derived from System.Windows.Forms.ToolStripItem in the System.Windows.Forms.ToolStripRenderer class.

 

 ToolStripItemRenderEventArgs(g: Graphics,item: ToolStripItem)
 """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 @staticmethod
 def __new__(self,g,item):
  """ __new__(cls: type,g: Graphics,item: ToolStripItem) """
  pass
 Graphics=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the graphics used to paint the System.Windows.Forms.ToolStripItem.



Get: Graphics(self: ToolStripItemRenderEventArgs) -> Graphics



"""

 Item=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.ToolStripItem to paint.



Get: Item(self: ToolStripItemRenderEventArgs) -> ToolStripItem



"""

 ToolStrip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of the System.Windows.Forms.ToolStripItem.Owner property for the System.Windows.Forms.ToolStripItem to paint.



Get: ToolStrip(self: ToolStripItemRenderEventArgs) -> ToolStrip



"""


