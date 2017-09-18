class IObserver:
 # no doc
 def OnCompleted(self):
  """
  OnCompleted(self: IObserver[T])

   Notifies the observer that the provider has finished sending push-based notifications.
  """
  pass
 def OnError(self,error):
  """
  OnError(self: IObserver[T],error: Exception)

   Notifies the observer that the provider has experienced an error condition.

  

   error: An object that provides additional information about the error.
  """
  pass
 def OnNext(self,value):
  """
  OnNext(self: IObserver[T],value: T)

   Provides the observer with new data.

  

   value: The current notification information.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
