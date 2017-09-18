class ToolStripItemClickedEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.ToolStrip.ItemClicked event.

 

 ToolStripItemClickedEventArgs(clickedItem: ToolStripItem)
 """
 @staticmethod
 def __new__(self,clickedItem):
  """ __new__(cls: type,clickedItem: ToolStripItem) """
  pass
 ClickedItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the item that was clicked on the System.Windows.Forms.ToolStrip.



Get: ClickedItem(self: ToolStripItemClickedEventArgs) -> ToolStripItem



"""


