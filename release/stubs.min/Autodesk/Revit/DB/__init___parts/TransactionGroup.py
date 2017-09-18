class TransactionGroup(object,IDisposable):
 """
 Transaction groups aggregate a number of transactions.

 

 TransactionGroup(document: Document,transGroupName: str)

 TransactionGroup(document: Document)
 """
 def Assimilate(self):
  """
  Assimilate(self: TransactionGroup) -> TransactionStatus

  

   Assimilates all inner transactions by merging them into a single undo item.

   Returns: If finished successfully,this method returns TransactionStatus.Committed.
  """
  pass
 def Commit(self):
  """
  Commit(self: TransactionGroup) -> TransactionStatus

  

   Commits the transaction group.

   Returns: If finished successfully,this method returns TransactionStatus.Committed.
  """
  pass
 def Dispose(self):
  """ Dispose(self: TransactionGroup) """
  pass
 def GetName(self):
  """
  GetName(self: TransactionGroup) -> str

  

   Returns the transaction group's name. It could be an empty string.

   Returns: The transaction group's current name.
  """
  pass
 def GetStatus(self):
  """
  GetStatus(self: TransactionGroup) -> TransactionStatus

  

   Gets the current status of the transaction group.

   Returns: The current status of the transaction group.
  """
  pass
 def HasEnded(self):
  """
  HasEnded(self: TransactionGroup) -> bool

  

   Determines whether the transaction group has ended already.

   Returns: True if the transaction group has already been committed or rolled back,False 

    otherwise.
  """
  pass
 def HasStarted(self):
  """
  HasStarted(self: TransactionGroup) -> bool

  

   Determines whether the transaction has been started yet.

   Returns: True if the transaction group has already started,False otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: TransactionGroup,disposing: bool) """
  pass
 def RollBack(self):
  """
  RollBack(self: TransactionGroup) -> TransactionStatus

  

   Rolls back the transaction group,which effectively undoes all transactions 

    committed inside the group.

  

   Returns: If finished successfully,this method returns TransactionStatus.RolledBack.
  """
  pass
 def SetName(self,name):
  """
  SetName(self: TransactionGroup,name: str)

   Sets the transaction group's name.

  

   name: A name for the transaction group.
  """
  pass
 def Start(self,transGroupName=None):
  """
  Start(self: TransactionGroup) -> TransactionStatus

  

   Starts the transaction group

   Returns: If started successfully,this method returns TransactionStatus.Started.

  Start(self: TransactionGroup,transGroupName: str) -> TransactionStatus

  

   Starts the transaction group with an assigned name.

  

   transGroupName: Name of the group.

     The name will be used only for a group that is 

    Autodesk.Revit.DB.TransactionGroup.Assimilateassimilated at the end.

  

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
 def __new__(self,document,transGroupName=None):
  """
  __new__(cls: type,document: Document,transGroupName: str)

  __new__(cls: type,document: Document)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsFailureHandlingForcedModal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Forces all transactions finished inside this group to use modal failure handling

   regardless of what failure handling options are set for those transactions.



Get: IsFailureHandlingForcedModal(self: TransactionGroup) -> bool



Set: IsFailureHandlingForcedModal(self: TransactionGroup)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: TransactionGroup) -> bool



"""


