class PropertyValueChangedEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.PropertyGrid.PropertyValueChanged event of a System.Windows.Forms.PropertyGrid.

 

 PropertyValueChangedEventArgs(changedItem: GridItem,oldValue: object)
 """
 @staticmethod
 def __new__(self,changedItem,oldValue):
  """ __new__(cls: type,changedItem: GridItem,oldValue: object) """
  pass
 ChangedItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.GridItem that was changed.



Get: ChangedItem(self: PropertyValueChangedEventArgs) -> GridItem



"""

 OldValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The value of the grid item before it was changed.



Get: OldValue(self: PropertyValueChangedEventArgs) -> object



"""


