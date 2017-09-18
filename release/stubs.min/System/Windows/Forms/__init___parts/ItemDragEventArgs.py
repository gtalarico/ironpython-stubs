class ItemDragEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.ListView.ItemDrag event of the System.Windows.Forms.ListView and System.Windows.Forms.TreeView controls.

 

 ItemDragEventArgs(button: MouseButtons)

 ItemDragEventArgs(button: MouseButtons,item: object)
 """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 @staticmethod
 def __new__(self,button,item=None):
  """
  __new__(cls: type,button: MouseButtons)

  __new__(cls: type,button: MouseButtons,item: object)
  """
  pass
 Button=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates which mouse buttons were pressed during the drag operation.



Get: Button(self: ItemDragEventArgs) -> MouseButtons



"""

 Item=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the item that is being dragged.



Get: Item(self: ItemDragEventArgs) -> object



"""


