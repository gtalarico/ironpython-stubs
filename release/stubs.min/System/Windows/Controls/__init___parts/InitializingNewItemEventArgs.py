class InitializingNewItemEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Controls.DataGrid.InitializingNewItem event.

 

 InitializingNewItemEventArgs(newItem: object)
 """
 @staticmethod
 def __new__(self,newItem):
  """ __new__(cls: type,newItem: object) """
  pass
 NewItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the new item added to the System.Windows.Controls.DataGrid.



Get: NewItem(self: InitializingNewItemEventArgs) -> object



"""


