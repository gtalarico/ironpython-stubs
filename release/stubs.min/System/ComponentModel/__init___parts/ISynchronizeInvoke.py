class ISynchronizeInvoke:
 """ Provides a way to synchronously or asynchronously execute a delegate. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ISynchronizeInvoke()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def BeginInvoke(self,method,args):
  """
  BeginInvoke(self: ISynchronizeInvoke,method: Delegate,args: Array[object]) -> IAsyncResult
  
   Asynchronously executes the delegate on the thread that created this object.
  
   method: A System.Delegate to a method that takes parameters of the same number and type that are contained in args.
   args: An array of type System.Object to pass as arguments to the given method. This can be null if no arguments are needed.
   Returns: An System.IAsyncResult interface that represents the asynchronous operation started by calling this method.
  """
  pass
 def EndInvoke(self,result):
  """
  EndInvoke(self: ISynchronizeInvoke,result: IAsyncResult) -> object
  
   Waits until the process started by calling System.ComponentModel.ISynchronizeInvoke.BeginInvoke(System.Delegate,System.Object[]) completes,and then returns the value 
    generated by the process.
  
  
   result: An System.IAsyncResult interface that represents the asynchronous operation started by calling 
    System.ComponentModel.ISynchronizeInvoke.BeginInvoke(System.Delegate,System.Object[]).
  
   Returns: An System.Object that represents the return value generated by the asynchronous operation.
  """
  pass
 def Invoke(self,method,args):
  """
  Invoke(self: ISynchronizeInvoke,method: Delegate,args: Array[object]) -> object
  
   Synchronously executes the delegate on the thread that created this object and marshals the call to the creating thread.
  
   method: A System.Delegate that contains a method to call,in the context of the thread for the control.
   args: An array of type System.Object that represents the arguments to pass to the given method. This can be null if no arguments are needed.
   Returns: An System.Object that represents the return value from the delegate being invoked,or null if the delegate has no return value.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 InvokeRequired=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the caller must call System.ComponentModel.ISynchronizeInvoke.Invoke(System.Delegate,System.Object[]) when calling an object that implements this interface.

Get: InvokeRequired(self: ISynchronizeInvoke) -> bool

"""


