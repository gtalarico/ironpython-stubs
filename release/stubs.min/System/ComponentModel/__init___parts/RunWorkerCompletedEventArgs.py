class RunWorkerCompletedEventArgs(AsyncCompletedEventArgs):
 """
 Provides data for the MethodNameCompleted event.

 

 RunWorkerCompletedEventArgs(result: object,error: Exception,cancelled: bool)
 """
 @staticmethod
 def __new__(self,result,error,cancelled):
  """ __new__(cls: type,result: object,error: Exception,cancelled: bool) """
  pass
 Result=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that represents the result of an asynchronous operation.



Get: Result(self: RunWorkerCompletedEventArgs) -> object



"""

 UserState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that represents the user state.



Get: UserState(self: RunWorkerCompletedEventArgs) -> object



"""


