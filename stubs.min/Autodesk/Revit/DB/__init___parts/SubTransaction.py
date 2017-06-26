class SubTransaction(object,IDisposable):
 """
 Sub-transactions are objects that provide control over a subset of changes in a document.
 
 SubTransaction(document: Document)
 """
 def Commit(self):
  """
  Commit(self: SubTransaction) -> TransactionStatus
  
   Commits all changes made to the model made during the sub-transaction.
   Returns: If finished successfully,this method returns TransactionStatus.Committed
  """
  pass
 def Dispose(self):
  """ Dispose(self: SubTransaction) """
  pass
 def GetStatus(self):
  """
  GetStatus(self: SubTransaction) -> TransactionStatus
  
   Returns the current status of the sub-transaction.
   Returns: The current status of the sub-transaction.
  """
  pass
 def HasEnded(self):
  """
  HasEnded(self: SubTransaction) -> bool
  
   Determines whether the sub-transaction has ended already.
   Returns: True if the sub-transaction has already been committed or rolled back,False 
    otherwise.
  """
  pass
 def HasStarted(self):
  """
  HasStarted(self: SubTransaction) -> bool
  
   Determines whether the sub-transaction has been started yet.
   Returns: True if the sub-transaction has already started,False otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: SubTransaction,disposing: bool) """
  pass
 def RollBack(self):
  """
  RollBack(self: SubTransaction) -> TransactionStatus
  
   Discards all changes made to the model during the sub-transaction.
   Returns: If finished successfully,this method returns TransactionStatus.RolledBack.
  """
  pass
 def Start(self):
  """
  Start(self: SubTransaction) -> TransactionStatus
  
   Starts the sub-transaction.
   Returns: If started successfully,this method returns TransactionStatus.Started.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,document):
  """ __new__(cls: type,document: Document) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: SubTransaction) -> bool

"""


