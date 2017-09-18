class IFailuresPreprocessor:
 """
 An interface that may be used to perform a preprocessing step to either filter out anticipated transaction failures

    or to mark certain failures as non-continuable.
 """
 def PreprocessFailures(self,failuresAccessor):
  """
  PreprocessFailures(self: IFailuresPreprocessor,failuresAccessor: FailuresAccessor) -> FailureProcessingResult

  

   This method is called when there have been failures found at the end of a 

    transaction and Revit is about to start processing them.

  

  

   failuresAccessor: The Interface class that provides access to the failure information.

   Returns: Notifies end of transaction code about further actions required. Return values 

    are interpreted as follows:

     Continue - the failure processing will 

    continue. Failures will be shown to the user,even if they were addressed by 

    this method.ProceedWithCommit - end of transaction checks and failure 

    processing will restart from the beginning.

     If some failures were resolved 

    here,they will be removed and not delivered to the user.

     ProceedWithCommit 

    cannot be returned if transaction is being rolled back.ProceedWithRollBack - 

    the failure processing will continue. Failures will be shown to the user,but 

    user will have no option

     to resolve or ignore them - only cancel option 

    will be available. If intent is to roll back transaction without showing 

    failures to the user,

     it can be achieved by setting failure handling option 

    to remove failures before returning ProceedWithRollBack.

     Other return 

    values are not allowed.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
