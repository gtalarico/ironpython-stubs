class FormClosedEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.Form.FormClosed event.

 

 FormClosedEventArgs(closeReason: CloseReason)
 """
 @staticmethod
 def __new__(self,closeReason):
  """ __new__(cls: type,closeReason: CloseReason) """
  pass
 CloseReason=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates why the form was closed.



Get: CloseReason(self: FormClosedEventArgs) -> CloseReason



"""


