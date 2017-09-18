class ErrorsChangedEventManager(WeakEventManager):
 # no doc
 @staticmethod
 def AddHandler(source,handler):
  """ AddHandler(source: INotifyDataErrorInfo,handler: EventHandler[DataErrorsChangedEventArgs]) """
  pass
 @staticmethod
 def RemoveHandler(source,handler):
  """ RemoveHandler(source: INotifyDataErrorInfo,handler: EventHandler[DataErrorsChangedEventArgs]) """
  pass
 ReadLock=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Establishes a read-lock on the underlying data table,and returns an System.IDisposable.

"""

 WriteLock=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Establishes a write-lock on the underlying data table,and returns an System.IDisposable.

"""


