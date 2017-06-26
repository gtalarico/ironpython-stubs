class FailuresAccessor(object, IDisposable):
    """ An interface class that provides access to failure information posted in a document and methods to resolve these failures. """
    def CanCommitPendingTransaction(self):
        """
        CanCommitPendingTransaction(self: FailuresAccessor) -> bool
        
            Checks if pending failure processing can be finished by committing a pending 
             transaction.
        
            Returns: True if there is a pending transaction and this transaction is allowed to be 
             committed.
        """
        pass

    def CanRollBackPendingTransaction(self):
        """
        CanRollBackPendingTransaction(self: FailuresAccessor) -> bool
        
            Checks if pending failure processing can be finished by rolling back a pending 
             transaction.
        
            Returns: True if there is a pending transaction and this transaction is allowed to be 
             rolled back
        """
        pass

    def CommitPendingTransaction(self):
        """
        CommitPendingTransaction(self: FailuresAccessor) -> TransactionStatus
        
            Finishes pending failures processing by committing the pending transaction.
            Returns: Result of attempt to commit the pending transaction.
        """
        pass

    def DeleteAllWarnings(self):
        """
        DeleteAllWarnings(self: FailuresAccessor)
            Deletes all FailureMessages of severity "Warning" currently posted in a 
             document.
        """
        pass

    def DeleteElements(self, idsToDelete):
        """ DeleteElements(self: FailuresAccessor, idsToDelete: IList[ElementId]) """
        pass

    def DeleteWarning(self, failure):
        """
        DeleteWarning(self: FailuresAccessor, failure: FailureMessageAccessor)
            Deletes one specific failure message of severity "Warning".
        
            failure: The accessor to the warning to be deleted.
        """
        pass

    def Dispose(self):
        """ Dispose(self: FailuresAccessor) """
        pass

    def GetAttemptedResolutionTypes(self, failure):
        """
        GetAttemptedResolutionTypes(self: FailuresAccessor, failure: FailureMessageAccessor) -> IList[FailureResolutionType]
        
            Returns list of the failure resolution types attempted for the failure in the 
             current transaction.
        
        
            failure: The failure.
            Returns: The list of the types of failure resolutions attempted for the failure.
        """
        pass

    def GetDocument(self):
        """
        GetDocument(self: FailuresAccessor) -> Document
        
            Provides access to a document for which failures are being processed or 
             preprocessed.
        
            Returns: The document for which failures preprocessing or processing is being performed.
        """
        pass

    def GetFailureHandlingOptions(self):
        """
        GetFailureHandlingOptions(self: FailuresAccessor) -> FailureHandlingOptions
        
            Provides access to the failure handling options for the transaction currently 
             being finished.
        
            Returns: The failure handling options for transaction currently being finished.
        """
        pass

    def GetFailureMessages(self, severity=None):
        """
        GetFailureMessages(self: FailuresAccessor) -> IList[FailureMessageAccessor]
        
            Provides access to the individual failure messages currently posted in the 
             document.
        
            Returns: The accessors to the individual failure messages posted in the document.
        GetFailureMessages(self: FailuresAccessor, severity: FailureSeverity) -> IList[FailureMessageAccessor]
        
            Provides access to the individual failure messages if a given severity 
             currently posted in the document.
        
        
            severity: The failure severity for which failure messages are requested.
           If the 
             requested severity is None, an empty collection is returned.
        
            Returns: Accessors to the individual failure messages of a given severity posted in the 
             document.
        """
        pass

    def GetSeverity(self):
        """
        GetSeverity(self: FailuresAccessor) -> FailureSeverity
        
            Provides access to the current failure severity.
            Returns: The highest severity of a failure message currently posted in the document.
        """
        pass

    def GetTransactionName(self):
        """
        GetTransactionName(self: FailuresAccessor) -> str
        
            Retrieves the name of the transaction for which failures are being processed.
            Returns: The name of the transaction for which failures are being processed.
        """
        pass

    def IsActive(self):
        """
        IsActive(self: FailuresAccessor) -> bool
        
            Method allows to check if this instance of the accessor is currently active.
            Returns: True if this instance is currently active and can be used.
        """
        pass

    def IsElementsDeletionPermitted(self, idsToDelete=None, reason=None):
        """
        IsElementsDeletionPermitted(self: FailuresAccessor) -> bool
        
            Checks if resolution of the failures by deleting failure elements is permitted.
            Returns: True if resolution of the failures by deleting failure elements is permitted.
        IsElementsDeletionPermitted(self: FailuresAccessor, idsToDelete: IList[ElementId]) -> bool
        IsElementsDeletionPermitted(self: FailuresAccessor, idsToDelete: IList[ElementId]) -> (bool, str)
        """
        pass

    def IsFailureResolutionPermitted(self, failure=None, resolutionType=None):
        """
        IsFailureResolutionPermitted(self: FailuresAccessor) -> bool
        
            Checks if resolution of failures is permitted.
            Returns: True if resolutions of failures is permitted.
        IsFailureResolutionPermitted(self: FailuresAccessor, failure: FailureMessageAccessor) -> bool
        
            Checks if default resolution of the failure is permitted.
        
            failure: The accessor to the failure to be resolved.
            Returns: True if default resolution of the failure is permitted
        IsFailureResolutionPermitted(self: FailuresAccessor, failure: FailureMessageAccessor, resolutionType: FailureResolutionType) -> bool
        
            Checks if resolution of the failure using given resolution type is permitted.
        
            failure: Accessor to the failure to be resolved.
            resolutionType: Type of the failure resolution to be used.
            Returns: True if resolution of the failure using given resolution type is permitted.
        """
        pass

    def IsPending(self):
        """
        IsPending(self: FailuresAccessor) -> bool
        
            Checks if the failure processing is pending.
            Returns: True if the failures processing is in the pending state.
        """
        pass

    def IsTransactionBeingCommitted(self):
        """
        IsTransactionBeingCommitted(self: FailuresAccessor) -> bool
        
            Checks if the transaction for which failures are processed is being committed 
             or rolled back.
        
            Returns: True if current transaction is being committed, false if the transaction is 
             being rolled back.
        """
        pass

    def JournalFailures(self, failures):
        """ JournalFailures(self: FailuresAccessor, failures: IList[FailureMessageAccessor]) """
        pass

    def PostFailure(self, failure):
        """
        PostFailure(self: FailuresAccessor, failure: FailureMessage)
            Posts an additional failure message to be processed for the current transaction.
        
            failure: Failure message to post.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FailuresAccessor, disposing: bool) """
        pass

    def ReplaceFailures(self, failure):
        """
        ReplaceFailures(self: FailuresAccessor, failure: FailureMessage)
            Deletes all failure messages currently posted in a document and replaces them 
             with one "generic" failure.
        
        
            failure: FailureMessage that should replace all currently posted messages. It must have 
             severity DocumentCorruption.
        """
        pass

    def ResolveFailure(self, failure):
        """
        ResolveFailure(self: FailuresAccessor, failure: FailureMessageAccessor)
            Resolves one failure using the failure resolution type last set for it.
        
            failure: The accessor to the failure to be resolved.
        """
        pass

    def ResolveFailures(self, failures):
        """ ResolveFailures(self: FailuresAccessor, failures: IList[FailureMessageAccessor]) """
        pass

    def RollBackPendingTransaction(self):
        """
        RollBackPendingTransaction(self: FailuresAccessor) -> TransactionStatus
        
            Finishes pending failures processing by rolling back the pending transaction.
            Returns: Result of attempt to roll back the pending transaction.
        """
        pass

    def SetFailureHandlingOptions(self, options):
        """
        SetFailureHandlingOptions(self: FailuresAccessor, options: FailureHandlingOptions)
            Sets failure handling options for the transaction currently being finished.
        
            options: The failure handling options to be set for the transaction currently being 
             finished.
        """
        pass

    def SetTransactionName(self, transactionName):
        """
        SetTransactionName(self: FailuresAccessor, transactionName: str)
            Changes the name of the transaction for which failures are being processed.
        
            transactionName: The name of the transaction to set.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FailuresAccessor) -> bool

"""


