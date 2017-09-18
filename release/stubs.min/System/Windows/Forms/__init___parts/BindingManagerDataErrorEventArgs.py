class BindingManagerDataErrorEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.BindingManagerBase.DataError event.

 

 BindingManagerDataErrorEventArgs(exception: Exception)
 """
 @staticmethod
 def __new__(self,exception):
  """ __new__(cls: type,exception: Exception) """
  pass
 Exception=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Exception caught in the binding process that caused the System.Windows.Forms.BindingManagerBase.DataError event to be raised.



Get: Exception(self: BindingManagerDataErrorEventArgs) -> Exception



"""


