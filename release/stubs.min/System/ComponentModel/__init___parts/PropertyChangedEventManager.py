class PropertyChangedEventManager(WeakEventManager):
 """ Provides a System.Windows.WeakEventManager implementation so that you can use the "weak event listener" pattern to attach listeners for the System.ComponentModel.INotifyPropertyChanged.PropertyChanged event. """
 @staticmethod
 def AddHandler(source,handler,propertyName):
  """ AddHandler(source: INotifyPropertyChanged,handler: EventHandler[PropertyChangedEventArgs],propertyName: str) """
  pass
 @staticmethod
 def AddListener(source,listener,propertyName):
  """
  AddListener(source: INotifyPropertyChanged,listener: IWeakEventListener,propertyName: str)
   Adds the specified listener to the list of listeners on the specified source.
  
   source: The object with the event.
   listener: The object to add as a listener.
   propertyName: The name of the property that exists on source upon which to listen for 
    changes. Set to System.String.Empty to indicate "any property".
  """
  pass
 @staticmethod
 def RemoveHandler(source,handler,propertyName):
  """ RemoveHandler(source: INotifyPropertyChanged,handler: EventHandler[PropertyChangedEventArgs],propertyName: str) """
  pass
 @staticmethod
 def RemoveListener(source,listener,propertyName):
  """
  RemoveListener(source: INotifyPropertyChanged,listener: IWeakEventListener,propertyName: str)
   Removes the specified listener from the list of listeners on the provided 
    source.
  
  
   source: The object to remove the listener from.
   listener: The listener to remove.
   propertyName: The name of the property that exists on source upon which to stop listening for 
    changes. Set to System.String.Empty to indicate "any property".
  """
  pass
 ReadLock=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Establishes a read-lock on the underlying data table,and returns an System.IDisposable.

"""

 WriteLock=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Establishes a write-lock on the underlying data table,and returns an System.IDisposable.

"""


