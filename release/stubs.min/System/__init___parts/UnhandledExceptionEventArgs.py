class UnhandledExceptionEventArgs(EventArgs):
 """
 Provides data for the event that is raised when there is an exception that is not handled in any application domain.

 

 UnhandledExceptionEventArgs(exception: object,isTerminating: bool)
 """
 @staticmethod
 def __new__(self,exception,isTerminating):
  """ __new__(cls: type,exception: object,isTerminating: bool) """
  pass
 ExceptionObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the unhandled exception object.



Get: ExceptionObject(self: UnhandledExceptionEventArgs) -> object



"""

 IsTerminating=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the common language runtime is terminating.



Get: IsTerminating(self: UnhandledExceptionEventArgs) -> bool



"""


