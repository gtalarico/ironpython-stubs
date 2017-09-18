class ListViewVirtualItemsSelectionRangeChangedEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.ListView.VirtualItemsSelectionRangeChanged event.

 

 ListViewVirtualItemsSelectionRangeChangedEventArgs(startIndex: int,endIndex: int,isSelected: bool)
 """
 @staticmethod
 def __new__(self,startIndex,endIndex,isSelected):
  """ __new__(cls: type,startIndex: int,endIndex: int,isSelected: bool) """
  pass
 EndIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index for the last item in the range of items whose selection state has changed



Get: EndIndex(self: ListViewVirtualItemsSelectionRangeChangedEventArgs) -> int



"""

 IsSelected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the range of items is selected.



Get: IsSelected(self: ListViewVirtualItemsSelectionRangeChangedEventArgs) -> bool



"""

 StartIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index for the first item in the range of items whose selection state has changed.



Get: StartIndex(self: ListViewVirtualItemsSelectionRangeChangedEventArgs) -> int



"""


