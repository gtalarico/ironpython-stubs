class AsyncOperation(object):
 """ Tracks the lifetime of an asynchronous operation. """
 def OperationCompleted(self):
  """
  OperationCompleted(self: AsyncOperation)

   Ends the lifetime of an asynchronous operation.
  """
  pass
 def Post(self,d,arg):
  """
  Post(self: AsyncOperation,d: SendOrPostCallback,arg: object)

   Invokes a delegate on the thread or context appropriate for the application model.

  

   d: A System.Threading.SendOrPostCallback object that wraps the delegate to be called when the 

    operation ends.

  

   arg: An argument for the delegate contained in the d parameter.
  """
  pass
 def PostOperationCompleted(self,d,arg):
  """
  PostOperationCompleted(self: AsyncOperation,d: SendOrPostCallback,arg: object)

   Ends the lifetime of an asynchronous operation.

  

   d: A System.Threading.SendOrPostCallback object that wraps the delegate to be called when the 

    operation ends.

  

   arg: An argument for the delegate contained in the d parameter.
  """
  pass
 SynchronizationContext=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Threading.SynchronizationContext object that was passed to the constructor.



Get: SynchronizationContext(self: AsyncOperation) -> SynchronizationContext



"""

 UserSuppliedState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an object used to uniquely identify an asynchronous operation.



Get: UserSuppliedState(self: AsyncOperation) -> object



"""


