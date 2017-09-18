class SelectionChangedEventArgs(RoutedEventArgs):
 """
 Provides data for the System.Windows.Controls.Primitives.Selector.SelectionChanged event.

 

 SelectionChangedEventArgs(id: RoutedEvent,removedItems: IList,addedItems: IList)
 """
 @staticmethod
 def __new__(self,id,removedItems,addedItems):
  """ __new__(cls: type,id: RoutedEvent,removedItems: IList,addedItems: IList) """
  pass
 AddedItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a list that contains the items that were selected.



Get: AddedItems(self: SelectionChangedEventArgs) -> IList



"""

 RemovedItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a list that contains the items that were unselected.



Get: RemovedItems(self: SelectionChangedEventArgs) -> IList



"""


