class AsyncCompletedEventArgs(EventArgs):
 """
 Provides data for the MethodNameCompleted event.

 

 AsyncCompletedEventArgs()

 AsyncCompletedEventArgs(error: Exception,cancelled: bool,userState: object)
 """
 def RaiseExceptionIfNecessary(self,*args):
  """
  RaiseExceptionIfNecessary(self: AsyncCompletedEventArgs)

   Raises a user-supplied exception if an asynchronous operation failed.
  """
  pass
 @staticmethod
 def __new__(self,error=None,cancelled=None,userState=None):
  """
  __new__(cls: type)

  __new__(cls: type,error: Exception,cancelled: bool,userState: object)
  """
  pass
 Cancelled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether an asynchronous operation has been canceled.



Get: Cancelled(self: AsyncCompletedEventArgs) -> bool



"""

 Error=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating which error occurred during an asynchronous operation.



Get: Error(self: AsyncCompletedEventArgs) -> Exception



"""

 UserState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the unique identifier for the asynchronous task.



Get: UserState(self: AsyncCompletedEventArgs) -> object



"""


