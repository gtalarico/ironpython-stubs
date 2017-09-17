class CurrentChangedEventManager(WeakEventManager):
 """ Provides a System.Windows.WeakEventManager implementation so that you can use the "weak event listener" pattern to attach listeners for the System.ComponentModel.ICollectionView.CurrentChanged event. """
 @staticmethod
 def AddHandler(source,handler):
  """ AddHandler(source: ICollectionView,handler: EventHandler[EventArgs]) """
  pass
 @staticmethod
 def AddListener(source,listener):
  """
  AddListener(source: ICollectionView,listener: IWeakEventListener)
   Adds the specified listener to the 
    System.ComponentModel.ICollectionView.CurrentChanged event of the specified 
    source.
  
  
   source: The object with the event.
   listener: The object to add as a listener.
  """
  pass
 @staticmethod
 def RemoveHandler(source,handler):
  """ RemoveHandler(source: ICollectionView,handler: EventHandler[EventArgs]) """
  pass
 @staticmethod
 def RemoveListener(source,listener):
  """
  RemoveListener(source: ICollectionView,listener: IWeakEventListener)
   Removes the specified listener from the 
    System.ComponentModel.ICollectionView.CurrentChanged event of the specified 
    source.
  
  
   source: The object with the event.
   listener: The listener to remove.
  """
  pass
 ReadLock=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Establishes a read-lock on the underlying data table,and returns an System.IDisposable.

"""

 WriteLock=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Establishes a write-lock on the underlying data table,and returns an System.IDisposable.

"""


