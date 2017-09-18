class IObservable:
 # no doc
 def Subscribe(self,observer):
  """
  Subscribe(self: IObservable[T],observer: IObserver[T]) -> IDisposable

  

   Notifies the provider that an observer is to receive notifications.

  

   observer: The object that is to receive notifications.

   Returns: A reference to an interface that allows observers to stop receiving notifications before the 

    provider has finished sending them.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
