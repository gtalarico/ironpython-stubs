class ListViewItemMouseHoverEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.ListView.ItemMouseHover event.

 

 ListViewItemMouseHoverEventArgs(item: ListViewItem)
 """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 @staticmethod
 def __new__(self,item):
  """ __new__(cls: type,item: ListViewItem) """
  pass
 Item=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the item the mouse pointer is currently hovering over.



Get: Item(self: ListViewItemMouseHoverEventArgs) -> ListViewItem



"""


