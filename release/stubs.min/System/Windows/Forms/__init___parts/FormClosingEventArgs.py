class FormClosingEventArgs(CancelEventArgs):
 """
 Provides data for the System.Windows.Forms.Form.FormClosing event.

 

 FormClosingEventArgs(closeReason: CloseReason,cancel: bool)
 """
 @staticmethod
 def __new__(self,closeReason,cancel):
  """ __new__(cls: type,closeReason: CloseReason,cancel: bool) """
  pass
 CloseReason=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates why the form is being closed.



Get: CloseReason(self: FormClosingEventArgs) -> CloseReason



"""


