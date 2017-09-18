class DoWorkEventArgs(CancelEventArgs):
 """
 Provides data for the System.ComponentModel.BackgroundWorker.DoWork event handler.

 

 DoWorkEventArgs(argument: object)
 """
 @staticmethod
 def __new__(self,argument):
  """ __new__(cls: type,argument: object) """
  pass
 Argument=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that represents the argument of an asynchronous operation.



Get: Argument(self: DoWorkEventArgs) -> object



"""

 Result=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that represents the result of an asynchronous operation.



Get: Result(self: DoWorkEventArgs) -> object



Set: Result(self: DoWorkEventArgs)=value

"""


