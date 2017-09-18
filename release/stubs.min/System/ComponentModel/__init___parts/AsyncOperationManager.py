class AsyncOperationManager(object):
 """ Provides concurrency management for classes that support asynchronous method calls. This class cannot be inherited. """
 @staticmethod
 def CreateOperation(userSuppliedState):
  """
  CreateOperation(userSuppliedState: object) -> AsyncOperation

  

   Returns an System.ComponentModel.AsyncOperation for tracking the duration of a particular 

    asynchronous operation.

  

  

   userSuppliedState: An object used to associate a piece of client state,such as a task ID,with a particular 

    asynchronous operation.

  

   Returns: An System.ComponentModel.AsyncOperation that you can use to track the duration of an 

    asynchronous method invocation.
  """
  pass
 SynchronizationContext=None
 __all__=[
  'CreateOperation',
 ]

