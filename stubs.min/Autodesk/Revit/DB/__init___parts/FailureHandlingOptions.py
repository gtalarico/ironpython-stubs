class FailureHandlingOptions(object, IDisposable):
    """
    Options to control how failures (if any occurred during the transaction)
       should be handled at the time the transaction is being ended.
    """
    def Dispose(self):
        """ Dispose(self: FailureHandlingOptions) """
        pass

    def GetClearAfterRollback(self):
        """
        GetClearAfterRollback(self: FailureHandlingOptions) -> bool
        
            Obtains the flag indicating if all posted failures should be removed silently 
             when transaction is being rolled back.
        
            Returns: True to clear posted failures silently if the transaction is being rolled back, 
             false to keep these failures in place (they may be displayed to the user).
        """
        pass

    def GetDelayedMiniWarnings(self):
        """
        GetDelayedMiniWarnings(self: FailureHandlingOptions) -> bool
        
            Obtains the flag indicating if showing of mini-warning dialog should be delayed 
             until the end of next transaction.
        
            Returns: True to delay the display of the mini-warning dialog until the end of the next 
             transation, false to display them as this transaction is completed.
        """
        pass

    def GetFailuresPreprocessor(self):
        """
        GetFailuresPreprocessor(self: FailureHandlingOptions) -> IFailuresPreprocessor
        
            Gets the callback to be invoked in the beginning of failure processing.
            Returns: The callback to be invoked in the beginning of failure processing.
        """
        pass

    def GetForcedModalHandling(self):
        """
        GetForcedModalHandling(self: FailureHandlingOptions) -> bool
        
            Obtains the flag indicating if the error handling dialog shown at the end of 
             the failing transaction should be modal.
        
            Returns: True if the options force Revit to use a modal error dialog, false if it allows 
             use of a non-blocking dialog for warnings resulting from this transaction.
        """
        pass

    def GetTransactionFinalizer(self):
        """
        GetTransactionFinalizer(self: FailureHandlingOptions) -> ITransactionFinalizer
        
            Gets the callback to be executed after transaction is completed.
            Returns: The callback to be executed after transaction is completed.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FailureHandlingOptions, disposing: bool) """
        pass

    def SetClearAfterRollback(self, bFlag):
        """
        SetClearAfterRollback(self: FailureHandlingOptions, bFlag: bool) -> FailureHandlingOptions
        
            Sets a flag indicating that Revit should clear all posted failures silently 
             when the failing transaction is being rolled back intentionally.  If
           not 
             set, the failures may still be displayed to the user during rollback.
        
        
            bFlag: True to clear posted failures silently if the transaction is being rolled back, 
             false to keep these failures in place (they may be displayed to the user).
        
            Returns: This FailureHandlingOptions object.
        """
        pass

    def SetDelayedMiniWarnings(self, bFlag):
        """
        SetDelayedMiniWarnings(self: FailureHandlingOptions, bFlag: bool) -> FailureHandlingOptions
        
            Sets a flag indicating if Revit should delay the display of the mini-warning 
             dialog (if one is to be shown as a result of warnings in the current 
             transaction)
           until the end of the next transaction.
        
        
            bFlag: True to delay the display of the mini-warning dialog until the end of the next 
             transation, false to display them as this transaction is completed.
        
            Returns: This FailureHandlingOptions object.
        """
        pass

    def SetFailuresPreprocessor(self, preprocessor):
        """
        SetFailuresPreprocessor(self: FailureHandlingOptions, preprocessor: IFailuresPreprocessor) -> FailureHandlingOptions
        
            Sets the callback to be invoked in the beginning of failure processing.
        
            preprocessor: The callback to be invoked in the beginning of failure processing.
            Returns: This FailureHandlingOptions object.
        """
        pass

    def SetForcedModalHandling(self, bFlag):
        """
        SetForcedModalHandling(self: FailureHandlingOptions, bFlag: bool) -> FailureHandlingOptions
        
            Sets a flag indicating whether Revit will show a modal (blocking) error dialog 
             if the transaction failed to finish.
        
        
            bFlag: True to force Revit to use a modal error dialog, false to allow a non-blocking 
             dialog for warnings resulting from this transaction.
        
            Returns: This FailureHandlingOptions object.
        """
        pass

    def SetTransactionFinalizer(self, finalizer):
        """
        SetTransactionFinalizer(self: FailureHandlingOptions, finalizer: ITransactionFinalizer) -> FailureHandlingOptions
        
            Sets the callback to be executed after the transaction is completed.
        
            finalizer: The callback to be executed after the transaction is completed.
            Returns: This FailureHandlingOptions object.
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

Get: IsValidObject(self: FailureHandlingOptions) -> bool

"""


