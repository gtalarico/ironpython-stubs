class IAsyncResult:
 """ Represents the status of an asynchronous operation. """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 AsyncState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a user-defined object that qualifies or contains information about an asynchronous operation.



Get: AsyncState(self: IAsyncResult) -> object



"""

 AsyncWaitHandle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Threading.WaitHandle that is used to wait for an asynchronous operation to complete.



Get: AsyncWaitHandle(self: IAsyncResult) -> WaitHandle



"""

 CompletedSynchronously=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the asynchronous operation completed synchronously.



Get: CompletedSynchronously(self: IAsyncResult) -> bool



"""

 IsCompleted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the asynchronous operation has completed.



Get: IsCompleted(self: IAsyncResult) -> bool



"""


