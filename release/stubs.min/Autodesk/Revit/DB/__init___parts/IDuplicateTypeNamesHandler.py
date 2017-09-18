class IDuplicateTypeNamesHandler:
 """
 An interface for custom handlers of duplicate type names encountered during a paste operation. When the destination document

    contains types that have the same names as the types being copied,but different internals,a decision must be made on how to proceed - whether to

    cancel the operation or continue,but only copy types with unique names.
 """
 def OnDuplicateTypeNamesFound(self,args):
  """
  OnDuplicateTypeNamesFound(self: IDuplicateTypeNamesHandler,args: DuplicateTypeNamesHandlerArgs) -> DuplicateTypeAction

  

   Called when the destination document contains types with the same names as the 

    types being copied.

  

  

   args: The information about the types with duplicate names.

   Returns: The action to be taken: copy only types with unique names or cancel the 

    operation.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
