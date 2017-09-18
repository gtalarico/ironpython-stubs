class ICentralLockedCallback:
 """
 An interface that may be used to control Revit's behavior when it tries to lock central

    and is blocked because another user already has locked central.
 """
 def ShouldWaitForLockAvailability(self):
  """
  ShouldWaitForLockAvailability(self: ICentralLockedCallback) -> bool

  

   Returns whether Revit should wait and try again to acquire the lock on central.

   Returns: True means wait and try again later.  False means immediately give up.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
