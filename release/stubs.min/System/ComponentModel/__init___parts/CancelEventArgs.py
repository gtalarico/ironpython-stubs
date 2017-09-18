class CancelEventArgs(EventArgs):
 """
 Provides data for a cancelable event.

 

 CancelEventArgs()

 CancelEventArgs(cancel: bool)
 """
 @staticmethod
 def __new__(self,cancel=None):
  """
  __new__(cls: type)

  __new__(cls: type,cancel: bool)
  """
  pass
 Cancel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the event should be canceled.



Get: Cancel(self: CancelEventArgs) -> bool



Set: Cancel(self: CancelEventArgs)=value

"""


