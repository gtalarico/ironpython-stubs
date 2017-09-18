class ItemsChangedEventArgs(EventArgs):
 """ Provides data for the System.Windows.Controls.ItemContainerGenerator.ItemsChanged event. """
 Action=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the action that occurred on the items collection.



Get: Action(self: ItemsChangedEventArgs) -> NotifyCollectionChangedAction



"""

 ItemCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of items that were involved in the change.



Get: ItemCount(self: ItemsChangedEventArgs) -> int



"""

 ItemUICount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of user interface (UI) elements involved in the change.



Get: ItemUICount(self: ItemsChangedEventArgs) -> int



"""

 OldPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the position in the collection before the change occurred.



Get: OldPosition(self: ItemsChangedEventArgs) -> GeneratorPosition



"""

 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the position in the collection where the change occurred.



Get: Position(self: ItemsChangedEventArgs) -> GeneratorPosition



"""


