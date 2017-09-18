class ProgressChangedEventArgs(EventArgs):
 """
 Provides data for the System.ComponentModel.BackgroundWorker.ProgressChanged event.

 

 ProgressChangedEventArgs(progressPercentage: int,userState: object)
 """
 @staticmethod
 def __new__(self,progressPercentage,userState):
  """ __new__(cls: type,progressPercentage: int,userState: object) """
  pass
 ProgressPercentage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the asynchronous task progress percentage.



Get: ProgressPercentage(self: ProgressChangedEventArgs) -> int



"""

 UserState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a unique user state.



Get: UserState(self: ProgressChangedEventArgs) -> object



"""


