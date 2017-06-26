class Transaction(object, IDisposable):
    """
    Transactions are context-like objects that guard any changes made to a Revit model
    
    Transaction(document: Document, name: str)
    Transaction(document: Document)
    """
    def Commit(self, options=None):
        """
        Commit(self: Transaction) -> TransactionStatus
        
            Commits all changes made to the model during the transaction.
            Returns: If finished successfully, this method returns TransactionStatus.Committed.
           
             Note it is possible the RolledBack status is returned instead as an outcome
           
             of failure handling. If TransactionStatus::Pending is returned it means that
          
              failure handling has not been finalized yet and Revit awaits a user actions.
         
               Until committing is fully finalized, no changes to the document can be made
         
               (including starting of new transactions).The returned status does not have to 
             be necessarily the same as
           the status returned by 
             Autodesk.Revit.DB.Transaction.GetStatus even when the method is called
           
             immediately after committing the transaction. Such a difference may happen due 
             to actions
           made by a transaction finalizer, if there was one set.
           (See 
             Autodesk.Revit.DB.FailureHandlingOptions for more details.)
        
        Commit(self: Transaction, options: FailureHandlingOptions) -> TransactionStatus
        
            Commits all changes made to the model during the transaction.
        
            options: A set of Autodesk.Revit.DB.FailureHandlingOptionsoptions
           to be used for 
             handling eventual failures during this call.
           The options are only used 
             temporarily during the commitment process. After
           the transaction is 
             finished, the options will be reset to their default values.
        
            Returns: If finished successfully, this method returns TransactionStatus.Committed
           
             Note it is possible the RolledBack status is returned instead as an outcome
           
             of failure handling. If TransactionStatus.Pending is returned it means that
           
             failure handling has not been finalized yet and Revit awaits user's actions.
          
              Until committing is fully finalized, no changes to the document can be made
          
              (including starting of new transactions).Be aware that the returned status 
             does not have to be necessarily the same like
           the status returned by 
             Autodesk.Revit.DB.Transaction.GetStatus even when the method is called
           
             immediately after committing the transaction. Such difference may happen due to 
             actions
           made by a transaction finalizer, if there was one set.
           (See 
             Autodesk.Revit.DB.FailureHandlingOptions for more details.)
        """
        pass

    def Dispose(self):
        """ Dispose(self: Transaction) """
        pass

    def GetFailureHandlingOptions(self):
        """
        GetFailureHandlingOptions(self: Transaction) -> FailureHandlingOptions
        
            Returns the current failure handling options.
            Returns: An instance of FailureHandlingOptions
        """
        pass

    def GetName(self):
        """
        GetName(self: Transaction) -> str
        
            Returns the transaction's name.
            Returns: The transaction's current name.
        """
        pass

    def GetStatus(self):
        """
        GetStatus(self: Transaction) -> TransactionStatus
        
            Returns the current status of the transaction.
            Returns: The current status of the transaction.
        """
        pass

    def HasEnded(self):
        """
        HasEnded(self: Transaction) -> bool
        
            Determines whether the transaction has ended already.
            Returns: True if the transaction has already been committed or rolled back, False 
             otherwise.
        """
        pass

    def HasStarted(self):
        """
        HasStarted(self: Transaction) -> bool
        
            Determines whether the transaction has been started yet.
            Returns: True if the transaction has already started, False otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Transaction, disposing: bool) """
        pass

    def RollBack(self, options=None):
        """
        RollBack(self: Transaction) -> TransactionStatus
        
            Rolls back all changes made to the model during the transaction.
            Returns: If finished successfully, this method returns TransactionStatus.RolledBack.
           
             Be aware that the returned status does not have to be necessarily the same like
             
           the status returned by Autodesk.Revit.DB.Transaction.GetStatus even when 
             the method is called
           immediately after rolling back the transaction. Such 
             difference may happen due to actions
           made by a transaction finalizer, if 
             there was one set.
           (See Autodesk.Revit.DB.FailureHandlingOptions for more 
             details.)
        
        RollBack(self: Transaction, options: FailureHandlingOptions) -> TransactionStatus
        
            Rolls back all changes made to the model during the transaction.
        
            options: A set of Autodesk.Revit.DB.FailureHandlingOptionsoptions
           to be used for 
             handling eventual failures during this call.
           The options are only used 
             temporarily during this rolling back process. After
           the transaction is 
             finished, the options will be reset to their default values.
        
            Returns: If finished successfully, this method returns TransactionStatus.RolledBack.
           
             Be aware that the returned status does not have to be necessarily the same like
             
           the status returned by Autodesk.Revit.DB.Transaction.GetStatus even when 
             the method is called
           immediately after rolling back the transaction. Such 
             difference may happen due to actions
           made by a transaction finalizer, if 
             there was one set.
           (See Autodesk.Revit.DB.FailureHandlingOptions for more 
             details.)
        """
        pass

    def SetFailureHandlingOptions(self, options):
        """
        SetFailureHandlingOptions(self: Transaction, options: FailureHandlingOptions)
            Sets options for handling failures to be used when the transaction is being 
             committed or rolled back.
        
        
            options: An instance of FailureHandlingOptions to be applied to the transaction
        """
        pass

    def SetName(self, name):
        """
        SetName(self: Transaction, name: str)
            Sets the transaction's name.
        
            name: A name for the transaction.
        """
        pass

    def Start(self, name=None):
        """
        Start(self: Transaction) -> TransactionStatus
        
            Starts the transaction.
            Returns: If finished successfully, this method returns TransactionStatus.Started.
           
             Note that unless starting is successful, changes cannot be made to the 
             document.
        
        Start(self: Transaction, name: str) -> TransactionStatus
        
            Starts the transaction with an assigned name.
        
            name: Name of the transaction; If the transaction already has name, this new one will 
             preplace it.
           The name will appear on the Undo menu in Revit if the 
             transaction is successfully committed.
        
            Returns: If finished successfully, this method returns TransactionStatus.Started.
           
             Note that unless starting is successful, changes cannot be made to the 
             document.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, document, name=None):
        """
        __new__(cls: type, document: Document, name: str)
        __new__(cls: type, document: Document)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: Transaction) -> bool

"""


