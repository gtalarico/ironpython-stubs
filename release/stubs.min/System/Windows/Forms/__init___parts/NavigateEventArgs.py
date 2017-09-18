class NavigateEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.DataGrid.Navigate event.

 

 NavigateEventArgs(isForward: bool)
 """
 @staticmethod
 def __new__(self,isForward):
  """ __new__(cls: type,isForward: bool) """
  pass
 Forward=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether to navigate in a forward direction.



Get: Forward(self: NavigateEventArgs) -> bool



"""


