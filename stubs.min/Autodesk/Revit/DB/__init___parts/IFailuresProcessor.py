class IFailuresProcessor:
 """ To create your own UI or fully automated tool to process Revit Failures,derive a class from this interface. """
 def Dismiss(self,document):
  """
  Dismiss(self: IFailuresProcessor,document: Document)
   This method is being called in case of exception or document destruction to 
    dismiss any possible pending failure UI that may
     have left on the screen
  
  
   document: Document for which pending failures processing UI should be dismissed
  """
  pass
 def ProcessFailures(self,data):
  """
  ProcessFailures(self: IFailuresProcessor,data: FailuresAccessor) -> FailureProcessingResult
  
   Method that Revit will invoke to process failures at the end of transaction.
  
   data: Provides all necessary data to perform the resolution of failures.
   Returns: The result of the failures processing.
     Continue - Should be returned if 
    there were no failures or highest failure severity was "Warning" and all 
    warnings were deleted.
     If some failures are still present and "Continue" is 
    returned,it will be treated as "ProceedWithRollback".
     Note: If this method 
    has attempted to resolve failures,it should return "ProceedWithCommit"
     to 
    repeat end of transaction checks and failures processing.ProceedWithCommit - 
    End of transaction checks and failure processing will restart from the 
    beginning.
     If some failures were resolved,they will be removed and not 
    delivered to the user.
     ProceedWithCommit cannot be returned if transaction 
    is being rolled back.ProceedWithRollBack - Transaction will be rolled back 	
    even if Commit was originally requested.WaitForUserInput - Should be returned 
    if method has activated modeless user interaction and is waiting for an 
    external event
     (typically user input) to complete failures processing.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
