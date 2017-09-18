class ListViewItemSelectionChangedEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.ListView.ItemSelectionChanged event.

 

 ListViewItemSelectionChangedEventArgs(item: ListViewItem,itemIndex: int,isSelected: bool)
 """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 @staticmethod
 def __new__(self,item,itemIndex,isSelected):
  """ __new__(cls: type,item: ListViewItem,itemIndex: int,isSelected: bool) """
  pass
 IsSelected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the item's state has changed to selected.



Get: IsSelected(self: ListViewItemSelectionChangedEventArgs) -> bool



"""

 Item=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the item whose selection state has changed.



Get: Item(self: ListViewItemSelectionChangedEventArgs) -> ListViewItem



"""

 ItemIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the item whose selection state has changed.



Get: ItemIndex(self: ListViewItemSelectionChangedEventArgs) -> int



"""


