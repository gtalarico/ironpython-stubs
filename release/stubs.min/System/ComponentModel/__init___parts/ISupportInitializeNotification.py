class ISupportInitializeNotification:
 """ Allows coordination of initialization for a component and its dependent properties. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ISupportInitializeNotification()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 IsInitialized=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component is initialized.

Get: IsInitialized(self: ISupportInitializeNotification) -> bool

"""


 Initialized=None

